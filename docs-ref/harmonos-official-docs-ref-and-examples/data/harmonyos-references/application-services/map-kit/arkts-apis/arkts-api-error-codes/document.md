# ArkTS API Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/HZObGHaVSV6ZITiCsYQxWg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062514Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=00C26C59B131D84CF4F841C462DDD670232D84013B91A6E3543E0DE6EF1B9AA2)

This section describes only module-specific error codes. For details about universal error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

#### 1002600001 System Internal Error

**Message**

System internal error.

**Description**

This error code is reported when a system internal error occurs.

**Possible causes**

Another unknown error occurs.

**Solution**

Try again or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1002600002 App Failed to Connect to Map Kit

**Message**

Failed to connect to the Map Kit server.

**Description**

This error code is reported when an app fails to connect to Map Kit.

**Possible causes**

1\. The network connection of the device is faulty.

2\. Failed to connect to Map Kit when automatic signing is used.

**Solution**

1\. Check the device network connection.

2\. Clear the existing certificate configuration, perform automatic signing again, and configure the client ID and certificate fingerprint. Starting from HarmonyOS 5.0.2(14), you can refer to [Preparations](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/map-config-agc) for the configuration.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/lUX46RLaSVunz3pI9S84Pg/en-us_image_0000002517279941.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062514Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=677A800A9D677DA64FFD3D03F0A1974787A7051D3A6AE3859DA019904C0104AC "Click to enlarge")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/S2RE1EgFRT2Mf10AWd9Xzw/en-us_image_0000002485000040.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062514Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5720E271E9586A3B65830E94AD3D2552D6F7CF46CA79B7D797D768EF40FC272F "Click to enlarge")

3\. If the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

#### 1002600003 App Identity Verification Failure

**Message**

App authentication failed.

**Description**

This error code is reported when identity verification fails for an app.

**Possible causes**

1.  The value of **client\_id** configured in the **module.json5** file of the project is different from that in AppGallery Connect.
2.  The public key fingerprint in AppGallery Connect is empty or incorrect.
3.  The identity verification timed out due to poor network connection.
4.  The configured public key fingerprint has not taken effect yet.
5.  Map Kit was enabled before the profile was configured.
6.  Automatic signing was configured repeatedly. As a result, the debug certificate in AppGallery Connect does not match the local certificate.

**Solution**

1\. Ensure that the value of **client\_id** configured in the **module.json5** file is the same as that in AppGallery Connect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/dGtFPXVER_iWKWI5HHluDQ/en-us_image_0000002485000038.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062514Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3CB04BF1D71E6D7F75190CF9EB1EA57DF9D614E8F6B4BC01CB76AEA2D6F1B832 "Click to enlarge")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/HOTksYFrT8ORdsgb03KxgA/en-us_image_0000002485160002.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062514Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=59E6026688E17973DA63CE8163D9B57B68155030196C89B73C2CA27D1DB97989 "Click to enlarge")

2\. Regenerate a signing certificate fingerprint [automatically](https://developer.huawei.com/consumer/en/doc/app/agc-help-signature-info-0000001628566748#section958212134217) or [manually](https://developer.huawei.com/consumer/en/doc/app/agc-help-signature-info-0000001628566748#section2049119231438), and then [configure it](https://developer.huawei.com/consumer/en/doc/app/agc-help-cert-fingerprint-0000002278002933) in AppGallery Connect.

3\. Check the network connection and try again.

4\. Set the system time of the device one day ahead.

5\. [Enable Map Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/map-config-agc#section16133115441516), [request a new debug profile](https://developer.huawei.com/consumer/en/doc/app/agc-help-add-debugprofile-0000001914423102), and [sign your app manually](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-signing#section297715173233).

6\. The mismatch of automatically signed certificates can be resolved in either of the following ways:

Solution 1: Use a locally generated CSR file to generate a new debug certificate in AppGallery Connect, and use the new debug certificate to generate a new certificate fingerprint.

By default, the generated CSR file is stored in the path shown in the following figure, where the masked portion represents the username.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/Fxwz84-GRd2x9uVsddppNg/en-us_image_0000002517199963.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062514Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=11E08453434E86E5F26EF1394B07DB422340A35A7328C6D09E513F0F522C4108 "Click to enlarge")

Generate a debug certificate in AppGallery Connect using the generated CSR file.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/KjCMH8xaTcKzSKsrU97Z4Q/en-us_image_0000002517199959.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062514Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0BA06C67646135B247DF2F750630573E64277E9A7EEF421D8C6FBEC71C6B694B "Click to enlarge")

