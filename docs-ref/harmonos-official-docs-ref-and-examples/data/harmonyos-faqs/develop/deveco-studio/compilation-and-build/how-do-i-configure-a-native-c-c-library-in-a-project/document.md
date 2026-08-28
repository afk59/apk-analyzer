# How do I configure a native C/C++ library in a project?

Configure the following in the **products** field of the module-level **project-level build-profile.json5** file:

"products": \[
  {
    "name": "default",
    "signingConfig": "default",
    "compatibleSdkVersion": "5.0.5(17)",
    "targetSdkVersion": "5.0.5(17)",
    "runtimeOS": "HarmonyOS",
  }
\],
