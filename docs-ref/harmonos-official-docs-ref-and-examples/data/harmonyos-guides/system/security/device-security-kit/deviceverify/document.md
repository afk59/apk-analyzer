# DeviceVerify

#### Use Cases

An app calls the **getDeviceToken** API of Device Security Kit to obtain a device token. The app server uses the device token to request the Device Security server to query and manage the app status on the device. This enables apps to record and query app status on devices even if the persistent device identifiers are not available.

Based on the app status returned by the Device Security server, the app can determine whether it is installed on the device for the first time or whether the user has obtained coupons on the device, supporting new user acquisition campaigns.

#### Restrictions

The DeviceVerify capability does not support simulators. The supported devices include phones, tablets, PCs/2-in-1 devices, and wearables. Starting from version 5.1.1(19), TVs are also supported.

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/aeLAHNWBRn2GPuMCuj4TrQ/en-us_image_0000002515108441.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062006Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C1177D15F2CB512126C354E6A0544A04F958530266D00A9F41E6C9E2F7E9CDAD "Click to enlarge")

The process is as follows:

1.  Your app calls the **getDeviceToken** API of Device Security Kit to obtain a device token.
2.  Device Security Kit returns the device token.
3.  Your app sends the device token in a service request (for example, a coupon claiming request) to the app server.
4.  The app server sends DeviceVerify REST requests to the Device Security server to perform operations such as query the device marking status (for example, whether a coupon has been claimed) through the **getDeviceStatus** API and update the device marking status through the **setDeviceStatus** API.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/lv25V__2S4q0JCf3PJp88Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062006Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=22C95C346966273D01D0D2268DF1C409A1DD764B157585C070E63249BB5B0F9B)
    
    The Device Security server provides two bits for each app on each device to store and query the device marking status. The meanings of the two bits are defined by the app.
    
    For example, **bit0** can be used to indicate whether a device has claimed the new user gift. The value **false** indicates that the device has not claimed the new user gift, and the value **true** indicates that the device has claimed the new user gift. When a user claims the new user gift on a device, the app server queries the device marking status on the Device Security server and processes accordingly based on the value of **bit0**:
    
    -   If the value of **bit0** is **true**, the device has claimed the new user gift. The app server can reject the device's new user gift claiming request.
    -   If the value of **bit0** is **false**, the device has not claimed the new user gift. The app server can grant the new user gift to the device and call the device marking status update API of the Device Security server to change the value of **bit0** to **true**.
    
5.  The Device Security server returns a DeviceVerify response.
6.  The app server processes the service based on the response returned by the Device Security server.
7.  The app server returns a service response.

#### API Description

