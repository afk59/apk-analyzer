# Layout Analysis

You can use ArkUI Inspector to view how your app looks on a real device via DevEco Studio and interact with the app to detect and analyze UI problems.

You can use ArkUI Inspector to:

-   View the UI display effect of an app on a device.
-   Export and import app UI snapshots, and view the UI display effect without the device.
-   View component attributes on the UI by selecting a UI component from the component tree.
-   View component attributes in the component tree by clicking a component on the UI.
-   Switch to the source code from a UI component.
-   View the display area of all components on the current canvas by selecting **Show Component Border**.
-   View the state variables configured for the selected component as well as affected components.
-   Expand the application in 3D by component, making it easy to view the nesting and occlusion relationships between components.

#### Scenarios

For apps with complex GUI, you can use ArkUI Inspector to:

-   View the parent-child relationship of components in the component tree to check for redundant components.
-   Analyze and locate UI display exceptions that occur when the app runs on a real device or the Emulator, especially UI errors and background logic errors that occur after complex UI operations.

#### Constraints

-   Only the apps running in the foreground can be viewed by ArkUI Inspector.
-   ArkUI Inspector works only when a device is connected using a USB cable or via Wi-Fi.
-   Only the projects based on the stage model are supported.
-   Only apps displayed in full screen and windows that are in focus in the foreground are supported.
-   Commercial signed apps on AppGallery are not supported.

#### Procedure

1.  Click **ArkUI Inspector** in the lower part of DevEco Studio to open ArkUI Inspector.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/RbV8uReXTm6UPfshG6P9Bg/en-us_image_0000002500909938.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=557B7215C9031982624EFF8C554B65078503525451EA3B1DC53350856968C4C3)
    
2.  Click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/-SC7PVggQfaVfq6IP9jCwA/en-us_image_0000002532669839.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=743DD708AA1BD3ADAB74042B9220F1A03C3F94000B22AC63FAF8A66DFA81CA8D) **Run** or ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/lrUj4oi-SC-ogRzKhzIKUQ/en-us_image_0000002532669875.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B440E24ABEC8B9076F6B40C2FABF29790A6D0588FF7A6DB0FAFA0111892238C2) **Debug** to push the app package to the connected device. In the device app list, select the UI process that is currently displayed in the foreground of the device.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/WEWv_Vh6TL-ftM1VQBhm0A/en-us_image_0000002532749811.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=27812726ECEF760408D05CB5682DCC1176314B66A2C796C80F72DDEB17C3C121)
    
3.  The left pane of ArkUI Inspector displays the component tree structure, the middle pane displays the UI of the current device, and the right pane displays the attributes of the selected component. You can select a component from the component tree on the left pane or click the component on the UI in the middle pane. When the UI on the device changes, you can click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/kLXuWBF0TQmviWNCNtu7_Q/en-us_image_0000002500909944.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BD977EFE35CF1267DA5E4A05076D67BCA4A503E67D060130836CFCDC36532DA7) in the upper right corner of the middle pane to refresh the UI effect.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/sHuemRhOSZ-KYpbxvmebig/en-us_image_0000002501069804.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D488589F0F7CCE53AD82BF77D28173A1F327A9B1AD204A2C2A28E71142159BAC)
    
4.  In the device box, click **Stop inspector** to disconnect from the device.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/wV6pmaMeRcya5Wz9nSxm0g/en-us_image_0000002532669877.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F003EC045614B859FAF75298229A33EDA98E7E16CD01B7A75DC6C9DA562AAC38)
    

#### Displaying Component Information

-   Click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/z3-IL2hDT426ac03LcEqTQ/en-us_image_0000002501069792.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6F17078F7EEF6FF5A1DEF92D71B37305EF83764D7D3F4869C933B06820302C06 "Click to enlarge") and select **Show Tree Statistics** to display the component information in the component tree.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/bP_aMGhMSnad-ZlmAsn0QQ/en-us_image_0000002532749783.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F170D1CBC7E408E0D9B6F13CA902B3D210631605B7125F0C56DBD242E1A2114D)
    
