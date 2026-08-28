# Examples

Assume that you want your app to come in the following editions:

1\. Community edition: a free of charge edition that provides most essential features of the app for individual developers, but does not support certain customized features or technical support.

2\. Ultimate edition: a paid edition that offers complete access to all essential features of the app, plus additional customized features and technical support.

As the Community and Ultimate editions share some features and yet unique in each, you may want to implement them with one-time development and differentiated configurations, so that they can be previewed, packaged, and debugged in specific running environments.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/-mmcSEEySLuTPO8ehEFmbw/en-us_image_0000002532670145.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=086DDC1B2EF6C4C86A43E4A51370CE59ADC4DC141C9C0496F6BCFFAF57ACAA78)

1\. App editions may differ in various aspects, including name, icon, and version statement. To add differentiators, add products under **app{}** > **products\[\]** in the project-level **build-profile.json5** file. In this example, products **Community** and **Ultimate** are added, and fields customized as required.

{
  "name": "Ultimate",
  // Configure the signature information for the Ultimate edition.
  "signingConfig": "Ultimate",
  // Bundle name for the Ultimate edition
  "bundleName": "com.example.ultimate.app",
  // App icon for the Ultimate edition
  "icon": "$media:app\_icon",
  // App label for the Ultimate edition
  "label": "$string:app\_name",
  "versionCode": 10000,
  "versionName": "1.0.0",
  // Resource directories for the Ultimate edition
  "resource": {
    "directories": \[
      "./AppScope/ultimateRes"
    \]
  },
  // Product name for the Ultimate edition
  "output": {
    "artifactName": "ultimate\_version"
  },
  "bundleType": "app",
  "compatibleSdkVersion": "6.0.2(22)",
  "runtimeOS": "HarmonyOS"
},
{
  "name": "Community",
  "signingConfig": "Community",
  // Configure the signature information for the Community edition.
  "bundleName": "com.example.community.app",
  // Bundle name for the Community edition
  "icon": "$media:app\_icon",
  // App icon for the Community edition
  "label": "$string:app\_name",
  // App label for the Community edition
  "versionCode": 10000,
  "versionName": "1.0.0",
  // Resource directories for the Community edition
  "resource": {
    "directories": \[
      "./AppScope/communityRes"
    \]
  },
  // Product name for the Community edition
  "output": {
    "artifactName": "community\_version"
  },
  "bundleType": "app",
  "compatibleSdkVersion": "6.0.2(22)",
  "runtimeOS": "HarmonyOS",
}

2\. You may want your app editions to deliver scenario-specific features. For example, in the Ultimate edition, you want feature A to be free of charge on phones and paid on TVs; in the Community edition, you want the startup page of feature B to display differently on 2-in-1 and wearable devices. In this case, you can define two targets in the module-level **build-profile.json5** file: **vip** and **free**.

{
  "name": "vip",
  // Product name for the vip target
  "output": {
    "artifactName": "vipVersion"
  },
  // Source code file for a specific page of the vip target
  "source": {
    "pages": \[
      "pages/vipIndex"
    \]
  },
  // Resource directories for the vip target
  "resource": {
    "directories": \[
      "./src/main/ultimateRes"
    \]
  },
  "config": {
    // Device types to which the vip target applies
    "deviceType": \[
      "phone",
      "tablet",
      "2in1"
    \]
  }
},
{
  "name": "free",
  // Product name for the free target
  "output": {
    "artifactName": "freeVersion"
  },
  // Source code file for a specific page of the free target
  "source": {
    "pages": \[
      "pages/freeIndex"
    \]
  },
  // Resource directories for the free target
  "resource": {
    "directories": \[
      "./src/main/communityRes"
    \]
  },
  "config": {
    // Device types to which the free target applies
    "deviceType": \[
      "phone",
      "tablet"
    \]
  }
}

3\. After adding products and targets, specify the mappings in **applyToProducts** under **targets\[\]** of **modules\[\]** in the project-level **build-profile.json5** file. to specify which products to which the current target applies.

"targets": \[
  {
    "name": "default",
    "applyToProducts": \[
      "default",
      "Community",
      "Ultimate"
    \]
  },
  {
    "name": "free",
    "applyToProducts": \[
      "default",
      "Community"
    \]
  },
  {
    "name": "vip",
    "applyToProducts": \[
      "default",
      "Ultimate"
    \]
  }
\]

According to the preceding configuration:

-   The **default** target applies to products **default**, **Ultimate**, and **Community**.
-   The **vip** target applies to products **default** and **Ultimate**.
-   The **free** target applies to products **default** and **Community**.

4\. Before starting a build, you can change the product-target mapping from the UI to create the required App Pack or HAP.

For example, to build an app of the Ultimate edition with the VIP features, set **product** to **Ultimate** and **target** to **vip**, and then click **apply**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/yY7-OfzrRo2VWAJlXXrmJA/en-us_image_0000002532750093.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=170518B165DDAD0A6A965BDEDAE50CDAC58B9B0403384DEAE30C7B1846419BC8)

View the build product.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/pEYqnnVzSLyRtkYQGcOQfA/en-us_image_0000002500910226.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=14F2E34B6452055E26167FAAFBDF0C84D8B4367A016BE26A0A86A0AAA8BD8466)
