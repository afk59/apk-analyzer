# Text Development FAQs

#### How Do I Optimize the Display of Text with an Undefined Glyph?

Currently, the undefined glyphs are displayed as blanks by default, which may confuse users.

The system provides a switch, which can display undefined glyphs as tofu blocks once enabled.

-   In ArkTS, you can use the **setTextUndefinedGlyphDisplay** API to enable the display of undefined glyphs as tofu blocks.
    
    import { text } from "@kit.ArkGraphics2D";
    
    text.setTextUndefinedGlyphDisplay(text.TextUndefinedGlyphDisplay.USE\_TOFU);
    
-   In C/C++, you can use the **OH\_Drawing\_SetTextUndefinedGlyphDisplay** API to enable the display of undefined glyphs as tofu blocks.
    
    #include "drawing/drawing\_text\_global.h"
    
    OH\_Drawing\_SetTextUndefinedGlyphDisplay(TEXT\_NO\_GLYPH\_USE\_TOFU);
    

The preceding two APIs control the same switch. You can use either of them.

Take the "\\uffffHello World\\uffff" text as an example. \\uffff indicates text with an undefined glyph.

The following figures show the comparison.

| Display Optimization Enabled or Not | Effect |
| :-- | :-- |
| Disabled | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/AuQqLVF0TWqrGbBJjBqb5w/en-us_image_0000002568684981.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062050Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F79E85BD6122A2C3BE0E1EBF50E6354F156B34FA3DC7785E797A5F60C6BD0349) |
| Enabled | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/firIrwLdR-iyAMLe-km-fg/en-us_image_0000002568764991.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062050Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=35B03DD4FA7571565375E5B1325A1984E2577D7489C0735E6886B3CAA5FADB8F) |
