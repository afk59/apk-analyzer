# What should I do if "No available entry module found" is reported during compilation?

**Symptom**

What should I do if the "No available entry module found" error occurs during DevEco Studio compilation?

**Solution**

During compilation, DevEco Studio checks whether an entry module is configured for feature modules and whether the configured entry module exists. If the issue occurs, perform the following:

1.  In the **build-profile.json5** file of the feature module, ensure that the value of the **entryModules** field is the same as the actual name of the entry module.
2.  In the **modules** field of the project-level **build-profile.json5** file, ensure that the feature module is located after the required entry module. DevEco Studio reads configurations in sequence during compilation. If the feature module is located before the entry module, an error is reported because the entry module is not read or configured. The build process is executed in sequence. As a result, the preceding module cannot obtain the configuration information of the subsequent module.
