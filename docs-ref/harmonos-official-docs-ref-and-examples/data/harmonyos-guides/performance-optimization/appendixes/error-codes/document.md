# Error Codes

#### 00701101 App Launch Failure

**Error Message**

Failed to start this app. If the app is of the release type, make sure you have enabled it to be started. For more details, see the logs.

**Symptom**

The app cannot be launched normally.

**Possible Causes**

Recording for the launch analysis automatically launches the app, during which the device is disconnected.

**Solution**

Reconnect the device and restart the recording.

#### 00701102 App Startup Failure

**Error Message**

App not started correctly. Start a new session and try again.

**Symptom**

The app failed to be started.

**Possible Causes**

During the recording for the launch analysis, the device disconnected when the app icon was tapped to launch the app.

**Solution**

Reconnect the device and restart the recording.

#### 00701202 Data File Import Failure

**Error Message**

Failed to import data file. Please check file version or storage space.

**Symptom**

Failed to import the data file due to version mismatch or insufficient disk space.

**Possible Causes**

1.  Version mismatch. The DevEco Studio version required for the data file import is incompatible with the current DevEco Studio version.
2.  Insufficient disk space.

**Solution**

1.  Import the data file using a version of DevEco Studio that matches or is higher than the version used for export.
2.  Free up the disk space.

#### 00702101 Offline Symbol Parsing Failure

**Error Message**

Failed to import offline symbols. Verify the offline symbol files.

**Symptom**

The offline symbol parsing failed.

**Possible Causes**

The imported .so library does not match the captured .so library.

**Solution**

Import the corresponding .so library that contains the symbol table information for parsing.

#### 00702102 Imported File Size Exceeds the Limit

**Error Message**

The imported file exceeds maximum size limit.

**Symptom**

The size of the imported file exceeds the limit.

**Possible Causes**

The imported file is too large in size.

**Solution**

Import a file that complies with the size limit.

#### 00702103 Incorrect Format of the Imported .jsleaklist File

**Error Message**

Invalid files: {0}.

**Symptom**

The format of the imported **.jsleaklist** file is incorrect.

**Possible Causes**

The format of the imported **.jsleaklist** file is incorrect.

**Solution**

Import a **.jsleaklist** file with the correct format.

#### 00702104 Mismatch Between the Imported .jsleaklist File and .heapsnapshot/.rawheap File

**Error Message**

Unmatched files: {0}.

**Symptom**

The imported **.jsleaklist** file does not match the imported **.heapsnapshot** or **.rawheap** file.

**Possible Causes**

The imported **.jsleaklist** file does not match the imported **.heapsnapshot** or **.rawheap** file.

**Solution**

Import a **.jsleaklist** file that matches the **.heapsnapshot** or **.rawheap** file.

#### 00702106 Expired CodeGenie Authorization

**Error Message**

The authentication information has expired. Please sign in again.

**Symptom**

The CodeGenie authorization has expired. Sign in again.

**Possible Causes**

The CodeGenie authorization has expired.

**Solution**

Sign in again.

#### 00702201 Offline Symbol Parsing Failure

**Error Message**

Failed to import offline symbols.

**Symptom**

The offline symbol parsing failed.

**Possible Causes**

The imported .so library does not contain the symbol table information.

**Solution**

Import a .so library that contains the correct symbol table information.

#### 00702203 Failed to Start Recording

**Error Message**

Since no Running Application is selected, recording cannot be started. Please select a Running Application first.

**Symptom**

The target app for debugging is not running, and the recording cannot start. Select a running app.

**Possible Causes**

The target app for debugging is not running.

**Solution**

Run the target app for debugging before starting the recording.

#### 00702204 Button-based Navigation Failure

**Error Message**

The corresponding slice is not available in the current view.

**Symptom**

Navigation triggered by a button tap failed.

**Possible Causes**

The target lane for navigation does not exist in the current file.

**Solution**

Record again. Ensure that the recording file contains the target lane for navigation.

#### 00702205 Maximum Session Limit Reached

**Error Message**

Maximum number of sessions reached. Delete some sessions and try again.

**Symptom**

The number of created sessions has reached the maximum limit.

**Possible Causes**

The number of created sessions has reached the maximum limit.

**Solution**

Clean up the created sessions.

#### 00702206 Lane Does Not Exist

**Error Message**

The lane does not exist. Please upgrade the DevEco Studio.

**Symptom**

The lane contained in the imported data file does not exist in the current version of DevEco Studio.

**Possible Causes**

Version mismatch. The lane contained in the imported data file does not exist in the current version of DevEco Studio.

**Solution**

Import the data file using a version of DevEco Studio that matches or is higher than the version used for export.

#### 00702208 Device Screen Locked

**Error Message**

Unlock the device and try again.

**Symptom**

The device screen is locked.

**Possible Causes**

The device is protected by a screen lock password and remains locked, preventing the app from being launched during recording.

**Solution**

Unlock the device and record again.

