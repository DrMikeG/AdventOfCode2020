import os
import multiprocessing
import time
import re
import shutil # for copying files/folders

import urllib.request


class Version():
    def __init__(self, major, minor, buildNumber):
        self.major = major
        self.minor = minor
        self.buildNumber = buildNumber
        
    def GetMajorVersion(self):
        return self.major
    
    def __repr__(self):
        return "%02d.%02d.%03d" %(self.major, self.minor, self.buildNumber)
        
    def __lt__(self, other):
        return (self.major*100000 + self.minor * 1000 + self.buildNumber) < (other.major*100000 + other.minor * 1000 + other.buildNumber)   

    def __gt__(self, other):
        return (self.major*100000 + self.minor * 1000 + self.buildNumber) > (other.major*100000 + other.minor * 1000 + other.buildNumber)
    
    def __ge__(self, other):
        return not self.__lt__(other)
    
    def __eq__(self, other):
        return not self<other and not other<self

class Bundle():
    def __init__(self, version, path, conAppPath):
        self.version = version
        self.path = path
        self.conAppPath = conAppPath

    def __lt__(self, other):
        return self.version < other.version  

    def __gt__(self, other):
        return self.version > other.version
    
    def __ge__(self, other):
        return not self.__lt__(other)
    
    def __eq__(self, other):
        return not self<other and not other<self
        
def GetVersionFromString(text):
    match = re.search("(\d\d)[^\d](\d\d)[^\d](\d\d\d)", text)
    version = None
    if match:
        version = Version(int(match.groups()[0]), int(match.groups()[1]), int(match.groups()[2]))
    #print(version)
    return version

timeForInternalReleases = 0
timeForRoot = 0
timeForSingleFolder = 0
numTries = 0
def TryToFindExecutable(path):
    global timeForInternalReleases, timeForRoot, timeForSingleFolder, numTries
    numTries += 1
    conAppPath = ""
    # This is expecting to be looking within \\plm\cbnas\users\vtk_users\yyvtk\internal_releases
    # where the path to conApp is expected to be \win64\ConApp.exe
    if os.path.isfile(os.path.join(path,"win64", "ConApp.exe")):
        conAppPath = os.path.join(path, "win64", "ConApp.exe")
    return conAppPath

def FindExecutable(args):
    (path, folder) = args
    version = GetVersionFromString(folder)
    if (version is not None):
        if version < Version(5,0,0):
            # release before VTK 05.00.000 do not support the xml in and out option so we ignore them
            return
                    
        newPath = os.path.join(path, folder)
        conAppPath = TryToFindExecutable(newPath)
        if conAppPath:
            return Bundle(version, newPath, conAppPath)


def FindVTKBundles(path):
    bundles = []
    versionFound = []
    subFolders = os.listdir(path)
    pool = multiprocessing.Pool(multiprocessing.cpu_count() * 4)
    args = [(path, subFolder) for subFolder in subFolders]
    foundBundles = pool.imap(FindExecutable, args)
    pool.close()
    pool.join()
    for bundle in foundBundles:
        if bundle  and (bundle.version not in versionFound):
            bundles.append(bundle)
            versionFound.append(bundle.version)
    bundles.sort()
    print("Found %u VTK bundles" % len(bundles))
    return bundles[-1]

def findNewestBundle():
    print("Step 1) Finding newest VTK to use as source for copy")
    path = '\\\\plm\\cbnas\\users\\vtk_users\\yyvtk\\internal_releases'
    if not os.path.exists(path):
        print("!!! Directory '%s' couldn't be found, so it was skipped" % (path))
    else:
        print("Directory '%s' found" % (path))
        newest = FindVTKBundles(path)
    print("Newest version found is %s" % newest.version)
    print("At path %s" % newest.path)
    return newest

