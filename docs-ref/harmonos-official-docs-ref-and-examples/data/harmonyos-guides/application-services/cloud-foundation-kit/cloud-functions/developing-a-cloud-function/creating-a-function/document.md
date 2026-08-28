# Creating a Function

#### Creating a Function

You need to first create a function in AppGallery Connect and add code to execute the function.

1.  Sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html) and click **Development and services**.
2.  Click the project for which you want to create a cloud function.
3.  Go to **Serverless** > **Cloud Functions**.
4.  Click **New** on the **Functions** tab page.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/L-HMOeOwSyiQGJ4_NVTqCQ/en-us_image_0000002440774588.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062101Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=707D92FBFE22A560C89D99394A674211E7B635151B321D880A311CA5480468ED "Click to enlarge")
    
5.  On the **Create Function** page displayed on the right, set relevant parameters in the **Function configuration** > **Trigger** > **Function Code** > **Layer configuration** sequence as prompted.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/plk793fPTieiZQRF0kuRpw/en-us_image_0000002474214409.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062101Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=93E0496DA83D70ACB6ED7708EBE0ADB41EED5A541503784A2FBF461E263B47A7)
    

#### Configuring a Function

1.  On the **Function configuration** page, set **Function name**, **Trigger mode**, **Timeout interval**, and other function parameters.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/SaSdBlrSQB-RUJOhZds9fw/en-us_image_0000002440774604.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062101Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=45BF366810DD3C2C12D91584E4199F0BF6FD9849E69C162501E0FE42CA6048A1)
    
    | 
    Parameter
    
     | 
    
    Description
    
     |
    | :-- | :-- |
    | 
    
    Function name
    
     | 
    
    Name of a function.
    
     |
    | 
    
    Description
    
     | 
    
    Description of a function.
    
     |
    | 
    
    Trigger mode
    
     | 
    
    Mode for triggering a function. Set this parameter to **Event**.
    
    This value indicates that the function will be called by a trigger.
    
     |
    | 
    
    Timeout interval (s)
    
     | 
    
    Maximum timeout interval for running a function, in seconds. If a function times out, it is considered to have failed by default. The value ranges from 1 to 1800. The value varies according to the call mode.
    
    -   In synchronous call mode, the maximum value is **55** seconds.
    
    -   In asynchronous call mode, the maximum value is **1800** seconds.
    
     |
    | 
    
    Instance concurrency
    
     | 
    
    Maximum number of concurrent function requests. The value ranges from 1 to 10000.
    
     |
    | 
    
    Environment variables
    
     | 
    
    Environment variables in key-value pairs. You can configure environment variables for a function, allowing it to read and use them during execution.
    
     |
    
2.  (Optional) Add environment variables in **Form** or **JSON** format as required. After adding environment variables, you can click **Export in JSON** to export an environment variable file in _Function name.json_ format for future use.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/4POhnlWdQG68kB82-BTecA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062101Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=42F78ED02B0DEBC8078A9F692406B871E025F173A81E9836D9373073EDEEE1A9)
    
    -   The key in an environment variable must be unique, and **PROJECT\_CREDENTIAL** and **AGC\_** are system-level environment variables. Do not add environment variables named after or prefixed with system-level environment variables.
    -   A maximum of 1000 environment variables are allowed.
    
    -   Form
        
        Click **Add** and enter the corresponding key and value. As shown in the figure below, **env1** and **test** indicate the key and value of the environment variable, respectively. You can click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/iGSsVo-XQiWhb-rqAzVmEg/en-us_image_0000002474214433.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062101Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=42C05CC365FC65F0BF495A375D4CBD237618922BEDB544519FB05866C913EAF3) next to a variable to delete it.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/Hn3w4UdqQEqW5HJfwPBhBA/en-us_image_0000002440774616.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062101Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FCC407E3D569EB6DBA3EC2DF0B7F146496642DA872FD9F40094693832BB1DC7F)
        
    -   JSON
        
        Click **JSON** and enter environment variables in JSON-format key-value pairs in the text box. If many environment variables are added, you can click **format** to format and sort the environment variables for easy check.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/ZYibjVxaSfOw-AYlXAjlgQ/en-us_image_0000002474214421.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062101Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0BD7D6B073A982817E5CB57D15DD2AF99B19B52DB0D85D781018A250FF319562)
        
3.  Click **Next**.

#### Configuring a Trigger

On the **Trigger** page, configure a trigger based on the function triggering scenario. In this scenario, an HTTP trigger is added. Retain the default values for **Trigger type** and **Method**, set **Authentication Type** and **Url Decode**, and click **Next**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/Qb0miD7KSpKg0QSlQmDacw/en-us_image_0000002474174569.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062101Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D96A8F2F94C0A5A06BD9EE93B5A6756D59A6FA149F9B77688B08A0BA6073E0C3)

| 
Parameter

 | 

Description

 |
| :-- | :-- |
| 

