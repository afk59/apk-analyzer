# Editor Basics

DevEco Studio allows you to develop apps/atomic services in multiple programming languages, including ArkTS, JS, and C/C++. When writing code, make most of the following editor tips to improve your work productivity.

#### Syntax/Semantic Highlighting

The editor displays code in different colors by keyword, operator, string, class, identifier, comment, and more. To customize the color scheme, choose **File** > **Settings** on the menu bar (on macOS, choose **DevEco Studio** > **Preferences**/**Settings**) and then choose **Editor** > **Color Scheme** from the left pane. The color scheme configured under **Language Defaults** applies to projects of all programming languages. To set the color scheme specific to a programming language, select the language from the left pane, and deselect **Inherit values from** on the right pane.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/z6gldv_sS4Wr5hqn1edXmA/en-us_image_0000002532670533.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CF364D8E1F140C78B7F3F0DDC3FD9355A01A4ABEC1F4D80DD335F4B46D100A98)

#### Code Navigation

You can move about your code with ease. To jump to the definition of a symbol, such as a class, method, parameter, or variable, just click it while pressing and holding **Ctrl** (**Command** on macOS). To find references to a symbol, simply click the symbol. If there is only one reference, you'll be redirected straightaway to it. If there is a list of references, you can choose which one you want to navigate to.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/58UvBc8LSwOECI0BwoRctQ/en-us_image_0000002532750495.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C7924A24D7DA2974DDD09634B3BFB2D77F95EECAA55905C8D309686D265A6823)

#### Cross-Language Navigation

If your code file (such as d.ts) contains a declaration of or a reference to a C/C++ function, you can navigate to that function easily. Just right-click a symbol name and choose **Go To** > **Implementation(s)** from the shortcut menu (or press **Ctrl+Alt+B**; press **Command+Option+B** on macOS).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/QSaeO5x7SdmLGDH0-d3tqg/en-us_image_0000002532670529.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=28B4FFBDAD9BB227ACC79E96319BC1D6919965F88BBAE33358D9940B91254B66)

#### Code Formatting

The editor can format your code to make it easier to read according to the preset code style settings. You can also apply custom code style settings to the specified files as follows: Under **File** > **Settings** > **Editor** > **Code Style** (**DevEco Studio** > **Preferences**/**Settings** > **Editor** > **Code Style** on macOS), select a file type, for example, **ArkTS**, and customize the code style settings.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/wcarvx-vSsiV-ddsARLp6w/en-us_image_0000002532670559.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=79D05337395A1D4D83733E4056E36D62E4AF61323240C725971A353D3ADA01B3)

You can use shortcut keys **Ctrl+Alt+L** (**Option+Command+L** on macOS) to quickly format selected code snippets.

To exclude certain code snippets from the automatic formatting scope, perform the following:

