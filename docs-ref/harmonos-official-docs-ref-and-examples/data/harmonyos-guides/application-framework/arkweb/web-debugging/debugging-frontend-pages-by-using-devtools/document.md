# Debugging Frontend Pages by Using DevTools

The **Web** component supports debugging of web frontend pages by using DevTools, a web frontend development and debugging tool that allows you to debug an application's frontend pages on a PC. Before you do this, use [setWebDebuggingAccess()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#setwebdebuggingaccess) to enable frontend page debugging for the **Web** component and make sure the test device connected to the PC runs 4.1.0 or a later version.

#### Wireless Debugging

Since API version 20, the wireless debugging API [setWebDebuggingAccess20+](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#setwebdebuggingaccess20) can be used to simplify the debugging process.

## Enabling Web Debugging for Application Code

Before debugging a web page, call the **setWebDebuggingAccess()** API to enable the web debugging feature.

If the web debugging function is not enabled, DevTools cannot detect the web page to be debugged.

1.  To enable the web debugging feature in application code, call the [setWebDebuggingAccess20+](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#setwebdebuggingaccess20) API to set the TCP socket port and enable the web debugging feature.
    
    import { webview } from '@kit.ArkWeb';
    import { BusinessError } from '@kit.BasicServicesKit';
    const DEBUGGING\_PORT: number = 8888;
    
    @Entry
    @Component
    struct WebComponent {
      controller: webview.WebviewController = new webview.WebviewController();
    
      aboutToAppear(): void {
        try {
          // Enable wireless web debugging and specify the TCP socket port.
          webview.WebviewController.setWebDebuggingAccess(true, DEBUGGING\_PORT);
        } catch (error) {
          console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
        }
      }
    
      build() {
        Column() {
          Web({ src: 'www.example.com', controller: this.controller })
        }
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/O6-muVkZTgWHBRNdhCIGmg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061949Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=72BB66E0A6D5011C66BDBE684850CBB35A0CCACDB5C5FA64A32E016C37887B61)
    
    Port 8888 used in the sample code is for reference only. You must ensure that the port number can be used by applications in practice. If the port cannot be used because the port is occupied or the application does not have the permission to use the port, the API throws an exception or the ArkWeb cannot enable the debugging mode.
    
2.  To enable the debugging feature, you need to add the following permission to the **module.json5** file of the application's HAP in DevEco Studio. For details, see [Declaring Permissions in the Configuration File](../../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/declaring-permissions/document.md#declaring-permissions-in-the-configuration-file).
    
     "requestPermissions":\[
       {
         "name" : "ohos.permission.INTERNET"
       }
     \]
    

## Opening the Debugging Tool Page in Chrome

1.  Input **chrome://inspect/#devices** in the address box of Chrome on the PC and open the page.
2.  Configure the Chrome debugging tool.
    
    Select **Discover network targets** to discover the web page to be debugged based on the specified IP address and port number.
    
    (1) Click the **Configure** button.
    
    (2) In **Target discovery settings**, add the IP address of the device to be debugged and the port specified in the [setWebDebuggingAccess20+](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#setwebdebuggingaccess20) API, for example, **192.168.0.3:8888**.
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/PD1NNfE3TMWgb8p4FQuNJw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061949Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E7C4E0FC4568AFF848666EC7C55CFEC03F789C2E21152D0C39A513C931D8BA88)

The debugging tool and the device to be debugged must be in the same LAN and can access each other. If the device to be debugged has multiple IP addresses, use the IP address that is in the same network segment as the IP address of the debugging tool.

## Waiting for the Page to Be Debugged

If the preceding steps are successful, the page to be debugged is displayed on the Chrome debugging page.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/qFXNLjx0T6aoPQ7J-SEoag/en-us_image_0000002568764761.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061949Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F256B121A0A000E5A98A87190607FAF0164CAFDC36A8854318326D669B3A114A)

## Starting Web Page Debugging

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/TmC-Z31BTjmiih-yTCZP2Q/en-us_image_0000002537765036.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061949Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1B34463AF89AE6BF896CEF2A99FE68D2E7D74B223D27884AB45F57EFF32E761D)

#### USB Debugging

## Enabling Web Debugging for Application Code

Before debugging a web page, call the [setWebDebuggingAccess()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#setwebdebuggingaccess) API to enable the web debugging feature.

If the web debugging function is not enabled, DevTools cannot detect the web page to be debugged.

1.  Enable web frontend page debugging in the application code.
    
    import { webview } from '@kit.ArkWeb';
    
    @Entry
    @Component
    struct WebComponent {
      controller: webview.WebviewController = new webview.WebviewController();
    
      aboutToAppear() {
        // Enable web frontend page debugging.
        webview.WebviewController.setWebDebuggingAccess(true);
      }
    
      build() {
        Column() {
          Web({ src: 'www.example.com', controller: this.controller })
        }
      }
    }
    
2.  To enable the debugging feature, you need to add the following permission to the **module.json5** file of the application's HAP in DevEco Studio. For details, see [Declaring Permissions in the Configuration File](../../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/declaring-permissions/document.md#declaring-permissions-in-the-configuration-file).
    
    "requestPermissions":\[
      {
        "name" : "ohos.permission.INTERNET"
      }
    \]
    

## Connecting the Device to a PC

Connect the device to a PC and enable Developer mode for subsequent port forwarding operations.

1.  Enable Developer mode and USB debugging on your device.
    
    (1) Choose **Settings** > **System** and check whether **Developer options** is available. If not, go to **Settings** > **About** and touch the version number for seven consecutive times until the message "Enable developer mode?" is displayed. Touch **OK** and enter the PIN (if set). Then the device will automatically restart.
    
    (2) Connect the device to the PC using a USB cable. Choose **Settings** > **System** > **Developer options** and enable USB debugging. In the displayed dialog box, touch **Allow**.
    
2.  Run the hdc command to connect to the device.
    
    Run the following command in the CLI to check whether hdc can discover the device.
    
    hdc list targets
    
    -   If a device ID is returned, the device is connected.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/khbLAQ17QH6kXcuRBFQV7Q/en-us_image_0000002537924976.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061949Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=91E5520A64D61899002537FFB5FCBCF4CBCAAFF6537DC546D59A7C12D4A781E9)
        
    -   If **\[Empty\]** is returned, the device is not found.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/ZAS7EqJSREauY80oBwowqw/en-us_image_0000002568684753.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061949Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A49A23CDB9293495272C0F797D31E24586CD2D788CEF6CAF7D9956A614E3BFA8)
        