Trigger type

 | 

Type of the trigger. Set this parameter to **HTTP trigger**.

 |
| 

Method

 | 

Request method. Set this parameter to **POST**, which is currently the only supported method for HTTP triggers.

 |
| 

Authentication Type

 | 

Authentication type of the HTTP trigger to be added.

-   **API client authentication (applicable to clients)**: device-side gateway authentication, applicable only to function calls from the app client (that is, from a local app or project).
-   **API client authentication (applicable to Server)**: cloud-side gateway authentication, applicable only to function calls from the app server (that is, from Cloud Functions).

 |
| 

Url Decode

 | 

Indicates whether to use the URLDecoder to decode the body of an HTTP-based function trigger request whose **contentType** is **application/x-www-form-urlencoded** before passing the decoded result to the function.

 |

#### Configuring Function Code

On the **Function Code** page, set **Runtime**, **Memory**, **Code input type**, and other parameters, and click **Next**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/DAXNA5_sRfyYqyFZ4x-I7g/en-us_image_0000002474174597.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062101Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5F6A494D3C070CA6F4DD58F53813B4081C105F817470D3237516EB07D5E12F13)

| 
Parameter

 | 

Description

 |
| :-- | :-- |
| 

Runtime

 | 

Environment for running the function container. Select **nodejs 20.x** or **latest**, where **latest** indicates the latest version.

 |
| 

Memory (MB)

 | 

Size of the memory occupied by the function container, in MB. The options are **500**, **1000**, **2000**, and **4000**.

 |
| 

Code input type

 | 

The value can be **Edit code inline** (default) or **\*.zip file**.

If you select **\*.zip file** for **Code input type** when creating a function, edit an entry point method file by referring to [Entry Point Method](../developing-a-function/node-js/document.md#en-us_topic_0000001658990474_section69815160394).

 |
| 

Function entry

 | 

The value is in _Entry point file name_._Entry point method name_ format, for example, **handler.myHandler**. In this example, **handler** is the name of the entry point file and **myHandler** is the name of the entry point method.

In the Node.js runtime, the entry point file must be stored in the root directory of the function deployment package. For details, please refer to [Preparing Your Function Deployment Package](../developing-a-function/node-js/document.md#en-us_topic_0000001658990474_section527564201715).

 |
| 

Code file

 | 

Code file that can be edited online or function deployment package to be uploaded.

-   If **Code input type** is set to **Edit code inline**, the **Create Function** page provides a web-based IDE, allowing you to edit function code online. The following will describe how to use a web-based IDE.
-   If **Code input type** is set to **\*.zip file**, click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/kB4i_7BYQHWITaC6SbnZaA/en-us_image_0000002474174621.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062101Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D0ED07DA4160A4EA9345D4B4E4F7F0F36B8726C33E0E4923A707105CCA884141) to upload a function deployment package or directly drag the ZIP file to the dotted box.

 |

**Web-based IDE**

If **Code input type** is set to **Edit code inline**, the **Create Function** page provides a web-based IDE, allowing you to edit function code online.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/1jBIJmwSRYGcg4qgHZQlcA/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062101Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F5F5C66BDBF803B5E2ED3A45AD81378073669521C96A9285DCE1A2A54423EF1E)

If you update function code or configurations when a function instance is running, AppGallery Connect will carry out a rolling update of the function instance. Wait for about 10 to 20 seconds.

The web-based IDE contains the directory tree, code editor, and maximize icon. After the editing is complete, AppGallery Connect will generate a deployment package and upload it.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/s67_dnTlTGSQqXz9kg4C2A/en-us_image_0000002474174585.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062101Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=03B71FFD8D4F245A7F28B8F7B0A6CA2B6EB82D6BD8D4AEE67FD31DBD0E1B0742)

| 
Component

 | 

Description

 |
| :-- | :-- |
| 

Directory tree

 | 

Supports the following functions:

-   Adding a folder: Select a file or folder and click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/kFgpV9TbRcW2DxsV582MBg/en-us_image_0000002440774576.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062101Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A27B53D6BC26AE8647F222A51CE59452832DD29454A4085869313B3DDF39C4CC) in the upper right corner. If a folder is selected, a subfolder will be added. If a file is selected, a same-level folder will be added.
-   Adding a file: Select a file or folder and click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/5UEP1OvpQziL0nx980g45g/en-us_image_0000002440934476.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062101Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2B3A4E64CF041F1F44207C36E97CB4B06C3093407E75E0EC3E6875D6ECE745C8) in the upper right corner. If a folder is selected, a file will be added to the folder. If a file is selected, a same-level file will be added.
-   Deleting a file or folder: Select a file or folder and click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/gTJdW0ypRISsYVnquPkIIQ/en-us_image_0000002440934432.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062101Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3384E6ED34539906A68CE136B4F85601314627FB944077EF0ACE87E11EFF0AAC) on the right to delete it. The root directory cannot be deleted.
-   Renaming a file or folder: Double-click a file or folder, enter a new name, and press **Enter**. The name can contain only letters, digits, underscores (\_), and hyphens (-).

 |
