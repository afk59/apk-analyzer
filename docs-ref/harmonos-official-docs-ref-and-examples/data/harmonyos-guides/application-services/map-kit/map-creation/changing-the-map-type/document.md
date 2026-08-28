# Changing the Map Type

#### Use Cases

Starting from 6.0.0(20), the satellite map and hybrid map are supported.

Map Kit supports the following types of maps:

-   **STANDARD**: standard map, which shows roads, artificial structures, and natural features such as rivers.
-   **NONE**: empty map without any data.
-   **TERRAIN**: topographic map, which is a standard map that provides a clear and complete depiction of terrain features, while still retaining other map elements such as administrative boundaries, POIs, and building footprints.
-   **SATELLITE**: satellite map, which shows satellite imagery. It is available only in China.
-   **HYBRID**: hybrid map, which displays both satellite imagery and road network information.

<table style="border-style: none;"><tbody><tr><td class="nocellnorowborder" style="border: none;" valign="top" width="50.71%"><div class="fignone"><span class="figcap"><b>Figure 1 </b>Standard map</span></div><p><span><img height="809.20392" originheight="2688" originwidth="1216" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/zTWTBjG1QQyUSzKeNzekNQ/en-us_image_0000002545789979.jpg?HW-CC-KV=V1&amp;amp;HW-CC-Date=20260410T062111Z&amp;amp;HW-CC-Expire=86400&amp;amp;HW-CC-Sign=273EEF149D103FEA04CD7769ABCB83145B1584FFCF0A05A40F2D12F8062AE89D" title="Click to enlarge" width="366.08250000000004"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="49.29%"><div class="fignone"><span class="figcap"><b>Figure 2 </b>Empty map</span></div><p><span><img height="804.812925" originheight="2688" originwidth="1216" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/Z7zdE9ilRsyAU9QRCysFtw/en-us_image_0000002545792793.jpg?HW-CC-KV=V1&amp;amp;HW-CC-Date=20260410T062111Z&amp;amp;HW-CC-Expire=86400&amp;amp;HW-CC-Sign=4CB8A8A8746EE84B0B645631EDA045DC802DBC2525551C5404EE82E1EA875D20" title="Click to enlarge" width="364.08750000000003"></span></p></td></tr><tr><td class="nocellnorowborder" style="border: none;" valign="top" width="50.71%"><div class="fignone"><span class="figcap"><b>Figure 3 </b>Terrain map</span></div><p><span><img height="804.81492" originheight="2688" originwidth="1216" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/pkwrkFe7R-eahPYLc4vZKg/en-us_image_0000002545794765.jpg?HW-CC-KV=V1&amp;amp;HW-CC-Date=20260410T062111Z&amp;amp;HW-CC-Expire=86400&amp;amp;HW-CC-Sign=0A62EE226A7D530108E7872265B4C9811BD8D238064C0DF06A51725491B79F69" title="Click to enlarge" width="364.08750000000003"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="49.29%"><div class="fignone"><span class="figcap"><b>Figure 4 </b>Satellite map</span></div><p><span><img height="798.1955100000001" originheight="2688" originwidth="1216" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/k1sBvLS-RvKUUBQwFBRo4g/en-us_image_0000002514157556.jpg?HW-CC-KV=V1&amp;amp;HW-CC-Date=20260410T062111Z&amp;amp;HW-CC-Expire=86400&amp;amp;HW-CC-Sign=AC92ED7BE7357BC248C8FD891567AA382678757CBFE43C5279785D8E0DEC2A6F" title="Click to enlarge" width="361.095"></span></p></td></tr><tr><td class="row-nocellborder" style="border: none;" valign="top" width="50.71%"><div class="fignone"><span class="figcap"><b>Figure 5 </b>Hybrid map</span></div><p><span><img height="802.379956" originheight="2688" originwidth="1216" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/Qp0HWAk7Qw6DQyS-OocIfQ/en-us_image_0000002514319040.jpg?HW-CC-KV=V1&amp;amp;HW-CC-Date=20260410T062111Z&amp;amp;HW-CC-Expire=86400&amp;amp;HW-CC-Sign=9FA784FA4384962F0BC6B064CF2687675CAF9B8F8D21CC39E8B9A50B43B210F5" title="Click to enlarge" width="362.97030000000007"></span></p></td><td class="cellrowborder" style="border: none;" valign="top" width="49.29%">&nbsp;&nbsp;</td></tr></tbody></table>

#### API Description

Map Kit provides two methods to set the map type:

Method 1: During initialization, set **mapType** in [MapOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section816451553012) to determine the map type to display.

| 
Attribute

 | 

Description

 |
| :-- | :-- |
| 

mapCommon.MapOptions.mapType

 | 

Map type in the map initialization parameters.

 |

Method 2: After a map is created, dynamically set the map type by using the [setMapType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section388992522618) method.

| 
Method

 | 

Description

 |
| :-- | :-- |
| 

[setMapType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section388992522618)(mapType: [mapCommon.MapType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#en-us_topic_0000001245084266_section18522846142615)): void

 | 

Sets the map type.

 |

#### Development Procedure

1.  Import required modules.
    
    import { mapCommon } from '@kit.MapKit';
    
2.  Set the map type.
    
    Method 1:
    
    During map initialization, add the **mapType** attribute with value [mapCommon.MapType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#en-us_topic_0000001245084266_section18522846142615).STANDARD to the **mapOptions** parameter.
    
    this.mapOptions = {
      position: {
        target: {
          latitude: 31.984410259206815,
          longitude: 118.76625379397866
        },
        zoom: 15
      },
      mapType: mapCommon.MapType.STANDARD
    };
    
    The following figure illustrates the effects.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/4T9z0JgKQbmfn3RgRqhIog/en-us_image_0000002545807049.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062111Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A9831DA858AD5CB61FC61998DFAF943E696D3939020F2AF2C73D62022AEA0899 "Click to enlarge")
    
    Method 2: After a map is created, call the [setMapType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section388992522618) method to set the map type to terrain map. The terrain effect is only visible at a zoom level greater than 5 and less than 14.
    
    this.mapController.setMapType(mapCommon.MapType.TERRAIN);
    
    The following figure illustrates the effects.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/5z9y22YEQICKTWdqB1hZEA/en-us_image_0000002514329342.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062111Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C224DFE3E67735B3E93D6EFB506291408B30A16B683C427F5511E7693B3D7B24 "Click to enlarge")