def delFolder(mydir):
    if not os.path.exists(mydir):
        print("!!! delFolder Directory '%s' couldn't be found" % (mydir))
    else:
        print("Emptying folder '%s'" %(mydir))
        try:
            shutil.rmtree(mydir)
        except OSError as e:
            print ("Error: %s - %s." % (e.filename, e.strerror))

def emptyFolder(folderToEmpty):
    delFolder(folderToEmpty)
    os.mkdir(folderToEmpty)


def delFile(myFile):
    if os.path.exists(myFile):
        os.remove(myFile)
    else:
        print("delFile() File '%s' not found" % (myFile))

def copyFile(filename,srcFolder,targetFolder):
    try:
        shutil.copyfile(os.path.join(srcFolder, filename),os.path.join(targetFolder, filename))
        print("Created file '%s'" %(os.path.join(targetFolder, filename)))
    except OSError as e:
        print ("Error: %s - %s." % (e.filename, e.strerror))

def copy_header_files_from_within_src_to_dest(srcdir,dstdir):
    for basename in os.listdir(srcdir):
        if basename.endswith('.hxx'):
            pathname = os.path.join(srcdir, basename)
            if os.path.isfile(pathname):
                shutil.copy2(pathname, dstdir)

def update_TPC_DCubed(argon_path,bundle_path):
    print("Step 2a) Replacing DCM files for TestPackageCreator")
    #D:\gitWorkSpace\Products\argon\TestPackageCreator\DCubed\include (all of VTK release version)
    # - Remove original folder D:\gitWorkSpace\Products\argon2\TestPackageCreator\DCubed\include\d3vm_inc
    # - Remove original folder D:\gitWorkSpace\Products\argon2\TestPackageCreator\DCubed\include\dcm2_inc
    # - Copy new folder  \\plm\cbnas\users\vtk_users\yyvtk\internal_releases\release_23_00_055\source\DCubed\include\d3vm_inc
    # - Copy new folder  \\plm\cbnas\users\vtk_users\yyvtk\internal_releases\release_23_00_055\source\DCubed\include\dcm2_inc
    delFolder(os.path.join(argon_path, "TestPackageCreator\\DCubed\\include"))
    shutil.copytree( os.path.join(bundle_path, "source\\DCubed\\include"), os.path.join(argon_path, "TestPackageCreator\\DCubed\\include"))

    #D:\gitWorkSpace\Products\argon\TestPackageCreator\DCubed\lib (subset of VTK release version)
    destFolderPath = os.path.join(argon_path, "TestPackageCreator\\DCubed\\lib\\lin64")
    srcFolderPath = os.path.join(bundle_path, "source\\DCubed\\lib\\lin64")
    # remove folder and recreate
    emptyFolder(destFolderPath)

    newestFileName = findLastFileWithPrefix(srcFolderPath,"libdcud3vm",".so")
    copyFile( newestFileName, srcFolderPath, destFolderPath)
    newestFileName = findLastFileWithPrefix(srcFolderPath,"libdcuvtkp3D",".so")
    copyFile( newestFileName, srcFolderPath, destFolderPath)
    newestFileName = findLastFileWithPrefix(srcFolderPath,"libdcux2d",".so")
    copyFile( newestFileName, srcFolderPath, destFolderPath)

    destFolderPath = os.path.join(argon_path, "TestPackageCreator\\DCubed\\lib\\win64")
    srcFolderPath = os.path.join(bundle_path, "source\\DCubed\\lib\\win64")
    # remove folder and recreate
    emptyFolder(destFolderPath)

    newestFileName = findLastFileWithPrefix(srcFolderPath,"dcud3vm",".dll")
    copyFile( newestFileName, srcFolderPath, destFolderPath)
    newestFileName = findLastFileWithPrefix(srcFolderPath,"dcuvtkp3D",".dll")
    copyFile( newestFileName, srcFolderPath, destFolderPath)
    newestFileName = findLastFileWithPrefix(srcFolderPath,"dcux2d",".dll")
    copyFile( newestFileName, srcFolderPath, destFolderPath)


