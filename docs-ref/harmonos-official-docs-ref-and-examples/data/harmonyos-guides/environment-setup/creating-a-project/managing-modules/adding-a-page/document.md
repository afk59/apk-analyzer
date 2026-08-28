# Adding a Page

To an ArkTS project you can add pages – each individual page is a separate document of the app/atomic service. You can design multiple pages for your app/atomic service, manage their files on a per-page basis, and schedule page redirection through routing APIs, so as to implement decoupling of app/atomic service functions. To add a page, perform the following, after which an .ets file is generated in the **pages** folder:

1.  In a project directory in the stage model, right-click **pages** in the **ets** folder, choose **New** > **Page** from the shortcut menu, and select any of the following page types:
    
    -   **Empty Page**: a common page that implements a basic Hello World example.
    -   **Map Page**: a map page that presents map views. This feature is only available on phones.
    -   **Payment Page**: a payment page that can trigger a payment dialog box when the designated button is tapped. This feature is only available on phones.
    -   **Iap Page**: a page for in-app purchases of virtual or digital goods. It follows the IAP Kit scenario-based template and allows for quick generation of related code.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/NrvFQnjGRVG0gO2QQOsByg/en-us_image_0000002500910666.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7BA2491DDCAA9F6C6A65D06E2E7BE661478E004B6610EED4D2F6EC0F5AA01563)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/1iMz7krUSqSSoo7N_9ENSg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B419EFBA6BD0FE9B5231BC9DF06FCD2EDBE98B6C7983A87D288EF955907724DB)
    
    For projects of API version 10, only common pages can be created. To create other types of pages, switch your project to API version 11 or later first.
    
2.  Enter a page name consisting of uppercase letters, lowercase letters, digits, and underscores (\_), and click **Finish**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/RCwTdR6rSUWA78_uNNnQNg/en-us_image_0000002532750537.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5E4140177D88BC153F6BE8B2FDD691C85F741E9E3FB8DFFFC6DF22C072BD20BE "Click to enlarge")
