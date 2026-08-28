# Standard Events and App Attribution Signatures

#### Standard Conversion Event Information

| 
**Definition**

 | 

**Return Value**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

App installation

 | 

0

 | 

The app is installed successfully.

NOTE:

The attribution result of the app installation event is open to partners through a trustlist. By default, the attribution result is not returned. (For details about joining the trustlist, contact Huawei operations personnel.)

 |
| 

Activation

 | 

1

 | 

A user activates an app for the first time.

 |
| 

Launch

 | 

2

 | 

A user launches an app.

 |
| 

Day 1 retention

 | 

3

 | 

A newly acquired user uses the app again the next day.

 |
| 

Payment

 | 

4

 | 

A user makes an in-app purchase.

 |
| 

Form submission

 | 

5

 | 

A user submits a form in an app.

 |
| 

Authorization

 | 

6

 | 

A user gives authorization in an app.

 |
| 

Registration

 | 

7

 | 

A user signs up for an app or a service.

 |
| 

Key page access

 | 

9

 | 

A user browses a key page.

 |
| 

Request

 | 

14

 | 

A user requests a service.

 |
| 

Order

 | 

18

 | 

A user places an order.

 |
| 

Pre-order

 | 

21

 | 

A user pre-orders a product, content, or a service.

 |

#### Attribution Source Signature Calculation Rules

1\. Concatenate relevant fields according to the following sequence and separator to obtain a character string for signature verification:

adTechId+ '\\u2063' + campaignId+ '\\u2063'  + destinationId+ '\\u2063' + serviceTag+ '\\u2063' + mmpIdStr + '\\u2063' + nonce + '\\u2063' + timestamp

The rule for generating **mmpIdStr** is as follows:

If the array of attribution monitoring platforms is not empty, concatenate the elements within the array using **'\\u2063'** as a separator. For example, if **mmpIds** contains two attribution monitoring platforms, the concatenation result should be like this:

mmpIdStr = mmpId1 + '\\u2063' + mmpId2

2\. Use the private key paired with the public key generated when a distribution platform registers a role on the cloud platform of the app attribution service. Perform the signature calculation based on the character string obtained in step 1. The signature uses the SHA256withRSA/PSS algorithm, and the generated key is in a length of RSA3072.

3\. Non-empty fields in the API will be used for signing and signature verification, while those left empty are exempt from the process.

#### Signature Generation Method

You can generate a signature by referring to the following code, or you can generate one by yourself:

import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import {AegRsaSign} from "@hw-agconnect/petal-aegis";  // For details, check out the note at the end of this sample code.

const TAG: string = 'SignUtil';
const SEPARATOR: string = '\\u2063';

export class SignUtil {
  public static genSignContent(adTechId: string, campaignId: string, destinationId: string, mmpIds: string\[\], serviceTag: string, nonce: string, timestamp: number) {
    // mmpIdStr = mmpId1 + '\\u2063' + mmpId2
    // signContent:string= adTechId+ '\\u2063' + campaignId+ '\\u2063'  + destinationId+ '\\u2063' + serviceTag+ '\\u2063' + mmpIdStr + '\\u2063' + nonce + '\\u2063' + timestamp
    let content = SignUtil.addSeparator(adTechId)
      + SignUtil.addSeparator(campaignId)
      + SignUtil.addSeparator(destinationId)
      + SignUtil.addSeparator(serviceTag)
      + SignUtil.genMmpIds(mmpIds)
      + SignUtil.addSeparator(nonce)
      + timestamp;
    hilog.info(0,TAG,\`content = ${JSON.stringify(content)}\`);
    return content;
  }

  private static addSeparator(value: string | undefined): string {
    return value ? value + SEPARATOR : '';
  }

  private static genMmpIds(mmpIds: string\[\]) {
    let result: string = '';
    for (let mmpId of mmpIds) {
      if (mmpId) {
        result += SignUtil.addSeparator(mmpId);
      }
    }
    return result;
  }

  public static getSign(content: string, privateKey: string): Promise<string> {
    return new Promise<string>((resolve) => {
      AegRsaSign.ohAegSignRSAWithPSSTextBase64(content, privateKey).then(async (sign: string) => {
        hilog.info(0, TAG, "getSign success.");
        resolve(sign);
      }).catch((error: BusinessError) => {
        hilog.error(0, TAG, \`getSign failed. code is ${error.code}, message is ${error.message}\`);      
      });
    })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/0e4AwrmzS0yfgjzlJ5Uqmg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062100Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9B3AB4E98F76109E50D1ADD0BCB796B6D2492AA1D2FF82BED101FD478A4D6BBE)

The statement **import {AegRsaSign} from "@hw-agconnect/petal-aegis"** is used to generate a signature with **AegRsaSign.ohAegSignRSAWithPSSTextBase64**. See the details as follows:

Run the installation command **ohpm i @hw-agconnect/petal-aegis**.

For details about the API usage, please refer to ohAegSignRSAWithPSSTextBase64.
