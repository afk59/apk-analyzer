# Instrument Test Error Codes

#### 00501001 Variables Included in the Test Suite Name

**Error Message**

XXX is a Variable. Please use string as a describe name.

**Symptom**

The test suite name contains a variable. Use a string as the test suite name.

**Possible Causes**

The test suite name contains variables.

**Solution**

Use a string as the test case name.

#### 00501002 Invalid Characters Included in the Test Case Name

**Error Message**

XXX is an invalid it value. Enter a value that contains only digits, letters, underscores (\_), and periods (.) or run from a higher level portal.

**Symptom**

The test case name contains invalid characters. The name must contain only digits, letters, underscores (\_), or periods (.), or the test must be run from a higher-level entry point.

**Possible Causes**

The test case name contains invalid characters.

**Solution**

-   Ensure that the test case name contains only digits, letters, underscores (\_), or periods (.).
-   If the test case name contains invalid characters, run the test suite, test file, or test directory instead.

#### 00501003 Duplicate Test Case Name

**Error Message**

Testing failed due to the duplicate test case name XXX. The test case name must be unique in a test suite.

**Symptom**

The test case name is duplicated. Test case names must be unique within a test suite.

**Possible Causes**

Test cases with the same name exist within a test suite.

**Solution**

Ensure that test case names are unique within the test suite.

#### 00501004 Duplicate Test Suite Name

**Error Message**

Testing failed due to the duplicate test suite name XXX. The test suite name must be unique in a test package.

**Symptom**

The test suite name is duplicated. Test suite names must be unique within a test directory.

**Possible Causes**

Duplicate test suite names exist within the test directory.

**Solution**

Ensure that test suite names are unique within the test directory.

#### 00501005 Variables Included in the Test Case Name

**Error Message**

XXX is a Variable. Please use string as an It-name or execute from the higher running entrance.

**Symptom**

The test case name contains a variable. Use a string as the test case name, or run the test from a higher-level entry point.

**Possible Causes**

The test case name contains variables.

**Solution**

-   Use a string as the test case name.
-   If the test case name is a variable, run the test suite, test file, or test directory instead.

#### 00501006 Variables Included in the Test Case Name

**Error Message**

XXX is a Variable. Please use string as an It-name.

**Symptom**

The test case name contains a variable. Use a string as the test case name.

**Possible Causes**

The test case name contains variables.

**Solution**

-   Use a string as the test case name.
-   If the test case name is a variable, run the test suite, test file, or test directory instead.

#### 00501007 Invalid Test Suite Name

**Error Message**

XXX is an invalid describe value. The value entered must contain only digits, letters, underscores (\_), and periods (.) and can only start with a letter.

**Symptom**

The test suite name is invalid. The name must contain only digits, letters, underscores (\_), or periods (.), and must start with a letter.

**Possible Causes**

The test suite name is invalid.

**Solution**

Ensure that the test suite name contains only digits, letters, underscores (\_), or periods (.), and starts with a letter.

#### 00502001 Corresponding Test Case Not Found in the Test File

**Error Message**

Current test case XXX not found in the test file.

**Symptom**

The corresponding test case cannot be found in the test file.

**Possible Causes**

The corresponding test case cannot be found in the test file.

**Solution**

-   Ensure that you select the correct test case and re-run the test.
-   Modify **Method name** in the run configuration window.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/cmCF7mtsQhG2Uaym-qANig/en-us_image_0000002505148182.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A008ECD52BE56BEC83539877F1B9F86BB39AA4E783EFAAD6231DE303171ADEED)
    

#### 00502002 No Test Case Found

No Any Test Case Found In The XXX.

**Symptom**

No test case can be found in the specified target.

**Possible Causes**

No test case is defined in the test file.

**Solution**

Ensure that at least one test case exists in the test file.

#### 00502003 Test File Does Not Exist

**Error Message**

File does not exist: XXX.

**Symptom**

The test file does not exist.

**Possible Causes**

The test file may have been deleted or moved.

**Solution**

Select an existing file for the test.

#### 00502004 No Function Registered in List.test.ets for the Current File

**Error Message**

The current file does not have any function registered in the list file.

**Symptom**

None of the functions in the current file are registered in the **List.test.ets** file.

**Possible Causes**

None of the functions in the current file are registered in the **List.test.ets** file.

**Solution**

Register the functions in the **List.test.ets** file, as shown in the following example:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/GruOTko-Twu2VuvgsHhS0w/en-us_image_0000002537027959.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BD22D92665127EEEE3759D4A78A1665495391E602EC3AC8EF311305BEAADCEB5)

#### 00502005 No Function Registered in List.test.ets for the Current Test Package

**Error Message**

The current package does not have any function registered in the list file.

**Symptom**

None of the functions in the current test package are registered in the **List.test.ets** file.

**Possible Causes**

None of the functions in the current test package are registered in the **List.test.ets** file.

**Solution**