1.  Choose **File** > **Settings** > **Editor** > **Code Style** (**DevEco Studio** > **Preferences**/**Settings** > **Editor** > **Code Style** on macOS), click **Formatter**, and select **Turn formatter on/off with markers in code comments**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/C1PpkeMhR4uk83bxcmq9Dw/en-us_image_0000002532750501.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=351BE299EBEB963374B999DC952579A6476A1BE71FA8F2466DDAADB9385EC5EE)
    
2.  To exclude a code snippet from formatting, add **//@formatter:off** and **//@formatter:on** to the start and end of the code snippet, respectively.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/c6Ddh110Q52iNhlI95-YTA/en-us_image_0000002500910628.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=81923503A9D7B354E483ED9C5ED90AF63293A8DA0C76D7E4431682320DA463C2)
    

If the project already has a **code-linter.json5** file configured, right-click the file and select **Apply CodeLinter Style Rules**. The code formatting rules will then be consistent with the rules defined in the configured **code-linter.json5** file. For details about how to configure the **code-linter.json5** file, see [Configuring Code Check Rules](../code-check/running-code-linter/document.md#section19310459444).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/SkquV6NIRG2Aw65iFx7CIQ/en-us_image_0000002500910610.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E4015DECD4781CFD5693C62684D81E2CF08DCBFBBA0297B7256E873470F78BE0)

#### Code Folding

You can collapse or fold blocks of code while you are not working on them. To quickly collapse or expand a block of code, just click the collapse or expand button on the left sidebar of the editor. Better yet, you can right-click a block of code and choose how you want to collapse it, including **Collapse**, **Collapse Recursively**, and **Collapse All**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/I0_d244LQLaArM8LdxBKRw/en-us_image_0000002501070444.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=124E90B871964EF4446F3E6210C4D8A1BF098E7D20999124563A82436FD8C789)

#### Code Comments

You can press **Ctrl+/** (**Command+/** on macOS) to quickly comment out a selected block of code. Press **Ctrl+/** (**Command+/** on macOS) again to uncomment.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/FYpB-ibLTe-O2zvCWfIsoA/en-us_image_0000002501070492.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2B47B44EE41FF889CA1C275B1FBBCB9317664DE59C56538F9B2B04DB9549EF87)

#### Code Structure Tree

Press **Alt+7** or **Ctrl+F12** (**Command+7** on macOS) to open the code structure tree, where you can easily locate code elements, such as global variables, functions, class member variables, and methods, and quickly navigate to the corresponding code in the editor.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/3SIgPTPXTZCQEO1lDydTAA/en-us_image_0000002500910624.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D5AAB72A27B42B6C0F5FF2178E54C281AA1C2FD1084B98DBB1B4632E8851730A)

#### Code Usage Search

With the Find Usages feature, you can search for the references of a code element, such as a variable, function, or class, throughout the codebase. This is useful for subsequent code refactoring and can greatly improve development efficiency.

Usage: Right-click the code element for which you want to find usage, and choose **Find Usages** from the shortcut menu or press **Alt+F7** (**Option+F7** for macOS). Click the ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/xzThm5SPRmy0cEgggCnUtA/en-us_image_0000002532750509.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A880BE0B7C718D6C27D1930951A276F2B3DB6D6F618D3431DDC09BA43DD169AA) icon to view where the variable is assigned, and click the ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/_k4GwsUgTuex-1SWlY3WaQ/en-us_image_0000002501070438.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A891A264AAAD721AF500F9A389494464BFE6F59FA9669FCEC94AC575778F44BD) icon to see where the variable is referenced.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/VfMRZD5SRc-auv9RbpdzlQ/en-us_image_0000002532670511.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=65A7CD97659058D18477D8479C45B97216361F1922862232F726C8FB196D89EB)

#### Code Comment Generation

An easy-to-use code comment generator is in place to help you quickly create comments for your code. In front of the code block of a function definition, enter **/\*\*** and press **Enter** to insert a commented line.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/WAHXVM6BRL63Z70p0GyG0A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=55905CDB83FD15CC728FF3E422D302C3025A718660C341CDC3198DDF6F6EE9B0)

In C++ files you can also enter **//!** and press **Enter** to quickly generate comments.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/EriF3UxaQXyN7BI71IC33w/en-us_image_0000002532750485.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ED827F2CF92625FCCD903EACDBC78DC334C6AE62B741F1FFCFA940D4096157BE)

#### Code Search

You can navigate through code by navigating between symbols, classes, or files. You can examine the call and type hierarchies and explore the structure of source files. Just press **Shift** twice to open the code search page, and enter the keywords in the search box. The search results are displayed in the lower part of the page in real time. Click a search result to go to where it is located.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/wu3lMoBrRuSfnZm5hcLsSQ/en-us_image_0000002501070436.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CD24FCB04295B380F56C04FBA0D4277CF5394BD48E5683AA529EFF00E90ECBA3)

#### Quickly Accessing API and Component Reference Documents

The editor provides instant access to reference documents for ArkTS/JS APIs or components, without the hassle of navigating to a specified web page.