The following table lists DeviceVerify APIs, including ArkTS APIs and REST APIs. For more information about the APIs, please refer to [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/devicesecurity-arktsapi).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[getDeviceToken(): Promise<string>](https://developer.huawei.com/consumer/en/doc/harmonyos-references/devicesecurity-deviceverify-api#section102884586336)

 | 

Obtains the device token of a device.

 |
| 

[checkDeviceToken](https://developer.huawei.com/consumer/en/doc/harmonyos-references/devicesecurity-deviceverify-checkdevicetoken)

 | 

Checks the device token.

 |
| 

[getDeviceStatus](https://developer.huawei.com/consumer/en/doc/harmonyos-references/devicesecurity-deviceverify-getdevicestatus)

 | 

Obtains the device marking status.

 |
| 

[setDeviceStatus](https://developer.huawei.com/consumer/en/doc/harmonyos-references/devicesecurity-deviceverify-updatedevicestatus)

 | 

Sets the device marking status.

 |
| 

[delDeviceStatus](https://developer.huawei.com/consumer/en/doc/harmonyos-references/devicesecurity-deviceverify-deletedevicestatus)

 | 

Deletes the device marking status.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/8B1jBgU0QzGHLsIMg2NIzg/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062006Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5DBF86EAA2FF5AED839491ADAF57A23138A8C3E6EA3FA7146F415D8E73386E1E)

If the **getDeviceToken** API cannot obtain the device token due to unstable network or other reasons, your app should be able to handle the exception to prevent unavailability of basic functions that rely on the device token. For example, your app can call the **getDeviceToken** API again or use other risk control factors for check.

#### Development Procedure

## Client Development

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/JybDWdDWTumVer8F4BOEIA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062006Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F81FD3053E4069CC70501020DC1D182DC78F959BAB5F2A970451AA1163933183)

Ensure that you have [enabled DeviceVerify](../preparations/enabling-device-security-kit/document.md) and [requested the debug profile](https://developer.huawei.com/consumer/en/doc/app/agc-help-debug-profile-0000002248181278).

1.  Import the Device Security Kit module and related public modules.
    
    import { deviceCertificate } from '@kit.DeviceSecurityKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    

2.  Obtain the device token.
    
    const TAG = "DeviceCertificateJsTest";
    
    // Request the device token and process the result.
    try {
      deviceCertificate.getDeviceToken().then((token) => {
          hilog.info(0x0000, TAG, 'Succeeded in executing getDeviceToken');
          // You process the device token.
      }).catch((err: BusinessError) => {
    	hilog.error(0x0000, TAG, 'getDeviceToken failed!  %{public}d %{public}s', err.code, err.message);
      });
    } catch(err) {
      let error: BusinessError = err as BusinessError;
      hilog.error(0x0000, TAG, 'getDeviceToken failed!  %{public}d %{public}s', error.code, error.message);
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/WKlLhA1uR6uUJLL3lUND9A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062006Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=926C736AE238A4150CAEAA1883D558A8CE30B5FB65E27D3E47EF24C713431C97)
    
    The device token is generated and encrypted by Device Security Kit. The token generated each time is different and is valid for 1 hour.
    

## Server Development

1.  Obtain the JWT. For details, please refer to [Generating a JWT Based on a Service Account](../preparations/generating-a-jwt-based-on-a-service-account/document.md).
2.  Call the **checkDeviceToken**, **getDeviceStatus**, **setDeviceStatus**, and **delDeviceStatus** APIs to check the device token, obtain the device marking status, set the device marking status, and delete the device marking status, respectively. For details, please refer to [REST APIs](https://developer.huawei.com/consumer/en/doc/harmonyos-references/devicesecurity-restapi).
    
    Sample code:
    
    import java.io.BufferedReader;
    import java.io.IOException;
    import java.io.InputStream;
    import java.io.InputStreamReader;
    import java.io.OutputStream;
    import java.net.HttpURLConnection;
    import java.net.URL;
    
    import com.alibaba.fastjson.JSONObject;
    
    public class DeviceTokenServer {
        // Device token obtained using the DeviceVerify function.
        static String deviceToken = "aes-gcm.gouLVEalfJxRLxt+3Gxh/orDAG9kDbkeFydkxGrDOHVJ3KEhiSDhIeW+/KH0ErqVxZ0vfkgtapaMu3yc0IND+lzC8ZH86NHxW+/GsqxYhvZ650TWUkanwdlZwYD0HPZ/KFnDPgIvGLvvWz1BdoPOOiFy5BuCQfGVNxl9OBTd7wsiJpl8kKywMRg/k1x61/8IpaH4F6tPrMV/Fv4N/WLfSHlC9AkB1ekZz4hxambDaXP8aXz59FYWItTl7tBOV09+JKnFqD0dB5ZmXjUhVLRKpYeGH8dPWG2gOmEksY6CsXvWBul+5HF76myfUeSvrWfD7Ee3+5Uuld3v+s8W+aFJkdUo8GSCF4xbiA+01BKnq0DIh0EKW/VJAQHjo/P/X/6jMwoDnbF7NWPmh827LHKQMIsN46zfke7qpdBsYpidKNxlXIb1azyAhD/izf5KQwkzwlVTctIvkUNH9XjTh1I6xb8yYb7TjZ7tnMGg2lWizNsejIcwAPqTTyXXupL5mPc8SwsZ424mDQhf1pCfacbZFaew0jWUC5ZQ2B8CiBeX";
        // JWT generated based on a service account.
        static String authorization = "Bearer eyJraWQiOiI5YTU5ZGRkZDZlYzY0MTgyYmUwMTc2MDNjZDU1YjEwNCIsInR5cCI6IkpXVCIsImFsZyI6IlBTMjU2In0.eyJhdWQiOiJodHRwczovL29hdXRoLWxvZ2luLmNsb3VkLmh1YXdlaS5jb20vb2F1dGgyL3YzL3Rva2VuIiwiaXNzIjoiMTE0MDIzMzQ1IiwiZXhwIjoxNzU0NDQ4NDU2LCJpYXQiOjE3NTQ0NDQ4NTZ9.cJEiLM53QBTSxzPjDAqK-HeteSv\_qWxnAuEiwaN\_udLQz78QZPcD54RFWSOqE459B0Y78hEL1-2eQlcCjbGn0OI2AQbwTwYzoRbLftAEyP5V9Juv1A-cfR8MoVapVdZ3pA9Jg6B5cBjcQLax-GTUJjevgI4PyTxQCIhLa-kaQq\_h-KOnpcWlVUx2weLRAcGs4Tr3wYqdLnSPE7Hp\_44C3S69dSoXoP8HL6-2L4aJzzvNn7uYoRiZAoCZoarJNHi7d8h9JEJ2K5vmaYV\_lJ9l0\_G4RDjpEmtCPOEkXLPIvjh5fwEBPyMZiUJqHyqTkdw8AjjgIaFe0wG9wCZk4sEo9GOruuy9tN6mEccFAEKbSf28gpUowWC23uKQPIYb9sdzrN8D3hpalrN5CDh1dv80wlhLxXeJOWWnfjCqYhA0m17UFC4xEhno-M52dEb4BODPsw-96xx02GX8\_VqDDjjUmXEr6lwj4yLE\_5feR1QFQS2NhC11Py4AzrsEPb9maFqR-bOUO2SfLdD1EjvMx2p-tELosFH8DmvwtbjNVYDN0zGEed150qhMtkDG9DUwT0dL3q\_ikRq73syB9WbQrlpWeJAWBmazkb0EoSf24UO2rRjcZ0hGmgFIIH7AzHgw4Ok2ijCJ5uVIY59DUsXXUIBIH7tMyNUjrdZG0\_ctDORrk\_s";
        // HAP name.
        static String bundleName = "com.huawei.myapplication.shoubiao412";
    
        public static void main(String\[\] args) throws IOException {
            checkDeviceToken();
            setDeviceStatus();
            getDeviceStatus();
            delDeviceStatus();
        }
        public static void checkDeviceToken() throws IOException {
            // URL of the **checkDeviceToken** API.
            String url = "https://connect-api.cloud.huawei.com/api/rms/v1/deviceVerify/checkDeviceToken";
            URL obj = new URL(url);
            HttpURLConnection con = (HttpURLConnection) obj.openConnection();
            createRequestHeader(con);
            JSONObject postBody = createRequestBody();
            sendRequestAndReadResponse(con, postBody);
        }
        public static void getDeviceStatus() throws IOException {
            // URL of the **getDeviceStatus** API.
            String url = "https://connect-api.cloud.huawei.com/api/rms/v1/deviceVerify/getDeviceStatus";
            URL obj = new URL(url);
            HttpURLConnection con = (HttpURLConnection) obj.openConnection();
            createRequestHeader(con);
            JSONObject postBody = createRequestBodyWithMode();
            sendRequestAndReadResponse(con, postBody);
        }
        public static void setDeviceStatus() throws IOException {
            // URL of the **setDeviceStatus** API.
            String url = "https://connect-api.cloud.huawei.com/api/rms/v1/deviceVerify/setDeviceStatus";
            URL obj = new URL(url);
            HttpURLConnection con = (HttpURLConnection) obj.openConnection();
            createRequestHeader(con);
            JSONObject postBody = createRequestBodyWithBit();
            sendRequestAndReadResponse(con, postBody);
        }
        public static void delDeviceStatus() throws IOException {
            // URL of the **delDeviceStatus** API.
            String url = "https://connect-api.cloud.huawei.com/api/rms/v1/deviceVerify/delDeviceStatus";
            URL obj = new URL(url);
            HttpURLConnection con = (HttpURLConnection) obj.openConnection();
            createRequestHeader(con);
            JSONObject postBody = createRequestBodyWithMode();
            sendRequestAndReadResponse(con, postBody);
        }
        public static JSONObject createRequestBody() {
            // Create a request body.
            JSONObject data = new JSONObject();
            data.put("deviceToken", deviceToken);
            // (Optional) Add the data as required.
            // data.put("transactionId", "xxx");
            // UTC time on the app server.
            data.put("timestamp", 1704038400000L);
            JSONObject postBody = new JSONObject();
            postBody.put("data", data);
            return postBody;
        }
        public static JSONObject createRequestBodyWithMode() {
            // Create a request body.
            JSONObject data = new JSONObject();
            // Granularity of the device marking status. The options are as follows: **1**: app-level; **2**: developer-level.
            data.put("mode", 1);
            data.put("deviceToken", deviceToken);
            // (Optional) Add the data as required.
            // data.put("transactionId", "xxx");
            // UTC time on the app server.
            data.put("timestamp", 1704038400000L);
            JSONObject postBody = new JSONObject();
            postBody.put("data", data);
            return postBody;
        }
        public static JSONObject createRequestBodyWithBit() {
            // Create a request body.
            JSONObject data = new JSONObject();
            // Granularity of the device marking status. The options are as follows: **1**: app-level; **2**: developer-level.
            data.put("mode", 1);
            data.put("deviceToken", deviceToken);
            // (Optional) Add the data as required.
            // data.put("transactionId", "xxx");
            // UTC time on the app server.
            data.put("timestamp", 1704038400000L);
            // First bit of the device marking status.
            data.put("bit0", 1);
            // Second bit of the device marking status.
            data.put("bit1", 0);
            JSONObject postBody = new JSONObject();
            postBody.put("data", data);
            return postBody;
        }
        public static void createRequestHeader(HttpURLConnection con) throws IOException {
            con.setRequestMethod("POST");
            con.setDoOutput(true);
    
            // Set the request header.
            con.setRequestProperty("Content-Type", "application/json;charset=utf-8");
            con.setRequestProperty("Authorization", authorization);
            // Set **bundleName**.
            con.setRequestProperty("bundleName", bundleName);
        }
        public static void sendRequestAndReadResponse(HttpURLConnection con, JSONObject postBody) throws IOException {
            try (OutputStream os = con.getOutputStream()) {
                byte\[\] input = postBody.toString().getBytes("utf-8");
                os.write(input, 0, input.length);
            }
            // Read the response code.
            int responseCode = con.getResponseCode();
            System.out.println("Response Code: " + responseCode);
    
            InputStream stream;
            if (responseCode >= 200 && responseCode < 300) {
                stream = con.getInputStream();
            } else {
                // Obtain error information.
                stream = con.getErrorStream();
            }
            // Read the response content (regardless of success or failure).
            StringBuilder response = new StringBuilder();
            String line;
            try (BufferedReader br = new BufferedReader(new InputStreamReader(stream, "utf-8"))) {
                while ((line = br.readLine()) != null) {
                    response.append(line);
                }
            } catch (Exception e) {
                System.out.println(e);
            }
            System.out.println("Response Content: " + response.toString());
        }
    }
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/VxYSz64yRpqw99pEOicMqg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062006Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=98A4BD3E468EECC858E67A30DFD6E3A41755800F347310196B7AF42DE5628FA0)

1.  The device marking status is valid for two years, counting from the last update time specified by **lastUpdateTime**.
2.  You can determine the validity period of the device marking status based on the **lastUpdateTime** field in the response to the **getDeviceStatus** call. For example, if you launch two promotional activities in May and June, you can determine which promotional activity the user has participated in based on the **lastUpdateTime** field. If the month in the value of **lastUpdateTime** is May, the user has participated in the promotional activity in May.
