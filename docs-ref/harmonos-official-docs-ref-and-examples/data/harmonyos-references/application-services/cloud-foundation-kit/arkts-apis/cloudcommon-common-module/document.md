# cloudCommon (Common Module)

This module provides the capability of initializing Cloud Foundation Kit.

**Start version**: 5.0.0(12)

#### Modules to Import

import { cloudCommon } from '@kit.CloudFoundationKit';

#### cloudCommon.init

init(options?: CloudOptions): void

Initializes Cloud Foundation Kit.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

options

 | 

[CloudOptions](#section6286921112312)

 | 

No

 | 

Initialization parameters.

 |

**Error codes:**

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |

**Example**:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/-kukQyu5RyCS7qAcz8FA0Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AD5D47CB583AA90CF26532AD39646B7A0D70B931DBDCBC1B471F30E9958A6C2F)

The Cloud Functions service does not require authentication. Therefore, you do not need to obtain user credentials when using this service for development. However, you need to obtain user credentials for development using Cloud Storage or Cloud DB. You can obtain user credentials using two methods. The following code shows an example of obtaining credentials through the Auth Service SDK of AppGallery Connect. For more information, please refer to [AuthProvider](#section136610231214).

import { cloudCommon } from '@kit.CloudFoundationKit';
import { request } from '@kit.BasicServicesKit';
import auth from '@hw-agconnect/auth';

let provider = auth.getAuthProvider(); // Call this method to obtain **authProvider** when a user successfully signs in.
cloudCommon.init({
  region: cloudCommon.CloudRegion.CHINA,
  authProvider: provider,
  functionOptions: { timeout: 10 \* 1000 },
  storageOptions: { mode: request.agent.Mode.BACKGROUND, network: request.agent.Network.ANY },
  databaseOptions: { schema: "schema.json", traceId: "traceId" }
})

#### CloudOptions

Initialization options.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

region

 | 

[CloudRegion](#section10763191910114)

 | 

No

 | 

Yes

 | 

Storage location. The default value is **CHINA**.

 |
| 

authProvider

 | 

[AuthProvider](#section136610231214)

 | 

No

 | 

Yes

 | 

Authentication provider.

 |
| 

functionOptions

 | 

[FunctionOptions](#section11284175361211)

 | 

No

 | 

Yes

 | 

Cloud Functions initialization settings.

 |
| 

storageOptions

 | 

[StorageOptions](#section1772621115138)

 | 

No

 | 

Yes

 | 

Cloud Storage initialization settings.

 |
| 

databaseOptions

 | 

[DatabaseOptions](#section2817232171313)

 | 

No

 | 

Yes

 | 

Cloud DB initialization settings.

 |

#### CloudRegion

Enumerated storage locations.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

CHINA

 | 

0

 | 

Data is stored in the Chinese mainland.

 |
| 

GERMANY

 | 

1

 | 

Data is stored in Germany.

 |
| 

RUSSIA

 | 

2

 | 

Data is stored in Russia.

 |
| 

SINGAPORE

 | 

3

 | 

Data is stored in Singapore.

 |

#### AuthProvider

Authentication provider. You can use the access token API of Account Kit to customize an **AuthProvider**.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

#### \[h2\]getAccessToken

getAccessToken(isForceRefresh: boolean): Promise<string>

Obtains user credentials. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

isForceRefresh

 | 

boolean

 | 

Yes

 | 

Indicates whether to forcibly refresh user credentials. **true**: yes; **false**: no.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<string>

 | 

User credentials returned through a promise. The user credentials can be generated through the API of Account Kit for obtaining a user-level credential.

 |

**Example**:

1.  Use the API of Account Kit for [obtaining a user-level credential](../../../account-kit/rest-apis/api-call-credentials/obtaining-a-user-level-credential/document.md) to obtain the refresh token, and then obtain the access token based on the refresh token to customize an **AuthProvider**. The sample code is as follows:
    
    import { cloudCommon } from '@kit.CloudFoundationKit';
    import { http } from '@kit.NetworkKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
    let accessToken = '';
    
    export class MyAuthProvider implements cloudCommon.AuthProvider {
      async getAccessToken(isForceRefresh: boolean): Promise<string> {
        let data =
          "grant\_type=refresh\_token&client\_id=xxxx&client\_secret=xxxx&refresh\_token=";
        let refreshToken =
          encodeURIComponent('xxxx'); // _xxxx_ is the refresh token obtained through Account Kit's API for obtaining a user-level credential.
        // Forcibly refresh the access token that has expired.
        if (isForceRefresh) {
          data = data + refreshToken;
          try {
            let httpRequest = http.createHttp();
            let ohosOptions: http.HttpRequestOptions = {
              method: http.RequestMethod.POST,
              header: {
                'Content-Type': 'application/x-www-form-urlencoded'
              },
              extraData: data,
            };
            let url = "https://oauth-login.cloud.huawei.com/oauth2/v3/token";
            let resp = await httpRequest.request(url, ohosOptions);
            accessToken = JSON.parse(resp.result.toString()).access\_token;
          } catch (err) {
            hilog.error(0x0000, 'testTag', \`Failed to get accessToken, code: ${err.code}, message: ${err.message}\`);
          }
        }
        return Promise.resolve(accessToken);
      }
    }
    
2.  Complete initialization using the custom **AuthProvider**.
    
    import { cloudCommon } from '@kit.CloudFoundationKit';
    import { request } from '@kit.BasicServicesKit';
    import { MyAuthProvider } from 'xxx'; // _xxx_ indicates the file path of the custom **AuthProvider**.
    
    let authProvider = new MyAuthProvider();
    cloudCommon.init({
      region: cloudCommon.CloudRegion.CHINA, // Enter the actual data processing location.
      authProvider: authProvider,
      functionOptions: { timeout: 10 \* 1000 },
      storageOptions: { mode: request.agent.Mode.BACKGROUND, network: request.agent.Network.ANY },
      databaseOptions: { schema: "schema.json", traceId: "traceId" }
    })
    

#### FunctionOptions

Cloud Functions initialization settings.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

timeout

 | 

number

 | 

No

 | 

Yes

 | 

Timeout interval for requesting a function, in milliseconds. The default interval is 70 x 1000 milliseconds.

The value range is unrestricted, and the value will be converted to the unsigned long type.

 |

#### StorageOptions

Cloud Storage initialization settings.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

mode

 | 

[request.agent.Mode](../../../../system/basic-functions/basic-services-kit/arkts-apis/data-file-processing/ohos-request-upload-and-download/document.md#requestagentmode10)

 | 

No

 | 

Yes

 | 

Task mode. After an app is switched to the background for a period of time, background tasks are not affected but foreground tasks will fail or pause. The default value is **BACKGROUND**.

-   **BACKGROUND**: background tasks
-   **FOREGROUND**: foreground task

 |
| 

network

 | 

[request.agent.Network](../../../../system/basic-functions/basic-services-kit/arkts-apis/data-file-processing/ohos-request-upload-and-download/document.md#requestagentnetwork10)

 | 

No

 | 

Yes

 | 

Network type. If the network does not meet the preset condition, tasks that have not been executed will await for execution, and tasks that are being executed will fail or pause. The default value is **Network.ANY**.

-   **Network.ANY**: network of any type
-   **Network.WIFI**: wireless network
-   **Network.CELLULAR**: cellular data network

 |

#### DatabaseOptions

Cloud DB initialization settings.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

schema

 | 

string

 | 

No

 | 

Yes

 | 

Complete data table structures and permissions. The **schema.json** configuration file is downloaded from the cloud and, by default, is obtained from the **rawfile** directory.

 |
| 

traceId

 | 

string

 | 

No

 | 

Yes

 | 

Custom trace ID, used to trace requests.

The custom trace ID must contain 1 to 32 characters and can only consist of the following two types of characters:

-   Letters (a to f)
-   Digits (0 to 9)

By default, the value is empty.

 |
