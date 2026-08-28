# Integration Modes for Host Apps

Share Kit provides two modes for host apps to integrate the system sharing capability.

| 
Integration Mode

 | 

Method & Application Scenario

 | 

Display Effect

 |
| :-- | :-- | :-- |
| 

Full integration

 | 

**Directly use the system sharing panel.**

This mode is applicable to Huawei-developed apps and apps which do not have business requirements on the sharing mode area. You can directly use the system sharing panel to reduce development costs.

 | 

**The system sharing panel is directly used.**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/xiYFIqNRQC6yhEWee3HS_A/en-us_image_0000002513409489.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062121Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B8F596DBDD53538796A62492E865B12646CB6D0C93B3A41B5A328C5BDC201EC3 "Click to enlarge")

 |
| 

Half integration

 | 

**You develop the sharing panel and provide the System Share entry on the sharing panel.**

This mode is applicable to apps which have business requirements for the sharing mode area or have their unique service logic.

 | 

On the left is a demo of your self-developed sharing panel, which provides the System Share entry. When a user taps **System Share**, the system sharing panel is displayed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/2H2C11hSTVK6VZZbzv-tPQ/en-us_image_0000002481169658.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062121Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F1DAD43CE46E004ECAE47864831A42743491BA58904F7ABF15A5E492DA0AB05D "Click to enlarge")

 |

#### Sample Code for the Full Integration Mode

[Reference: Development Procedure for Initiating Content Sharing Through System Share in a Mobile App](../initiating-content-sharing-through-the-sharing-panel/document.md#section8909161014458)

#### Code Snippet for the Half Integration Mode

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/Hz1WzCgtSumLBxNK4ZZjiw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062121Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=390D75107205379244B200EB0E4A4A2843C4F069550A523E2118BC96EF236E1C)

To enhance sharing experience, use the HarmonyOS system resource **$r('sys.symbol.share')** for the icon and **System Share** for text. Do not change the settings.

// Use the icon in Symbol format provided by the system as the sharing icon.
SymbolGlyph($r('sys.symbol.share'))
// Use **System Share** as the text.
Text('System Share')

For details about the complete sample code, please refer to [Sample Code - Access Model](https://gitcode.com/harmonyos_samples/share-kit_-sample-code_-clientdemo_-arkts/blob/master/entry/src/main/ets/components/AccessModel.ets).