def update_TPC_Parasolid(argon_path,bundle_path):
    print("Step 2b) Replacing DCM files for TestPackageCreator")
    delFolder(os.path.join(argon_path, "TestPackageCreator\\Parasolid"))
    shutil.copytree( os.path.join(bundle_path, "source\\Parasolid"), os.path.join(argon_path, "TestPackageCreator\\Parasolid"))

def update_TPC_VTK(argon_path,bundle_path):
    print("Step 2c) Replacing VTK files for TestPackageCreator")
    #D:\gitWorkSpace\Products\argon\TestPackageCreator\VTK\lib\win64\VTK.lib
    destFolderPath = os.path.join(argon_path, "TestPackageCreator\\VTK\\lib\\win64")
    # Source is within route of release bundle
    srcFolderPath = os.path.join(bundle_path, "win64")
    emptyFolder(destFolderPath)
    copyFile( "VTK.lib", srcFolderPath, destFolderPath)

    #D:\gitWorkSpace\Products\argon\TestPackageCreator\VTK\lib\lin64\libVTK.so
    destFolderPath = os.path.join(argon_path, "TestPackageCreator\\VTK\\lib\\lin64")
    srcFolderPath = os.path.join(bundle_path, "lin64")
    emptyFolder(destFolderPath)
    copyFile( "libVTK.so", srcFolderPath, destFolderPath)

    #D:\gitWorkSpace\Products\argon\TestPackageCreator\VTK\run
    destFolderPath = os.path.join(argon_path, "TestPackageCreator\\VTK\\run\\lin64")
    srcFolderPath = os.path.join(bundle_path, "lin64")
    emptyFolder(destFolderPath)
    copyFile( "libSession.so", srcFolderPath, destFolderPath)
    copyFile( "libVTK.so", srcFolderPath, destFolderPath)
    copyFile( "libVTKUNIT023.so", srcFolderPath, destFolderPath)

    destFolderPath = os.path.join(argon_path, "TestPackageCreator\\VTK\\run\\win64")
    srcFolderPath = os.path.join(bundle_path, "win64")
    emptyFolder(destFolderPath)
    copyFile( "Session.dll", srcFolderPath, destFolderPath)
    copyFile( "VTK.dll", srcFolderPath, destFolderPath)
    copyFile( "VTKUNIT023.dll", srcFolderPath, destFolderPath)

    #D:\gitWorkSpace\Products\argon\TestPackageCreator\VTK\Api (added all headers + hidden function headers)
    destFolderPath = os.path.join(argon_path, "TestPackageCreator\\VTK\\Api")
    emptyFolder(destFolderPath)
    srcFolderPath = os.path.join(bundle_path, "headers")
    copy_header_files_from_within_src_to_dest(srcFolderPath,destFolderPath)

    destFolderPath = os.path.join(argon_path, "TestPackageCreator\\VTK\\Api\\HiddenFunctions")
    emptyFolder(destFolderPath)
    srcFolderPath = os.path.join(bundle_path, "source\\VTK\\Api\\HiddenFunctions")
    copy_header_files_from_within_src_to_dest(srcFolderPath,destFolderPath)


def replaceFilesForTestPackageCreator(bundle,argon_path):
    print("Step 2) Replacing files for TestPackageCreator")
    if not os.path.exists(argon_path):
        print("!!! Directory '%s' couldn't be found" % (argon_path))
    else:
        print("Updating TestPackageCreator files in Directory '%s'" % (argon_path))
        update_TPC_DCubed(argon_path,bundle.path)
        update_TPC_Parasolid(argon_path,bundle.path)
        update_TPC_VTK(argon_path,bundle.path)

    #If changing dcubed lib names or incrementing major VTK Unit version, update TestPackageCreator/copy_required_external_dlls.bat

