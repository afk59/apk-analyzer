# Common Event Manager

Common Event Manager (cem) provides the common event debugging and testing capabilities that enable you to print common event information such as all common event subscribers, sent common events, and recipients, and publish common events.

#### Environment Requirements

Before using this tool, you need to obtain [hdc](../../performance-analysis-kit/command-line-tools/hdc/document.md) and run the **hdc shell** command.

#### cem Commands

| Command | Description |
| :-- | :-- |
| help | Displays the cem help information. |
| publish | Publishes a common event. |
| dump | Dumps information about common events. |

#### help

\# Display the cem help information.
cem help

#### publish

\# Publish a common event.
cem publish \[<options>\]

**Parameters**

| Name | Description |
| :-- | :-- |
| \-e/--event | Name of the common event to publish. This parameter is mandatory. |
| \-o/--ordered | Indicates that the common event to publish is ordered. By default, non-ordered events are published. This parameter is optional. |
| \-c/--code | Result code of the common event. This parameter is optional. |
| \-d/--data | Data carried in the common event. This parameter is optional. |
| \-h/--help | Help information. |

**Example**

\# Publish a common event named testevent.
cem publish --event "testevent"

\# Publish an ordered common event named testevent. The result code of the event is 100 and the data carried is "this is data".
cem publish -e "testevent" -o -c 100 -d "this is data"

#### dump

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/z-XU-8TER2KXTnafhvb26A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062032Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C1D46DC4BAB766B02D4FE51B44CF66FA14DBFA1E0AD1900C89E8D285F8A47092)

Common Event Manager has two editions: **eng** and **user**. The **dump** command can be used only in the **eng** edition. If it is used in the **user** edition, the message **error: user version cannot use dump** is reported.

\# Dumps information about common events.
cem dump \[<options>\]

**Parameters**

| Name | Description |
| :-- | :-- |
| \-a/--all | Information about all common events that have been sent since system startup. |
| \-e/--event | Information about a specific event. |
| \-h/--help | Help information. |

**Example**

\# Display details of a common event named testevent.
cem dump -e "testevent"