Add a public key fingerprint and select the newly generated debug certificate. (Note: The map may not be displayed immediately after the configuration due to the authentication cache. To resolve this, try to clear the cache or adjust the device's system time one day later.)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/F-_YLMcLRQuL2s1BXeoX-g/en-us_image_0000002485160000.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062514Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5596BFB90F6BEB79AB2E24BB2425E88483725AB900DD1E424F189D940DB773A9 "Click to enlarge")

Solution 2: Delete the local existing automatically signed certificate and the debug certificate in AppGallery Connect, and regenerate a new automatic signature. A new debug certificate will be generated automatically. Then use the new debug certificate to generate a public key fingerprint.

Delete the **signingConfigs** parameter from the **build-profile.json5** file.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/KcbXZbbPRbaJS07gnIl8-A/en-us_image_0000002485000036.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062514Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7CDAD05936508696278D35A778D6CA17D12BDF6BE18FD8506AC2F46151CB0369 "Click to enlarge")

Delete all content from the **config** folder.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/p9nxkzBnRYWDHPPY2-_e4w/en-us_image_0000002485160004.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062514Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1E1ACB80BD48B268AF3C7387E2BDC70F36ACF4BE53055B02BB572EB5B851B76C "Click to enlarge")

Delete the automatically signed debug certificate in AppGallery Connect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/H_iWDY1kS32CE7JPsY4l5w/en-us_image_0000002517279945.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062514Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7774C1C7FEC4ACE728A6C42D2001D8159577A89ADD46CF9798AE08D45E9597CE "Click to enlarge")

