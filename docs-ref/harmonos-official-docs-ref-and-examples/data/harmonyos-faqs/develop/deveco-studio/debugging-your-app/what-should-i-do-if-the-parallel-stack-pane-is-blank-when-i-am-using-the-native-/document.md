# What should I do if the parallel stack pane is blank when I am using the native debugging stack visualization feature?

**Symptom**

When the native debugging stack visualization feature is enabled, switching between any two tabs may cause the parallel stack pane to be displayed as blank.

**Solution**

This issue may be due to incompatibility of the computer's GPU, or using DevEco Studio in a cloud desktop environment.

Double-click **Shift** in DevEco Studio, search for **Registry** in the window that is displayed, select **ide.browser.jcef.gpu.disable** on the **Registry** page, close the window, and restart DevEco Studio.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/bjC_Xa87Q8KyIQr_tCDZNQ/en-us_image_0000002521308425.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062624Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BFE4087104B9D47A8EF5EA5CAE47C857F8EF5E556457F0D0E1B0B34F98EF013E)