-   Click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/Tlm7lX8aTSW1toINQQrgOQ/en-us_image_0000002532669831.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=70865BAC8C034C40439DA699315B59D6D476CE5AA538D6DBF2AEDF798255D033 "Click to enlarge") and select **Show Hidden Components** to display hidden components.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/6WouBN9GRNesKATJnDPNJg/en-us_image_0000002532749781.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C4197E0FD90A878A1F7C9114498BF7593CFF8FE30731FF88A29A1E068DAFF77C)
    
-   Click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/AYBFuZSlQaqMbCvdsm2PQA/en-us_image_0000002500909904.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AFC379B69BA3C11F9A75A858C16FE1CD996187F15E3E0AF663C9E5A0D7FF80A8 "Click to enlarge") and select **Show Custom Components** to filter custom components.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/lwZ8t718RsiXW53s8N2bxA/en-us_image_0000002532749809.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=151D1782196D8EC381ED2F55D16DFA5DAC412427BA0C5ED0550FE7FDAE7F28A0)
    
-   Click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/9_L0KBYcR-2KT3LlctI2yA/en-us_image_0000002500909920.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=10794603CE435DD16049CC91063CD423DD28E341D116F94F436FC8569AD1EB4A) and select **Show System Components** to filter system components.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/DIEarmIbQBOsgD7zj9zX4g/en-us_image_0000002500909940.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9E7042FA88E6C4520D95C39D6730EA86F65297081166020977681A038BA6AFC1)
    

#### Importing/Exporting UI Snapshots

UI snapshots enable you to view the UI display effects without the device.

-   To import a local UI snapshot, click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/O5HO0-xsSFm_3YbHJoysCA/en-us_image_0000002532749769.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1B4F33C9DC9F1E0639BF3AA56E4757FB1C6895EC590BB38868B1917A303593C6) in the middle pane. The imported snapshot is opened in DevEco Studio.
-   To export an app UI snapshot, click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/3JRIzQkISTiwwDZ9EWWtLw/en-us_image_0000002501069806.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F68F08CE3CA195A453A694B6AEF05F1718ECBE1853F6BD045DA9ED454A7755AD) in the middle pane. The exported snapshot is opened in DevEco Studio by default.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/oRR61gjYRqC4WiJLHzc7iA/en-us_image_0000002532669867.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5A1976319847D47524472398009451AEF25F7CECCA4E2B005BD89A32B05AE7BA)

#### Navigating to Source Code from UI Components

1.  Choose **Run** > **Edit Configurations**, select **Enable DebugLine**, and click **OK** to enable source code navigation.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/6IHp4AFsQ8CDYYSdO8agIA/en-us_image_0000002532749801.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2AAFA26E6CDCCCF99E7993B1E72070DDC0F6D9F25A711982F85EB3F97416B323)
    
2.  In ArkUI Inspector, select a UI component and click the redirect button in the right pane to go to the source code of the UI component.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/lTnWvES2Qci_kzNoBC8s-Q/en-us_image_0000002501069796.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=068F125E09A7CAD62AB812BE1F486B87DC08B3762930387EECF2401C2B912FF2 "Click to enlarge")
    

#### Displaying Layout Bounds

In the UI display settings, select **Show Component Border** to display the layout bounds for all components on the current canvas.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/7jnOXu2MSGeJTOz8JfSfFQ/en-us_image_0000002500909954.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5B7E5D2C52EBEC046913F12D8005D9C97C0A69DC4C0DDD9134CAF353C5A3DD27)

#### Viewing State Variables of UI Components

Click a custom component to view its state variables, as well as the next layer of components that are influenced by these state variables.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/RhFh9WfHQWmmadr9Ezprqg/en-us_image_0000002501069760.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9DEA4FAC21D01C5B1AC8C9A05D1A2D5CC1E300B4FF105400CABDC8494D92BA30)

#### Expanding Applications in 3D

ArkUI Inspector supports 3D expansion of applications at the component granularity, which means the UI can expand along the Z-axis, making it easy to view the nesting and occlusion relationships between components.

