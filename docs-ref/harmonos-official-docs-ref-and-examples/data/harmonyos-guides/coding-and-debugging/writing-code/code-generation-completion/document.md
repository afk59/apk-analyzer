# Code Generation/Completion

#### Intelligent Code Completion

With the intelligent code completion feature, the editor displays context-sensitive suggestions – fuzzy matching supported – for names of classes, methods, fields, keywords, and more.

By default, items in the suggestion list are sorted by the shortest path. To sort them by recency, choose **File** > **Settings** (**DevEco Studio** > **Preferences**/**Settings** on macOS) > **Editor** > **General** > **Code Completion** and select **Sort suggestions by recently used**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/CNr6la0zQnG2cpgnHROweA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4F877BA1C70781F4653D2D32DAA4F6600D9F957888D0C4A3C6F496E0D3F3DA53)

If the settings do not take effect, make sure **Sort suggestions alphabetically** is deselected on the **Code Completion** page.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/DCJOdL-cRIaMjinSVW4q7g/en-us_image_0000002500910380.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AB0635393EE42EF3D063C3DF3ED969CFCC16AE73EB63B9FEBC3132284738BAF3)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/j7-ME0GtQgWH3dRgX0Hv8w/en-us_image_0000002501070228.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C5C18862340486194DA5DF97DAB4BF3C50E59EE3D4A6B205764C4BB44564A9A3)

#### Overriding Methods of a Parent Class

The Override Methods feature helps you quickly generate methods from the predefined template of a parent class. Place the caret within the class where you want to override members from the base class, press **Ctrl+O** (**Control+O** on macOS), or right-click **Generate...**, choose **Override Methods** from the shortcut menu, specify the member (such as method and variable) to override, and click **OK**. The code of the overridden member is automatically generated.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/HDlSTHtrR7akbPp0CSNrjg/en-us_image_0000002532670301.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=02A789796DAF68CE44FC817FCA6B287C292EC736237FC57D5620370676E37855)

#### Quickly Generating Constructors

The editor can quickly generate a constructor for a class.

Place the caret within the target class and press **Alt+Insert** (**Command+N** on macOS). Alternatively, right-click the class and choose **Generate...** from the shortcut menu. When prompted, select **Constructor**, select one or more parameters to be initialized in the new constructor, and click **OK**. If you select **Select None**, a constructor without parameters is generated.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/S0H6yPAvQsWZETKK76vFHA/en-us_image_0000002532750247.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DE8B49A14B72E1109269A1E2062B66FA32AD5B260884A9A1F0485FE25E4C1E4D)

#### Quickly Generating Getters and Setters

The editor can quickly generate a getter and setter for a class member variable or object attribute.

Place the caret within the target class, right-click and choose **Generate...** > **Getter and Setter**, or press **Alt+Insert** (**Command+N** on macOS) and select **Getter and Setter**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/JVvuj60YT1OPwfxW_GWWvA/en-us_image_0000002532670297.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D58FA59E35CC3426398E370970F64544E0AAC14C514043DA79A8888B4BBD999F)

#### Quickly Generating Declaration Information to an Index File

The editor enables the batch declaration of information in HSP and HAR modules that needs to be exposed externally, such as variables, methods, interfaces, and classes, in the **Index.ets** file, to facilitate calls from other modules.

To use this feature, in the file editing window of an HSP or a HAR module, right-click anywhere and choose **Generate...** > **Declarations**, or press **Alt+Insert** (**Command+N** on macOS) and select **Declarations** from the drop-down menu. While pressing and holding the **Ctrl** key, select the variables, methods, APIs, and classes that you need to declare. The corresponding declaration information will be batch generated in the module's **Index.ets** file.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/q7dYwk0qSkKacDJpayJNjA/en-us_image_0000002501070226.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=400DF271078647304BCBF7A5CAEFDB4926ACC1808BCEF65D17639CF542F3525A)