| 

Editor

 | 

Provides the following capabilities:

-   Syntax highlighting: highlights code based on the syntax of Node.js.
-   Syntax verification: displays error information when a syntax error is found.
-   Code suggestion: automatically displays suggested code during coding.
-   Code autocomplete: autocompletes with suggested code.
-   Formatting: formats the code through **Ctrl+Shift+B**.
-   Shortcut keys: supports **Ctrl+V**, **Ctrl+C**, **Ctrl+Z**, **Ctrl+X**, **Ctrl+F**, **Ctrl+/**, and others.

 |
| 

Maximize icon

 | 

You can click the maximize icon ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/1rhGR9rfRuWhj5oytkmyfw/en-us_image_0000002474174581.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062101Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=47E2D61A25DB0168CFE93467A6450D8CD4E35D3B053B48A3B123BAC6EBEF65A7) to enlarge the online editing area. To restore it, click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/PshJWJ48S_O7uqRQWC-bSw/en-us_image_0000002440934472.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062101Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=92DBC6D08D4549C6CCDF303C68E18C5ABB038C03064A9961C739F0F7637C48D9) or press **Esc**.

 |

#### Configuring a Layer

Layers allow you to release and deploy common dependency libraries. By extracting the common libraries and dependencies that your function needs into a layer, you can bind this layer to your function and use the libraries within the function without including them in the function's code package. This can reduce the size of the function's code package, shorten deployment time, and avoid potential errors that may occur during dependency installation and packaging due to the use of the function code. For details about layer management, please refer to [Managing Layers](https://developer.huawei.com/consumer/en/doc/AppGallery-connect-Guides/agc-cloud-function-layer-0000001517762624).

If no layer has been created, skip the following steps and click **Create** at the bottom of the page to define the function. After creating a layer, you can configure the layer and bind it to the function on the function details page. If you have created a layer before creating a function, perform the following steps:

1.  On the **Layer configuration** page, click **Bind layer**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/07eJtj_gS2iBiS1GyT1m8Q/en-us_image_0000002440934428.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062101Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=16ACF7DE90486CE0915576C0B0F20E0018CA8744773EF47633C97C75B3B01D68)
    
2.  On the **Bind layer** page, set **Layer name** and **Version**, and click **OK**. Note that other parameters like **Layer scope** will be automatically filled. A function can be bound to a maximum of five layers.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/VDkEEHSqRnKiccmHEKtnQw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062101Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8A488CDE80F0DB552EA3D85761EE8A7F879FE3699B340A99DAC341FF1CBE1446)
    
    When selecting a layer, the compatible runtime environment of the layer must comply with the function runtime environment. The system will automatically filter layers. If no layer is available, [create a layer](https://developer.huawei.com/consumer/en/doc/AppGallery-connect-Guides/agc-cloud-function-layer-0000001517762624#section11358162018572) with a runtime environment same as the function runtime environment and then bind it to the function.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/mUFgXQ4iS6CD0RPCbBIwEg/en-us_image_0000002440934440.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062101Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=26FB5F84C95FDF355832E6B7FB5FBE166CEA8D023D95259DF46B905C8990F5B1)
    
    | 
    Parameter
    
     | 
    
    Description
    
     |
    | :-- | :-- |
    | 
    
    Layer name
    
     | 
    
    Name of a layer. If a layer with the specified name already exists, a new version will be automatically added to the existing layer.
    
     |
    | 
    
    Version
    
     | 
    
    Version of a layer. If a layer has multiple versions, select a version to bind to the function.
    
     |
    | 
    
    Layer scope
    
     | 
    
    Sharing scope of a layer.
    
    -   **Sharing Within Project**
    -   **Sharing Within team**
    
     |
    | 
    
    Compatible runtime
    
     | 
    
    Runtime environment used by the layer. Select **nodejs**.
    
     |
    | 
    
    Layer description
    
     | 
    
    Description of a layer, which can contain up to 1024 characters.
    
     |
    
3.  View the bound layer on the **Layer configuration** page. To unbind a layer from the function, click **Unbind** in the **Action** column of the layer.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/gKcEHJsXSCOrVFxt7-kfCQ/en-us_image_0000002474214453.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062101Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=02A8EEE498EF1119C11FA47AEAAC1E6FEC6C2C7745E6B6B7B2392917D2912EF6)
    
4.  Click **Create** to complete function creation. During function creation, you can click **Previous** to go back to the **Function configuration**, **Trigger**, or **Function Code** page and modify information on the page.

#### More You May Need to Know

After configuring a function, you can [modify its advanced configurations](https://developer.huawei.com/consumer/en/doc/AppGallery-connect-Guides/modify-function-advanced-config-0000001734287937).
