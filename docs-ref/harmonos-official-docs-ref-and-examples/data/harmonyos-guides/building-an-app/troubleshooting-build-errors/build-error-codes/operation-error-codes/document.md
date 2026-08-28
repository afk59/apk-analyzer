# Operation Error Codes

#### 00308001 Failed to Delete the File

**Error Message**

Failed to delete the file: XXX.

**Symptom**

File deletion failed.

**Possible Causes**

1.  The file does not exist.
2.  The user does not have the permission to delete the file.
3.  The file is locked by another process.

**Solution**

1.  Verify that the file exists at the specified path.
2.  Ensure that the current user has the permission to delete the file.
3.  Check if the file is locked by another process. If yes, wait until it is released and try again.
4.  Try manually deleting the file.

#### 00308002 Failed to Run the Command During Hvigor Environment Initialization

**Error Message**

XXX execute failed.

**Symptom**

The command fails to be executed during Hvigor environment initialization.

**Possible Causes**

The cause varies in different scenarios. For details, see the error message.

**Solution**

Troubleshoot based on the error message.

#### 00308003 Hvigor Entry File Not Found

**Error Message**

ENOENT: no such file XXX.

**Symptom**

The Hvigor entry file cannot be found.

**Possible Causes**

Some misoperations damage the integrity of Hvigor.

**Solution**

Delete the **\\.hvigor\\project\_caches\\**_xxxxxxxx_**\\workspace** directory and try again.

#### 00308004 Failed to Delete the build Directory

**Error Message**

Unable to delete XXX.

**Symptom**

The **build** directory fails to be deleted.

**Possible Causes**

One or more files in the directory are in use.

**Solution**

Close the files in use and try again.

#### 00308005 Failed to Write the File

**Error Message**

Write file failed: XXX, at file: YYY.

**Symptom**

Failed to write the file.

**Possible Causes**

-   The file does not exist.
-   The user does not have the permission to write the file.
-   The file is in use.

**Solution**

-   Ensure that the file exists.
-   Request the permission to write the file.
-   Close the file in use and try again.

#### 00308006 Encryption or Decryption Failure

**Error Message**

Encryption and decryption errors occur. The specific error message depends on the situation.

**Symptom**

Encryption and decryption errors occur.

**Possible Causes**

Unknown.

**Solution**

[Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei technical support will get back to you as soon as possible.

#### 00308007 File Operation Failed

**Error Message**

Failed to operate file as XXX.

**Symptom**

File operation failed.

**Possible Causes**

The current user does not have the permission to operate the file, or the specified file path is invalid.

**Solution**

1.  Grant the current user appropriate permissions for the file.
2.  Ensure the file path is correct and accessible.

#### 00308008 Failed to Write the File

**Error Message**

Failed to write File: XXX.

**Symptom**

Failed to write the file.

**Possible Causes**

The file permission is incorrect, the path is incorrect, or the disk space is insufficient.

**Solution**

1.  Request the permission to write the file.
2.  Configure a correct and valid file path.
3.  Delete unnecessary files to ensure sufficient disk space.

#### 00308009 File Write Failure Due to File Not Found

**Error Message**

Failed to write File: please check File Path: XXX.

**Symptom**

The file fails to be written because it cannot be found.

**Possible Causes**

The file path is incorrect, or the file does not exist.

**Solution**

Configure a correct and valid file path.

#### 00308010 Failed to Execute the pnpm store prune Command

**Error Message**

Error: pnpm store prune execute failed.

**Symptom**

Failed to execute the **pnpm store prune** command.

**Possible Causes**

You do not have the permissions to modify or delete files when running the **pnpm store prune** command.

**Solution**

Ensure that you have sufficient permissions to operate the pnpm cache directory in the user directory.

#### 00308013 Failed to Delete the Directory

**Error Message**

Failed to delete the directory: XXX.

**Symptom**

Failed to delete the directory.

**Possible Causes**

1.  The user does not have the permission to delete the directory.
2.  One or more files in the directory are in use by another process.

**Solution**

1.  Request the permission to delete the directory.
2.  Close the files in use and try again.

#### 00308014 Failed to Copy the File

**Error Message**

Failed to copy the file: XXX.

**Symptom**

Failed to copy the file.

**Possible Causes**

1.  The file to be copied does not exist.
2.  The user does not have the permission to read the file.

**Solution**

1.  Ensure that the file exists and request the permission to read the file.
2.  If the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei will get back to you as soon as possible.

#### 00308015 Failed to Copy the Folder

**Error Message**

Failed to copy the directory: XXX.

**Symptom**

Failed to copy the folder.

**Possible Causes**

1.  The folder to be copied does not exist.
2.  The user does not have the permission to read the folder.

**Solution**

1.  Ensure that the folder exists and request the permission to read the folder.
2.  If the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei will get back to you as soon as possible.

#### 00308017 Cache Material Error

**Error Message**

Cache material error. Please ensure that no cache materials have been added or modified in the meta/ac, ce, and fd directories. At file: XXX.

**Symptom**

A cache material error occurs due to added or modified cache materials in the **meta/ac**, **meta/ce**, or **meta/fd** directories.

**Possible Causes**

The cache materials are added or modified by mistake.

**Solution**

1.  Check the number of cache materials in the **.hvigor/meta** directory under **Users/_username_** to confirm it is correct: there should be 1, 1, and 3 files or folders in the **ac**, **ce**, and **fd** directories, respectively. Ensure no additions or modifications have been made to the content of these folders.
2.  Delete the **meta** directory under **.hvigor** and recompile.
