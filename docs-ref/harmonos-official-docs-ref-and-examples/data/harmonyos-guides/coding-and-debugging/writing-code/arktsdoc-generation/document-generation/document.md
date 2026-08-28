# Document Generation

DevEco Studio makes it easy to create ArkTSDoc documentation using the Generate ArkTSDoc feature. With this feature, you can quickly generate reference documents for variables, methods, APIs, classes, and other information that you want to expose from your code.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/A-v2Zu4PS_qBZuWGSJAGNw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062148Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A5D5C304BCB2905CAC7BCC06AC36AB478B2D7DD83269EE4B95B2EE12C190CFD9)

-   You can generate ArkTSDoc documentation for .ets, .ts, .js, and .md files in your project or directory.
-   Only exported variables, methods, APIs, and classes are included in the generated ArkTSDoc documentation. Unexported items are not included.
-   If you choose to export documentation for the entire project or directory, the generated ArkTSDoc documentation will maintain the same directory structure as the original.

#### Procedure

1.  On the menu bar, choose **Tools** > **Generate ArkTSDoc...** to open the **Generate ArkTSDoc** dialog box.
2.  Set the scope for the documentation generation and the output directory.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/SJ_RBt5mQ_SEPh-vxUDeJA/en-us_image_0000002532750265.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062148Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=396DD512FAF4CF2E71298C57DBD656E0D7D5B39E3185D9B953AA19A7461C5642)
    
3.  To enable the ArkTSDoc documentation to automatically open in the browser after being generated, select **Open generated documentation in browser**. When you are done, click **Generate** to start the scanning and documentation generation.
    
    The left panel of the generated ArkTSDoc mirrors your project's directory structure, while the right panel allows you to navigate to specific variables, methods, APIs, or classes in the documentation.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/xHv2db0AT9yOrCIeuNVTsg/en-us_image_0000002500910396.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062148Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2432518D3C3F474B17B2B3AE0280189E72541D8DE7A628B8FEFA109806AE036F "Click to enlarge")
    
    If the **Open generated documentation in browser** option is not selected, a notification will pop up in the lower right corner of DevEco Studio after the documentation is generated. You can click **Go to Folder** to navigate to the generated ArkTSDoc folder and open the **index.html** file in a browser to view the documentation.
    

#### Example of Generated Documentation

Comment format: Currently, only the **/\*\* \*/** comment format is supported. It also supports [standard tags](../standard-tags/document.md) such as **param** and custom tags such as **myTag** for generating documentation.

/\*\*
 \* Prints "log" logs.
 \*
 \* @param { string } message - Text to print.
 \* @myTag
 \* @since 11
 \*/

Sample code:

/\*\*
 \* Defines the demo class
 \*
 \* @since 11
 \*/
export class Demo {
    /\*\*
     \* Prints "log" logs.
     \*
     \* @param { string } message - Text to print.
     \* @myTag
     \* @since 11
     \*/
    static log(message: string): void {
        
    }
}

Example of generated ArkTSDoc

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/aks6jUUlTo6Jpw8bfmsgvw/en-us_image_0000002500910394.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062148Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=49A96CFAF2639862A0EBF4D434A989CABB84B4DB90B97AAE279D99B6E503ED38 "Click to enlarge")