Hovering over an API or component displays a popup with a quick view of its definition across different API versions. To obtain the full API reference document, click **Show in API Reference** in the lower right corner of the popup, or right-click an API or component and choose **Show in API Reference** from the shortcut menu.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/OzHZFez-Q3e58h5VK6-DSg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4BE9EC9A7EB1F3AF6DA0E59239457FCD38ACA9224A2947EDD2B5129269ED1820)

The API reference documents integrated in DevEco Studio may not be up to date. To obtain the latest version, see [HarmonyOS API References](https://developer.huawei.com/consumer/en/doc/harmonyos-references/development-intro-api).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/4qTSb7QdQGq_qaNwIu-m6w/en-us_image_0000002501070466.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BB8B3105EEDDC1FAD238AF10157722DE7675388C4D79AAD39A7BA6A47A693224)

In the popup, the following information is available:

1.  Whether the API requires any permission declaration and whether it is available only in the test framework.
2.  Status of the API: The **deprecated** tag indicates that the API is no longer recommended and may be removed in a future release. For such an API, use the API marked **useinstead**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/cW_lI4BbRwe7dI9LwOUc8Q/en-us_image_0000002532670565.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DB8CBD7569D02DDAF2E4627C205318DC1A08C998AB0890A57AC366B6E71542A4)

#### Optimize Imports

The editor's Optimize Imports feature helps you remove unused imports and merge or sort imports based on preset rules. Select a file or directory and press **Ctrl+Alt+O** (**Control+Option+O** on macOS), or choose **Code** > **Optimize Imports** from the menu bar.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/jal2RPMRTbKe2-QjEiJdRw/en-us_image_0000002501070440.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2277D44766EB0601E8331F8ACBFA59A64A9857EF7674E298A9762C216B37392B)

