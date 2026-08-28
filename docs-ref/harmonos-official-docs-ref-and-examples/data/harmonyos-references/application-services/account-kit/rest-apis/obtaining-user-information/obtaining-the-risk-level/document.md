# Obtaining the Risk Level

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/Al6hscOnQtCgUbTTDq6tYw/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062502Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=663A2C6DB605F8807739882BAF3697F783666793F372F6EF0F8FBF77643C7424)

To ensure secure network access, use the TLS 1.2 protocol and the specified cipher suites. If your app server accesses Account Kit using TLS 1.0, TLS 1.1, or unsupported cipher suites, the connection may fail.

For details about TLS 1.2 and the specified cipher suites, see [TLS Protocol and Cipher Suites](../../common-description/document.md#section1329115361128).

#### Function

This API is called by the app server from the Account Kit server to obtain the risk level of a HUAWEI ID user ([Obtaining the Risk Level](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-get-risklevel)).

#### Scenario

After the app obtains an access token through the authorization code, it can use the access token to obtain the user's risk level.

#### Restrictions

-   Ensure that the network on the caller side is normal.
-   To use this function, the app needs to request the **riskLevel** scope (required for obtaining the user risk level). Then, the app includes this scope when obtaining the authorization code. For details about how to request this scope, please refer to [Prerequisites](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-get-risklevel-byquicklogin#section13466111683216).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/ohnQym0jRGm89ZIAisXwUA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062502Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E34C5A7F1DC650F8A31E764D097F80B6B4DF5B3B1CE3FFB885044B2A2ED01CCE)

If the app does not request the **riskLevel** scope or does not include this scope when obtaining the authorization code, an error will be returned, and **errCode=403** will be contained in the response body.

#### Prototype

<table><tbody><tr><th class="firstcol" id="mcps1.3.5.2.1.3.1.1" valign="top" width="18.740000000000002%"><p><strong>Protocol</strong></p></th><td class="cellrowborder" valign="top" width="81.26%"><p>HTTPS POST</p></td></tr><tr><th class="firstcol" id="mcps1.3.5.2.1.3.2.1" valign="top" width="18.740000000000002%"><p><strong>Direction</strong></p></th><td class="cellrowborder" valign="top" width="81.26%"><p>Developer server -&gt; Account Kit server</p></td></tr><tr><th class="firstcol" id="mcps1.3.5.2.1.3.3.1" valign="top" width="18.740000000000002%"><p><strong>API URL</strong></p></th><td class="cellrowborder" valign="top" width="81.26%"><p>https://account.cloud.huawei.com/user/getuserrisklevel</p></td></tr><tr><th class="firstcol" id="mcps1.3.5.2.1.3.4.1" valign="top" width="18.740000000000002%"><p><strong>Data Format</strong></p></th><td class="cellrowborder" valign="top" width="81.26%"><p>Request: Content-Type: application/json;charset=utf-8</p><p>Response: Content-Type: application/json;charset=utf-8</p></td></tr></tbody></table>

#### Request Parameters

## Request Header

| 
Parameter

 | 

Mandatory

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

Content-Type

 | 

Yes

 | 

String

 | 

Content type. The value is **application/json;charset=utf-8**.

NOTE:

The request body parameters must comply with the request header format. Otherwise, the request may fail. For details about the parameters to pass, please refer to [Sample Code](#section1888515151299).

 |

## Request Query Parameter

| 
Parameter

 | 

Mandatory

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

clientID

 | 

Yes

 | 

String

 | 

Unique ID allocated by AppGallery Connect to a newly-created app. For details about the value, please refer to the **OAuth 2.0 client ID > Client ID** field in [Viewing App Basic Information](https://developer.huawei.com/consumer/en/doc/app/agc-help-appinfo-0000001100014694).

 |
| 

transactionID

 | 

Yes

 | 

String

 | 

Transaction ID. This field is mandatory for each message.

Generation rule: _YYYYMMDDhhmmssxxxxxxxxxx_, for example, **202502121546232352164151**

_YYYYMMDDhhmmss_ is the request generation time, which is a 14-digit number.

_xxxxxxxxxx_ is a random number, 10–20 digits long.

 |

## Request Body

| 
Parameter

 | 

Mandatory

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

accessToken

 | 

Yes

 | 

String

 | 

Access token obtained through the API for [Obtaining a User-Level Credential](../../api-call-credentials/obtaining-a-user-level-credential/document.md). The authorization code used to obtain an access token must contain the **riskLevel** scope.

 |
| 

scene

 | 

Yes

 | 

String

 | 

Service scenario of obtaining the user risk level.

-   **registration**: registration
-   **marketing**: marketing campaign

 |

#### Request Example

Send a POST request. Example:

POST /user/getuserrisklevel?clientID=_<clientID>_&transactionID=_<transactionID>_ HTTP/1.1
Host: account.cloud.huawei.com
Content-Type: application/json;charset=utf-8

{"accessToken":"_<Access Token>_", "scene":"_<scene>_"}

#### Response Parameters

## Response Header

| 
Parameter

 | 

Mandatory

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

Content-Type

 | 

Yes

 | 

String

 | 

Content type. The value is **application/json;charset=utf-8**.

 |

## Response Body

| 
**Parameter**

 | 

Mandatory

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

errCode

 | 

Yes

 | 

Int

 | 

Error code. If the API is successfully called, **0** will be returned. Otherwise, an error code will be returned.

 |
| 

errMsg

 | 

Yes

 | 

String

 | 

Error message. If the API is successfully called, an empty string will be returned. Otherwise, an error message will be returned.

 |
| 

riskLevel

 | 

No

 | 

Int

 | 

Risk level, which is returned only upon request success. (See Appendix 1 below for details.)

-   **0**: No obvious risks detected.
-   **1**: Low risk.
-   **2**: Medium risk.
-   **3** High risk.
-   **4**: Undetermined.

 |
| 

riskTag

 | 

No

 | 

String\[\]

 | 

Risk tag. (See Appendix 2 below for details.)

 |

Appendix 1: Risk levels and handling suggestions

| 
**Level**

 | 

**Description**

 | 

**Handling Suggestion**

 |
| :-- | :-- | :-- |
| 

0

 | 

No obvious risks detected. For example, a user legally registers an account and uses a Huawei phone properly, without engaging in abnormal activities such as performing batch operations, using automation tools, and farming accounts.

 | 

Lift restrictions upon confirmation of no risks.

 |
| 

1

 | 

Low risk. Risks are detected and are rated as low risk after overall evaluation.

 | 

Implement simple verification through methods such as verification code and SMS or manual review.

 |
| 

2

 | 

Medium risk. Risks are detected and are rated as medium risk after overall evaluation.

 | 

Implement measures to avoid damage based on the service scenario. For example, reduce the likelihood of high-level rewards in marketing campaigns, downweight votes in ranking campaigns, and require secondary verification for sign-in and registration.

 |
| 

3

 | 

High risk. Risks are detected and are rated as high risk after overall evaluation.

 | 

Intercept the behavior. For example, return no prize or the smallest amount for red envelope campaigns, not count votes for ranking campaigns, require secondary verification for sign-in or registration, and perform other high-risk operations.

 |
| 

4

 | 

Undetermined risk. (The risk level cannot be clearly assessed at this time.)

 | 

Make the final decision by taking into account the account's historical behavior and the service context.

 |

Appendix 2: Risk tags and their descriptions

| 
**riskTag**

 | 

**Name**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

spamMailbox

 | 

Binding to a spam email

 | 

Suspected of binding to a spam email.

 |
| 

riskPhoneNumber

 | 

Binding to a mobile number purchased from a SIM card vendor

 | 

Suspected of binding to a mobile number purchased from a SIM card vendor.

 |
| 

riskDevice

 | 

Using a device with risks

 | 

Suspected of using abnormal devices such as an automation tool or bulk control device for registration or sign-in.

 |
| 

ipCluster

 | 

IP clustering

 | 

Suspected of IP clustering within half a year.

 |
| 

deviceCluster

 | 

Device clustering

 | 

Suspected of device clustering within half a year.

 |
| 

batchBehavior

 | 

Batch operations

 | 

Suspected of batch synchronization operations with a large number of junk accounts within half a year.

 |
| 

illegalLogin

 | 

Unauthorized sign-in

 | 

Suspected of unauthorized sign-in using the current HUAWEI ID.

 |
| 

activityFraud

 | 

Fraud

 | 

Suspected of engaging in fraudulent activities in marketing campaigns within half a year.

 |

#### Response Example

## Request Success

HTTP/1.1 200 OK
Content-Type: application/json;charset=utf-8

{
    "errCode": 0,
    "errMsg": "",
    "riskLevel": 2,
    "riskTag": \[
        "spamMailbox"
    \]
}

## Request Failure

HTTP/1.1 200 OK
Content-Type: application/json;charset=utf-8

{
    "errCode": 403,
    "errMsg": "no permission"
}

#### Sample Code

The Java sample code is as follows. Before running it, [configure the sample code environment](../../common-description/document.md#section444143185314). (Place this sample code and the **CallUtils** utility class in the same directory. If not, manually add the corresponding **import** statement to the sample code.)

import com.alibaba.fastjson2.JSONArray;
import com.alibaba.fastjson2.JSONObject;
import lombok.extern.slf4j.Slf4j;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpPost;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.Objects;

/\*\*
 \* Obtain a user's risk level.
 \*/
@Slf4j
public class GetUserRiskLevelDemo {
    public static void main(String\[\] args) throws IOException {
        // URL of the API for obtaining the user risk level.
        String url = "https://account.cloud.huawei.com/user/getuserrisklevel";
        // Replace it with the client ID of your app.
        String clientID = "_<Client ID>_";
        // Replace it with the transaction ID of your app.
        String transactionID = "_<transactionID>_";
        // Replace it with the user-level access token you obtained.
        String accessToken = "_<Access Token>_";
        // Replace it with the scene of your app.
        String scene = "_<scene>_";
        JSONObject result = getUserRiskLevel(url, clientID, transactionID, accessToken, scene);
        // Parse the result to obtain errCode.
        Integer errCode = result.getInteger("errCode");
        // Parse the result to obtain errMsg.
        String errMsg = result.getString("errMsg");
        // Parse the result to obtain riskLevel.
        Integer riskLevel = result.getInteger("riskLevel");
        // Parse the result to obtain riskTag.
        JSONArray riskTag = result.getJSONArray("riskTag");
    }

    private static JSONObject getUserRiskLevel(String url, String clientID, String transactionID,
        String accessToken, String scene) throws IOException {
        HttpPost httpPost = new HttpPost(url + "?" + "clientID=" + clientID + "&transactionID=" + transactionID);
        Map<String, String> reqBody = new HashMap<>();
        reqBody.put("accessToken", accessToken);
        reqBody.put("scene", scene);
        httpPost.setHeader("Content-Type", "application/json;charset=utf-8");
        httpPost.setEntity(CallUtils.wrapJsonEntity(reqBody));
        return CallUtils.toJsonObject(CallUtils.remoteCall(httpPost, (CloseableHttpResponse response, String rawBody) -> {
            int statusCode = response.getStatusLine().getStatusCode();
            // If the returned HTTP status code is not 200, the request fails.
            if (statusCode != 200) {
                return new IOException("call failed! http status code: " + statusCode + ", response data: " + rawBody);
            }
           // If the returned HTTP status code is 200, parse the response body and determine the service error code.
            JSONObject errorResponseBody = CallUtils.toJsonObject(rawBody);
            // Error code.
            Integer errCode = errorResponseBody.getInteger("errCode");
           // The value 0 of errCode indicates a success, and a value other than 0 indicates a failure.
            if (Objects.nonNull(errCode) && errCode != 0) {
                return new IOException("call failed! http status code: " + statusCode + ", response data: " + rawBody);
            }
            return null;
        }));
    }
}

#### HTTP Response Codes

| 
HTTP Response Code

 | 

Description

 | 

Solution

 |
| :-- | :-- | :-- |
| 

200

 | 

The current API call is successful. (A successful API call does not mean successful service processing. The actual service processing result must be determined via **errCode** in **Response Body**.)

 | 

\-

 |
| 

400

 | 

Incorrect parameter.

 | 

Check whether the request parameters comply with the specifications.

 |
| 

403

 | 

No access permission.

 | 

Check the network environment configuration to see if the access is blocked by the caller's network security policy. If the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

 |
| 

404

 | 

Service not found.

 | 

Verify that the request URI is correct.

 |
| 

405

 | 

Unsupported HTTP request method.

 | 

Ensure that the method for the HTTP request complies with the API specifications.

 |
| 

415

 | 

The media type is not supported.

 | 

Ensure that the content type (**contentType**) for the HTTP request complies with the API specifications.

 |
| 

500

 | 

Internal service error.

 | 

[Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

 |
| 

502

 | 

Connection error. This typically occurs when network connectivity is unstable.

 | 

Try again later. If the problem persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |
| 

504

 | 

Connection timed out. This typically occurs when network connectivity is unstable.

 | 

Try again later. If the problem persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |
| 

590

 | 

Internal service error.

 | 

[Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

 |

| 
errCode

 | 

Description

 | 

Solution

 |
| :-- | :-- | :-- |
| 

6

 | 

Session invalidation (**session timeout**).

Possible causes:

-   The access token is invalid or has expired.
-   The access token format is incorrect.
-   Other internal causes.

 | 

-   Check whether the passed parameters are correct. If yes, try to obtain a new access token.
-   The request data format of this API is **application/json;charset=utf-8**. When constructing a request body, ensure that the URL encoding is not performed on the **access\_token** parameter. For details on parameter assembly, please refer to [Sample Code](#section1888515151299).
-   Rectify the error based on the returned error description. If the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |
| 

403

 | 

No access permission.

 | 

Go to AppGallery Connect to request scopes for your app. For details, please refer to [Requesting Scopes](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-config-permissions).

 |
| 

503

 | 

System rate limiting triggered.

 | 

Try again later.

 |
| 

70001201

 | 

Invalid request parameter.

 | 

Modify the parameters in the request URL or request body.

 |
| 

70001402

 | 

System authentication error.

 | 

The authentication system is abnormal. If the problem persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |
| 

70020002

 | 

Internal API request timeout.

 | 

Try again later.

 |
| 

70001401

 | 

Internal API error.

 | 

Rectify the error based on the returned error description. If the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |
