# What should I do if test cases fail to be executed when the original project is opened using the new DevEco Studio version?

**Symptom**

If a project is created in a version earlier than DevEco Studio 3.1.0.400, after DevEco Studio is upgraded to 3.1.0.400 or later, the project fails to run test cases and the error message "A page configured in 'test\_pages.json' must have one and only one '@Entry' decorator" is displayed.

**Figure 1**  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/EzaLgrJsRzC_LfB1c3EJOg/en-us_image_0000002229604113.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062625Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9F0C44613B51AF157E6985B965B23B3FAF95968320BD4CC33964FDAAC2B2833D "Click to enlarge")

**Solution**

Rename the **TestRunner** and **TestAbility** directories **testrunner** and **testability**, which are in lowercase, and run the test cases again.

**Figure 2**  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/3UVCClrrQsafKwt1QiSMRQ/en-us_image_0000002194158732.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062625Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E5662E467C5D21E297E84AE695AD1D724958D8A331596083399B292047563E6D "Click to enlarge")
