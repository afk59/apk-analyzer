# What should I do if clicking the "New Emulator" button does not work?

**Symptom**

There is no response to the click on the **New Emulator** button.

**Solution**

1.  Open settings on the local computer, choose **Optional Features**, and select **Add an Optional Feature**.
2.  Search for **wmic** and click **Install**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/Bf5jwgv4RGygIqbxWL9DbQ/en-us_image_0000002229758369.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062622Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=43219BE9C69A777C112134ED313A3F859D8AB3D1F7E8F027D61053868102E4E2 "Click to enlarge")
    
3.  Configure system environment variables. Take Windows 10 as an example, choose **This PC** > **Properties** > **Advanced System Settings** > **Advanced** > **Environment Variables**, and add **%SystemRoot%\\\\System32\\\\Wbem** to the system path variable.
