# hilogtool

#### Scenarios

Currently, HiLog files are encoded in binary and saved in .gz format, which cannot be directly decompressed or downloaded after being exported from the **/data/log/hilog** directory of the device. With hilogtool, you can easily decompress the log files and convert them into plaintext.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/xJ7rS8-STWqf-d83Ow0_uA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062033Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9679316FA36C899D0F291E19EBEE9F2B2E0849E00E01D3C96FFCCBBED1552DEF)

In the current mechanism, kmsg logs are not affected and can be viewed directly; the HiLog files can be viewed online by running the **hilog** command in the **shell** window.

#### Usage

## How to Obtain

Download the HarmonyOS SDK. By default, you can obtain hilogtool from the **hms/toolchains** directory of the corresponding OS (Windows/Linux/macOS).

## Environment Configurations

**For Windows**

Choose **This computer** > **properties** > **advanced system settings** > **advanced** > **environment variables** > **Path** > **Edit**. Add the path of **hilogtool.exe** to **Path**. After that, restart the PC, and run the **hilogtool** command in the cmd window.

**For MacOS**

1\. Start the terminal tool and run the following command:

echo $SHELL

a. If the output is **/bin/bash**, open the **.bash\_profile** file.

vi ~/.bash\_profile

b. If the output is **/bin/zsh**, open the **.zshrc** file.

vi ~/.zshrc

2\. Press **i** to enter the **Insert** mode.

3\. Add the path of **hilogtool.exe**:

export PATH=$PATH:/path/to/your/hilogtool

4\. Press **Esc** to exit the edit mode, and then enter **:wq** and press **Enter** to save the settings and exit.

5\. Run the following command for the environment variable to take effect.

a. If the output is **.bash\_profile** in step 1, run the following command:

source ~/.bash\_profile

b. If the output is **.zshrc** in step 1, run the following command:

source ~/.zshrc

6\. After the environment variables are configured, restart the PC.

## How to Use

**Command:**

hilogtool parse -i xxx -o xxx -d xxx

hilogtool parse --input xxx --output xxx --dict xxx

**Parse command parameters:**

| 
Options

 | 

Description

 | 

Example

 |
| :-- | :-- | :-- |
| 

\-h/--help

 | 

Displays the help information.

 | 

hilogtool -h

 |
| 

\-i/–-input _inputDir_

 | 

Specifies the input path. All HiLog files in the directory are scanned and parsed.

By default, it is the current command path.

 | 

Parse all HiLog files in the **D:\\temp\\hilog** directory:

hilogtool parse -i D:\\temp\\hilog

Parse all HiLog files in the current directory:

hilogtool parse -i .\\

 |
| 

\-i/–-input _inputFile_

 | 

Parses a specified HiLog file.

 | 

Parse a specified HiLog file:

hilogtool parse -i D:\\temp\\data\\log\\hilog.706.20230711-071816.gz

hilogtool parse -i .\\hilog.706.20230711-071816.gz

 |
| 

\-o/–-output _outputDir_

 | 

Specifies the output path, which is the path for saving parsed log files.

The default value is the path of the parsed original HiLog file.

 | 

Parse the log files in the current directory to the **D:\\temp** directory:

hilogtool parse -i .\\ -o D:\\temp

 |
| 

\-d/--dict dictFile

 | 

Specifies the path of the data dictionary.

By default, the latest data dictionary file (for example, **hilog\_dict.20230908-142200.zip**) is matched in the current command path.

 | 

Parse all HiLog files in the **D:\\temp\\hilog** directory and specify the data dictionary in the directory.

hilogtool parse -i D:\\temp\\hilog -d D:\\temp\\hilog\\hilog\_dict.20230908-142200.zip

 |
| 

\-v/--version

 | 

Checks the current version.

 | 

hilogtool -v

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/iYTwS_I3RqumqbyOVLaN_Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062033Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9FDDFD0F07DEB64D1B15B39B546AF16E9B41E8D8BF0A95FB2216B229EE64C930)

1\. The data dictionary file is stored in the **data/log/hilog** directory and named in the format of **hilog\_dict.2024xxxx-xxxxxx.zip**. The file is automatically generated when the device is started and is required for parsing logs.

Log parsing may fail if the data dictionary is missing. Restart the device to regenerate a data dictionary.

2\. The default format of the flushed HiLog log file is **hilog\\\\.\\\\d{3}\\\\.\\\\d{8}-\\\\d{6}\\\\.gz$**. If the file name is customized by running the **hilog\\\\.\\\\d{3}\\\\.\\\\d{8}-\\\\d{6}\\.gz$** command during development, the log file may fail to be parsed. To resolve this problem, upgrade hilogtool to 1.0.0b or later.

#### Common Parsing Commands

## (Recommended) Parsing All HiLog Files in the Current Directory