Register the functions in the **List.test.ets** file, as shown in the following example:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/FScvlNLeTTCKaEzqgtbCEg/en-us_image_0000002537147927.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6355C21A9EFE439A6641A8FDEE1EF3AB9FB6D396F3711A1FA4FB3A9DF40AFBD3)

#### 00502006 Function Not Registered in List.test.ets

**Error Message**

The function where the suite XXX is located is not registered in the ''List.test.ets'' file!

**Symptom**

The function where the test suite is located is not registered in the **List.test.ets** file.

**Possible Causes**

The function is not registered in the **List.test.ets** file.

**Solution**

Register the function in the **List.test.ets** file, as shown in the following example:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/nlfzjeb3TpK-Ux-Rocvlqw/en-us_image_0000002505308022.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3283B076D45B859C2FCBF0B4AAE8039D87C431B9F66582EB22D60269F705FA1B)

#### 00502007 Test Suite Not Found in the Test File

**Error Message**

Current suite XXX not found in the test file.

**Symptom**

The test suite cannot be found in the test file.

**Possible Causes**

The test suite does not exist in the test file.

**Solution**

-   Ensure that you select the correct test suite and re-run the test.
-   Modify **Suite name** in the run configuration window.

#### 00503001 Invalid HAP Name

**Error Message**

Invalid HAP file name.

**Symptom**

The HAP name is invalid.

**Possible Causes**

The HAP name contains invalid characters.

**Solution**

Ensure that the HAP name contains only digits, letters, underscores (\_), hyphens (-), or periods (.).

#### 00503002 File Not Found in the HAP

**Error Message**

The XXX file in the hap file does not exist.

**Symptom**

The file cannot be found in the HAP.

**Possible Causes**

The corresponding file does not exist in the HAP.

**Solution**

Rebuild the HAP.

#### 00503003 Empty File

**Error Message**

The XXX file is empty.

**Symptom**

The file is empty.

**Possible Causes**

The file in the HAP does not exist or has an incorrect format.

**Solution**

Rebuild the HAP.

#### 00504001 Test Suite Name Not Specified

**Error Message**

The 'Suite name' is not specified.

**Symptom**

The test suite name is not specified.

**Possible Causes**

No test suite is selected in the run configuration.

**Solution**

Select a test suite.

#### 00504002 Test Package Not Specified

**Error Message**

The 'Package' is not specified.

**Symptom**

The test package is not specified.

**Possible Causes**

No test package is selected in the run configuration.

**Solution**

Select a test package.

#### 00504003 Test Case Not Specified

**Error Message**

The 'Method name' is not specified.

**Symptom**

The test case is not specified.

**Possible Causes**

No test case is selected in the run configuration.

**Solution**

Select a test case.

#### 00504004 Test File Not Specified

**Error Message**

The 'File name' is not specified.

**Symptom**

The test file is not specified.

**Possible Causes**

No test file is selected in the run configuration.

**Solution**

Select a test file.

#### 00505001 Instrument Test Run Failure

**Error Message**

Instrumentation run failed due to XXX.

**Symptom**

The instrument test run has failed.

**Possible Causes**

The test suite contains **Promise(async, await)**.

**Solution**

Ensure that **Promise(async, await)** is not used in the test suite.

#### 00506001 Mismatch Between Returned and Expected Number of Instrument Tests

**Error Message**

XXX. Expected YYY tests, received ZZZ.

**Symptom**

An error occurs during the instrument test run.

**Possible Causes**

The number of tests returned does not match the expected number.

**Solution**

Make corrections based on the error message.

#### 00506002 No Test Results

**Error Message**

No test results because XXX.

**Symptom**

No test results are generated.

**Possible Causes**

The device screen is locked with a password and has not been unlocked.

**Solution**

Unlock the screen and run the test again.

#### 00506003 Failed to Execute the Historical Test Task

**Error Message**

Build history project failed.

**Symptom**

Execution of the historical test task failed.

**Possible Causes**

The historical task is no longer valid, or the execution environment has been modified.

**Solution**

Do not execute the historical task. Create a new one instead.

#### 00507001 Path Does Not Exist

**Error Message**

The path XXX does not exist. Check whether the hap/hsp package is signed.

**Symptom**

The path does not exist. Check whether the HAP/HSP package is signed.

**Possible Causes**

The corresponding HAP or HSP package is not signed.

**Solution**

Check whether the HAP/HSP package is signed. If not, [configure a debug signature](../../../../configuring-a-debug-signature/document.md).

#### 00507002 Invalid Value of scope

**Error Message**

scope=XXX is invalid. Enter a value that contains only digits, letters, underscores (\_), and periods (.). Use commas (,) to separate multiple test suites or test cases.

**Symptom**

The value of **scope** in the command is invalid. Enter a value containing only digits, letters, underscores (\_), or periods (.), and use commas (,) to separate multiple test suites or test cases.

**Possible Causes**

The value of **scope** in the command is invalid.

**Solution**

Set **scope** to a value containing only digits, letters, underscores (\_), or periods (.), and use commas (,) to separate multiple test suites or test cases.

#### 00507003 No Test Results Due to Failure to Unlock the Screen