To modify the optimization settings, choose **File** > **Settings** (**DevEco Studio** > **Preferences**/**Settings** on macOS) > **Editor** > **Code Style** and select a programming language (ArkTS is used as an example here). On the **Imports** tab page, set the fields based on your needs.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/-8rFRAJMQY-iH3eqMlypkg/en-us_image_0000002500910620.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4FD728B7D7A0747913E53AFBEB93135408085201071F088CC1CA16E388DB7CB5)

#### API Change Query

Starting from version 5.1.0 Release, DevEco Studio provides the capability to query and compare behavioral changes in the ArkTS APIs used by the current project since a specified SDK version, along with adaptation guide links to facilitate code modification.

Since DevEco Studio 5.1.1 Release, this feature also supports C APIs, enabling cross-version change queries.

Since DevEco Studio 6.0.2 Beta1, a scan progress indicator has been added. The specific locations of changed APIs in your code can be viewed in **Code Location**.

## Constraints

-   Deprecated APIs are not included in the API change scanning scope.
-   During ArkTS API function calls, the change query feature is not supported when you use APIs involving generic type parameters with the **extends** or **keyof** keywords. Example:
    
    // API definition
    interface ProgressInterface {
      <Type extends keyof ProgressStyleMap>(options: ProgressOptions<Type>): ProgressAttribute<Type>;   // Change query is not supported for APIs with extends or keyof keywords.
    }
    // API calling
    Progress({ value: 10, type: ProgressType.Capsule })
    .style({content:'Install'})
    

-   Querying for changes to API functions implemented in C++ is not supported. Example:
    
    template <class \_Rep, class \_Period>
    cv\_status condition\_variable::wait\_for(unique\_lock<mutex>& \_\_lk,const chrono::duration<\_Rep, \_Period>& \_\_d)  // Querying for changes to API functions implemented in C++ is not supported.
    
-   During C API scanning, the presence of functions that share a name with a modified API may cause the tool to report false positives in its change analysis results.
-   The change query feature does not support for APIs called in special ways. Example:
    
    // Example: via function pointers
    int (\*sigptr)(int, const struct sigaction \*\_\_restrict, struct sigaction \*\_\_restrict) = &sigaction;
    sigptr(NULL,NULL);
    // Example: via callbacks
    callback(sigaction);
    // Example: via custom macros
    #define MySig sigaction
    MySig(NULL,NULL);
    

## Procedure

**Perform the following steps if DevEco Studio 6.0.0 Release or later is used:**

1.  On the menu bar, choose **Tools** > **API Change Assistant**. On the **API Change Assistant** tab, select the SDK version range for comparison and click **Start Scan**, with a progress bar indicating the scan status. Upon completion, you can view the API changes by module.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/Q0fPMe4VQEG1L5AfvN2gPw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CDAB39C257A64C534A97813823CBA68449491CF93CF74452D7A1A3A4D19E7F57)
    
    The API change query feature uses the selected starting version as a baseline to check for behavioral changes in the APIs used in the current project. For example, when you select SDK versions from 5.0.0(12) Release to 6.0.0(20) Release, the query covers changes introduced between 5.0.1(13) Beta3 and 6.0.0(20) Release, compared with the baseline of 5.0.0(12) Release.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/nXeUHzxtQv2eVmudVzNlzw/en-us_image_0000002532670515.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=79979E56752568448268CF1E0E5D8641843FDC51A9E1D04D592A099067202B7A)
    
2.  Click the code location in the scan results to jump directly to the corresponding code. For details, click the change description highlighted in blue to access the version description document. After modification, click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/09UNdcOgTOye0MO9xCfCyw/en-us_image_0000002532670517.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=19E193B4791A4FEA65E8D3BC9F5FE561EF96AFBC5D2F06FCDD930900AAAAB988) to mark the item as fixed. Use the following options to search or filter the API change scan results, and export the data:
    
    -   **Search**: Enter an API name or a file path in the search box to find specific results.
    -   **API Version**: Set this field to filter the scan results by the selected API version.
    -   **Language**: Set this field to filter the scan results by programming language (ArkTS or C).
    -   **API ID**: Set this field to filter the scan results by API ID.
    -   **Fix Status**: Set this field to filter the scan results by their fix status (**All**, **Fixed**, or **Unfixed**).
    -   **Scan Again**: Restart the scanning process.
    -   **Export**: Export the API change scan results to the local PC.
    -   **Settings**: Configure the maximum heap memory size (in MB) allocated for API scanning. The default value is **3072**. Adjust this value to speed up scanning for large, code-heavy projects.
    -   **Code Location**: This panel shows the exact locations of changed APIs in your code files. Click any entry to navigate directly to that line of code.
    

**Perform the following steps if a version earlier than DevEco Studio 6.0.0 Release is used:**

1.  On the menu bar, choose **Tools** > **API Change Assistant**. On the **API Change Assistant** tab, select the SDK version range for comparison and click **Start Scan** to view the API changes by module.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/D0HTu-FvQa-Mvmnkw2PDbQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1AD0BA12F040193D14E3DA50C5F656505E62D85FA2B660A65C051859125DCD81)
    
    The API change query feature uses the selected starting version as a baseline to check for behavioral changes in the APIs used in the current project. For example, when you select SDK versions from 5.0.0(12) Release to 6.0.0(20) Release, the query covers changes introduced between 5.0.1(13) Beta3 and 6.0.0(20) Release, compared with the baseline of 5.0.0(12) Release.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/53lvk9mUQWm8bjrKf_-KLw/en-us_image_0000002532750525.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3A0D05F93D480C85548371630260E9E53ABA834D9676641BCA9F107D346BF4C0)
    
2.  Click the code address in the **Code Location** column to go to the corresponding code writing location. For more guidance, click the link in the **Guidance link** column to go to the version description document for details.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/LKw2pDuvR0qlWHseus7r2Q/en-us_image_0000002500910622.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C3E68D4C5331C72008048FC0CACAAC84B7B3C69650E00A5ED3300AAF711A632F)
    
3.  Click **Export**, select the location for storing API change data, and export the data. You can click **Scan Again** for rescan. You can set the maximum heap memory size allocated for API scanning via the **Settings** button. If the scanning is slow for large projects, increase this value from its default of 3072 MB.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/9pyb34dhTTic8Ge5JdYLTg/en-us_image_0000002532670519.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7504702D2CABEBFE578817D1FFB32EA53F3128E7BECE37B68F6CC5EDAC50A318)
    

#### Navigation Between Parent and Child Classes

In the editor you can quickly navigate to the parent or child class of the selected interface, class, method, and property. You can navigate to its parent or child interface or class by clicking the corresponding gutter icons on the left of the code editing area. If there are multiple inheritance relationships, simply select the desired interface or class from the list presented in the popup window.

-   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/CW4HWZPXQU6nlUJxrA1Bng/en-us_image_0000002532750497.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=275A269365682BB733077249975E7E024DBC3D6DF3A347A5E5B591AA1B528891) Implemented: navigates to the corresponding implementation classes or sub-interfaces and their respective properties and methods.
-   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/7-L9h-PdT5SEaQ3mgvTZgQ/en-us_image_0000002532750463.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=35D3BB30A02FA9B8D1F361CC0D5A91D93EF01C1FB76C05E54ED467D9782265B2) Implementing: navigates to the corresponding parent interface or its properties and methods.
-   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/F_XK2iaVQdmlKvjzV65kvw/en-us_image_0000002501070490.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9BC33D2B853488217284CC25ACBA728A37CA08E10CDF45E3B197DCF7DF4010FD) Overridden: navigates to the corresponding child class or the properties/methods of the child class.
-   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/iNjQwbNoQa2NXv5xmmrLzw/en-us_image_0000002501070446.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CFF7A20D38CC8DA6F477B791B4718B21C519EF6E4BDF5FCCF019C27164FDB69C) Overriding: navigates to the corresponding parent class or the properties/methods of the parent class.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/3OB3M45FTx-1eYb0nZGGSw/en-us_image_0000002500910616.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=67B2EA31871D73B1B40EA44322C4DB98CB8AF65B167E8D99A595C900244DB27F "Click to enlarge")

The preceding features under **Gutter Icons** are enabled by default. To enable or disable these features, choose **File** > **Settings** (**DevEco Studio** > **Preferences**/**Settings** on macOS) > **Editor** > **General** > **Gutter Icons** from the menu bar, and select or deselect the check boxes as needed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/mKHlzg5fRqWY5yqApTJ_iQ/en-us_image_0000002532750479.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=508610627484E9D935EBC7DC3FA56D93499E2814833982065F3D3028269023E2)