def replaceFilesForArgonItself(bundle,argon_path):
    print("Step 3) Replacing files for Argon DCM integrations")
    if not os.path.exists(argon_path):
        print("!!! Directory '%s' couldn't be found" % (argon_path))
    else:
        print("Updating TestPackageCreator files in Directory '%s'" % (argon_path))
    
        #D:\gitWorkSpace\Products\argon\DCubed\include\dcm2_inc
        delFolder(os.path.join(argon_path, "DCubed\\include\\dcm2_inc"))
        shutil.copytree( os.path.join(bundle.path, "source\\DCubed\\include\\dcm2_inc"), os.path.join(argon_path, "DCubed\\include\\dcm2_inc"))

        #D:\gitWorkSpace\Products\argon\DCubed\lib\lin64\libdcux2d720101.so
        destFolderPath = os.path.join(argon_path, "DCubed\\lib\\lin64")
        emptyFolder(destFolderPath)
        srcFolderPath = os.path.join(bundle.path, "source\\DCubed\\lib\\lin64")
        newestFileName = findLastFileWithPrefix(srcFolderPath,"libdcux2d",".so")
        copyFile( newestFileName, srcFolderPath, destFolderPath)

        #D:\gitWorkSpace\Products\argon\DCubed\lib\win64\dcux2d720101.dll
        #D:\gitWorkSpace\Products\argon\DCubed\lib\win64\dcux2d720101.lib
        destFolderPath = os.path.join(argon_path, "DCubed\\lib\\win64")
        emptyFolder(destFolderPath)
        srcFolderPath = os.path.join(bundle.path, "source\\DCubed\\lib\\win64")
        newestFileName = findLastFileWithPrefix(srcFolderPath,"dcux2d",".dll")
        copyFile( newestFileName, srcFolderPath, destFolderPath)
        newestFileName = findLastFileWithPrefix(srcFolderPath,"dcux2d",".lib")
        copyFile( newestFileName, srcFolderPath, destFolderPath)
        
        #D:\gitWorkSpace\Products\argon\DCubed\lib\wasm
        delFolder(os.path.join(argon_path, "DCubed\\lib\\wasm"))
        shutil.copytree( os.path.join(bundle.path, "source\\DCubed\\lib\\wasm"), os.path.join(argon_path, "DCubed\\lib\\wasm"))


def findLastFileWithPrefix(folder,prefix,suffix):
    lastFile = 0
    if os.path.exists(folder):
        files = os.listdir(folder)
        files.sort()
        for possibleFile in files:
            if possibleFile.startswith(prefix) and possibleFile.endswith(suffix):
                #print(possibleFile)
                lastFile = possibleFile
    else:
        print("!!! Directory '%s' couldn't be found when searching for file with prefix '%s'and suffix '%s'" % (folder, prefix,suffix))
    return lastFile


def processLineOfInputIntoStruct(line,struct):
    rulePassword = line.split(":",2)
    ruleLetterMinMax = rulePassword[0].split(" ",2)
    ruleMinMax = ruleLetterMinMax[0].split("-",2)
    #struct.append(ruleMinMax)
    struct.append((ruleLetterMinMax[1].strip(),int(ruleMinMax[0].strip()),int(ruleMinMax[1].strip()),rulePassword[1].strip()))

def processInputFile(filePath):
    
    struct = []
    if os.path.exists(filePath):
        f = open(filePath, "r")
        for x in f:
            processLineOfInputIntoStruct(x,struct)
    return struct

def processStruct(struct):
    validValues = []
    for value in struct:
        countVal = value[3].count(value[0])
        if (countVal >= value[1]) and (countVal <= value[2]) :
            validValues.append(value[3])
    print(validValues)
    print(len(validValues))

def mainTask():

    input_path = "C:\\Users\\gibbens\\Documents\\Arduino\\AdventOfCode2020\\02a\\tool_src\\input.txt"

    struct = processInputFile(input_path)
    processStruct(struct)


if __name__ == "__main__":

    mainTask()