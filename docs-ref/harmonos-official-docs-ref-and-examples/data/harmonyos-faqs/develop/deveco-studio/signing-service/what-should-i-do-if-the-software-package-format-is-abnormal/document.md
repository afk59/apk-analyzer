# What should I do if the software package format is abnormal?

**Symptom**

1.  The error message "find zip central directory failed" is displayed during packaging and signing.
2.  The error message "ERROR - hap-sign-tool: error: cd end offset not equals to eocd offset,maybe this is a zip64 file" is displayed during packaging and signing.

**Possible Causes**

The HAP or APP file to be signed is not in .zip format. However, the SDK signing tool supports only the .zip format.

**Common Error Scenarios**

The size of the HAP file exceeds 4 GB, or the number of its files and directories exceeds 65,535, which exceeds the upper limit of the .zip format. As a result, the HAP file is compressed into a .zip64 file.

**Solution**

Reduce the size of the HAP file and the number of files and directories in the HAP file.
