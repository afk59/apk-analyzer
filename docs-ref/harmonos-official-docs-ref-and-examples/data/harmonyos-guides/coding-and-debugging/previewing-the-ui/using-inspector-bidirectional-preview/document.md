# Using Inspector Bidirectional Preview

DevEco Studio provides bidirectional preview between the UI preview pages and source code files in .ets format. To enable bidirectional preview, click the ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/ol7hMKToR1utIeQPv3hLWA/en-us_image_0000002532670035.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=16BBC04AD11B3AAE77AC7D88F39DA5B41BC65621F1FBAE10A97C234B5CF0E447) icon on the menu bar.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/BJWj4odyQtKeAgNNQvB9fg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=73DA1456A9E2F9310DD8E2D01DB81A6540DA860B90ED0F5968DB405743D25EF6)

Bidirectional preview is not supported for service widgets.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/Po51IXh5TQGJPZo9SaCwag/en-us_image_0000002532749987.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5D3F166C083F915F8FCA8849BE2ECC8A18E9DE49CE4D40E129A31138BD2C8650 "Click to enlarge")

Enabling bidirectional preview allows coordination between the code editor, UI, and component tree:

-   If a component on the UI is selected, it is also selected in the component tree and highlighted in the code block in the editor.
-   If a code block in the layout file is selected, it is also highlighted on the UI and the corresponding control node in the component tree is also selected.

-   If a component in the component tree is selected, it is also highlighted in the corresponding code block and on the UI.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/FRdHrjxBSrGR_mLzrtWS8A/en-us_image_0000002532749985.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C2B1232667327AC6627CD87950B6B2814582FCB9E8C0ECD6F9EC5D5913D17A05 "Click to enlarge")

With the Previewer, you can modify certain attributes or styles on the attribute panel. Saving your modifications will automatically update your source code in the code editor and refresh the UI in real time. Similarly, saving your modifications in source code editor will update the UI, component tree, as well as control attributes in real time.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/EJYnxLFpTDu0XhKregmcRA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DA37515DF082A915DF1E7FCDF0BFBC104141D5BD65EEABE29FD0D0E271FA3D86)

-   If there is data binding in a component, its attributes cannot be modified from the attribute panel.
-   If a component involves animations, its attributes cannot be modified from the attribute panel.
-   Bidirectional preview is not supported during multi-device preview.