In the current log directory, enter the **shell** window through the **cmd** window. In the **shell** window, run the **hilogtool parse** command to parse the log files, as shown in the following figure.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/v7XmzH_UQk2ry6-rMg0-cA/en-us_image_0000002529594789.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062033Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7BB08AE80E84A6C8AAF2438E3D67C7B225FAEBF806ED6B9CC1A24D7608CFFCC7 "Click to enlarge")

## Parsing HiLog Files in the Specified Directory

hilogtool parse -i D:\\09-temp\\dict-test -d D:\\09-temp\\dict-test

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/0KW_--VtRsinGfr1ypEqaQ/en-us_image_0000002497754814.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062033Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=40A3C6EC0100BCF990280CE3E2583A6475582F2E470ECF79159954821251E0FC "Click to enlarge")

## Parsing a Single HiLog File

hilogtool parse -i D:\\09-temp\\dict-test\\hilog.025.20231020-154659.gz -d D:\\09-temp\\dict-test

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/RLsle7jmRJKqJ_o98lGazg/en-us_image_0000002529714755.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062033Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0577395EB83BFD1E976AF6368F5FAB51343431EC43EC0CEAF395FFE28E17CFE9 "Click to enlarge")

#### Automatic Scripts

The automatic script is named **get\_hilog.bat**. Place it in the same directory as hilogtool. The script exports logs in the **data/log/hilog** from the device and automatically converts the logs to plaintext.

## For Windows

The **get\_hilog.bat** script on Windows is as follows:

@set Ymd=%date:~0,4%\_%date:~5,2%%date:~8,2%\_%time:~0,2%%time:~3,2%%time:~6,2%
@set Ymd=%Ymd: =0%
@set Dir=LOG\_%YMD%
md %Dir%
hdc file recv /data/log/hilog/ .\\%Dir%\\
hilogtool parse -i .\\%Dir% -d .\\%Dir%
pause

Script execution result:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/P5tR1Nr_Qq2_NfKEI9JJIA/en-us_image_0000002497914792.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062033Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FC46BD1DA3EC5921F8C81E838B912F76609182039F85772AD8B98B4654E9D38E "Click to enlarge")

## For macOS

The script on macOS is as follows:

Ymd=$(date "+%Y\_%m%d\_%H%M%S")
Dir=LOG\_$Ymd
mkdir $Dir
hdc file recv /data/log/hilog/ ./$Dir/
./hilogtool parse -i ./$Dir -d ./$Dir

#### Scenarios That May be Affected

## Automatic Log Analysis

In some domains, automatic analysis is required for plaintext log files in the **/data/log/hilog** directory. As HiLog uses the lightweight implementation, logs are saved in the binary format. Therefore, hilogtool needs to be adapted for automatic decompilation of binary logs.

## Log Forwarding

The log files obtained from the **/data/log/hilog** directory of the device by using **recv** are in the binary format and cannot be viewed directly. You are advised to parse the log files before sending them, or forward the binary log files together with the data dictionary.

#### Error Code

| 
Error Code

 | 

Description

 | 

Handling Method

 |
| :-- | :-- | :-- |
| 

200

 | 

Decoding is successful.

 | 

Not involved.

 |
| 

300

 | 

Decoding failed because logs in some domains do not match the dictionary.

 | 

1\. If only some logs fail to be parsed, the problem does not affect self-debugging and can be ignored.

2\. If the self-debugging is affected, generate the data dictionary incrementally by referring to the following FAQs.

 |
| 

500

 | 

The parsing tool version does not match.

 | 

Update the version of hilogtool.

 |
| 

999

 | 

The log is saved in plaintext and does not require parsing.

 | 

Not involved.

 |

#### FAQs

**Symptom**

During parsing, "there is no hilog dict zip in xxx, use -d to specify", or "open dict xxx fail, errno is: No such file or directory" is displayed.

In the parsed log, "OpenUuidFile fail, unknown log, uuid is: xxxxxx" is displayed.

**Possible Causes**

The corresponding data dictionary is not found during log parsing.

**Answer**

1\. The parsing command is incorrect. For details, see [Common Parsing Commands](#section742131815517).

2\. The **bin/so** file is replaced locally for debugging. In such a case, a new data dictionary needs to be generated for parsing by performing one of the following operations:

(1) Run the **hilog -d xxx** command to incrementally generate a data dictionary.

For example, push the **hilogTest** file (.bin file) to the **/system/bin/** directory. Then, run the following command to incrementally generate the data dictionary of **hilogTest**:

hdc shell hilog -d /system/bin/hilogTest

After the data dictionary is successfully generated, the **hilogTest** can print logs.

(2) Run the **service\_control stop hilogd && service\_control start hilogd** command to restart hilogd.

(3) Restart the device.

3\. The data dictionary is deleted. Check whether the exported logs contain data dictionary files named in the format of **hilog\_dict.2024xxxx-xxxxxx.zip**.

If there is no such a data dictionary, it is possibly deleted by running the **rm -rf data/log/hilog/\*** command. In this case, restart the device to generate a new data dictionary.
