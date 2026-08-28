# Dynamically Managing App Icons Through AppGallery Connect

With the icon management service, you can use AppGallery Connect to dynamically manage personalized app icons and switch them on the app side without requiring an app version update.

#### Requesting the Service

Before using the icon management service, send an email to Huawei operations personnel in the following format to request the service permission. The review takes 1 to 3 working days. You will receive the result via email and in the [interaction center](https://developer.huawei.com/consumer/en/doc/app/agc-help-interaction-center-0000002276985946).

-   Ensure that the app for which you want to enable the icon management service has been officially released. Otherwise, the service will fail to be enabled.
-   For details about how to query the app information and developer account information, please refer to [Viewing App Information](https://developer.huawei.com/consumer/en/doc/app/agc-help-view-app-info-0000002282674569).

<table><tbody><tr><td class="cellrowborder" valign="top" width="17.169999999999998%"><p>Email Address</p></td><td class="cellrowborder" valign="top" width="82.83%"><p>agconnect@huawei.com</p></td></tr><tr><td class="cellrowborder" valign="top" width="17.169999999999998%"><p>Email Subject</p></td><td class="cellrowborder" valign="top" width="82.83%"><p>Request to enable HarmonyOS app icon management for <em>app name</em></p></td></tr><tr><td class="cellrowborder" valign="top" width="17.169999999999998%"><p>Email Content</p></td><td class="cellrowborder" valign="top" width="82.83%"><p>Developer ID:</p><p>App name:</p><p>App ID:</p><p>App package name:</p><p>App status:</p></td></tr></tbody></table>

#### Configuring App Icons Through AppGallery Connect

Sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html#/), click **Apps and atomic services**, select your HarmonyOS app that has enabled the icon management service, and go to **Distribution** > **Services** > **Icons**. On the displayed page, you can manage personalized icons of the HarmonyOS app.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/GBrWUbVnQJaSUtrkEdcRxw/en-us_image_0000002337734704.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062059Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FAAE1B17E5FB815E7A8B3C680EF5509BEA9B473734DE28D7B1E491F68201E989 "Click to enlarge")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/VlIHMh2GQluYaH8keaFnmw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062059Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E7769AFB7C740FBB36E054D0D6E1B15B74EA79E6931B0DECC02D701211698558)

-   Only officially released HarmonyOS apps support management of personalized icons.
-   Before creating a personalized icon, prepare the icon file to be uploaded. The icon file must meet the [AppGallery Review Guidelines](https://developer.huawei.com/consumer/en/doc/app/50104).

#### Creating an Icon

1.  On the **Icons** page, click **New icon**.![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/gBWN66k8SQeNSQXEEiOHJg/en-us_image_0000002371652813.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062059Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C633F7D029EFFC0E1614CD396605A45026C69C1550524618E5F4E69BF843D9D6 "Click to enlarge")
2.  On the displayed page, enter an icon ID and icon name, select a device type, upload an icon file, and click **Save** or **Submit** to save the icon as a draft or submit the icon for review.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/6qwe2zWdQgW9qdKGa_7s4Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062059Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D21F5B66E2361A3E947967F9314B977AFDB6C6BAE4493682E677642D8D03A8E7)

-   Newly created icons can be used by your app only after being approved by AppGallery.
-   The icon review takes 1 to 3 working days. The review status and comments will be displayed on the icon information page, without other notifications.

#### Editing and Updating an Icon

1.  On the **Icons** page, select a draft or rejected icon and click **Edit**. Alternatively, select an approved icon and click **Update**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/cHzaipn3SoqZrfxTqyXkbg/en-us_image_0000002371732653.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062059Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A08D75D0733872427FF7A62D839A8774D20F3E33DB990F62B0F460AC65B5AE1B "Click to enlarge")
    
2.  On the displayed page, enter an icon ID and icon name, select a device type, upload an icon file, and click **Save** or **Submit** to save the icon as a draft or submit the icon for review.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/XwMzfzKASZqwpSRWA8u2ng/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062059Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C604EC8999DD2A26E1067AADAA4DF2AA4D3949CC079FAB8B29129C20429922C6)

-   Draft and rejected icons can be edited, but icons under review cannot. However, you can click **Cancel** to withdraw an icon from review, changing its status to draft.
-   Approved icons can be updated; however, only the icon name and file can be modified. The icon ID and device type remain fixed. Updates to icons must also be approved before they take effect.

#### Deleting an Icon

1.  On the **Icons** page, select an icon, click **Delete**, and click **OK** in the displayed dialog box.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/VpNtyWtISzWyyi4ze_nh1Q/en-us_image_0000002371652817.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062059Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1B5F70AF52CDA67D22E1FE4D649524B2F89FF2B4F313602D5934DFE2D82A7EAE "Click to enlarge")
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/2qNu3U4fReSIw-nmaR-SEw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062059Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D6580EA4C8C289162E3AF9FA6FD2A3EA7C4D1AEB90496951AFD2A906FF088743)

-   Deleting an icon does not need to be approved. Deleted icons cannot be restored. Exercise caution when performing this operation.
-   If an icon is currently displayed on users' device screens, deleting it will not automatically revert the display to the previous icon. The client must manually trigger the icon switching.
