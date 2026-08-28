# About This Kit

Natural Language Kit provides multiple basic capabilities related to text semantic understanding, helping you better process and analyze text data. To be specific, this kit implements the following functions:

1.  Word segmentation: Divides a piece of text into independent word units to identify each word in a sentence. This is a basic step for natural language processing, laying a foundation for subsequent tasks such as semantic analysis and information extraction.
2.  Entity extraction: Identifies text entities with specific meanings, such as persons' names, place names, dates and times, digits, mobile numbers, and email addresses. These entities play an important role in many scenarios, for example, information retrieval, knowledge graph construction, and intelligent Q&A.
    
    By leveraging these capabilities and integrating them with your specific service scenarios, you can create a wide range of intelligent apps to meet your service objectives.
    

#### Restrictions

## Supported Devices

Phones, tablets, and PCs/2-in-1 devices.

## Supported Country/Region

Currently, this capability is available only in the Chinese mainland.

## Restrictions on Capabilities

| 
AI Capability

 | 

Restriction

 |
| :-- | :-- |
| 

Word segmentation

 | 

-   Supported languages: simplified Chinese, English within a Chinese context, and traditional Chinese
-   Text length: no more than 1,000 characters

 |
| 

Entity extraction

 | 

-   Supported languages: simplified Chinese, English within a Chinese context, and traditional Chinese
-   Supported entities: time, location, email address, courier number, flight number, person's name, mobile number, website link, verification code, and certificate number
-   Text length: no more than 1,000 characters

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/cq0hfaE3ScC01u4-cvhgxQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062128Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=66E2DF1F59F275EC5AB7E78A50D836C3C2CA2C3A297BF3AF2F3CBEE97331858C)

Natural Language Kit allows multiple users to access its features concurrently. However, a user cannot call the same feature concurrently. If a process calls the same feature multiple times at the same time, the system will return a busy error. If multiple processes call the same feature at the same time, only one request will be executed, while the others will be queued.

#### Emulator Support

Currently, this kit does not support emulators.