3.  Enter the hdc shell.
    
    After the device is connected, run the following command to enter hdc shell:
    
    hdc shell
    

## Port Forwarding

After the application code calls the **setWebDebuggingAccess** API to enable web debugging, the ArkWeb kernel starts a domain socket listener to enable DevTools to debug web pages.

However, Chrome cannot directly access the domain socket on the device. Therefore, the domain socket on the device needs to be forwarded to the PC.

1.  Run the following command in hdc shell to obtain the domain socket created by ArkWeb on the device.
    
    cat /proc/net/unix | grep devtools
    
    -   If the preceding operations are correct, the domain socket port is displayed.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/EdTz6Cm1QlCWoLxS8HXdSg/en-us_image_0000002568764763.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061949Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2DBFAC44445D980BFBE9AEE056E94620EE347579D3082EC08EF3006C4895E32B)
        
    -   If it is not displayed, check the following items again.
        
        (1) The web debugging function is enabled for the application.
        
        (2) The application uses the **Web** component to load the web page.
        
2.  Exit hdc shell, and run the following command to forward the obtained domain socket to TCP port 9222 of the PC.
    
    Run the **exit** command to exit the hdc shell.
    
    exit
    
    Run the following command to forward the port:
    
    hdc fport tcp:9222 localabstract:webview\_devtools\_remote\_38532
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/Z5_gF556T6y-nCol1Cvncw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061949Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1596AD7EB0BCF6B53B7553FF613A34408B949E9170A1C78D112E066422C05169)
    
    The number following **webview\_devtools\_remote\_** indicates the process ID of the application where the **Web** component is located. The number is not fixed. Change the number following **webview\_devtools\_remote\_** to the obtained value.
    
    If the process ID of the application changes (for example, the application is restarted), configure port forwarding again.
    
    The following figure shows a successful forwarding.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/CtHC221lSMW3TRFWH_ujng/en-us_image_0000002537765038.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061949Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=07A58798E17A45705B47BC6DD363E3804229FE78185FBCCBE26FEC508FB6DCF4)
    
