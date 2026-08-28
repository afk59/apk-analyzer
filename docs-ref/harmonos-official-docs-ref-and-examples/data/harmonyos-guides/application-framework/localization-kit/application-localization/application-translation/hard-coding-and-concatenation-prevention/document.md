# Hard Coding and Concatenation Prevention

#### Use Cases

A key part of localization is the translation of resource files. To improve the translation efficiency, avoid hard coding and concatenation during development.

Unlike obtaining data from external systems or dynamically generating data during running, hard coding refers to directly writing data, parameters, and constants into the program code to implement specific features. Hard-coded content displayed on the UI, including text in images, audios, and subtitles, is prohibited as this can increase the difficulty and workload in localization. In addition, a complete piece of text on the UI should not be concatenated from multiple segments. Concatenation makes it difficult to obtain the complete sentence, potentially resulting in translation errors or semantic errors. For example, in the following figure, when **Rain tomorrow** and **Bring an umbrella** are directly concatenated, a capitalization error will occur.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/rSwosQOwQG2hyJTgIrXFWA/en-us_image_0000002568764801.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061956Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AE0FF4B206E51BAF3C1DC744EB9818380C0E8E7B8C829F50AD81220805FA09D9)

#### Constraints

1.  Avoid using hard coding. Extract the strings to be translated into resource files, separate them from the code, and use dedicated APIs for loading. For details, see [Multilingual Resource Provisioning](../../multilingual-resource-provisioning/document.md).
    
2.  Do not directly concatenate strings. If variables (for example, **Video** and **Browser** in **Open Video** and **Open Browser**) are present, use placeholders as the substitute of variables to make the syntax complete.
    
    Example of a resource placeholder:
    
    {
      "name": "string1",
      "value": "Open %s"
    }