This feature is available since DevEco Studio 6.0.0 Beta1. To use it, the device system version must be upgraded to API 20.

## Scenarios

-   Clicking a layer allows accurate selection and viewing of occluded components, which can be used to locate issues such as whether a component is occluded.
-   The 3D view visualizes all components from the component tree that are involved in rendering. This allows you to identify which components require rendering, such as extensive lists or off-screen elements, and optimize your app's rendering performance accordingly.
-   For scenarios with complex pages and many small components, where component selection is difficult in the component tree or 2D view, the increased distance between layers in the 3D view can effectively highlight small components, making them easier to select.

## Accessing the 3D View

Click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/n9L942n-S467z2A_c2ZrKA/en-us_image_0000002500909916.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A0BF687539B7F219E644B6CE64C4460382F0F15034EA673660831E00125BA055) **3D View** to access the 3D view. The first access to the 3D view triggers 3D data loading. Wait for the data loading to complete.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/TafapgbgSHy6j-Q64HfVTA/en-us_image_0000002501069770.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=370BD060379901D09DC76B0E03CD002411F2E65531F2661ACD9F6007AE91BB23)

## Basic Operations

-   Rotating the view: Hold down the left mouse button and move.
-   Panning the view: Hold down the right mouse button and move.
-   Zooming in/out on the view: Scroll the mouse wheel.

## Hiding Front Layers

After selected, the layer will display a blue border. Click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/DQfZ9CupRo2z2O-oLJZC7w/en-us_image_0000002500909906.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B08DFA2303C64E967DF963FEF86B8CBB06E569920D065E33FD4AA1C042F8471B) **Hide Views in Front** to hide all layers in front of the currently selected layer (facing the user), avoiding interference from unnecessary layers.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/sTtXYPGgRLaqxnJI6-e--Q/en-us_image_0000002532749771.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A36352F5B782C5399E6730B0639ACA66183BBEF809E5B70AB438B749C532462C)

## Hiding Rear Layers

The operation is similar to that of hiding front layers. After selecting a layer, click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/-PJi3ZkfQkiiVfml6Pb1_g/en-us_image_0000002532749789.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FFE711CAD0706F33DEAFEEBEC906EA7E4EB2FA1130AF1F774D634221F5771B53) **Hide Views Behind** to hide all layers behind the currently selected layer.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/W5FnA-BMTnmVJX55OcZS-w/en-us_image_0000002501069788.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3719CB4393CA681ECD2195C1C10F7E783CC3E067A2CCF44B023FA350E1A76DC3)

## Restoring Hidden Layers

Click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/CeWMAtIjQCCaS-h9lwK6LQ/en-us_image_0000002532669881.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C709F704826BFD06593C00558FBF263F63005EB0B0A8A908A61CC0A49B7F4D8A) **Restore Hidden Views** to restore all hidden front and rear layers.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/RapJpbC8SDS9vusdp4TDTg/en-us_image_0000002532669843.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4AAF6AF89D04DBE7DDDCA78D741EF138335A8EBF3F16D4DFF27140A4FAFE133B)

## Switching the Layer Arrangement Order

There are two layer arrangement orders: ID order and layer order.

-   ID order: The default order, which follows the rendering sequence and actual display order of components. The occlusion relationships between layers are consistent with those in the actual application, with each layer displayed on a separate Z-axis plane. However, a large number of layers may result in an excessively long Z-axis, making operations inconvenient.
-   Layer order: Components at the same layer in the component tree are displayed on the same Z-axis plane in the 3D view, which can effectively reduce the Z-axis length in the 3D view.