3.  Run the following command to check whether the port is successfully forwarded.
    
    hdc fport ls
    
    -   If a port forwarding task is returned, the operation is successful.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/CZHge5ILRCK4pYMv8YkW0w/en-us_image_0000002537924978.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061949Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D9E3B922729B37DF8FC038674B84F9C520A599ADA2953ECF14BB5B948FDA1426)
        
    -   If **\[Empty\]** is returned, the operation fails.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/fRSr37shTUaSYPD8OKSylQ/en-us_image_0000002568684755.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061949Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AD33BCE827989F1119ABA067F702344401CFA61F895BC73FDC3D074664F5E2BD)
        

## Script

**On Windows**

Copy the following information to create a .bat file, enable application debugging, and run the file.

@echo off
setlocal enabledelayedexpansion

:: Initialize port number and PID list
set PORT=9222
set PID\_LIST=

:: Get the list of all forwarded ports and PIDs
for /f "tokens=2,5 delims=:\_" %%a in ('hdc fport ls') do (
    if %%a gtr !PORT! (
        set PORT=%%a
    )
    for /f "tokens=1 delims= " %%c in ("%%b") do (
        set PID\_LIST=!PID\_LIST! %%c
    )
)

:: Increment port number for next application
set temp\_PORT=!PORT!
set /a temp\_PORT+=1
set PORT=!temp\_PORT!

:: Get the domain socket name of devtools
for /f "tokens=\*" %%a in ('hdc shell "cat /proc/net/unix | grep devtools"') do (
    set SOCKET\_NAME=%%a

    :: Extract process ID
    for /f "delims=\_ tokens=4" %%b in ("!SOCKET\_NAME!") do set PID=%%b

    :: Check if PID already has a mapping
    echo !PID\_LIST! | findstr /C:" !PID! " >nul
    if errorlevel 1 (
        :: Add mapping
        hdc fport tcp:!PORT! localabstract:webview\_devtools\_remote\_!PID!
        if errorlevel 1 (
            echo Error: Failed to add mapping.
            pause
            exit /b
        )

        :: Add PID to list and increment port number for next application
        set PID\_LIST=!PID\_LIST! !PID!
        set temp\_PORT=!PORT!
        set /a temp\_PORT+=1
        set PORT=!temp\_PORT!
    )
)

:: If no process ID was found, prompt the user to open debugging in their application code and provide the documentation link
if "!SOCKET\_NAME!"=="" (
    echo No process ID was found. Please open debugging in your application code using the corresponding interface. You can find the relevant documentation at this link: \[https://gitcode.com/openharmony/docs/blob/master/en/application-dev/web/web-debugging-with-devtools.md\]
    pause
    exit /b
)

:: Check mapping
hdc fport ls

echo.
echo Script executed successfully. Press any key to exit...
pause >nul

:: Try to open the page in Edge
start msedge chrome://inspect/#devices

:: If Edge is not available, then open the page in Chrome
if errorlevel 1 (
    start chrome chrome://inspect/#devices
)

endlocal

**On Linux or macOS**

Copy the following information to create an .sh file. Note that you need to run the **chmod** command and convert the file format. Enable the application debugging and run the file.

This script will delete all port forwarding. If other tools (such as DevEco Studio) are using port forwarding, they will be affected.

#!/bin/bash

# Get current fport rule list
CURRENT\_FPORT\_LIST=$(hdc fport ls)

# Delete the existing fport rule one by one
while IFS= read -r line; do
    # Extract the taskline
    IFS=' ' read -ra parts <<< "$line"
    taskline="${parts\[1\]} ${parts\[2\]}"

    # Delete the corresponding fport rule
    echo "Removing forward rule for $taskline"
    hdc fport rm $taskline
    result=$?

    if \[ $result -eq 0 \]; then
        echo "Remove forward rule success, taskline:$taskline"
    else
        echo "Failed to remove forward rule, taskline:$taskline"
    fi

done <<< "$CURRENT\_FPORT\_LIST"

# Initial port number
INITIAL\_PORT=9222

# Get the current port number, use initial port number if not set previously
CURRENT\_PORT=${PORT:-$INITIAL\_PORT}

# Get the list of all PIDs that match the condition
PID\_LIST=$(hdc shell cat /proc/net/unix | grep webview\_devtools\_remote\_ | awk -F '\_' '{print $NF}')

if \[ -z "$PID\_LIST" \]; then
    echo "Failed to retrieve PID from the device"
    exit 1
fi

# Increment the port number
PORT=$CURRENT\_PORT

# Forward ports for each application one by one
for PID in $PID\_LIST; do
    # Increment the port number
    PORT=$((PORT + 1))

    # Execute the hdc fport command
    hdc fport tcp:$PORT localabstract:webview\_devtools\_remote\_$PID

    # Check if the command executed successfully
    if \[ $? -ne 0 \]; then
        echo "Failed to execute hdc fport command"
        exit 1
    fi
done

# List all forwarded ports
hdc fport ls

## Opening the Debugging Tool Page in Chrome

1.  Input **chrome://inspect/#devices** in the address box of Chrome on the PC and open the page.
    
2.  Configure the Chrome debugging tool.
    
    The web page to be debugged needs to be discovered from the local TCP port 9222. Therefore, ensure that **Discover network targets** is selected. Then, configure the network.
    
    (1) Click the **Configure** button.
    
    (2) Add **localhost:9222** to **Target discovery settings**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/99PxcnARSeaJUCWhxQKv4A/en-us_image_0000002568764765.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061949Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8C6891AAFCFAFD165576B52D99124F5A9146604427BE9A345478576268C3B00F)
    
