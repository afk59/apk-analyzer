# Capturing Screenshots

During the debugging process, you can capture screenshots in various ways.

#### Using DevEco Studio

1.  Connect to a real device or the Emulator, and run an app on the device or Emulator.
2.  On DevEco Studio, open the **Log** tab page.
3.  Click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/O5a7egfgRRqcXgQKHyCnWQ/en-us_image_0000002532750261.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1C392FE614D9AD7ADEB00A1E30DCF2ED3217068469C7D4B39D1FB43009D7E11B) on the toolbar on the left to capture a screenshot.
    
    The screenshot is displayed in DevEco Studio.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/wuNJEx--RViuDYUOEoPkDQ/en-us_image_0000002500910388.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CF948E647B0A8C3091121468A82ADB37600E32B84771C3B6CFA60C39BC7E13F8)
    
4.  (Optional) Right-click the image display area and choose **Copy Path/Reference** from the shortcut menu to view the local path of the screenshot or display the local path below the menu bar.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/ii9UCuPSQfaPmRHbVY-EZQ/en-us_image_0000002501070234.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=05C303219D8989A7B40013E006DCF06FABFDD7BE12FD156C5E9225DD6C6C94CB)
    

#### Using Commands

hdc is a command line tool used for debugging. You can use this tool to capture screenshots. For details about hdc, see [hdc](../../../system/debugging-tools/performance-analysis-kit/command-line-tools/hdc/document.md).

## Using hdc shell snapshot\_display

hdc shell snapshot\_display -f /data/local/tmp/0.jpeg  // -f specifies the directory for saving the image on the device. If this parameter is not specified, the default directory is displayed after the command is executed.
hdc file recv /data/local/tmp/0.jpeg  // Send the image from the device to a local directory. In this example, the image is sent to the directory where the hdc command is executed.

## Using hdc shell wukong special -p

wukong is a tool used to perform system stability tests. You can specify the **\-p** parameter to capture screenshots. For details about wukong, see [wukong User Guide](../../../system/debugging-tools/test-kit/wukong-user-guide/document.md).

hdc shell wukong special -p

The following figure shows the command execution result. **Report currentTestDir** indicates the directory where the test result including the screenshot is stored.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/Kt9ggK--QiiMdrSlKdUUZw/en-us_image_0000002500910390.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FEC0F18E4595846A0057DDBB5B74141E1824190B6E0A3E05DEA543DB0F73D9B2)

Run the hdc command to send the file in the directory to the local side, for example, send it to the current directory where the hdc command is executed.

hdc file recv /data/local/tmp/wukong/report/20231010\_141610/
