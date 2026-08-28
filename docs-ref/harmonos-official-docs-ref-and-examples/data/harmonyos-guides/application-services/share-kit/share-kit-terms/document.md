# Share Kit Terms

#### Content Area

Displays the title, preview, and selection of the shared content.

#### Host App

App that initiates the sharing. The host app calls the sharing API to configure information such as the content to be shared and preview style and displays the sharing panel.

#### Operation Area

Provides content-related operations, such as copying, saving, saving as, and printing.

#### Recommendation Area

Integrates Share Kit and [Intents Kit](../../../ai/intents-kit/about-this-kit/document.md) and uses algorithms to efficiently and accurately recommend devices and target app users that can process the shared content.

#### Sharing Mode Area

Obtains target apps that support the shared content through the package management service of HarmonyOS. The following redirection methods are supported:

1\. Redirects to the **UIAbility** component in the target app.

2\. Redirects to the **ExtensionAbility** component provided by the target app.

The target app developer needs to configure the description of the **UIAbility** and **ExtensionAbility** components in the [module.json5 configuration file](../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md) to declare the supported types of shared data.

#### Sharing Details Page

Displayed when a user taps a sharing mode.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/PFxpHqZ2SN6DHpkeyj9wGw/en-us_image_0000002513409497.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062121Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=894C7146AB288CBC476851AAC6BBDEC3817CA1269CD95702FE0E0927092A9442 "Click to enlarge")

#### Source Device

Device that initiates content sharing. The source device sends the shared data to the target device through Huawei Share.

#### Target App

App that receives the shared content. You need to develop the data processing ability in the target app and declare the ability according to the target app integration guide, so that the package management service can identify the ability supported by the app.

#### Target Device

Device that receives the shared content. The target device chooses the appropriate app to store or open the shared content based on the data type.
