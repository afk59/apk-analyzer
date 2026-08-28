# Debugging Failure Error Codes

#### 00403001 Failed to Parse the Offline HiLog File

**Error Message**

Failed to parse the HiLog file: XXX.

**Symptom**

Failed to parse the offline HiLog file.

**Possible Causes**

Failed to parse the offline HiLog file.

**Solution**

Reselect a valid offline HiLog file.

#### 00403003 Failed to Parse the App Stack

**Error Message**

Error messages related to app stack parsing vary by specific case.

**Symptom**

An error occurs during app stack parsing.

**Possible Causes**

The cause depends on the specific error message.

**Solution**

Follow the instructions in [What should I do if error messages related to stack trace analysis for release applications are displayed](https://developer.huawei.com/consumer/en/doc/harmonyos-faqs/faqs-app-debugging-17).

#### 00403028 App Terminates Unexpectedly

**Error Message**

App have been shutdown unexpectedly.

**Symptom**

The app terminates unexpectedly.

**Possible Causes**

The debug service terminates because the app process terminates unexpectedly.

**Solution**

Restart debugging.

#### 00403029 Empty sourceMaps.map File

**Error Message**

The JSON content is empty when the sourceMaps.map file is read.

**Symptom**

The JSON content is empty when the **sourceMaps.map** file is read.

**Possible Causes**

The **sourceMaps.map** file contains no valid JSON data.

**Solution**

Choose **Build** > **Clean Project** on the menu bar to clear the cache and try again.

#### 00403030 Failed to Connect to the WebSocket Server

**Error Message**

Failed to connect to the WebSocket. Restart the debugging. If the problem persists, restart DevEco Studio and start debugging again.

**Symptom**

Failed to establish a WebSocket connection.

**Possible Causes**

1.  The WebSocket connection between DevEco Studio and the target device failed.
2.  For a 2-in-1 device, the app acceleration service may be enabled.

**Solution**

1.  Restart debugging. If the issue persists, restart DevEco Studio and start debugging again.
2.  For a 2-in-1 device, go to **Settings** > **Apps & services** > **App acceleration** and disable the app acceleration service.

#### 00403031 Invalid Process PID

**Error Message**

The process has invalid pid.

**Symptom**

The process PID is invalid.

**Possible Causes**

The process PID fails to be obtained.

**Solution**

Restart debugging.

#### 00403032 Failed to Connect to the Debug Server

**Error Message**

Failed to connect to the debug server. Try again. If the issue persists, collect logs and choose Help > Contact Support for assistance.

**Symptom**

Failed to connect to the debug server.

**Possible Causes**

The connection to the Panda debug server failed.

**Solution**

Try the operation again. If the issue persists, collect logs and choose **Help** to contact technical support.

#### 00403033 Failed to Obtain ROM Image Version

**Error Message**

Failed to obtain the ROM image version.

**Symptom**

Failed to obtain the ROM image version from the device.

**Possible Causes**

The device connection is abnormal.

**Solution**

Reconnect the device, or run the **hdc kill -r** command to restart the hdc process, and try again.

#### 00403043 Failed to Start the Previewer

**Error Message**

Failed to start the Previewer. Try again. If the issue persists, collect logs and choose Help > Contact Support for assistance.

**Symptom**

Failed to start the Previewer.

**Possible Causes**

The Previewer fails to be started.

**Solution**

Try the operation again. If the issue persists, collect logs and choose **Help** to contact technical support.

#### 00403044 Failed to Start the Simulator

**Error Message**

Failed to start the simulator. Try again. If the issue persists, collect logs and choose Help > Contact Support for assistance.

**Symptom**

Failed to start the Simulator.

**Possible Causes**

The Simulator fails to be started.

**Solution**

Try the operation again. If the issue persists, collect logs and choose **Help** to contact technical support.

#### 00403045 Compilation Failed

**Error Message**

Compilation failed.

**Symptom**

The compilation process failed.

**Possible Causes**

The compilation process failed.

**Solution**

Choose **Build** > **Clean Project** on the menu bar to clear the cache and try again.

#### 00403046 Jerry Adapter File Not Found

**Error Message**

Jerry adapter file not found.

**Symptom**

The Jerry adapter file cannot be found.

**Possible Causes**

The required Jerry adapter file is missing from the DevEco Studio installation directory.

**Solution**

[Download and install DevEco Studio](https://developer.huawei.com/consumer/en/download/deveco-studio) from the official website.

#### 00403047 Invalid Node.js Path

**Error Message**

Node path is invalid.

**Symptom**

The Node.js path is invalid.

**Possible Causes**

The Node.js path cannot be obtained.

**Solution**

Check whether the Node.js tool exists in the **tools** directory under the DevEco Studio installation directory. If it does not exist, [download DevEco Studio](https://developer.huawei.com/consumer/en/download/deveco-studio) again from the official website.

#### 00403048 Failed to Start webpack

**Error Message**

Unable to start webpack.

**Symptom**

Failed to start the webpack service.

**Possible Causes**

The webpack service fails to be started.

**Solution**

Choose **Build** > **Clean Project** on the menu bar to clear the cache and try again. If the issue persists, restart DevEco Studio.

#### 00403049 Previewer Plugin Not Fully Installed

**Error Message**

The Previewer plugin not fully installed. Please verify.

**Symptom**

The Previewer plugin is not fully installed.

**Possible Causes**

The Previewer plugin is not fully installed.

**Solution**

[Download and install DevEco Studio](https://developer.huawei.com/consumer/en/download/deveco-studio) from the official website.

#### 00403050 Jerry Adapter Fails to Connect to the Server

**Error Message**

Jerry Adapter fails to connect to the engine.

**Symptom**

The Jerry adapter fails to connect to the server.

**Possible Causes**

The Jerry debugging connection fails.

**Solution**

Choose **Build** > **Clean Project** on the menu bar to clear the cache and try again. If the issue persists, restart DevEco Studio.

#### 00403051 Jerry Debug Engine Stops Abnormally

**Error Message**

Adapter server or engine stopped abnormally.

**Symptom**

The Jerry debug engine stops abnormally.

**Possible Causes**

The Jerry debug engine stops abnormally.

**Solution**

Choose **Build** > **Clean Project** on the menu bar to clear the cache and try again. If the issue persists, restart DevEco Studio.
