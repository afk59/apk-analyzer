# CardRecognition (Card Recognition Control)

The card recognition control provides structured recognition services for ID cards, vehicle licenses, driver's licenses, passports, and bank cards. The system can automatically determine the type of a certificate and return its structured information as well as image information.

**Start version**: 5.0.0(12)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/C9knKifLR8azR3MVEIPVgw/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062525Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DEFD73226BFE156EB47DADE30B473442F69E44FB2A57FB246702D86557D7CA93)

Using this control will create and display a modal pop-up window. Therefore, starting and exiting this control will both trigger a lifecycle change of the accessed page. Specifically, starting the control will trigger **onPageHide** of the page, while exiting the control will trigger **onPageShow**.

#### Module Import

import { CardRecognition, CardRecognitionResult, CardType, CardSide, 
CardRecognitionConfig, ShootingMode, CardContentConfig, BankCardConfig } from "@kit.VisionKit";

#### CardRecognition

Card recognition control, which can be integrated to implement card recognition.

**Decorator type**: @Component

**System capability**: SystemCapability.AI.Component.CardRecognition

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Decorator Type

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

supportType

 | 

[CardType](#section156871424104118)

 | 

Yes

 | 

\-

 | 

Supported card types. Currently, only cards in the Chinese mainland can be recognized.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

cardSide

 | 

[CardSide](#section1823389379)

 | 

No

 | 

\-

 | 

Side of a card to be recognized. The default value is **DEFAULT**.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

callback(deprecated)

 | 

[Callback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<[CallbackParam](#section51945431662)\>

 | 

Yes

 | 

\-

 | 

Used to return the card recognition result.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

NOTE:

This parameter has been deprecated since version 5.1.1(19). You are advised to use **onResult** instead.

 |
| 

onResult

 | 

[Callback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<[CardRecognitionResult](#section161551745133610)\>

 | 

Yes

 | 

\-

 | 

Used to return the card recognition result.

**Atomic service API**: This API can be used in atomic services since API version 5.1.1(19).

**Start version**: 5.1.1(19)

 |
| 

cardRecognitionConfig

 | 

[CardRecognitionConfig](#section14439151274411)

 | 

No

 | 

\-

 | 

Card recognition configuration.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |

#### CardType

Enumeration of supported card types.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AI.Component.CardRecognition

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

CARD\_AUTO

 | 

0

 | 

Automatic card type recognition is used, and no card type is preset.

 |
| 

CARD\_ID

 | 

1

 | 

ID card.

 |
| 

CARD\_BANK

 | 

2

 | 

Bank card.

 |
| 

CARD\_PASSPORT

 | 

3

 | 

Passport.

 |
| 

CARD\_DRIVER\_LICENSE

 | 

4

 | 

Driver's license.

 |
| 

CARD\_VEHICLE\_LICENSE

 | 

5

 | 

Vehicle license.

 |

#### CardSide

Enumeration of card sides to be recognized.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AI.Component.CardRecognition

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

FRONT

 | 

0

 | 

Portrait side of an ID card or front side of other cards.

 |
| 

BACK

 | 

1

 | 

National emblem side of an ID card or back side of other cards.

 |
| 

DEFAULT

 | 

2

 | 

Default side. For example, the value is the portrait side of an ID card or the front side of any other cards.

 |

#### CallbackParam(deprecated)

Card recognition result parameters.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AI.Component.CardRecognition

**Start version**: 5.0.0(12)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/qZxZhcRMQ-qH501itXaIrQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062525Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B2AD91F2C987C859ECDEFB73F6A0575915E2213B65FD2B638A8B3D7F1667FDBF)

This API has been deprecated since version 5.1.1(19). You are advised to use [CardRecognitionResult](#section161551745133610) instead.

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

code

 | 

number

 | 

No

 | 

No

 | 

Result code (**200**: recognition success; **\-1**: recognition failure).

 |
| 

cardType

 | 

[CardType](#section156871424104118)

 | 

No

 | 

Yes

 | 

Card type. The default value is **CARD\_AUTO**.

 |
| 

cardInfo

 | 

Record<string, Record<string, string>>

 | 

No

 | 

Yes

 | 

Card information. The default value is **undefined**.

For a double-sided card, the information is **front** and **back**.

For a single-sided card, the information is **main**.

 |

#### CardRecognitionResult

Card recognition result parameters.

**Atomic service API**: This API can be used in atomic services since API version 5.1.1(19).

**System capability**: SystemCapability.AI.Component.CardRecognition

**Start version**: 5.1.1(19)

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

code

 | 

number

 | 

No

 | 

No

 | 

Result code.

**200**: The recognition is successful.

**1008701001**: Unrecognized.

**1008701002**: The recognition failed.

**1008701003**: Partial recognition failed.

**1008701004**: Recognition not completed.

 |
| 

cardType

 | 

[CardType](#section156871424104118)

 | 

No

 | 

Yes

 | 

Card type. The default value is **CARD\_AUTO**.

 |
| 

cardInfo

 | 

Record<string, Record<string, string>>

 | 

No

 | 

Yes

 | 

Card information. The default value is **undefined**.

For a double-sided card, the information is **front** and **back**.

For a single-sided card, the information is **main**.

 |

#### CardRecognitionConfig

Card recognition configuration.

**System capability**: SystemCapability.AI.Component.CardRecognition

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

defaultShootingMode

 | 

[ShootingMode](#section592243214505)

 | 

No

 | 

Yes

 | 

Photo shooting mode. The default value is **ShootingMode.MANUAL**.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

isPhotoSelectionSupported

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether images can be selected from the gallery.

-   **true**: yes (The gallery button is displayed and images can be selected from the gallery.)
-   **false**: no (The gallery button is not displayed and images cannot be selected from the gallery.)
    
    The default value is **true**.
    

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

setCardMargins

 | 

number

 | 

No

 | 

Yes

 | 

Margins around a cropped card image. Value range: \[10, 10000\]

If the specified margins are greater than the margin of any side of the original image, that side will retain its original margin and not be cropped.

The default value is **10**. The unit is px.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**Start version**: 5.0.3(15)

 |
| 

cardContentConfig

 | 

[CardContentConfig](#section11229154525217)

 | 

No

 | 

Yes

 | 

Card content configuration.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |

#### ShootingMode

Enumeration of shooting modes.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AI.Component.CardRecognition

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

AUTO

 | 

0

 | 

Automatic.

 |
| 

MANUAL

 | 

1

 | 

Manual.

 |

#### CardContentConfig

Card content configuration. You can set specific parameters for each type of card.

**System capability**: SystemCapability.AI.Component.CardRecognition

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

bankCard

 | 

[BankCardConfig](#section15184777561)

 | 

No

 | 

Yes

 | 

Specific configuration for bank card recognition.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

idCard

 | 

[IdCardConfig](#section1380264221010)

 | 

No

 | 

Yes

 | 

Specific configuration for ID card recognition.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

**Start version**: 5.0.2(14)

 |

#### BankCardConfig

Specific configuration for bank card recognition.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AI.Component.CardRecognition

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

isBankNumberDialogShown

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to display the bank card number confirmation dialog box after a bank card is recognized.

-   **true**: yes
-   **false**: no

The default value is **true**.

 |

#### IdCardConfig

Specific configuration for ID card recognition.

**System capability**: SystemCapability.AI.Component.CardRecognition

**Start version**: 5.0.2(14)

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

isPhotoNeeded

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to return the portrait image of an ID card after the portrait side of the ID card is recognized.

**true**: yes

**false**: no

The default value is **false**.

 |
| 

isQualityDetectionNeeded

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to enable quality check.

**true**: yes

**false**: no

The default value is **false**.

 |

#### cardInfo

Detailed card information, including the portrait and national emblem sides of an ID card, the bank card, the passport, the front and back sides of a driver's license, as well as the front and back sides of a vehicle license.

Portrait side of an ID card:

**Start version**: 5.0.0(12)

| 
Parameter

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- |
| 

name

 | 

string

 | 

Name.

 |
| 

sex

 | 

string

 | 

Gender.

 |
| 

nationality

 | 

string

 | 

Ethnicity.

 |
| 

birth

 | 

string

 | 

Date of birth.

 |
| 

address

 | 

string

 | 

Address.

 |
| 

idNumber

 | 

string

 | 

Identification number.

 |
| 

cardImageUri

 | 

string

 | 

Image URI of the portrait side of an ID card (excluding the background).

 |
| 

originalImageUri

 | 

string

 | 

Image URI of the portrait side of an ID card (including the background).

 |
| 

photoUri

 | 

string

 | 

Image URI of the portrait on the portrait side of an ID card. This parameter is returned only when **isPhotoNeeded** is set to **true**.

**Start version**: 5.0.2(14)

 |
| 

photoLocation

 | 

string

 | 

Coordinates of a portrait image within an ID card image (portrait side) specified by **cardImageUri**. In the parameter value, **top**, **left**, **width**, and **height** indicate the top point, left point, width, and height of the portrait image, respectively.

This parameter is returned only when **isPhotoNeeded** is set to **true**.

**Start version**: 5.0.2(14)

 |
| 

completenessProbability

 | 

string

 | 

Probability of completeness. The value range is (0, 1). A larger value indicates a higher probability of completeness.

**Start version**: 5.0.2(14)

 |
| 

reflectionProbability

 | 

string

 | 

Probability of light reflection. The value range is (0, 1). A larger value indicates a higher probability of light reflection.

**Start version**: 5.0.2(14)

 |
| 

clarityProbability

 | 

string

 | 

Probability of clarity. The value range is (0, 1). A larger value indicates a higher probability of clarity.

**Start version**: 5.0.2(14)

 |
| 

occlusionProbability

 | 

string

 | 

Probability of occlusion. The value range is (0, 1). A larger value indicates a higher probability of occlusion.

**Start version**: 5.0.2(14)

 |

National emblem side of an ID card:

**Start version**: 5.0.0(12)

| 
Parameter

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- |
| 

authority

 | 

string

 | 

Issuing authority.

 |
| 

validPeriod

 | 

string

 | 

Validity period.

 |
| 

cardImageUri

 | 

string

 | 

Image URI of the national emblem side of an ID card (excluding the background).

 |
| 

originalImageUri

 | 

string

 | 

Image URI of the national emblem side of an ID card (including the background).

 |
| 

completenessProbability

 | 

string

 | 

Probability of completeness. The value range is (0, 1). A larger value indicates a higher probability of completeness.

**Start version**: 5.0.2(14)

 |
| 

reflectionProbability

 | 

string

 | 

Probability of light reflection. The value range is (0, 1). A larger value indicates a higher probability of light reflection.

**Start version**: 5.0.2(14)

 |
| 

clarityProbability

 | 

string

 | 

Probability of clarity. The value range is (0, 1). A larger value indicates a higher probability of clarity.

**Start version**: 5.0.2(14)

 |
| 

occlusionProbability

 | 

string

 | 

Probability of occlusion. The value range is (0, 1). A larger value indicates a higher probability of occlusion.

**Start version**: 5.0.2(14)

 |

Bank card:

**Start version**: 5.0.0(12)

| 
Parameter

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- |
| 

bankNum

 | 

string

 | 

Bank card number.

 |
| 

validPeriod

 | 

string

 | 

Validity period.

 |
| 

cardImageUri

 | 

string

 | 

Image URI of a bank card (excluding the background).

 |
| 

originalImageUri

 | 

string

 | 

Image URI of a bank card (including the background).

 |

Passport:

**Start version**: 5.0.0(12)

| 
Parameter

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- |
| 

cardNum

 | 

string

 | 

Passport number.

 |
| 

name

 | 

string

 | 

Name.

 |
| 

sex

 | 

string

 | 

Gender.

 |
| 

nationality

 | 

string

 | 

Nationality.

 |
| 

birth

 | 

string

 | 

Date of birth.

 |
| 

address

 | 

string

 | 

Place of birth.

 |
| 

issueDate

 | 

string

 | 

Date of issue.

 |
| 

issuePlace

 | 

string

 | 

Place of issue.

 |
| 

expiryDate

 | 

string

 | 

Date of expiry.

 |
| 

authority

 | 

string

 | 

Issuing authority.

 |
| 

pochn

 | 

string

 | 

Passport for private affairs.

 |
| 

cardImageUri

 | 

string

 | 

Image URI of a passport (excluding the background).

 |
| 

originalImageUri

 | 

string

 | 

Image URI of a passport (including the background).

 |

Front side of a driver's license:

**Start version**: 5.0.0(12)

| 
Parameter

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- |
| 

cardNum

 | 

string

 | 

License number.

 |
| 

name

 | 

string

 | 

Name.

 |
| 

sex

 | 

string

 | 

Gender.

 |
| 

nationality

 | 

string

 | 

Nationality.

 |
| 

birth

 | 

string

 | 

Date of birth.

 |
| 

address

 | 

string

 | 

Address.

 |
| 

dateOfFirstIssue

 | 

string

 | 

Date of first issue.

 |
| 

carClass

 | 

string

 | 

License class.

 |
| 

validPeriodStart

 | 

string

 | 

Start date of the validity period.

 |
| 

validPeriodEnd

 | 

string

 | 

End date of the validity period.

 |
| 

cardImageUri

 | 

string

 | 

Image URI of the front side of a driver's license (excluding the background).

 |
| 

originalImageUri

 | 

string

 | 

Image URI of the front side of a driver's license (including the background).

 |

Back side of a driver's license:

**Start version**: 5.0.0(12)

| 
Parameter

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- |
| 

cardNum

 | 

string

 | 

License number.

 |
| 

name

 | 

string

 | 

Name.

 |
| 

archivesNum

 | 

string

 | 

Archive number.

 |
| 

record

 | 

string

 | 

Record of additional information.

 |
| 

cardImageUri

 | 

string

 | 

Image URI of the back side of a driver's license (excluding the background).

 |
| 

originalImageUri

 | 

string

 | 

Image URI of the back side of a driver's license (including the background).

 |

Front side of a vehicle license:

**Start version**: 5.0.0(12)

| 
Parameter

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- |
| 

licensePlateNumber

 | 

string

 | 

License plate number.

 |
| 

vehicleType

 | 

string

 | 

Vehicle type.

 |
| 

owner

 | 

string

 | 

Owner.

 |
| 

address

 | 

string

 | 

Address.

 |
| 

useCharacter

 | 

string

 | 

Use character.

 |
| 

model

 | 

string

 | 

Model.

 |
| 

vin

 | 

string

 | 

Vehicle identification number.

 |
| 

engineNum

 | 

string

 | 

Engine number.

 |
| 

registerDate

 | 

string

 | 

Registration date.

 |
| 

issueDate

 | 

string

 | 

Issue date.

 |
| 

cardImageUri

 | 

string

 | 

Image URI of the front side of a vehicle license (excluding the background).

 |
| 

originalImageUri

 | 

string

 | 

Image URI of the front side of a vehicle license (including the background).

 |

Back side of a vehicle license:

**Start version**: 5.0.0(12)

| 
Parameter

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- |
| 

cardNum

 | 

string

 | 

License plate number.

 |
| 

size

 | 

string

 | 

Vehicle dimensions.

 |
| 

remark

 | 

string

 | 

Remarks.

 |
| 

record

 | 

string

 | 

Inspection records.

 |
| 

cardImageUri

 | 

string

 | 

Image URI of the back side of a vehicle license (excluding the background).

 |
| 

originalImageUri

 | 

string

 | 

Image URI of the back side of a vehicle license (including the background).

 |
