# Debugging and Verification

The test cases are classified by preset condition.

**Preset condition 1:**

1.  The Huawei Health app has been installed on a phone and you have signed in to the app with a HUAWEI ID.
2.  Your app has been installed on the phone.

| 
Test Case

 | 

Procedure

 | 

Expected Result

 |
| :-- | :-- | :-- |
| 

Launching the user authorization screen

 | 

1.  Open your app on the phone and call the user authorization API.
2.  On the user authorization screen, select the required permissions.
3.  Confirm the authorization at the bottom of the screen.
4.  Call the API for a certain permission granted in Step 3.

 | 

-   In Step 2, the user authorization screen is displayed.
-   In Step 4, the error message "The HUAWEI ID is not authorized" is not returned when the API is called.

 |

**Preset condition 2:**

1.  The Huawei Health app has been installed on a phone and you have signed in to the app with a HUAWEI ID.
2.  Your app has been installed on the phone.
3.  Your app has been installed on the wearable device.
4.  The wearable device has been paired with and connected to the Huawei Health app.
5.  Permissions have been granted to your app.

| 
Test Case

 | 

Procedure

 | 

Expected Result

 |
| :-- | :-- | :-- |
| 

Obtaining information about paired wearable devices

 | 

Your phone app calls the API for the paired devices.

 | 

The API is successfully called and information about the paired wearable devices is returned.

 |
| 

Launching the wearable app from the phone

 | 

Your phone app calls [startRemoteApp](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section169404201361) to launch the wearable app.

 | 

The API is successfully called to launch the wearable app and returns result code **201** or **202**.

 |
| 

Pinging the connection with the phone from the wearable device

 | 

Your wearable app calls the API for pinging the connection with the phone app.

 | 

The API is successfully called to ping the connection with the phone app and returns the result code **205**.

 |
| 

Sending messages from the phone to the wearable device

 | 

1.  Your wearable app calls the API for registering a message receiver.
2.  Your phone app calls the API for sending messages to the wearable app.
3.  Verify that the message received by your wearable app is consistent with that sent by the phone app.
4.  Your wearable app calls the API for deregistering the message receiver.
5.  Your phone app calls the API for sending messages to the wearable device.
6.  Check whether the wearable device has received the message.

 | 

-   In Step 2, your phone app successfully sends the message, the sending progress is displayed as **100**, and the return code is **207**.
-   In Step 3, the message received by your wearable app is consistent with that sent by the phone app.
-   In Step 5, your phone app fails to send the message, and the return code is **206**.
-   In Step 6, your wearable app does not receive the message.

 |
| 

Sending files from the phone to the wearable device

 | 

1.  Your wearable app calls the API for registering a file receiver.
2.  Your phone app calls the API for sending files to the wearable app.
3.  Verify that the file received by your wearable app is consistent with that sent by the phone app.
4.  Your wearable app calls the API for deregistering the file receiver.
5.  Your phone app calls the API for sending files to the wearable device.
6.  Check whether the wearable device has received the file.

 | 

-   In Step 2, your phone app successfully sends the file, the sending progress is displayed as **100**, and the return code is **207**.
-   In Step 3, the file received by your wearable app is consistent with that sent by the phone app. (Demo on the wearable device is used.)
-   In Step 5, your phone app fails to send the file, and the return code is **206**.
-   In Step 6, your wearable app does not receive the file.

 |
| 

Sending messages from the wearable device to the phone

 | 

1.  Your phone app calls the API for registering a message receiver.
2.  Your wearable app calls the API for sending messages to the phone app.
3.  Verify that the message received by your phone app is consistent with that sent by the wearable app.
4.  Your phone app calls the API for deregistering the message receiver.
5.  Your wearable app calls the API for sending messages to the phone app.
6.  Check whether the phone has received the message.

 | 

-   In Step 2, your wearable app successfully sends the message, the sending progress is displayed as **100**, and the return code is **207**.
-   In Step 3, the message received by your phone app is consistent with that sent by the wearable app.
-   In Step 5, your wearable app fails to send the message, and the return code is **206**.
-   In Step 6, your phone app does not receive the message.

 |
