# Using Smart Step Into

When multiple functions are nested or invoked in a line of the editor, you can use the Smart Step Into feature to step into the function to be debugged. If you want to skip some files during debugging, you can customize the list of files to skip.

#### Procedure

1.  Start debugging. If there are multiple method calls on the line where the breakpoint is located, you can highlight the available functions to step into by clicking the ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/881ahgpORu2LZnHTb4rdbQ/en-us_image_0000002532670643.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2D6D1C042B207AB56D527145DC975608E34C8588DB6AC9D4736195A048631C83) button in the debugging window or pressing **Shift+F7**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/yHl5cPNTSsqrnFc5DTyW-w/en-us_image_0000002532750595.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=11D402DDC8DB0483E41C5DB1E708C4E9CA553F5D3167FF49BFCAABB7847EE051)
    
2.  Click one of the functions.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/eV6xtF_STBaoUspMra0wvA/en-us_image_0000002532750593.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D15809721557A982891E2BD9468311606D34FB99B83F940100B60C4F4B7BFDDD)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/1lp-jbNjTDSo0BZ2lJG8tQ/en-us_image_0000002500910730.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=06D34FCF5AD0D4DC8D55E4163666E5223E0DB4DD640AA4D82E0B9462C88DE8A7)
    

#### Filtering Script Files

1.  Choose **File** > **Settings** (**DevEco Studio** > **Preferences**/**Settings** on macOS) > **Build, Execution, Deployment** > **Debugger** > **Stepping** and select **Do not step into ArkTs scripts** to prevent smart stepping into certain scripts during debugging. Use the toolbar button to manage the list of scripts to skip.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/obqz7MEcQUGpBrdF92bILw/en-us_image_0000002501070572.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=50EEF2D72EDE975EEC12FB07EA0A1B5AC39EB44BDF9B17D04C0E1D283E5CBDAF)
    
2.  Click **+** to add a script filter. In the displayed dialog box, enter the name of the file to skip or use wildcards. For example, to always skip JavaScript files, enter **\*.js**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/-3jkB49iS3-dXaoLIsHELQ/en-us_image_0000002532670641.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C473EB4B991BC0D9A438638A7FD938788B8AB5EDDD8645F1BDAB5428EADBB967)
