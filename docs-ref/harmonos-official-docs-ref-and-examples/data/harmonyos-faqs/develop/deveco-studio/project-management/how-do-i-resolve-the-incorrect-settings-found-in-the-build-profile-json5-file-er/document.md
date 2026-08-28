# How do I resolve the "Incorrect settings found in the build-profile.json5 file" error during a project check?

**Solution**

1.  Check the project-level **build-profile.json5** file against the following specifications. Pay special attention to the positions and formats of **compatibleSdkVersion**, **targetSdkVersion**, and **runtimeOS**.
    
    {
      "app": {
        "signingConfigs": \[\],
        "products": \[
          {
            "name": "default",
            "signingConfig": "default",
            "compatibleSdkVersion": "4.0.0(10)", //Specify the minimum version compatible with HarmonyOS applications/services. The version number needs to be changed to "4.0.0 (10)", please use English carefully And ()
            "targetSdkVersion": "4.0.0(10)",     //Specify the target version for HarmonyOS applications/services. If not set, the default is compatibleSdkVersion
            "runtimeOS": "HarmonyOS",            //Designated as HarmonyOS/OpenHarmony
          }
        \],
        // ...
    }
    
2.  Make sure **runtimeOS** is configured under **products** in the project-level **build-profile.json5** file. Check for and delete the **runtimeOS** configuration from all module-level **build-profile.json5** files.
