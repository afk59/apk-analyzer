# How do I resolve the "The useNormalizedOHMUrl settings of packages xxx and the project useNormalizedOHMUrl: xxx do not match" error?

**Symptom**

The error message "The useNormalizedOHMUrl settings of packages xxx and the project useNormalizedOHMUrl: xxx do not match" is displayed during compilation.

**Solution**

When **useNormalizedOHMUrl** is set to **true**, the ohmurl uses a new method of concatenation and parsing. As such, it cannot be mixed with the old ohmurl; otherwise, it cannot be recognized at runtime.

You can resolve this issue in two ways:

-   Modify the **useNormalizedOHMUrl** field in the project-level **build-profile.json5** file of the problematic dependency package to be consistent with the current project. Then, regenerate the dependency package and replace the original one (the default value for **useNormalizedOHMUrl** is **false**).
    
    {
      "app": {
        "signingConfigs": \[\],
        "products": \[
          {
            // ...
            "buildOption": {
              "strictMode": {
                "useNormalizedOHMUrl": true
              }
            }
          }
        \],
        // ...
    }
    
-   If there are multiple dependency packages that are inconsistent with the project, you are advised to change the value of **useNormalizedOHMUrl** in the project-level **build-profile.json5** file and replace all inconsistent dependency packages.

If the issue persists, the HSP is a local package. In this case, import the HSP by adding it to **modules** in the project-level **build-profile.json5** file. The following is an example:

"modules": \[
  {
    name: "hsp",   // The referenced hsp package dependency
    srcPath: "../MyApplication\_stageB/hsp",   // The path to the hsp package being referenced (both absolute and relative paths are okay)
  }
\],

**Reference**

[Module-level build-profile.json5 File](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-hvigor-build-profile)