3.  To debug multiple applications at the same time, add multiple port numbers in **Configure** of the **Devices** option on the Chrome debugging tool page.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/Jwr_rsiCTSeFr39_xnDLBw/en-us_image_0000002537765040.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061949Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B776904E01DE7ED2126B8D1F5CF51B3EC475E3C6817003FC9458F1BECCA2AFDA)
    

## Waiting for the Page to Be Debugged

If the preceding steps are successful, the page to be debugged is displayed on the Chrome debugging page.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/Twl94IYoSQCG55Y-NvmL1w/en-us_image_0000002568764761.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061949Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=11F9F19D34D5DE5101E9AD243228594BB614013564A43184BC7384175FD41935)

## Starting Web Page Debugging

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/4gzzWHRFTauIS7fHoIslvQ/en-us_image_0000002537765036.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061949Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=92B141D247527BB6E3ADBA776B5B4258B1B496BDA417F6512C099F0FA5DCD659)

#### FAQs

## Can I debug web pages opened in the system browser?

It depends on whether the web debugging feature is enabled for the system browser.

-   If yes, follow the steps in [USB Debugging](#usb-debugging).

## What should I do if hdc cannot discover devices?

**Symptom**

The device ID is not displayed after the following command is executed.

hdc list targets

**Solution**

-   Ensure that USB debugging is enabled on the device.
-   Ensure that the device is connected to the PC.

## What should I do if "unauthorized" is displayed in the hdc command output?

**Symptom**

When the hdc command is executed, the system displays a message indicating that the device is "unauthorized".

**Possible Causes**

The PC is not authorized to debug the device.

**Solution**

When a device with USB debugging enabled is connected to an unauthorized PC, a dialog box is displayed, asking you whether to allow USB debugging. In this case, select **Allow**.

## What should I do if the domain socket of DevTools cannot be found?

**Symptom**

No result is displayed after the following command is executed in hdc shell.

cat /proc/net/unix | grep devtools

**Solution**

-   Ensure that the step of [Enabling Web Debugging for Application Code](#enabling-web-debugging-for-application-code) is performed.
-   Ensure that the application uses the **Web** component to load the web page.

## What should I do if port forwarding fails?

**Symptom**

The configured forwarding task is not displayed after the following command is executed.

hdc fport ls

**Solution**

-   Ensure that the domain socket exists on the device.
-   Ensure that **tcp:9222** on the PC is not occupied.
    
    If **tcp:9222** is occupied, forward the domain socket to another TCP port that is not occupied, for example, **tcp:9223**.
    
    If the domain socket is forwarded to a new TCP port, you need to change the port number in **Target discovery settings** of Chrome on the PC.
    

## What should I do if the web page to be debugged cannot be found in Chrome on the PC after port forwarding is successful?

**Symptom**

The web page to be debugged cannot be found in Chrome on the PC.

**Possible Causes**

The port forwarding may be invalid due to the following reasons:

-   The device is disconnected from the PC. As a result, all forwarding tasks in hdc are cleared.
-   The hdc service is restarted. As a result, all forwarding tasks in hdc are cleared.
-   The process ID of the application on the device is changed (for example, the application is restarted). As a result, the previous forwarding tasks in hdc become invalid.
-   Exceptions occur when multiple forwarding tasks are forwarded to the same port.

**Solution**

-   Ensure that the local **tcp:9222** (or other configured port) on the PC is not occupied.
    
-   Ensure that the domain socket exists on the device.
    
-   Ensure that the process ID in the domain socket name is the same as that of the application to be debugged.
    
-   Delete unnecessary forwarding tasks from hdc.
    
-   After the domain socket is successfully forwarded, open **[http://localhost:9222/json](http://localhost:9222/json)** using the Chrome on the PC. Change **9222** in the URL to the actual TCP port number.
    
    -   If the web page is normally displayed, the port forwarding is successful. On the Chrome debugging page, perform the operation of [Waiting for the Page to Be Debugged](#waiting-for-the-page-to-be-debugged).
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/rZ21TloHS_qNeB-V9QjSmw/en-us_image_0000002537924980.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061949Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F5EB16EB576B1B5748DB6B21B54347EB72E2671B24C8644F4B0AA4957EE903D8)
        
    -   If an error page is displayed, port forwarding fails. For details, see [What should I do if port forwarding fails](#what-should-i-do-if-port-forwarding-fails).
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/J_NtCcmBS3eO9HwCjy7e9w/en-us_image_0000002568684757.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061949Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=19EE21B32C4D1117F2DF7D8353F9ADF2E8DB2DA5D43A6863BEFF99E7FD4D2557)
        
-   If the **[http://localhost:9222/json](http://localhost:9222/json)** page is normally displayed on Chrome, but the debugging target cannot be found on the Chrome debugging page, perform the following operations:
    
    -   Ensure that the port number in **Configure** on the Chrome debugging page is the same as the TCP port number specified for port forwarding.
    -   In this topic, the default TCP port number is **9222**.
        
        If you use another TCP port number (for example, **9223**), change the TCP port number in [port forwarding](#port-forwarding) and [Configure on the Chrome debugging tool page](#opening-the-debugging-tool-page-in-chrome).
        

## What should I do if the Chrome browser on the PC cannot find the web page to be debugged after the wireless debugging mode is enabled?

**Symptom**

After the wireless debugging mode is enabled for ArkWeb, the Chrome on the PC cannot detect the web page to be debugged.

**Possible Causes**

-   The wireless debugging mode is not enabled.
-   The network between the debugging tool and the device to be debugged is disconnected.

**Solution**

-   Ensure that the port can be used by applications.
-   Ensure that the debugging tool and the device to be debugged are in the same LAN and the network between them is normal.

## What should I do if the Web component cannot be debugged using DevTools?

**Symptom**

The web page to be debugged cannot be found in Chrome on the PC.

**Possible Causes**

-   When both hdc and ADB are used, ADB interferes with the WebSocket connection between DevTools and the device.

**Solution**

-   In this case, stop the ADB process and ensure that DevTools establishes a WebSocket connection with the device.

## What should I do if error 404 is reported when DevTools is used for debugging?

**Symptom**

When a web page is debugged in the Chrome browser on the computer, the error message "HTTP/1.1 404 Not Found" is displayed.

**Possible Causes**

-   The Chrome browser version is too early to support DevTools debugging.

**Solution**

-   Solution 1: Upgrade the Chrome browser to the latest version.
-   Solution 2: If you do not want to upgrade the browser, manually combine the URL. The complete URL is **devtools://devtools/bundled/inspector.html?ws=localhost:9222/devtools/page/xxx**.
    -   The URL consists of two parts. The first part **devtools://devtools/bundled/inspector.html** is fixed. The second part **?ws=localhost:9222/devtools/page/xxx** needs to be modified based on the actual configuration.
    -   After the port forwarding is successful, use Chrome to open the **[http://localhost:9222/json](http://localhost:9222/json)** page. Replace **9222** in the URL with the actual TCP port number. Then, obtain the value **?ws** and the following part of **devtoolsFrontendUrl**.
