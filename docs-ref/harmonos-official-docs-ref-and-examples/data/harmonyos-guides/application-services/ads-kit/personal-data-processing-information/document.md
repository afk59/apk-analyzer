# Personal Data Processing Information

In personal data processing, Huawei serves as the end user data controller. For appropriate and legal processing of personal data, the following are provided:

-   List of personal data processed by Huawei
-   Guidance for users to exercise their rights as a data subject

#### List of Personal Data Processed by Huawei

The following table lists the personal data processed by Ads Kit and the retention period.

| 
**Personal Data**

 | 

**Processing Purpose**

 | 

**Retention Period**

 |
| :-- | :-- | :-- |
| 

Device identifier (OAID), device model, device hardware information, operating system, device status, system settings, basic app information, app usage information, magnetometer, acceleration sensor, sensor information, gyroscope, network information, carrier information, IP address or IP address location, WLAN information (Wi-Fi parameters and Wi-Fi status), BSSID, SSID, data of other related Huawei apps, HUAWEI ID information, reported content, **contact information (email address or mobile number)**, supporting materials (images or videos), age, gender, personal preferences, app settings, search records, subscription information, and transaction records

 | 

To provide advertising services to users, assist in detecting and preventing fraud and other malicious activities in ads, attribute ad conversions for developers, ensure the smooth operation of developers' apps and Huawei apps, ensure cyber security as required by laws and regulations, fulfill statistics and settlement purposes, refine product strategies, process complaints and reports, and deliver personalized ads.

 | 

Until the end of the retention period. For purposes such as personalized recommendations, personalized advertising, marketing, user inquiries and suggestions, help and feedback, as well as complaints and reports, the personal information is usually kept for no more than two years. For product O&M, the personal information is usually kept for no more than five years.

 |

#### Guidance for Users to Exercise Their Rights as a Data Subject

## Disclosing Personal Information Processed by Ads Kit in the Privacy Policy

**We require you to inform users of how we will process their personal data in your privacy policy and obtain users' consent or other legal bases** before you integrate and use Ads Kit. You can contain a link in your user privacy policy or statement, so users can view [how Petal Ads uses relevant data](https://legal.cloud.huawei.com.cn/terms/scope/huawei/ads-hmos/privacy-statement.htm?&amp;code=CN&amp;language=en-US&amp;branchid=0&amp;contenttag=default) through this link.

Users can exercise their rights as a data subject by referring to the [Statement About Petal Ads and Privacy](https://legal.cloud.huawei.com.cn/terms/scope/huawei/ads-hmos/privacy-statement.htm?&amp;code=CN&amp;language=en-US&amp;branchid=0&amp;contenttag=default). If users have any further requests, questions, comments, or suggestions regarding their rights as a data subject, they can contact us through the information provided under the "Contacting Us" section of the **Statement About Petal Ads and Privacy**. We will reply as soon as possible and help users exercise their rights.

## Configuration of the Personalized Ad Recommendation Function

Ads Kit provides the capability of configuring personalized ad recommendation. Enable or disable the function based on your requirements.

You can call the [AdOptions.nonPersonalizedAd](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-advertising#adoptions) API to enable or disable the personalized ad function. If the function is disabled, non-personalized ads will be displayed to users. After the personalized ad function is disabled, the number of ads received by users will not decrease, but the ad content will be less relevant to them.
