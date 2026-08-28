# Examples

This section describes the configuration of project-level and module-level customized parameters and the switch of products to display different messages.

#### Creating a Project and a HAR Module

To use a custom parameter **productMessage** across all modules in your project, you can configure the project-level **build-profile.json5** file as follows.

You switch between different **productMessage** values by changing the product.

{
  "app": {
    "products": \[
      {
        "name": "default",
        "signingConfig": "default",
        "compatibleSdkVersion": "6.0.2(22)",
        "runtimeOS": "HarmonyOS",
        "buildOption": {
          "arkOptions": {
            // Project-level custom parameter 
            "buildProfileFields": {
              "productMessage": 'defaultMessage'
            }
          }
        }
      },
      {
        "name": "mirror",
        "signingConfig": "default",
        "compatibleSdkVersion": "6.0.2(22)",
        "runtimeOS": "HarmonyOS",
        "buildOption": {
          "arkOptions": {
            // Project-level custom parameter 
            "buildProfileFields": {
              "productMessage": 'mirrorMessage'
            }
          }
        }
      },
      {
        "name": "product",
        "signingConfig": "default",
        "compatibleSdkVersion": "6.0.2(22)",
        "runtimeOS": "HarmonyOS",
        "buildOption": {
          "arkOptions": {
            // Project-level custom parameter 
            "buildProfileFields": {
              "productMessage": 'productMessage'
            }
          }
        }
      }
    \],
    "buildModeSet": \[
      {
        "name": "debug",
      },
      {
        "name": "release"
      }
    \]
  },
  "modules": \[
    {
      "name": "entry",
      "srcPath": "./entry",
      "targets": \[
        {
          "name": "default",
          "applyToProducts": \[
            // Associate with multiple products.
            "default",
            "product",
            "mirror"
          \]
        }
      \]
    },
    {
      "name": "har",
      "srcPath": "./har"
    }
  \]
}

Configure the following code in **build-profile.json5** of the HAR module:

{
  "apiType": "stageMode",
  "buildOption": {
    "arkOptions": {
      // Customized parameter of the HAR module
      "buildProfileFields": {
        "targetMessage1": 'this is target buildProfileValue1',
        "targetMessage2": 'this is target buildProfileValue2'
      }
    }
  },
  "buildOptionSet": \[
    {
      "name": "release",
      "arkOptions": {
        "obfuscation": {
          "ruleOptions": {
            "enable": true,
            "files": \[
              "./obfuscation-rules.txt"
            \]
          },
          "consumerFiles": \[
            "./consumer-rules.txt"
          \]
        }
      },
    },
  \],
  "targets": \[
    {
      "name": "default"
    }
  \]
}

Add the following code to **MainPage.ets** of the HAR module:

import BuildProfile from "../../../../BuildProfile"

@Preview
@Component
export struct MainPage {
  // The default value is the value of **productMessage** configured in the project-level **BuildProfile**.
  @State message: string = BuildProfile.productMessage
  build() {
    Row() {
      Column() {
        Flex({ direction: FlexDirection.Row, alignItems: ItemAlign.Start, justifyContent: FlexAlign.SpaceAround }) {
          Button("Button 1").width("40%")
            .onClick(() => {
              // Click to display the customized field **targetMessage1**.
              this.message = BuildProfile.targetMessage1;
            })
          Button("Button 2").width("40%")
            .onClick(() => {
              // Click to display the customized field **targetMessage2**.
              this.message = BuildProfile.targetMessage2;
            })
        }.margin(20)
        .width(315)
        Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start, justifyContent: FlexAlign.SpaceBetween }) {
          Text(this.message)
            .textAlign(TextAlign.Start)
            .fontSize(12)
            .border({ width: 1 })
            .padding(10)
            .width('100%')
        }.height(600).width(350).padding({ left: 35, right: 35})
      }
    }
  }
}

Reference the local HAR module in **oh-package.json5** of the HAP:

{
  "name": "entry",
  "version": "1.0.0",
  "description": "Please describe the basic information.",
  "main": "",
  "author": "",
  "license": "",
  "dependencies": {
    "har": "file:../har"
  }
}

Reference the HAR package in the **Index.ets** file of the HAP and use the **MainPage** method:

import { MainPage } from "har"

@Entry
@Component
struct Index {
  build() {
    Row() {
      MainPage()
    }
  }
}

#### Pushing the Package to the Device for Debugging After Preview or Signing

Click **har** and choose **Build** > **Generate Build Profile 'har'**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/58n3NUXSTJWKQAp9_vb_dA/en-us_image_0000002501070298.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062155Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CFC93EA4B88F8FA85416CF6B84FBDAF9B61554A606D1C524E570D294620F176A)

If **Product** is set to **default**, the initialized message is **defaultMessage**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/5j5IeMD0TZ2SSh7orK7abw/en-us_image_0000002532670371.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062155Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=64018A27DACF957C90A34EC9DB6758067F75337D59578D1EF26267FC4FCDE231)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/_xcdpVs-SlObRQxRmQCw2Q/en-us_image_0000002500910448.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062155Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7A15A9636FD418758E441DB8CB0A5984DE168A9A7D428A2B321BB0111EB44D05)

By switching **Product** values, you can use different customized parameters to initialize the message.

Switch **Product** to **mirror**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/pJLZbwKkSheBZ58DfVwjCQ/en-us_image_0000002500910446.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062155Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2F2EB226093830931E79FC4D7F0C1BCEAC9F3359970052D93C21A4830EDC95B4)

The initialized message is **mirrorMessage**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/DAQp0bVfTpWj2TXzWc4kqA/en-us_image_0000002501070294.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062155Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4DE4C7A8B26CD3F4970D0F44B418D516A6583F04F8E68CDD6FC91C91421B31B3)

You can click a button to change the initialized message to the corresponding customized value.

**Figure 1** Clicking Button1  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/UdJWFIV6QIu9MPS6IyjL5Q/en-us_image_0000002532750321.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062155Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3B9B3F7F186B29BFACD23B2F54BD8A3EDB46DF086F64724FEBBED67F47E98F02)

**Figure 2** Clicking Button2  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/mohkT3eMTyGDpmGQjtgm2Q/en-us_image_0000002532750317.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062155Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=000A0B407F4196DF694B8EADC60760BD0699B2AF35016767CB8B1871661C044B)