**Error Message**

No test results because unlock screen failed in developer mode.

**Symptom**

No test results are generated due to the failure to unlock the screen.

**Possible Causes**

The device screen is locked with a password, and the attempt to unlock the screen failed.

**Solution**

Unlock the screen and run the test again.

#### 00507004 coverageFile Contains Paths Pointing to Files That Do Not Exist

**Error Message**

coverageFile contains a file that does not exist.

**Symptom**

The **coverageFile** parameter contains paths pointing to files that do not exist.

**Possible Causes**

The files pointed to by the paths in the **coverageFile** parameter do not exist.

**Solution**

Ensure that the files pointed to by the paths in the parameter value exist.

#### 00507005 Project Path Does Not Exist

**Error Message**

projectPath does not exist.

**Symptom**

The project path does not exist.

**Possible Causes**

The path specified in the **projectPath** parameter does not exist during the execution of the **hvigorw** command.

**Solution**

Ensure that the path specified in the parameter value exists.

#### 00507006 Report Path Does Not Exist

**Error Message**

reportPath does not exist.

**Symptom**

The report path does not exist.

**Possible Causes**

The path specified in the **reportPath** parameter does not exist during the execution of the **hvigorw** command.

**Solution**

Ensure that the path specified in the parameter value exists.

#### 00507007 Path Specified in coverageFile Does Not Exist

**Error Message**

coverageFile does not exist.

**Symptom**

The path specified in **coverageFile** does not exist.

**Possible Causes**

The path specified in the **coverageFile** parameter does not exist during the execution of the **hvigorw** command.

**Solution**

Ensure that the path specified in the parameter value exists.

#### 00507008 Failed to Obtain the Initial Coverage Data

**Error Message**

getInitCoverageData failed.

**Symptom**

Failed to obtain the initial coverage data.

**Possible Causes**

The **init\_coverage.json** file contains incorrect content.

**Solution**

Choose **Build** > **Clean Project** on the menu bar to clear the cache and run the test again.

#### 00507009 Failed to Obtain the JS Coverage Data

**Error Message**

getjsCoverageData failed.

**Symptom**

Failed to obtain the JS coverage data.

**Possible Causes**

The **js\_coverage.json** file contains incorrect content.

**Solution**

Choose **Build** > **Clean Project** on the menu bar to clear the cache and run the test again.

#### 00507010 Failed to Merge the Coverage Data

**Error Message**

merge coverageJson failed.

**Symptom**

Failed to merge the coverage data.

**Possible Causes**

The update to DevEco Studio 5.0.2 has altered the coverage data structure. As a result, the coverage data cannot be merged.

**Solution**

Use the coverage data generated by the same version of DevEco Studio for merging.

#### 00507011 Same Path Specified in include and exclude

**Error Message**

The same path defined in include and exclude list in coverage-filter.json5.

**Symptom**

The same path is specified in both the **include** and **exclude** parameters in the **coverage-filter.json5** file.

**Possible Causes**

The same path is specified in both the **include** and **exclude** parameters.

**Solution**

Ensure that different paths are specified for the **include** and **exclude** parameters.

#### 00507012 Failed to Generate the Coverage Report

**Error Message**

report failed, error: XXX.

**Symptom**

Failed to generate the coverage report.

**Possible Causes**

An exception occurs when the contents of the folder pointed to by **reportPath** are cleared during report generation.

**Solution**

Modify **reportPath** or manually clear the folder pointed to by **reportPath**.

#### 00507013 Failed to Connect to the Device

**Error Message**

\[Fail\]ExecuteCommand need connect-key? please confirm a device by help info.

**Symptom**

The device connection failed. Follow the prompts to establish a connection

**Possible Causes**

1.  No device is connected, or USB debugging is not enabled in **Developer options**.
2.  Multiple devices are connected when you run tests via the CLI.

**Solution**

1.  Connect to the device by referring to [Running Your App on a Local Real Device](../../../../running-your-app-on-a-local-real-device/document.md) and enable USB debugging in **Developer options**.
2.  Remove any extra connected devices to ensure only one device is connected.

#### 00508010 Failed to Generate the Coverage Report

**Error Message**

Coverage report generation failed! Please attempt to clean project first.

**Symptom**

Failed to generate the coverage report. Clean the project and retry.

**Possible Causes**

The coverage report cannot be generated.

**Solution**

Choose **Build** > **Clean Project** on the menu bar to clear the cache and try again.

#### 00508013 App Launch Timeout

**Error Message**

App launch timed out. Make sure the screen is unlocked.

**Symptom**

The app launch times out. Ensure that the screen is unlocked.

**Possible Causes**

The device screen is locked.

**Solution**

Unlock the device screen.

#### 00508014 The Previewer Does Not Support This App

**Error Message**

Previewer does not support this app.

**Symptom**

The Previewer does not support this app.

**Possible Causes**

The Previewer is used to run an instrument test.

**Solution**

The Previewer does not support instrument tests. Use a real device or an emulator to run the test.
