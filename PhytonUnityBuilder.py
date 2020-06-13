import os
import time
import threading
import glob

unityPath = r'"C:\Program Files\Unity\Hub\Editor\2019.3.4f1\Editor\Unity.exe"';
projectPath = r'"C:\Users\Admin\Documents\Repository\moster-fall"';
buildMethodName = 'BuildTool.PerformBuildAndroid -fileName "file name"';
adbPath = "c:/android-sdk/platform-tools";
buildsFolder = "C:/Users/Admin/Documents/Repository/moster-fall/Builds/*";
packageName = "com.Platinio.NightFall";
installCommand = unityPath +" -quit -batchmode -projectPath "+ projectPath +" -executeMethod " + buildMethodName;

global isInstalling;
isInstalling = True;



def getUnityBuild():
    error = os.system('cmd /c "'+ installCommand +'"');
    error = 0;
    global isInstalling;
    isInstalling = False;
    return error;
    

def loadAnimation():
    animation = "|/-\\"
    idx = 0
    global isInstalling;
    while isInstalling:
        print(animation[idx % len(animation)], end="\r")
        idx += 1
        time.sleep(0.1)
def setIsInstalling():
    global isInstalling;
    isInstalling = False;

print("Unity build process started ");
thread = threading.Thread(target=loadAnimation, args=())
thread.daemon = True                          
thread.start();  
error = getUnityBuild();

if(error != 0):
    print("Build error with code " + error);   
else:
    
    list_of_files = glob.glob(buildsFolder) # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    latest_file = latest_file.replace("\\" , "/");
    latest_file = latest_file.replace("/" , "\\");

    cdCommand = "cd " + adbPath;
    adbUninstall = "adb uninstall " + packageName;
    adbInstall = "adb install " + latest_file;
    
    os.chdir(adbPath);
    os.system('cmd /c "'+ adbUninstall +'"');

    os.chdir(adbPath);
    os.system('cmd /c "'+ adbInstall +'"');
    
    runAppCommand = "adb shell monkey -p "+ packageName + " -v 1 ";
    os.chdir(adbPath);
    os.system('cmd /c "'+ runAppCommand +'"');

    print("your app is running :)");

    




