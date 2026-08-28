# @system.fetch (Data Request)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/R8CeRNI4S4qZ2mnb8Qfvtg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062348Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5A39B99C01499E77FA0345044825B146B69B7AC7DADF069F6AA03275FBD6A101)

-   The APIs of this module are no longer maintained since API version 6. You are advised to use [@ohos.net.http](../../arkts-apis/ohos-net-http-data-request/document.md).
    
-   The initial APIs of this module are supported since API version 3. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    

#### Modules to Import

import fetch from '@system.fetch';

#### fetch.fetch3+

fetch(options:{

url: string;

data?: string | object;

header?: Object;

method?: string;

responseType?: string;

success?: (data: FetchResponse) => void;

fail?: (data: any, code: number) => void;

complete?: () => void;

} ): void

Obtains data through a network.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| url | string | Yes | Resource URL. |
| data | string | Object | No | Request parameter, which can be a string or a JSON object. For details, see the mapping between **data** and **Content-Type**. |
| header | Object | No | Request header. |
| method | string | No | Request method. The default value is **GET**. The value can be **OPTIONS**, **GET**, **HEAD**, **POST**, **PUT**, \*\*DELETE \*\*or **TRACE**. |
| responseType | string | No | Response type. The return type can be text or JSON. By default, the return type is determined based on **Content-Type** in the header returned by the server. For details, see return values in the **success** callback. |
| success | Function | No | Called when the API call is successful. The return value is defined by [FetchResponse](#fetchresponse3). |
| fail | Function | No | Called when an API call fails. |
| complete | Function | No | Called when an API call is complete. |

**Table 1** Mapping between data and Content-Type

| data | Content-Type | Description |
| :-- | :-- | :-- |
| string | Left unspecified | The default value of Content-Type is **text/plain**, and the value of data is used as the request body. |
| string | Any type | The value of data is used as the request body. |
| Object | Left unspecified | The default value of **Content-Type** is **application/x-www-form-urlencoded**. The **data** value is encoded based on the URL rule and appended in the request body. |
| Object | application/x-www-form-urlencoded | The value of data is encoded based on the URL rule and is used as the request body. |

#### FetchResponse3+

**System capability**: SystemCapability.Communication.NetStack

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| code | number | No | No | Server status code. |
| data | string | Object | No | No | The type of the returned data is determined by **responseType**. For details, see the mapping between **responseType** and **data** in **success** callback. |
| headers | Object | No | No | All headers in the response from the server. |

**Table 2** Mapping between responseType and data in success callback

| responseType | data | Description |
| :-- | :-- | :-- |
| N/A | string | When the type in the header returned by the server is **text/\***, **application/json**, **application/javascript**, or **application/xml**, the value is the text content. |
| text | string | Text content. |
| json | Object | A JSON object. |

**Example**

export default {
  data: {
    responseData: 'NA',
    url: "test\_url",
  },
  fetch: function () {
    var that = this;
    fetch.fetch({
      url: that.url,
      success: function(response) {
        console.info("fetch success");
        that.responseData = JSON.stringify(response);
      },
      fail: function() {
        console.info("fetch fail");
      }
    });
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/sS4yFdxSQBKQoShPOk412w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062348Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2C538C215CAB75F13D95BD55A6F52CF0A5045364A4562F9EC32D2554165317AA)

HTTPS is supported by default. To support HTTP, you need to add **"network"** to the **config.json** file, and set the attribute **"cleartextTraffic"** to **true**, as shown below:

{
  "deviceConfig": {
    "default": {
      "network": {
        "cleartextTraffic": true
      }
      ... // Other configuration information
    }
  }
  ... // Other configuration information
}