#### Inheritance Hierarchy View

In the editor you can examine the hierarchy of interfaces and classes. Select the desired class or interface name or hover the cursor over it, then press **Ctrl+H** (**Control+H** on macOS) or choose **Type Hierarchy** on the **Navigate** tab page. In the displayed **Hierarchy** window, view the inheritance hierarchy of the class or interface.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/yX6A9aEiTyu05qTJuVoYgw/en-us_image_0000002532670557.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B85687C50D78CC8B479FF63ACDA01698D23EA13922D298C922F782D9BA6A0C17)

The table below describes the icons in the **Hierarchy** window.

| 
Icon

 | 

Description

 |
| :-- | :-- |
| 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/dq5FmJb7SCmjNljVraWcrw/en-us_image_0000002500910654.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2A50692561756F83579ED0C0249E4A7B8075179074B75E78DC9CFAC690DD1F8B "Click to enlarge")

 | 

Displays the parent and child classes of the selected class.

This feature does not support the query of inheritance relationships.

 |
| 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/-B8N_-zMQMWkoX4I4d9WIw/en-us_image_0000002532670561.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9F9A53CCF902EB3AAD2899E0F2EF89C8CEDAAFB73BE1D27E06A8CAFE910AA2D4 "Click to enlarge")

 | 

Displays the parent class of the selected class or interface.

 |
| 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/MBwkjLURSxmYKtFw6mYVnQ/en-us_image_0000002500910636.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0CA4DF72AC4A71D4879DB5AABC840B6F54244E84637DFC03B9E249A02A9CC669 "Click to enlarge")

 | 

