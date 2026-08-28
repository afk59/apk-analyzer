# ArkTS Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/OhWbYN8oSu-tXmuURdbz3g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AAC1534ADA8D2C910EA648DDFAD9385DBD48E2D474CBFDA55F78EDF1B628DDF8)

This section describes only module-specific error codes. If a universal error code is returned, handle it by referring to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md). If the error message contains any other error codes, refer to the following links for details:

-   [Cloud Functions](https://developer.huawei.com/consumer/en/doc/AppGallery-connect-References/errorcode-nodejs-0000001733038624)
-   [Cloud Storage](https://developer.huawei.com/consumer/en/doc/AppGallery-connect-References/0000001057683679-0000001056723660)
-   [Cloud DB](https://developer.huawei.com/consumer/en/doc/AppGallery-connect-Guides/agc-clouddb-error-code-0000001117436042)

#### 1008210001 Internet Connection Error for Cloud Functions

**Message**

Network connection error.

**Description**

Internet connection error for Cloud Functions.

**Possible causes**

1.  A proxy server is configured for the network.
2.  No network is available for the device.

**Solution**

Check the network.

#### 1008210009 Internal Error of the Cloud Functions Client

**Message**

Client internal error.

**Description**

Internal error of the Cloud Functions client.

**Possible causes**

Client internal error.

**Solution**

[Submit a ticket online](<https://developer.huawei.com/consumer/en/support/feedback/#/add/101704353566310877?level2=101704353626565886&amp;level3=101723605535783370&amp;keyWord=Cloud Foundation Kit&amp;channel=ICS0000>) to contact technical support.

#### 1008211001 Error on the Cloud Functions Server

**Message**

Server error.

**Description**

Error on the Cloud Functions server.

**Possible causes**

The Cloud Functions server is abnormal or authentication fails.

**Solution**

[Submit a ticket online](<https://developer.huawei.com/consumer/en/support/feedback/#/add/101704353566310877?level2=101704353626565886&amp;level3=101723605535783370&amp;keyWord=Cloud Foundation Kit&amp;channel=ICS0000>) to contact technical support.

#### 1008220001 Internet Connection Error for Cloud Storage

**Message**

Network connection error.

**Description**

Internet connection error for Cloud Storage.

**Possible causes**

1.  A proxy server is configured for the network.
2.  No network is available for the device.

**Solution**

Check the network.

#### 1008220009 Internal Error of the Cloud Storage Client

**Message**

Client internal error.

**Description**

Internal error of the Cloud Storage client.

**Possible causes**

Client internal error.

**Solution**

[Submit a ticket online](<https://developer.huawei.com/consumer/en/support/feedback/#/add/101704353566310877?level2=101704353626565886&amp;level3=101723605535783370&amp;keyWord=Cloud Foundation Kit&amp;channel=ICS0000>) to contact technical support.

#### 1008221001 Cloud-Side Execution Error for Cloud Storage

**Message**

Server error.

**Description**

Cloud-side execution error for Cloud Storage.

**Possible causes**

The cloud file requested by the Cloud Storage client does not exist, the cloud security rules are incorrectly configured, or the authentication fails.

**Solution**

Check whether the cloud resources and request are correct based on the error information.

#### 1008230001 Cloud DB Internet Connection Error

**Message**

Network connection error.

**Description**

Cloud DB Internet connection error.

**Possible causes**

1.  A proxy server is configured for the network.
2.  No network is available for the device.

**Solution**

Check the network.

#### 1008230009 Internal Error of the Cloud DB Client

**Message**

Client internal error.

**Description**

Internal error of the Cloud DB client.

**Possible causes**

Client internal error.

**Solution**

[Submit a ticket online](<https://developer.huawei.com/consumer/en/support/feedback/#/add/101704353566310877?level2=101704353626565886&amp;level3=101723605535783370&amp;keyWord=Cloud Foundation Kit&amp;channel=ICS0000>) to contact technical support.

#### 1008230002 Incorrect Schema Configuration of Cloud DB

**Message**

Schema config error.

**Description**

The **schema.json** file of Cloud DB is incorrectly configured.

**Possible causes**

1.  The **schema.json** file does not exist or the file path is incorrect.
2.  The storage object in the **schema.json** file is inconsistent with that created in the code. The possible cause is that the storage object on the cloud has changed, but the **schema.json** file is not exported again.
3.  The **schema.json** file exists in both the **AppScope** and **entry** directories. When you update the storage object in the **schema.json** file in the **entry** directory, the update will be overwritten by the **schema.json** file in the **AppScope** directory during compilation and build. For details, please refer to [Resource Categories](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/resource-categories-and-access#resource-categories).

**Solution**

1.  Download the **schema.json** file and save it to the **rawfile** directory.
2.  Ensure that the object in the **schema.json** file is consistent with the storage object created in the code. For details, please refer to [Importing an Object Type File](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/cloudfoundation-database-add-file).
3.  Move the **schema.json** file from the **entry** directory to the **AppScope** directory for maintenance.

#### 1008230003 Incorrect Code Object of Cloud DB

**Message**

Natural object error.

**Description**

Incorrect code object of Cloud DB.

**Possible causes**

The storage object name in the code is inconsistent with the actual one.

**Solution**

Check whether the input storage object name is the same as the actual one.

#### 1008231001 Cloud DB Server Error

**Message**

Server error.

**Description**

Cloud DB server error.

**Possible causes**

The Cloud DB server is abnormal or authentication fails.

**Solution**

[Submit a ticket online](<https://developer.huawei.com/consumer/en/support/feedback/#/add/101704353566310877?level2=101704353626565886&amp;level3=101723605535783370&amp;keyWord=Cloud Foundation Kit&amp;channel=ICS0000>) to contact technical support.
