# Permission Error Codes

#### 00307001 Failed to Create or Write a File

**Error Message**

EPERM: operation not permitted,create XXX failed.

**Symptom**

Failed to create or write file _XXX_.

**Possible Causes**

Users do not have the permission to create or write files.

**Solution**

Request the permissions to create and write files.

#### 00307003 Incorrect bundleType of the HSP Dependency Package

**Error Message**

The currentBundleType is shared, but the Package XXX bundleType is not shared.

**Symptom**

**bundleType** of the project is **shared**, but the **bundleType** of package _XXX_ is not.

**Possible Causes**

**bundleType** in the **app.json5** file of the project is **shared**, but the **bundleType** of the dependency package is not.

**Solution**

Remove the dependency package.