#### 00702209 Concurrent Import of .heapsnapshot and .rawheap Files Not Allowed

**Error Message**

The .heapsnapshot and .rawheap files cannot be imported at the same time.

**Symptom**

The .heapsnapshot and .rawheap files cannot be imported at the same time.

**Possible Causes**

The .heapsnapshot and .rawheap files are imported at the same time.

**Solution**

Import the .heapsnapshot and .rawheap files separately.

#### 00702210 Insufficient Permissions for the Data Export Directory

**Error Message**

The selected directory has no permissions.

**Symptom**

Insufficient permissions to access the target directory for saving files.

**Possible Causes**

Insufficient permissions to access the selected directory during data export.

**Solution**

Select a directory with sufficient permissions for data export.

#### 00702211 Imported File Count Exceeds the Limit

**Error Message**

Only a single .insight/.ftrace/.htrace/.nas/.txt/.perfdata/.data/.sys file or 1-10 .heapsnapshot/.jsleaklist/.rawheap files are allowed to be imported.

**Symptom**

The number of imported files exceeds the limit. Only one **.insight**, **.ftrace**, **.htrace**, **.nas**, **.txt**, **.perfdata**, **.data**, or **.sys** file can be imported, or a maximum of 10 **.heapsnapshot**, **.jsleaklist**, or **.rawheap** files can be imported.

**Possible Causes**

The number of imported files exceeds the limit.

**Solution**

Import one **.insight**, **.ftrace**, **.htrace**, **.nas**, **.txt**, **.perfdata**, **.data**, or **.sys** file, or a maximum of 10 **.heapsnapshot**, **.jsleaklist**, or **.rawheap** files.

#### 00702212 Disallowed Characters in the File Name During Export

**Error Message**

Make sure the file name does not contain the following characters:\* : ? " < > |

**Symptom**

The file name contains disallowed characters (such as **\***, **:**, **?**, **"**, **<**, **\>**, and **|**) during export.

**Possible Causes**

The file name contains disallowed characters (such as **\***, **:**, **?**, **"**, **<**, **\>**, and **|**) during export.

**Solution**

Ensure that the file name does not contain the following characters during export: **\***, **:**, **?**, **"**, **<**, **\>**, and **|**.

#### 00702213 File Name Exceeds the Length Limit During Export

**Error Message**

Make sure that the file name does not exceed 238 characters.

**Symptom**

The file name exceeds the 238-character limit during export.

**Possible Causes**

The file name exceeds the 238-character limit during export.

**Solution**

Ensure that the file name does not exceed 238 characters during export.

#### 00702214 Save Path Does Not Exist

**Error Message**

Invalid save path: {0}

**Symptom**

The specified save path does not exist.

**Possible Causes**

The specified save path does not exist.

**Solution**

Verify that the save path exists before saving.

#### 00703201 Recording File Too Large to Parse

**Error Message**

The recording file is too large and cannot be parsed. Restart a new recording session with shorter duration.

**Symptom**

The recording file is too large, causing the parsing to fail. Reduce the recording duration and start a new recording session.

**Possible Causes**

The recording file is too large, causing the parsing to fail.

**Solution**

Reduce the recording duration and start a new recording session.

#### 00703202 Profiler Memory Allocation Limit Exceeded

**Error Message**

The memory allocated to Profiler has reached the upper limit. To maintain normal operation, consider increasing the heap size.

**Symptom**

The memory allocated to the Profiler has reached the upper limit. To maintain normal operation, consider increasing the heap size.

**Possible Causes**

The memory allocated to the Profiler has reached the upper limit, preventing normal operation.

**Solution**

Manually increase the maximum memory available to the virtual machine in the DevEco Studio configuration file. For details, see [What should I do if DevEco Studio cannot run properly due to high memory usage](https://developer.huawei.com/consumer/en/doc/harmonyos-faqs/faqs-profiler-3).

#### 00703204 Recorded Data Mismatch with the Opened Source Project

**Error Message**

Unable to navigate to source code. Make sure the SymbolTable file exists in the corresponding module directory and the recorded data matches the source code project, and then rebuild the project.

**Symptom**

The recorded data does not match the source code project opened in the current DevEco Studio window.

**Possible Causes**

The recorded data does not match the source code project opened in the current DevEco Studio window, preventing correct navigation to the source code.

**Solution**

Verify that the recorded app matches the project opened in the current DevEco Studio window.

#### 00703205 Navigation to the Corresponding Source Code Failed

**Error Message**

Source file not found.

**Symptom**

Navigation to the corresponding source code failed.

**Possible Causes**

The source code to which the recorded data needs to navigate does not exist.

**Solution**

Verify that the recorded app matches the project opened in the current DevEco Studio window.

#### 00703301 Failed to Stop Recording

**Error Message**

Failed to stop the session.

**Symptom**

Failed to stop the recording session.

**Possible Causes**

An error occurs in the plugin during the recording stop process.

**Solution**

Start a new recording session after the current one ends.
