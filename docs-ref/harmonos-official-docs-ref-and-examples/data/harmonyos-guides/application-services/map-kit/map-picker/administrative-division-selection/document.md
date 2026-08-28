# Administrative Division Selection

#### Use Cases

This section describes how to integrate the division selection control. This control does not apply to smart watches.

This control can load the administrative division information of the world or a specified country or region and display the information in a tree structure. The following functions are supported:

-   View the lower-level divisions of an administrative division.
-   Recommend popular administrative divisions.
-   Launch the administrative division selection control in a subwindow, suitable for wide-screen devices.

<table style="border-style: none;"><tbody><tr><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><div class="fignone"><span class="figcap"><b>Figure 1 </b>Selecting the country</span><br><span><img height="701.6964290000001" originheight="657" originwidth="297" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/EwxE6zRNSVCS__LDyhgclA/en-us_image_0000002554718681.png?HW-CC-KV=V1&amp;amp;HW-CC-Date=20260410T062113Z&amp;amp;HW-CC-Expire=86400&amp;amp;HW-CC-Sign=1E7106C81782AD9AE47AF747169BABEFE51782B2CF0642F41CE4100156B2189E" title="Click to enlarge" width="317.20500000000004"></span></div></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><div class="fignone"><span class="figcap"><b>Figure 2 </b>Selecting the province and city</span><p><span><img height="706.1093690000001" originheight="657" originwidth="297" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/QtaDU7jNRjqk6lXgZhk7pQ/en-us_image_0000002523798784.png?HW-CC-KV=V1&amp;amp;HW-CC-Date=20260410T062113Z&amp;amp;HW-CC-Expire=86400&amp;amp;HW-CC-Sign=966F238AAE7787678F436BCDA336514733503EB44004945B4424451D50C3FA23" title="Click to enlarge" width="319.20000000000005"></span></p></div></td></tr><tr><td class="cellrowborder" style="border: none;" valign="top" width="50%"><div class="fignone"><span class="figcap"><b>Figure 3 </b>Launching the administrative division selection control in a subwindow</span></div><p><span><img height="711.8160000000001" originheight="944" originwidth="590" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/JrP5v339SMuzu9tbYXR1fA/en-us_image_0000002554838713.png?HW-CC-KV=V1&amp;amp;HW-CC-Date=20260410T062113Z&amp;amp;HW-CC-Expire=86400&amp;amp;HW-CC-Sign=C7C277B6D6C65E62836803F38692B4ED36D340D1E690D585D486B8143A15D82D" title="Click to enlarge" width="444.88500000000005"></span></p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%">&nbsp;&nbsp;</td></tr></tbody></table>

#### Constraints

To use this function, the following condition must be met:

-   The device must be a mobile phone, tablet, or 2-in-1 device.

#### API Description

Functions of this control are mainly provided by the [selectDistrict](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-scenemap#section1567213912302) method in the [sceneMap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-scenemap) namespace. For more information about the APIs, please refer to [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-scenemap).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[DistrictSelectOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-scenemap#section17211958161110)

 | 

Initial options on the division selection page.

 |
| 

[selectDistrict](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-scenemap#section1567213912302)(context: [common.Context](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-context), options: [DistrictSelectOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-scenemap#section17211958161110)): Promise<[DistrictSelectResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-scenemap#section3745121172118)\>

 | 

Displays the division selection page.

 |
| 

[DistrictSelectResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-scenemap#section3745121172118)

 | 

Division selection result.

 |

#### Development Procedure

1.  Import required modules.
    
    import { sceneMap } from '@kit.MapKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Create request parameters for division selection and call the [selectDistrict](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-scenemap#section1567213912302) method to display the division selection page.
    
    let districtSelectOptions: sceneMap.DistrictSelectOptions = {
      countryCode: "CN",
      // Enable page displaying in a subwindow.
      subWindowEnabled: true
    };
    // Display the division selection page.
    sceneMap.selectDistrict(this.getUIContext().getHostContext(), districtSelectOptions).then((data) => {
      console.info("SelectDistrict", "Succeeded in selecting district.");
    }).catch((err: BusinessError) => {
      console.error("SelectDistrict", \`Failed to select district, code: ${err.code}, message: ${err.message}\`);
    });