| 

Sending files from the wearable device to the phone

 | 

1.  Your phone app calls the API for registering a file receiver.
2.  Your wearable app calls the API for sending files to the phone app.
3.  Verify that the file received by your phone app is consistent with that sent by the wearable app.
4.  Your phone app calls the API for deregistering the file receiver.
5.  Your wearable app calls the API for sending files to the phone app.
6.  Check whether your phone can receive the file.

 | 

-   In Step 2, your wearable app successfully sends the file, the sending progress is displayed as **100**, and the return code is **207**.
-   In Step 3, the file received by your phone app is consistent with that sent by the wearable app. (Demo on the phone is used.)
-   In Step 5, your wearable app fails to send the file, and the result code starting with "199" is returned.
-   In Step 6, your phone app does not receive the file.

 |
| 

Querying the status of the wearable device

 | 

Querying the battery level and wearing status is used as an example:

1.  Your phone app calls the API for querying the battery level of the wearable device.
2.  Put on the wearable device.
3.  Your phone app calls the API for querying the wearing status of the wearable device.
4.  Take off the wearable device from the wrist.
5.  Your phone app calls the API for querying the wearing status of the wearable device.

 | 

-   In Step 1, the battery level of the wearable device can be queried.
-   In Step 3, the device status queried by your phone app is that the wearable device is worn.
-   In Step 5, the device status queried by your phone app is that the wearable device is not worn.

 |
| 

Subscribing to the wearable device status

 | 

Subscribing to the connection status and wearing status is used as an example:

1.  Your phone app calls the API for subscribing to the wearing status of the wearable device.
2.  Keep your phone away from the wearable device until the phone is disconnected from the wearable device.
3.  Reconnect the phone to the wearable device.
4.  Your phone app calls the API for subscribing to the wearing status of the wearable device.
5.  Put on the wearable device.
6.  Take off the wearable device from the wrist.
7.  Your phone app unsubscribes from the connection status and wearing status.
8.  Take off the wearable device, and keep your phone away from the wearable device until the phone is disconnected from the wearable device.

 | 

-   In Step 2, your phone app receives a wearable device disconnection event.
-   In Step 3, your phone app receives a wearable device connection event.
-   In Step 5, your phone app receives an event that the wearable device is worn.
-   In Step 6, your phone app receives an event that the wearable device is removed.
-   In Step 8, your phone app does not receive an event that the wearable device is disconnected from the phone.

 |
| 

Sending notifications from the phone to the wearable device

 | 

1.  Your phone app calls the API for sending notifications to the wearable device.
2.  Verify that the notification received by your wearable app is consistent with that sent by the phone app.

 | 

In Step 2, the notification received by the wearable device is consistent with that sent by the phone, including the message content, title, and button.

 |

**Preset condition 3:**

1.  The Huawei Health app has been installed on a phone and you have signed in to the app with a HUAWEI ID.
2.  Your app has been installed on the phone.
3.  Your app has been installed on the wearable device.
4.  The wearable device has been paired with and connected to the Huawei Health app.
5.  Permissions have been granted to your app.

| 
Test Case

 | 

Procedure

 | 

Expected Result

 |
| :-- | :-- | :-- |
| 

Obtaining the list of sensors on the wearable device

 | 

Your phone app calls the API to obtain the list of sensors on the wearable device.

 | 

The API is successfully called to return the device sensor list (such as the ACC), including the sensor name, ID, type, precision, and resolution.

 |
| 

Reading the sensor data of the wearable device

 | 

1.  Your phone app calls the API to read the sensor data of the wearable device.
2.  Your phone app calls the API to stop reading the sensor data of the wearable device.

 | 

-   In Step 1, the API is successfully called. Your phone app receives data reported by the wearable device. The data includes both the value and the timestamp.
-   In Step 2, the API is successfully called. Your phone app no longer receives data reported by the wearable device.

 |
