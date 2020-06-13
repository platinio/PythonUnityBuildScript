using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using UnityEditor;
using UnityEngine;
using System;
using System.Threading;


public class BuildTool
{
    [MenuItem("Platinio/Build")]
    public static void PerformBuildAndroid()
    {
        string[] scenes = { "Assets/Main/Scenes/Main.unity" };
        string path = "./Builds/" + DateTime.Now.ToString("MM-dd-yy-HH-mm-ss") + ".apk";        
        BuildPipeline.BuildPlayer(scenes, path , BuildTarget.Android , BuildOptions.Development);


        Thread.Sleep(5000);
        while (BuildPipeline.isBuildingPlayer)
            Thread.Sleep(2000);

        Process.Start(@Application.dataPath + "/../Builds");

    }
}
