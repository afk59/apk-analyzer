# What should I do if the user directory does not contain an .npmrc file?

**Symptom**

During an attempt to create a project, the error message "Error: The hvigor depends on the npmrc file. Configure the npmrc file first." is displayed.

**Possible Causes**

The user directory does not contain an .npmrc file.

**Solution**

Create an .npmrc file in your user directory and configure the following information:

registry=https://repo.huaweicloud.com/repository/npm/
@ohos:registry=https://repo.harmonyos.com/npm/
