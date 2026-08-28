# How do I resolve the "Cannot depend on HAP modules outside of this project" error?

**Symptom**

The "Cannot depend on HAP modules outside of this project" error is reported during compilation.

**Possible Causes**

In the **build-profile.json5** file located in the project root directory, the value of the **srcPath** field contains a reference to a HAP module outside of the current project.

**Solution**

Replace any references to HAP modules outside of the current project with references to HSP or HAR modules.
