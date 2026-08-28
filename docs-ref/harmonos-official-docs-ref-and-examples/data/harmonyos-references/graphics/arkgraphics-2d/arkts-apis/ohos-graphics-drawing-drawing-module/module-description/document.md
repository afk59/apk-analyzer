# Module Description

During application development, you often need to draw different elements. Typically, you can use ArkUI components to draw the desired elements or effects. However, sometimes these components cannot meet the needs for custom graphics or effects. In such cases, you can turn to the Drawing module for flexible custom drawing. This module provides basic drawing capabilities, such as drawing rectangles, circles, points, straight lines, custom paths, and fonts.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/Tc1HfXj8Rri4bdVn62ojmQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062446Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ECD19C8D66FF75666A1258B7CA9BC245F976ECEA6219A36A5348BA1D0888703A)

-   The initial APIs of this module are supported since API version 11. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   This module uses the physical pixel unit, px.
    
-   The module operates under a single-threaded model. The caller needs to manage thread safety and context state transitions.
    

#### Modules to Import

import { drawing } from '@kit.ArkGraphics2D';
