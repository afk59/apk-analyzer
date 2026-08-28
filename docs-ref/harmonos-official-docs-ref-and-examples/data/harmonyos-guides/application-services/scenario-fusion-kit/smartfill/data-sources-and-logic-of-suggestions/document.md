# Data Sources and Logic of Suggestions

SmartFill obtains information from Account Kit, clipboard, calendar events, contacts, and recent forms to provide filling suggestions.

| 
Rule

 | 

Description

 |
| :-- | :-- |
| 

Data source suggestion priority

 | 

Data source suggestion priority in the multi-box suggestion scenario: Clipboard > Recent forms > Account Kit > Contacts

 |
| 

Data source suggestion priority in the single-box suggestion scenario: Clipboard > Calendar events > Account Kit

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/VCwkDGotTGeVmIM3po9T9w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062119Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8C24EAABF7378BE2C155F55938B4E915FD5D319F8518CCBF5C8AB3B985D908B6)

The priority definition in the preceding table is recommended by default. SmartFill prioritizes suggestion data sources based on how well they match the data, with the highest priority given to data from the clipboard.

#### Suggestion Modes of Data Sources

| 
Data Source

 | 

Active Suggestion

 | 

Matched Suggestion

 |
| :-- | :-- | :-- |
| 

Account Kit

 | 

Yes

 | 

Yes

 |
| 

Contacts

 | 

No

 | 

Yes

 |
| 

Calendar events

 | 

Yes

 | 

No

 |
| 

Clipboard

 | 

Yes

 | 

Yes

 |
| 

Recent forms

 | 

No (Active suggestion is available for license plate number/passport input scenarios.)

 | 

Yes

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/5W2Fmp1sSHGw8X9xQmgRPQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062119Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CF4B7B8E02621B29A300AEFD3CEC16DFCB6CD36BDEA3C71BA6AB2C5A179CBEB2)

Currently, only Chinese names and addresses are supported for suggestions based on clipboard content.

## Differences Between Proactive and Matched Suggestions

| 
Suggestion Mode

 | 

Description

 |
| :-- | :-- |
| 

Proactive suggestion

 | 

1.  When a user taps an input component, SmartFill provides suggestions actively.
2.  A maximum of two suggestions can be displayed.

 |
| 

Matched suggestion

 | 

1.  When a user inputs text in an input component, SmartFill matches data based on the existing input from data sources for suggestions.
2.  A maximum of three suggestions can be displayed.

 |

#### Suggestion Data Sources in Some Scenarios

| 
Scenario

 | 

Data Source Description

 |
| :-- | :-- |
| 

Single-box address input

 | 

Only location information from the clipboard and calendar events is used for suggestion.

 |
| 

Single-box nickname input

 | 

Only the nickname associated with a HUAWEI ID is suggested.

 |
| 

Single-box input for a license plate number with multiple input boxes (one for each character)

 | 

Suggestions are made only based on the device owner's recent form information. (The owner is identified by the signed-in HUAWEI ID, which is the combination of real name + mobile number/email address. To determine the real name information, the Account Kit data source needs to be enabled.) In this scenario, only active suggestion is supported.

 |
| 

ID card number suggestion logic

 | 

If a device does not have a lock screen password, the ID card information from Account Kit and recent forms is used for suggestion. If a user actively copies ID card information, the ID card information from the clipboard can also be used for suggestion.

 |
| 

Passport information suggestion logic

 | 

1\. Currently, only Chinese names and pinyin names (family name + given name) can be suggested. 2. If the device does not have a lock screen password or has no real-name-verified HUAWEI ID signed in, input suggestions are not supported. 3. Active suggestion is available only for the device owner (with the owner information the same as the real-name information of the signed-in HUAWEI ID). To determine the real name information, the Account Kit data source needs to be enabled. 4. Matched suggestion supports pinyin names (family name + given name).

 |
| 

Sign-in of different HUAWEI ID types

 | 

When a HUAWEI ID that belongs to an adult in the Chinese mainland signs in on a device, information from the clipboard, calendar events, contacts, Account Kit, and recent forms can be used for suggestion. For other types of HUAWEI IDs, the data sources that are supported include only the clipboard, calendar events, and contacts.

 |
