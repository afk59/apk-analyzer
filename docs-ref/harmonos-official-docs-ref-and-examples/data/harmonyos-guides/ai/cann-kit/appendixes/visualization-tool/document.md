# Visualization Tool

#### Overview

[Netron](https://github.com/lutzroeder/netron/tags) is a neural network model visualization tool that supports the visualization of many mainstream AI framework models. [Netron](https://github.com/lutzroeder/netron/tags) 5.1.6 and later versions support .om model visualization. As shown in the following figure, after an .om model is loaded using Netron, its topology structure, graph, and node information are displayed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/wn7hNUB3QnuC5R-snkVI8g/en-us_image_0000002505661676.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062125Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ED991007B251B5020CC6CE1B6CCCEB0CC68EDBD06B71BD1906BD69CCE8EB84F8 "Click to enlarge")

#### Function Description

-   Load .om models.
-   Display the topology structure and data stream shape.
-   View model parameters such as the format, input, and output.
-   View the subgraph and operator device information of a compiled model.
-   View information about nodes, such as **NODE PROPERTIES**, **ATTRIBUTES**, **INPUTS**, and **OUTPUTS**.
-   Save and export the visualization result as an image.

#### Using the Visualization Tool

## Installing the Tool

1.  Download the latest [Netron](https://github.com/lutzroeder/netron/tags).
2.  Install Netron.
    
    -   macOS: Download the .dmg file or run the **brew cask install netron** command.
    -   Linux: Download the .AppImage file or run the **snap install netron** command.
    -   Windows: Download the .exe file or run the **winget install netron** command.
    -   Python server: Run **pip install netron** to install Netron, and then run the **netron \[FILE\]** or **netron.start('\[FILE\]')** to load a model.
    -   Browser: Open the web-based [Netron](https://netron.app/) and you can use it without the need to install it.
    

3.  After the installation is complete, drag the model to the window to open it.

## Viewing Subgraphs

View the subgraphs of a compiled model as follows:

1.  Drag the compiled model to the [Netron](https://netron.app/) tool to open it.
2.  Click the subgraph node, go to **ATTRIBUTES > subgraph** on the right, and click the attribute value of **subgraph**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/msPo2kP_R0mTBn1ac94jRw/en-us_image_0000002528408529.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062125Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6A3612A8BF1685C32B8C0EE95F05360BC9DA8F27F3A283F58231FD9FE1EF4F84)
    
3.  View information about subgraph nodes, such as **NODE PROPERTIES**, **ATTRIBUTES**, **INPUTS**, and **OUTPUTS**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/MtNxo0zQQEOOtJmixQGz7A/en-us_image_0000002496568526.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062125Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=08AA74B2C6CF064FE1C0395E0A4B4BD684275D8363990A1476739B3F80916C80)
    
4.  Click the arrow in the upper left corner to return to the main graph.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/zAANbBhURx2-R2-VQcxhcQ/en-us_image_0000002528408531.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062125Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D2FFDB107AB32CFE912325BC877E0686AC2A82DFC922E6BC0A017E99C0867E20)
