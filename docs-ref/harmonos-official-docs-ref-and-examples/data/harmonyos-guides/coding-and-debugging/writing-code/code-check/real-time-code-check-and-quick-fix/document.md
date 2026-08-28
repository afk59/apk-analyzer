# Real-time Code Check and Quick Fix

#### Real-time Code Check

The editor analyzes your code in real time and highlights any problematic code it detects based on the severity level. If you hover over the highlighted code, the detailed error information will appear.

Since DevEco Studio 4.0 Release, the editor also analyzes your ArkTS code on the fly for performance issues when **compileSdkVersion** is greater than or equal to 10.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/bA2uBOlUTuiUQQtCPETPFA/en-us_image_0000002500910168.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=998EC244B65B23ABAAB3C0E271719569A29D04D0E7F0A0B34F1B848D80912F6B)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/tq3YPq1PTc2EDPW-1zloTQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A4D194DE3FED90399710FDBE3383067DC3EF44135C3966B0A529CCBD5093D764)

If the value of **compileSdkVersion** is greater than or equal to 10 and the value of **arkTSVersion** is greater than or equal to 1.1 (default), ArkTS strict type checking can be conducted in real time.

#### Quick Fix

The Quick Fix feature in DevEco Studio helps you quickly fix detected issues with ArkTS and C++ code.

**View issues**: Press the **Shift** key twice to open the search window. In the search field, enter **problems** to access the issue list. Double-clicking an issue displays the source code location and cause of the issue.

**Quick fix**: When an issue is highlighted, move the cursor over it, and a popup will appear to provide the issue description and suggested quick-fix solutions; click **More actions** to view more quick-fix suggestions. Alternatively, when a light bulb icon appears on the page, you can click the icon and implement quick fixes based on the suggestions provided.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/YDhcdgIJQtOKaKGjjoPM8Q/en-us_image_0000002501070004.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BDCFFA9C0436C69444EF2713F4B26C65F543CD52A988129D17D931F354BF6072)

#### Examples

The following describes how to use Quick Fix for C++ code.

## Autocompleting Switch Statements

Quick Fix can automatically create missing cases for C++ switch statements.

Place the caret at the condition of the problematic switch statement, click the light bulb, and select **Create missing switch cases** from the drop-down list box.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/g9hsMnDeQMagOU3MaZSYdg/en-us_image_0000002500910164.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4B1D4981F343D40C9AEA6CC866E9ED54737CA3A5AECA948FC56F3CA783AFE5E7)

## Replacing a Type with auto

You can use Quick Fix to quickly replace the types declared for iterators, new expressions, and cast expressions with **auto**. Place the caret at the type name, click the light bulb, and select **Replace the type with 'auto'** from the drop-down list.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/8SU_3DV8QyeXRosZUavrqQ/en-us_image_0000002532670079.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AB7A28716F9710C349F3A454505887A3E958DEE449C4B0960571DDF8C0AA6440)

## Replacing if-else with the "?:" Ternary Operator

With Quick Fix, you can quickly replace an if-else statement with the "?:" ternary operator. Place the cursor at the if statement, click the light bulb, and select **Replace 'if else' with '?:'** from the drop-down list.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/x5_vQyQ_Sk2twbtNxNltww/en-us_image_0000002532750037.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6AB29F7F0DA97379B868C040792D277FFE786A1E5F830096B9F4B2EC29C57A63)

## Creating a Constructor

If an undefined constructor is detected in your code, you can use Quick Fix to create a new constructor. Place the caret at the constructor name, click the light bulb, and select **Create new constructor 'xxx'** from the drop-down list.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/lMzRmWcgTe64-kTVtn46Fw/en-us_image_0000002532750035.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4BE396AE79B919E3F4FDBDF468CD80CA355CF9F8F969A833B4603DD986098A14)

## Splitting a Variable into Declaration and Assignment

Place the caret at the variable that you want to split into declaration and assignment, click the light bulb, and select **Split into declaration and assignment** from the drop-down list.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/Ei-eh8L3R4Wbi-9935g9ow/en-us_image_0000002500910166.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7F44098A46CE4B28600B71A8B09F6985332123159C3EB6EFAE22B397A2AD04D2)