After existing certificates are deleted, generate a new automatic signature. The debug certificate is created synchronously. Then, use the new debug certificate to generate a new fingerprint. (Note: The map may not be displayed immediately after the configuration due to the authentication cache. To resolve this, try to clear the cache or adjust the device's system time one day later.)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/qsAtxGteQXm410esaUMm5A/en-us_image_0000002485000042.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062514Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6FF712D5EE524BC8CED869D26F6B8107CA830B3D22020026CDBDBE2CEDB71C05 "Click to enlarge")

7\. If the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

#### 1002600004 Map Kit Not Enabled for the App

**Message**

The Map permission is not enabled.

**Description**

This error code is reported when Map Kit is not enabled for the app.

**Possible causes**

1\. Map Kit has not been enabled.

2\. client\_id has not been set.

**Solution**

1\. [Enable Map Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/map-config-agc#section16133115441516).

2\. Set **client\_id**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/EtCzNtZGSmS4v42AlGdDRg/en-us_image_0000002517279943.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062514Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=41F8CFBA56891CAB2A7F8243319F49B1FF14E775EF939BB0DF75771B96969AD9 "Click to enlarge")

3\. If the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

#### 1002600005 Unavailable Network

**Message**

The network is unavailable.

**Description**

This error code is reported when the network is unavailable.

**Possible causes**

The network is unavailable.

**Solution**

Verify the network connection and try again or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1002600006 API Call Quota Used Up

**Message**

The API call times exceed the quota.

**Description**

This error code is reported when API call quota is used up.

**Possible causes**

The API call quota is used up.

**Solution**

[Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

#### 1002600007 API QPS Quota Used Up

**Message**

The API QPS exceeds the quota.

**Description**

This error code is reported when API QPS quota is used up.

**Possible causes**

The API QPS quota is used up.

**Solution**

[Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

#### 1002600008 API in Arrears

**Message**

The API is in arrears.

**Description**

This error code is reported when the API is in arrears.

**Possible causes**

The API is in arrears.

**Solution**

[Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

#### 1002600009 No Pay-as-you-go Plan Subscribed for the API

**Message**

The API has not subscribed to any pay-as-you-go package.

**Description**

This error code is reported when you have not subscribed to any pay-as-you-go plan for the API.

**Possible causes**

You have not subscribed to any pay-as-you-go plan.

**Solution**

[Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

#### 1002600010 Server Busy

**Message**

The server is busy. Please wait and try again.

**Description**

This error code is reported when the server is busy.

**Possible causes**

The server is busy.

**Solution**

Try again or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1002600011 Server Error

**Message**

Server error.

**Description**

This error code is reported when a system internal error occurs.

**Possible causes**

1\. There is a server error.

2\. The network is unavailable.

**Solution**

Try again or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1002600012 Country/Region Code Error

**Message**

The country code is not supported.

**Description**

This error code is reported when the input country/region code is incorrect.

**Possible causes**

The country/region code is not supported.

**Solution**

Change the country/region code.

#### 1002600013 Unknown Routing Destination

**Message**

The current routing location is unknown. Try again later.

**Description**

The current routing destination is unknown.

**Possible causes**

Failed to obtain the routing destination of the current device.

**Solution**

1.  Verify that the device network connection is normal.
2.  Try again or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1002600014 Failed to Start the Map App

**Message**

Failed to start the map app.

**Description**

The map app failed to be started.

**Possible causes**

The map app is not installed on the device, and the map app download page of AppGallery failed to be displayed.

**Solution**

1.  Search for the map app on AppGallery and install it.
2.  Try again or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1002600015 Heatmap ID Already Exists

**Message**

The heatmap ID already exists.

**Description**

The heatmap ID already exists.

**Possible causes**

The heatmap ID already exists.

**Solution**

Change the heatmap ID or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1002600999 Unknown Error

**Message**

Unknown error.

**Description**

This error code is reported when a system internal error occurs.

**Possible causes**

Another unknown error occurs.

**Solution**

Try again or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1002601001 Object to Be Operated Does Not Exist

**Message**

The object to be operated does not exist.

**Description**

The error code is reported when the object to be operated does not exist.

**Possible causes**

The object to be operated does not exist.

**Solution**

Try again or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1002601002 Custom Map Style File Does Not Exist

**Message**

The custom map style file does not exist.

**Description**

This error code is reported when the custom map style file does not exist.

**Possible causes**

1\. The custom map style file does not exist.

2\. The device network is unavailable.

**Solution**

1\. Verify that the style ID exists on [Petal Maps Studio](https://developer.petalmaps.com/console/studio/).

2\. Verify that the device network connection is normal.

3\. Try again or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1002601004 Incorrect Style Content Format

**Message**

The style content format is incorrect.

**Description**

This error code is reported when the style content format is incorrect.

**Possible causes**

The style content format is incorrect.

**Solution**

Try again or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1002601005 Failed to Generate a Custom Component Icon

**Message**

Failed to generate the icon of the custom component.

**Description**

Failed to generate an icon for the custom component.

**Possible causes**

Failed to generate an icon for the custom component.

**Solution**

Try again or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1002602001 Departure Place or Destination Having No Home Country or Service Error

**Message**

The start and end points do not have home countries, or a service error occurred.

**Description**

This error code is reported when the departure place or destination does not have country affiliation or a service error occurs.

**Possible causes**

Invalid parameter.

**Solution**

Verify the departure place or destination and try again or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1002602002 Cross-Region Route Planning Not Supported

**Message**

Cross-region route planning is not supported.

**Description**

This error code is reported when routes across different regions are planned.

**Possible causes**

Invalid parameter.

**Solution**

Ensure that the input departure place and destination are in the same region.

#### 1002602003 Number of Departure Places or Destinations Exceeds 100

**Message**

The number of start points or end points exceed 100.

**Description**

This error is reported when the number of departure places or destinations exceeds 100.

**Possible causes**

Invalid parameter.

**Solution**

Ensure that the number of departure places or destinations in the input parameter does not exceed the upper limit.

#### 1002602004 Linear Distance Between Two Points Exceeds the Upper Limit

**Message**

The linear distance between the start point and end point exceeds the upper limit.

**Description**

The linear distance between two points exceeds the upper limit.

**Possible causes**

Invalid parameter.

**Solution**

Check the input parameter and ensure that the linear distance between two points does not exceed the upper limit.

#### 1002602005 Departure Place, Destination, or Waypoint Does Not Support Navigation

**Message**

The start point, end point, or waypoint does not support navigation.

**Description**

This error code is reported when the departure place, destination, or waypoint does not support navigation.

**Possible causes**

Invalid parameter.

**Solution**

Verify the input parameter.

#### 1002602006 Request Points Are Mapped to the Same Point on the Road

**Message**

The request point is mapped to the same point on the road.

**Description**

This error code is reported when the request points are mapped to the same point on the road.

**Possible causes**

Invalid parameter.

**Solution**

Verify the input parameter.

#### 1002603001 Empty result

**Message**

Zero result.

**Description**

This error code is reported when an empty result is returned.

**Possible causes**

Invalid parameter.

**Solution**

Verify the input parameter.

#### 1022100001 Map Controller to Be Operated Does Not Exist

**Message**

The map controller to be operated does not exist.

**Description**

The map controller to be operated does not exist.

**Possible causes**

The map controller to be operated does not exist.

**Solution**

Try again or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 401 Invalid Input Parameter

**Message**

Invalid input parameter.

**Description**

This error code is reported when an invalid input parameter is passed.

**Possible causes**

Invalid input parameter.

**Solution**

Verify the input parameter.

#### 801 Function Not Supported; Failed to Call the API Due To Limited Device Capabilities

**Message**

Capability not supported. Failed to call the API due to limited device capabilities.

**Description**

The function is not supported. Due to limitations in the device's capabilities, the API call was unsuccessful.

**Possible causes**

This API is not supported on this device.

**Solution**

Replace the device or use an alternative API.