Click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/P7Ne2QLlRcuPHtzJceu2gQ/en-us_image_0000002532749823.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9B03C622FAADC5618C6F07BC0794AB2574930E1410F1C5F7F939443F33842B42) **Switch to Layer Order**/**Switch to Id Order** to implement switching between two orders.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/PieXmcI4TH2Id96NBNp4RA/en-us_image_0000002532669823.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A496A67E79C52DBE3A64D0299220AD7697D3C1E2BD507797457104051C312CD9)

## Adjusting the Layer Spacing

Hover the mouse over ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/qot2tfLnScioo64LO8bhZg/en-us_image_0000002501069758.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=94A0D8112A617BE05C4E77A70691099D99ACE6CC619873189592FD53984E1633) **Adjust the Gap of Layers** to display a slider and drag the slider to adjust the distance between layers, with a range of 0 px to 100 px.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/HREIziQsSf-bfb1rGrmeqQ/en-us_image_0000002500909922.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1F54AE0F6AD7B4A0A896592ED8E20E6FA611F2EAFBB00017628F1A938CC3198B)

## Showing/Hiding Layer Borders

DevEco Studio adds borders to layers by default. These borders are not part of the application and are used to facilitate viewing of transparent layers. Click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/MtJnDuy0SyKfpFRX5DsTMg/en-us_image_0000002501069800.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=319A3138EECC9DA943D5E0109F1312FBA091DFFB8241F68687A13791EB0FF48C) **Hide Border** or ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/RGTjOJ1xRYSJcAFT1vRGHQ/en-us_image_0000002532669821.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=855A2A781F7B50F4263C105D3A55696C55010927787D39A34F4779E7943E4DD8) **Show Border** to hide or show layer borders.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/jK5B_Tp0R-iIekDF_aPlUA/en-us_image_0000002500909936.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9DBB9A2854716341B7F2F51242F47D2CA96B198C0BC5A569276885C5D7664052)

## Zooming In or Out on the View

Click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/dsrEH6obTnS6kUYXEJDsKw/en-us_image_0000002501069772.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=035DA0B186A677B94F9E6F894862AAE8FAEA58FD0655AF08DE0420682711A0E6) **Zoom In** or ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/T0vIgEAcSya0N0z7xO-D4w/en-us_image_0000002532749815.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E6B6D789822F044A3F199242E02F4C19905C6D0BF2F58576B0E5AD23DD78C522) **Zoom Out** to zoom in or out on the 3D view.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/tLepkhy9RgSbHtWV-HDrTQ/en-us_image_0000002500909934.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D159F59353355048ABD47A678B0B4661E832F8B35858C146B3790ECE0F820A78)

## Fitting to Window

Click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/XeDR-x6lQWuFG1FFMDhX4Q/en-us_image_0000002532749797.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B2E01DCFF7239D08476751E19D38FC2A0D073F5A8B88CA30A2B7688D9FD32297) **Zoom to Fit Screen** to automatically adjust the scaling ratio of the 3D layer based on the window size and move the 3D view to the center of the area.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/ncW9MudbQQOmZC5bcbxvLg/en-us_image_0000002500909924.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B988F36AECBF7A2D70DCB8E2713A7CEBE1FB93F7D440AEA962A1ACFE08072BD6)

## Switching Between the Front and Side Views

By default, DevEco Studio displays the side view. After complex rotation, you can click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/3pNJcxGtR22PZDRGTzRR-g/en-us_image_0000002500909930.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2EB805E8B8DFF092A6721A5314AD029F149CA1EB8945FE3AC3A25CE467A28010) **Switch to Front View** or ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/180nTvUCRyaIKX8z6tQWmQ/en-us_image_0000002501069794.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EE54A0AE3872BB1DEEEDA469CA76E5724E3EC6A83E59843801D7F0D558A3B747) **Switch to Side View** to automatically adjust the 3D view to the preset front or side view.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/hnE0pFuAR7OvLMmrapq1_w/en-us_image_0000002532669855.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CF59CD8B1D26B7C7E8DEB8631F9BC3A4F9E1C701A5CA7DE65D28E6E9D9340C33)

## Returning to the 2D View

Click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/Ta5hU0DiSu6HenNLbnxKWA/en-us_image_0000002532749803.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7C70CF57A228A6D14C1EA2F8A49A57D9BD4D23FF2FB61872EF3FD5A7B80F2A72) **2D View** to switch to the 2D view.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/EehFn-IISTGntd-sHWHa8A/en-us_image_0000002532749807.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9EB4F31F8FBC36DDCFD8C77D8A18874E8926FF3F4688DC29AF9FAB7D5077F3DD)