Displays the child class of the selected class or interface.

 |
| 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/7M0YD70pQFueYHyyMcZ9nA/en-us_image_0000002500910606.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1DAFB606BF5C89BE9A6AA0ED2B4C0C344F78A1D481478705B7C912D48E7D4DED "Click to enlarge")

 | 

Sorts all sibling elements in the inheritance structure tree alphabetically.

 |
| 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/uDyH4CaORcyG2dzI42i2lg/en-us_image_0000002532750499.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E9E11D8601D860EE1F21861660F9A97D6D525AB8C8C8657C99336DC013AB4D51 "Click to enlarge")

 | 

Updates the inheritance structure for all classes or interfaces.

 |
| 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/ZY_ysRk5RM655d-XMB6Whg/en-us_image_0000002500910608.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B77D59F03DA0003FE5024F1378605AF1B67EA84DF8662B3859D449D65F399665 "Click to enlarge")

 | 

Enables you to navigate to the code location of a class or interface in the editor with a single click of the class or interface name in the structure tree. By default, a double-click is needed for the navigation.

 |
| 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/lNVx8BjbTk2bqI7cgxVLEA/en-us_image_0000002501070488.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F86D84413B612831D8F227052E58C57920D4B0783753BE64BBE94B3068F256C0 "Click to enlarge")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/P5-rklNfTE24CchNU8eNnA/en-us_image_0000002501070484.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=19D426889EB44E6A66439D98388607161BE06A044A83E059D71BC522C4FD661E "Click to enlarge")

 | 

Expands or collapses the inheritance structure.

 |
| 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/xbSoSg9SQniJq4hm6DEFHA/en-us_image_0000002501070486.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=59BB0A057B8257742C3E2B173053FFF5A8F81266EDC5C8FE24C7B9DED38A8CF4 "Click to enlarge")

 | 

Locks the current **Hierarchy** window to stay on top of the editor window.

 |
| 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/Ugnw4iveTPWaZ2WghAvKsA/en-us_image_0000002501070458.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=95C2AAE2C8A7B30E1B6FB9932A181752D8CC619232C7AC3F9839DEA24D594F84 "Click to enlarge")

 | 

Exports the inheritance structure of the selected class or interface to a text file.

 |
| 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/E6_Nz5yRRFiaFGUgFY8XbA/en-us_image_0000002501070448.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A73DB11F02B6E93D37DD501C2E0F0FC013F46D4B4BD6EB1AE79614DA20C124FB "Click to enlarge")

 | 

Closes the window.

 |

#### Enabling Inlay Hints

Since DevEco Studio 6.0.0 Beta2, enabling inlay hints during editing provides code description information such as parameter names and types, improving code readability.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/QqpYmVrIRh2Xx126gyfJww/en-us_image_0000002532750505.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6A44B73BB847673AD747B99C46CD156F32E411BB24546256E88DAD4881E14E58)

Go to **File** > **Settings** (**DevEco Studio** > **Preferences**/**Settings** on macOS) > **Editor** > **Inlay Hints**, configure and check the variable name, property, parameter, and return value types you want to display, and click **OK** for the settings to take effect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/S7GNh8voTJ2Ekjr0nYNV5g/en-us_image_0000002500910626.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D76E16486F2D2937C05CD92E2582B2BCFCE4C6468DDC55CFE6D2C27D1049F92D)

#### Copy Reference

Copy reference is supported since DevEco Studio 6.0.0 Beta2. On the editing page, select code lines or names of classes, methods, parameters, and variables, right-click and select **Copy / Paste Special** > **Copy Reference**. This will automatically copy the address of the definition. Once copied, the address can be searched in the search box that pops up by a double-press on Shift, helping you quickly locate the definition of the API.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/YtGcu16vQZapY8pUctWODQ/en-us_image_0000002500910634.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A868836A5A99A735F3B7356A4436E067C4221FC15F677DBC960F830AB14E7398)
