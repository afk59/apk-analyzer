# About This Kit

Speech Kit, a scenario-based voice service, integrates AI-powered speech capabilities, including **TextReader** (reading control) and **AICaptionComponent** (AI caption control). It enables seamless interaction between users and devices, allowing users to have articles read aloud effortlessly.

#### Use Cases

-   The reading control is widely used when it is inconvenient for a user to view texts on the screen, and the control will read news and provide information for the user.
-   The AI caption control offers a captioning service for users who are unfamiliar with the audio source language or when the audio is muted. It allows them to follow along with the content through captions.

#### Restrictions

## Supported Devices

Phones, tablets, and PCs/2-in-1 devices.

## Supported Countries/Regions

Currently, this kit is available only in the Chinese mainland.

## Restrictions on Capabilities

| 
AI Capability

 | 

Restriction

 |
| :-- | :-- |
| 

Reading control

 | 

Supported language: Chinese

 |
| 

AI caption control

 | 

Supported languages: Chinese and English

Supported audio streams:

-   Audio type: Only PCM is supported.
-   Audio sampling rate: Only sampling rate 16000 is supported.
-   Audio channel: Only one audio channel is supported.
-   Audio sampling bit depth: Only 16-bit is supported.

This control is not supported on some device models. If the call fails, the [initialization failure](https://developer.huawei.com/consumer/en/doc/harmonyos-references/speech-errorcode#section1989336165612) error code is returned.

 |

#### Emulator Support

Currently, this kit does not support emulators.
