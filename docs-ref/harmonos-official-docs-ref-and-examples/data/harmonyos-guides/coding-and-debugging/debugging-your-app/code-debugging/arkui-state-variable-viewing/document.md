# ArkUI State Variable Viewing

DevEco Studio 6.0.2 Beta1 and later versions allow you to view real-time changes of ArkUI state variables during debugging.

In the debugging window, click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/wXYP1haBQKyT65lI8lezxw/en-us_image_0000002501069814.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=98D3FACAA4DA2F707C37512D21E9AD734D8BEC8D882A959D33323A735472C5C9) **Layout Settings** and check **ArkUI State** to open the ArkUI state variable panel.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/rICdOeCTRKK-g-kLKqT-lw/en-us_image_0000002501069818.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F40B9DDE84CC2BC202772BC296158878FE2AE3458D7634E02CA3CF8952A0F79C)

The state variable panel is divided into two sub-panels: **Summary** and **Current Value**.

-   The **Summary** panel provides an overview of state variable updates during app runtime, including the variable name, update count, decorator type, owning component, and owning class.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/IlQP2gr7Qa6xNZRsc3TYUQ/en-us_image_0000002500909974.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2FFA8575CE44D813BE99FE2DACF021DE860743D34F51BE746A96A5EACA6DFA2A)
    
-   The **Current Value** panel records real-time changes of state variables, displaying the update timestamp, variable name, owning component, owning class, decorator type, current value, and the number of affected components.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/8O8T1fcYSL2ZdKlVssTA1A/en-us_image_0000002500909968.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0C858A93E57F79CB2A9BE84C89D3A01C4358BCDA254476AC27ED3AADDE4AB24A) When you click the arrow on the right, a new panel will appear showing the list of components affected by the selected state variable, including the component name, component ID, and component type (custom component or not).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/qxsJcLrUT4efeReGuEsRcQ/en-us_image_0000002532749833.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=00CBCBD5C8510C53F537BF988A7511B21213227B856134FB926775D1D7140789)
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/wy8faXRCSTSqT3DoB-obuw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DD14615E48B3112A0045EB800647A82E8C0B42D10B7BE52EE1CB9C3DA4A2011D)

-   Note that listening for state variable updates only begins after the state variable panel is opened. Therefore, updates that occurred before opening the panel cannot be viewed.
-   During the same debugging session, closing the state variable panel does not clear previously collected data. The **Current Value** panel displays up to 1,000 entries; if this limit is exceeded, only the latest 1,000 entries are shown.
