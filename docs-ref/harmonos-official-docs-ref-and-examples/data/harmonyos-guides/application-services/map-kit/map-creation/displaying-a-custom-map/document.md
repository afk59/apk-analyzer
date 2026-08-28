# Displaying a Custom Map

#### Use Cases

This section describes how to add a custom-style map to your app.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/a6bXuaMHStehGLMm9dErtw/en-us_image_0000002514526452.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A44A3BC1F1B3DEAEDFD02B8B8BB46E4DBA61B3482ACAB307F8AFEE6583035E8E "Click to enlarge")

#### API Description

The map style customization function is mainly provided by [CustomMapStyleOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section13899143818719) and [setCustomMapStyle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section70103143520). For more information about the APIs, please refer to [setCustomMapStyle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section70103143520).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[CustomMapStyleOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section13899143818719)

 | 

Custom style parameters.

 |
| 

[setCustomMapStyle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section70103143520)(customMapStyleOptions: [mapCommon.CustomMapStyleOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section13899143818719)): Promise<void>

 | 

Sets the map style to a custom style.

 |

#### Development Procedure

Map Kit provides the following methods to customize map styles:

-   Specifying a style ID: Use [Petal Maps Studio](https://developer.petalmaps.com/console/studio/) to manage map styles, and specify a style ID to apply the corresponding style to your map. You can create new styles or import existing styles to [Petal Maps Studio](https://developer.petalmaps.com/console/studio/). Once a map style is released, it will be applied to all apps that use it.
-   Configuring style properties: Change the map style by passing customized JSON. For details about the JSON definition, please refer to [Style Reference](#section156991344101012).

## Specifying a Style ID

1.  Import required modules.
    
    import { MapComponent, mapCommon, map } from '@kit.MapKit';
    import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
    
2.  Create a style ID.
    
    1.  Sign in to [Petal Maps Studio](https://developer.petalmaps.com/console/studio/).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/UYhAULteQDKHcT4qtJebrA/en-us_image_0000002485000274.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B9C331DDDB6B11E995F1A0FC89D541CF55674CA5D508C495A5A1114A0B2F2FAE "Click to enlarge")
    
    2.  Click **Create map** to create a custom map style.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/5WbCO1KvQaam6sJVLECFEw/en-us_image_0000002485160182.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=85376139B0A220788C7EED21A4955A8AED3F5614E74783081AE6E3797B5B249B "Click to enlarge")
    
    3.  Click **Import** to import a JSON style file.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/DfC7KXr9Sqy8WphHL_4qGw/en-us_image_0000002485160334.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=22D835D2BEC30863049D64C12AC8306BCEC89CFD3731D4F7F44435E24155E4C1 "Click to enlarge")
    
    4.  Modify the style in the editor.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/MLrQ65EISkGdgO_X52afUQ/en-us_image_0000002517200219.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=21E8873AE33940D9B1976B769DFC370D72E3FFB6DC96A6DEFC0BA08D5474D9FB "Click to enlarge")
    
    5.  Click **SAVE** to generate a preview ID that can be used to test the style effect. The preview ID of a style will be regenerated when you edit the style. Click **PUBLISH** to generate a style ID, which is unique and never changes once the style is released.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/NsGiJYWUTbmBlw7iDnDB7g/en-us_image_0000002485160230.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=401AD3811890F5F223D39794FFE6AA5E77DEE0688D3F9C7CFCA5D7E68A0BF181 "Click to enlarge")
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/0n11FCJJT0aJwPbjUK7KIA/en-us_image_0000002517200129.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=50C1A4F36A7F6D5B2B525A273F9C06BF0DC3F467276A85F856B4F1F131E8B5DE "Click to enlarge")
        
3.  Map Kit provides two methods to specify style IDs.
    -   Specify a style ID after a map is created.
        
        @Entry
        @Component
        struct CustomMapStyleDemo {
          private TAG = "CustomMapStyleDemo";
          private mapOptions?: mapCommon.MapOptions;
          private mapController?: map.MapComponentController;
          private callback?: AsyncCallback<map.MapComponentController>;
        
          aboutToAppear(): void {
            // Map initialization parameters.
            this.mapOptions = {
              position: {
                target: {
                  latitude: 31.984410259206815,
                  longitude: 118.76625379397866
                },
                zoom: 15
              }
            };
            this.callback = async (err, mapController) => {
              if (!err) {
                this.mapController = mapController;
                // Style customization parameter. Replace **styleId** with your own style ID or preview ID. The style ID or preview ID can be created on [Petal Maps Studio](https://developer.petalmaps.com/console/studio/).
                let param: mapCommon.CustomMapStyleOptions = {
                   styleId: "XXX"
                };
                // Set a custom style. 
                await this.mapController.setCustomMapStyle(param).then(() => {
                  console.info(this.TAG + \`setCustomMapStyle OK\`);
                }).catch((error: BusinessError) => {
                  console.error(this.TAG + \`Failed in getting CustomMapStyle. Code: ${error.code}; message: ${error.message}\`);
                })
              } else {
                console.error(\`Failed to initialize the map. Code: ${err.code}; message: ${err.message}\`);
              }
            };
          }
        
          build() {
            Stack() {
              Column() {
                MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback });
              }.width('100%')
            }.height('100%')
          }
        }
        
    -   Set the style ID during map initialization.
        
        @Entry
        @Component
        struct CustomMapStyleDemo {
          private mapOptions?: mapCommon.MapOptions;
          private mapController?: map.MapComponentController;
          private callback?: AsyncCallback<map.MapComponentController>;
        
          aboutToAppear(): void {
            // Map initialization parameters.
            this.mapOptions = {
              position: {
                target: {
                  latitude: 31.984410259206815,
                  longitude: 118.76625379397866
                },
                zoom: 15
              },
              // Style customization parameter. Replace **styleId** with your own style ID or preview ID. The style ID or preview ID can be created on [Petal Maps Studio](https://developer.petalmaps.com/console/studio/).
              styleId: "XXX"
            };
            this.callback = async (err, mapController) => {
              if (!err) {
                this.mapController = mapController;
              } else {
                console.error(\`Failed to initialize the map. Code: ${err.code}; message: ${err.message}\`);
              }
            };
          }
        
          build() {
            Stack() {
              Column() {
                MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback });
              }.width('100%')
            }.height('100%')
          }
        }
        
        The following figure shows the effect after the style ID is set.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/A6zILJlTRmKHLATwjXajaw/en-us_image_0000002514366538.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5B1F293C7A1C4C164262814850BE5B452011E744B2FA669E97FB1A5931660728 "Click to enlarge")
        

## Configuring Style Properties

1.  Import required modules.
    
    import { MapComponent, mapCommon, map } from '@kit.MapKit';
    import { AsyncCallback } from '@kit.BasicServicesKit';
    
2.  Configure style properties.
    
    @Entry
    @Component
    struct CustomMapStyleDemo {
      private mapOptions?: mapCommon.MapOptions;
      private mapController?: map.MapComponentController;
      private callback?: AsyncCallback<map.MapComponentController>;
    
      aboutToAppear(): void {
        // Map initialization parameters.
        this.mapOptions = {
          position: {
            target: {
              latitude: 31.984410259206815,
              longitude: 118.76625379397866
            },
            zoom: 15
          }
        };
        this.callback = async (err, mapController) => {
          if (!err) {
            this.mapController = mapController;
            // Style customization parameters.
            let param: mapCommon.CustomMapStyleOptions = {
                   styleContent: \`\[{
                       "mapFeature": "landcover.natural",
                       "options": "geometry.fill",
                       "paint": {
                           "color": "#8FBC8F"
                       }},
                       {
                      "mapFeature": "water",
                      "options": "geometry.fill",
                      "paint": {
                          "color": "#4682B4"
                      }}\]\`
            };
            // Set a custom style. 
            await this.mapController.setCustomMapStyle(param);
          } else {
            console.error(\`Failed to initialize the map. Code: ${err.code}; message: ${err.message}\`);
          }
        };
      }
    
      build() {
        Stack() {
          Column() {
            MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback });
          }.width('100%')
        }.height('100%')
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/3fyTAQMEQsCRBHPHuu51Ew/en-us_image_0000002545846441.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0718D4E8C5C29848503DD28C6F0A67B63D305D5C6F09876ACCFDE42FA1CE43BC "Click to enlarge")
    

## Style Reference

The JSON file defines the map style using four elements:

-   **mapFeature**: map elements.
-   **options**: element options.
    -   **geometry.fill**: geometric filling.
    -   **geometry.stroke**: geometric stroke.
    -   **geometry.icon**: geometric icon.
    -   **labels.text.fill**: text filling.
    -   **labels.text.stroke**: text stroke.
-   **paint**: drawing attributes.
    -   **color**: color in hexadecimal format, for example, **#FFFF00**.
    -   **weight**: stroke width. The value is an integer ranging from 0 to 8. The default value is **0**. A value larger than 0 indicates a wider stroke.
    -   **saturation**: saturation. The value is an integer ranging from -100 to 100. The default value is **0**.
    -   **lightness**: brightness. The value is an integer ranging from -100 to 100. The default value is **0**.
    -   **icon-type**: icon type. Currently, the options include **night**, **simple**, and **standard**.
-   **visibility**: visibility. The default value is **true**.
    -   **true**: visible
    -   **false**: invisible

The following tables describe the map elements that can be modified.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/VL_oATurR86d8egIvQ59Ag/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A9FBD0C2854E1582523CE5F6A494D648C69C4DF66369CCCF4462C8A36006EA45)

-   The options for **icon-type** include **standard**, **night**, and **simple**.
-   You can set **saturation** and **lightness** in **color**.

1.  All
    
    The value **all** indicates a collection of all categories. The supported capability scope is the same as that in all other tables.
    
2.  Administrative
    
    | 
    Element Type
    
    Feature type
    
     | 
    
    Geometry
    
     | 
    
    Labels
    
     | 
    
    Icon
    
     |
    | :-- | :-- | :-- | :-- |
    | 
    
    Fill Color
    
    fill.
    
    color
    
     | 
    
    Filling Width
    
    fill.
    
    weight
    
     | 
    
    Stroke Color
    
    stroke.
    
    color
    
     | 
    
    Stroke Weight
    
    stroke.
    
    weight
    
     | 
    
    Fill Color
    
    fill.
    
    color
    
     | 
    
    Text Size
    
    fill.
    
    weight
    
     | 
    
    Stroke Color
    
    stroke.
    
    color
    
     | 
    
    Stroke Weight
    
    stroke.
    
    weight
    
     | 
    
    Icon Type
    
    icon-type
    
     |
    | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
    | 
    
    Capital
    
    Capital
    
     | 
    
    \-
    
     | 
    
    \-
    
     | 
    
    \-
    
     | 
    
    \-
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/8knrFlwQQ-uWg5626g1txg/en-us_image_0000002485160306.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=742436A32EF4571F7040B788BDB9FC67D2D84EAFDFA01E760FCD524F5597BFDD)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/xum_r1bdRY21OcBsFq2gWA/en-us_image_0000002517200193.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=22F405202D6C93F688FA28CE54F820D248D70F79B40F7C3F0CA4F1E9213CAC0E)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/u4leY2nWT-yGgp5hMBuiwQ/en-us_image_0000002485000194.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9D84EBE59F9FFC4F0ED759487B2DC9D724A2ABFE7AC4BB20E68AFB4B3C32F20D)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/j391RQnzRum2o3q5gF4LBg/en-us_image_0000002485000236.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=73C4EEC519D4DABAC61443ECDC3335D54D3C1024CE199462E18BF604835EED3C)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/ugfyMxv3Te-3LubDvewlUA/en-us_image_0000002485160300.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E75E7EDD5C96A8873CFE98EB6C28FC8AC97ADF9DF95D54125221ACDC943A1BD4)
    
     |
    | 
    
    Country
    
    Country
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/qHn0kql5SYCoX8wLfmxnPw/en-us_image_0000002485160214.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5EF7E5450C3EB7801F421A70F575C808186F88AE8D83E76914F2E694B879B507)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/XSGeBHSZSBKXAZIn2qVyMw/en-us_image_0000002517280213.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5DAD1485406A2BC35D78172D49D5EE9701FBA055ADC55AF05EA015AA2A76660F)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/KZK7SPjrQtyiwhvISRFDfA/en-us_image_0000002517280241.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=54C0AD1B51CEB19CCC690FE0A76B6C3C37720AE1A6DC95651C73AEFAD58E581D)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/Q3tBNU80T2KSsbRkOLQ19A/en-us_image_0000002485000272.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=92A1DB2430A4696B9651C78DF8D6CD5F7AEA597D1889A05EF8B07BE39491BB1B)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/FZewf6tqQdyEUldSlvObNg/en-us_image_0000002485000338.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0E14BAAB8ACF0481CD5D5CD9196208AB7217C4FA48E926F2A3CB2C097F85E3AB)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/FHY6S1wsTuqarn8Rryew8w/en-us_image_0000002517200135.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2C051D6619CAB4494F70BA9CA7610D4DE8AB93D329F43609E670F3C2FBC2DA1C)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/sVlRbwFsRrG-khMBWnLEOA/en-us_image_0000002485000204.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D7257FF2F360E00807A727D143AAF589F36F60392885D0E020945347E670E33C)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/CwHnFIlJQVWPC2Y33v3DFw/en-us_image_0000002517280197.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=18A0C5FE5CA469748E60D01BF557273BC7A33CEB1E1D505E9FECF391ED794D66)
    
     | 
    
    \-
    
     |
    | 
    
    District
    
    District/County
    
     | 
    
    \-
    
     | 
    
    \-
    
     | 
    
    \-
    
     | 
    
    \-
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/nY9IssXmSDO5GaxDwr8SsA/en-us_image_0000002485000362.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1AE624FAD9D5DE3E07111E6563EF988A5C469F5236952C78EB34046F9C73C1CB)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/zd9FnWWjTk-vmPorfPId-A/en-us_image_0000002485000234.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=66A7F97E2787AB2D22285C35CDFE781133B5BA163145A0DE0FE4206639E6BD2B)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/h4iaXJDsTnO5h7uTLXmSDQ/en-us_image_0000002517200305.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=063CE45FFFF9D9F88339CD2D294DDA9C93ADC6CA6183BAF4F2EBE9D9F9FF5741)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/cVk9AxEtSsOpptoMgIQAaw/en-us_image_0000002517280189.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=00D95B93CC877C0E3B4EC055B09242139969FF7894FBD75E7FB72C45F0437EA4)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/e2xUR80XSPGruotZz9WvWA/en-us_image_0000002517280167.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9CF067D35A51EC5B50046BA2C2E03214D902560624B6E2324B04CE66E9C08FD3)
    
     |
    | 
    
    Locality
    
    Rural Area and Town
    
     | 
    
    \-
    
     | 
    
    \-
    
     | 
    
    \-
    
     | 
    
    \-
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/tLG4jf0tT9erTmcC_G6jnw/en-us_image_0000002517280215.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EAE610B492CF16B37849CEC8FCC32C9BAA82E8F25193E095077F16033F257928)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/AestJVhQQDu9IOK3wyIhSQ/en-us_image_0000002517280095.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=95562B697C12CF34FF5E008EDBF336426A2CB104E2E6BE20846F965776235EC2)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/vHn5PvJyQwihdfLAva7UGg/en-us_image_0000002485160318.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0A24F3C0B66A506F728A02F934DB5807ABE314D11B1370CA90A3A6B7CE893623)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/qRF7bWfGTcGMohVAdmk9-Q/en-us_image_0000002485000266.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=72D6D4C9AAE2E42A857FE1403605D311A5FCB2888C1717D0CA9AD865C0CB403D)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/f04MkFjXR6eSooqR5_sqYg/en-us_image_0000002517280165.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=87A4F82232BAB57797229856EE60AF9B661CF9165F2C410EF9D0FA1A6348606D)
    
     |
    | 
    
    Major-city
    
    Level 1-4 City
    
     | 
    
    \-
    
     | 
    
    \-
    
     | 
    
    \-
    
     | 
    
    \-
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/zZPOuKnbQlW0TE3DuCJ4dg/en-us_image_0000002485000328.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=39511AF078C5E93D9D4D37E79011AB0424707070CE5E4C2D13997B46ADCF3D42)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/7GDHcPoFSEyqooZJM4qyfA/en-us_image_0000002485160202.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9324A177AC6D1C62D6C29895223A0DEFD35CA085E93C9B8F285853798EA1416E)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/8my_29o1REqDEa-K5Qke1A/en-us_image_0000002517200215.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F6130E520F07A28BFB1B9D8E69C33416C6F6D1E45ABF1C85664BAF39B5279AB9)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/GA3td9btTnydoBZrziJqzg/en-us_image_0000002485000202.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CAE903EE6F53CAFD0D373CAD57744F9BB7F25D42DA30073E4AA1211EB5397922)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/lAwER3M_RKi26-6FlfO0Hg/en-us_image_0000002517280303.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1E2A5CED6D010FFE324D44E42DEBE42A9B195827DE1EC2DE60A9740659EE048C)
    
     |
    | 
    
    Province
    
    Province
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/CqNt3CR8QhqFQEwNeyoa-A/en-us_image_0000002517200145.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AC4B86ACD76D7B3E4AB9D7DD7D9C1BBCB7BC9A279D93254D5B567166C733473C)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/MlYNqIU5TdioSL7nfbFhFA/en-us_image_0000002517280111.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B25736D6DAFF944A5AEA78CEF2513C26200875BC7FD30D0317CFC1EC1C5407B2)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/53P-H64AT4ODCV6gDs4KVg/en-us_image_0000002485000270.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C97ECEB13D61E14BDB01D00EA1B0D4DB2D9702CE57C84EB362B25BEC14CB2790)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/jlcPy3DeR8qa-vXQ--tMog/en-us_image_0000002517200119.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DC29165DEC6E8B0670D65CEAEE10BD2962CA8CE54002BB08484B54458422EC28)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/ZFdxZ18_RGilDQaOpdsxgw/en-us_image_0000002485000316.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2D2B486CFAFA89E43968FE110463E09FA7F1E762A53008599C8F486CD5B26EA9)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/4sj33QEiQ-2iwhnC_8pM7g/en-us_image_0000002485000276.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=05D2E37A0D1A397B2FBE3DFE5E46AD6E90D2A6EB3B35F3A5059D4A5BDE023EE0)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/eimzY5MsTliz34GzOTtoIg/en-us_image_0000002517280147.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D4FFBFA099B28B7D335F5410EE997C3B19157832108AA64BBB964F550D111025)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/dhhkExw5RjuW7v4HAKldZA/en-us_image_0000002517280187.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=259F5373E2598228C3F49F38F7438A23806B5D5470E5C0A5359F4C5A406DAF39)
    
     | 
    
    \-
    
     |
    
3.  Landcover
    
    | 
    Element Type
    
    Feature type
    
     | 
    
    Geometry
    
     | 
    
    Labels
    
     |
    | :-- | :-- | :-- |
    | 
    
    Fill Color
    
    fill.color
    
     | 
    
    Stroke Color
    
    stroke.color
    
     | 
    
    Fill Color
    
    fill.color
    
     | 
    
    Text Size
    
    fill.weight
    
     | 
    
    Stroke Color
    
    stroke.color
    
     | 
    
    Stroke Weight
    
    stroke.weight
    
     |
    | :-- | :-- | :-- | :-- | :-- | :-- |
    | 
    
    Attraction
    
    Playground, zoo, and botanical garden
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/Ez-XOi0gTGqoezRNnMg4Lg/en-us_image_0000002517280135.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=64D7446975084CABCA803459D3A5E5B614810674A7CA500475F7364CE9DEC227)
    
     | 
    
    \-
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/OS6pAic6R9OYQy8CY_njoA/en-us_image_0000002517200229.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E7A4FA0FB43561427AF2DFF6673A3ABD3542CA2C75FA3DF15C7A649E6DF4C094)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/wYtBgwv6SKi0fWVVifmwrA/en-us_image_0000002517280131.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B24E0A3D6BAD2C909B8935F277764DFDC1195FE4B3B8322F9B1AE1775CE4316D)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/0D7eHGGrR8CANJwEIeijbA/en-us_image_0000002485160262.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4E290695599295F54C1BB606D16E76CD123D6A262A115A2F133BA019122F4D31)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/3AXtDC7YTbq1t-hLdK9vxQ/en-us_image_0000002485160206.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=94F310EAFEB77F662D117DE5E901E7A5CB55BAE36A243B957B8F544772CF71EB)
    
     |
    | 
    
    Business
    
    Shopping center and business district
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/QIP52kFzRyyMtLpZCZUgdA/en-us_image_0000002517200161.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1C4E2ED49711BBA560127830EEC2BA27E634257F60E0FBBB4D749C3E599D1456)
    
     | 
    
    \-
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/Ws-IQuhGQCu-JPQr6oz8ng/en-us_image_0000002517200211.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BC8943FB567F35700A5DC5F995EB26CD6F6CD69F9DA2D0A6B8FCA310A6DD0AEC)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/EvpMIUdaQxKg8GJgw8X29Q/en-us_image_0000002485160144.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=918ED4D7B662EA921340DA2BF221B26248B50376763904A1A4284B568DDC32E1)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/z6iYPPteRZ-84-sRq51TpA/en-us_image_0000002517280211.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=502E97779914C6988E830932010E801540E2F3FD19F6A0FE1AC1E00CA33CF3B8)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/UTWMqZisR9WxgEEFcB7Ohw/en-us_image_0000002485000216.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0966D766F9264427D71CB1B89CD4D9AFA66DCF5030C5A8E41B8E2BD056209CF6)
    
     |
    | 
    
    College
    
    College
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/M4ghNBSjRoG1lqDQHrKsDA/en-us_image_0000002485160238.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5CCE1483ADC970C134AAEB8DE0330C9B67BC4EC52998A82AD38D9A7A77AC68C1)
    
     | 
    
    \-
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/6BcH7HGKT_6NaGupWAwVEw/en-us_image_0000002485160150.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0484C1A8AC29FF780AA104DA072A6AAD9E16EF0CB3B05F1DCA5332309D0636B8)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/PWLyjRowSHyHCm0P4vIXBA/en-us_image_0000002485000210.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BD6F400926CB9C1158F3047FD81A5F7500F48FAFCAD5FE39715A593AD7A27FD8)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/TzgrfB7iTSSRfPGCViIaDA/en-us_image_0000002517280137.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=119A1A4752C3F7CB76C796E988808AC66FBD03A4C85514E5D6D21B86CE1B6002)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/SFXjn_pzRCWvROu7WWX5Aw/en-us_image_0000002485160190.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3AD4A8D4809B1E5D41CEC0107FD1D5AE14F15B65E7857F9140E18B794F90F575)
    
     |
    | 
    
    Hospital
    
    Hospital
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/O-wPIf3dQqyC6GTj64_WIg/en-us_image_0000002517200175.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=495C121E611942435BA797D0E52715B19E3F1475831E5CDB2FC90FE20AC86873)
    
     | 
    
    \-
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/rFjDQrCjRV-hNAFBSGJliw/en-us_image_0000002485160220.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A2560146D88045C8BE60875E97BA99B8939EA55AE07BEE079B94095EC772E364)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/RdL6WVmeQSWmLl2KhQIwfg/en-us_image_0000002485000318.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=11DF13DA215DC9E003C36A9032D36368583BDA2470EB03FF8D666E164B2EEAFC)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/aZsjGZF2QbiCaneUgSlmpw/en-us_image_0000002517200183.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=904DD35E082203C625C54CA5382828EBC5AB1245EF52CC7DB6470D3CFEC3FC77)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/XIBHPsFtRX61s_pUJ-9WNA/en-us_image_0000002485160192.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=743F75949D51A34EE9049634692358AE6C6615E78A7FCE389AE82DB633BA4BDD)
    
     |
    | 
    
    Human-made
    
    Habitation area, community, industrial area, and prison
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/GDr5Sc5WQb6W8BrDNwfqWw/en-us_image_0000002485160196.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E3B9C6CB05A4757C43A5C9DBF87E0C7CA616CDE341A215636F155657062DB155)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/Zy-JcMwBR4iSpRMR1Gu8kg/en-us_image_0000002517200179.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=41D178D149BC7EB66DF426D325267BED75E77B0EB0194BF15A46007EB6C84CF4)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/BoDzxzAGS7KGmbKKmr7Jww/en-us_image_0000002485000342.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5EEDD18E2AE816B63F99479664CA834E590BBCA9BE52AFEEB72015E7FE70AB12)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/PE3saMcKSr-Urr1ZAE1Kfg/en-us_image_0000002517200141.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=059B5CEF5A39C94644146026A033C7FE9F67F9A491A90AE3E3A3D17CBD4F790B)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/XY2gOFw5T6OxXkF__Z9E4A/en-us_image_0000002517280153.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=76D20718BD1C630BB1546AD7074AE96397244FAB3E39CEF4A9BCF1A217D5D217)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/zSyEaJn5Sb6SBB9T4kh6tQ/en-us_image_0000002485160168.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2799EC71BE8DC2FF92E55301E6023B98EFA7988448BA1ECCA4784763B06B129A)
    
     |
    | 
    
    Human-made
    
    Building
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/eJFoqizkTd2wk7RZC5aoUA/en-us_image_0000002485000288.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DCCF56E34352108E70F72E55A103F660539947BE76B56912FA375A82798FA29E)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/PSnR5Lx6T9Wge4LS_wPHFA/en-us_image_0000002485160294.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=714F657991FFC2B18F47A352B1D014D1A7670EBFC672F771DB42B9BE2B9DA686)
    
     | 
    
    \-
    
     | 
    
    \-
    
     | 
    
    \-
    
     | 
    
    \-
    
     |
    | 
    
    Natural
    
    Land, island, beach, and glacier
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/UXsqZKlzSSOpG0B1PUb9jg/en-us_image_0000002485160218.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DC43B2C873D0F923318ED3483ACC8470D2EB09C8E9DEEF3B02A08BBC03D7D6CC)
    
     | 
    
    \-
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/opEqnZvJRsOtfSyrAHUCVA/en-us_image_0000002485000348.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7547AB73DBBFF316DD942B1E330F171D5E3DBDB9C6780AC2184FAB03FFDA9660)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/TeH3U2TPTSGrr_iXyVxD4g/en-us_image_0000002485000192.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8C54868A857F37D3DF6C72C700AA02DCF7F859ED2715BD3EB07A97D97D1A37C9)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/mRwfDRheQ-SOlDFGzGXKZA/en-us_image_0000002485160266.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=93459A4EEDFA963C1AEE89AD216132D930037220725F64617D68046934F11E35)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/NA2Gk4_bSh20ZwTFcIKQXg/en-us_image_0000002485160240.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3B4F7309E4E76AF487CC3D0142A9597AEBBFAF337F0C76904BC8083C11537CAD)
    
     |
    | 
    
    Parkland
    
    Forest, park, wasteland, and golf course
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/Vtj6__CjTOOZfmDLUt1Gog/en-us_image_0000002485160180.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E711D499E87BA6D7F4772664BD39A34406FB109435096F633EB22A1C4EEFD441)
    
     | 
    
    \-
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/Tv0xQiAlSymD2BJQd8bMpA/en-us_image_0000002517280155.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=062D2397CC9618E3DCB3E4C83CE717165FCF26F01E49692DE45193EDFE0650C7)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/Tre4xtJmSwGctVnawunI9Q/en-us_image_0000002517200317.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9E36ABE68086AD89B9FA51BCE34107F4F62092E231696AB941CAC4D312D53C3D)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/SqyldF8tS0CIeAes6L9mmw/en-us_image_0000002485160244.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8BB1952B2BEB02653A95B1B133B9CF73443405C4689BD0E8614C76E668107833)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/dvDU8V5hTxOT1sY-v0PNSw/en-us_image_0000002485160186.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6AB1A0F34029FF16041BB7490BCBA54E8352F884305C5E53986B12499249721C)
    
     |
    
4.  Poi
    
    | 
    Element Type
    
    Feature type
    
     | 
    
    Labels
    
     | 
    
    Icon
    
     |
    | :-- | :-- | :-- |
    | 
    
    Fill Color
    
    fill.color
    
     | 
    
    Text Size
    
    fill.weight
    
     | 
    
    Stroke Color
    
    stroke.color
    
     | 
    
    Stroke Weight
    
    stroke.weight
    
     | 
    
    Icon Type
    
    icon-type
    
     |
    | :-- | :-- | :-- | :-- | :-- |
    | 
    
    Airport
    
    Airport
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/ieRZ7awcQ7yd6VLVv_-NgA/en-us_image_0000002485160260.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D0A12932E86E3DDB514ECAACFDBB194AA584FD8ADD22D48E72042F47107DAF6A)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/OsjTm22KRyugL6IhSjky6A/en-us_image_0000002517200209.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D5A5A13EDF9E64E5F431B84A830690974FBF5501213156396CCF557B37DB675E)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/uNOk-FVjRSegGURIytbU-g/en-us_image_0000002485000298.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DD4AF71FCD88AC2E5D5CE142EDA1ADF1CFD6170E985B1D93B9564B3AC5D75546)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/-LoZvSZ7RUSrcs3fOlmwxQ/en-us_image_0000002517200191.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=18C7FA090B7E78C590D3E4F1E51CE3DF3B5C6E6191D68DA0877DEA576C5D505E)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/6NdEyXgsT9iXC3j3VfSPUQ/en-us_image_0000002517200163.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5C50FFDB5F0296E21299008AF7C41C6E15B73C53DFCA1FCEDBFFA43B23AE861C)
    
     |
    | 
    
    Automotive
    
    Auto repair, charging pile, and car washing
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/P9i7zPwJRqux3tgXXvT5Wg/en-us_image_0000002517280161.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=43A5AAE7AE39B0BCAFA64EDDEEA8E87EAEB42BB69F778C84959B31500B4DCF4B)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/FqEyyh1hRqi8K0XlcYgJQg/en-us_image_0000002517200181.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=009524CFB9B890C4C973C77BD6C3533627D97A7D75952E747A623D2397F6AF61)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/Lnq19x43S_KlGRQKKsW-JQ/en-us_image_0000002485000296.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=267AFEEFB57FBD26525524422EC591B3E650A7F79D8D19BC6E6C7B6395EE0512)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/zz5XXVLhTfqYq3DEDAdSCA/en-us_image_0000002485160292.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=22F7361AB6E920474E5106C0788087F1E59EBF7A68D7A2739EAF43A059B96CCC)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/P960p5MKRsKJ9IPKPz1gGQ/en-us_image_0000002485160276.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=41B57F36D0945A67DF8DB6B0D75C2639297CA1A1003362028DB079DE3E9BB557)
    
     |
    | 
    
    Beauty
    
    Beauty center
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/LrC3g8UPQQeW0P3csOuePg/en-us_image_0000002517200269.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=945A37832E037D0BC9A1CFC7EC279F8E4613CD43787272D06F87A696398054C9)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/-AGgcFCMQlSi7GlvVxBfYA/en-us_image_0000002517200203.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BA0784E373755477EC8979A56C8D0106E75973300D7238C9B9B9847543521775)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/CNby50CeQkGl2_hmJJzgnw/en-us_image_0000002517280191.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C11872622651537D9F06FF06382B60BEEBE21DC01BA9C833DF62546B3E87A431)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/nyBvFAnVTHGJ5reF_CQGnw/en-us_image_0000002517200213.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1EA242D8CC3683BE99CB556604A8ECFC44D7952D6A0D0A5913E0EAB7C04235D9)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/rf5h3L5ZSqeb6JOlurU9_w/en-us_image_0000002485000258.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BA3A63F810527E0275B36B4B4328A69123F7271EFD1C80D4E4649CFDAB044B4C)
    
     |
    | 
    
    Business
    
    Company and business building
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/YprnVUWKRpGqwJ3YshztYA/en-us_image_0000002517280157.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B18E8C70F835DF69CD9014A6BB270A01112A2A426C06C242E82963F1C91C3402)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/e0rmcBH_T9y_BrfgqcRVZA/en-us_image_0000002485000200.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3A161A0110FD83BB1409B4775D7729E55FA0FAE3D87FBF3CDC9A684B609FBFFB)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/uu5-P3AXScCn1aZMp6l1FA/en-us_image_0000002517200295.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A93D89CC176C64237F5CF37ACFA5A4ABFFB31814E0D3FBB52B1EFFB07A45CC79)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/UPpyWwBhRm2z2qHoPYE0NQ/en-us_image_0000002485000302.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6F15A4C3E309FE19972FFA4E081FD5AA093BD6E5E7631C60FA207DDA13B5B759)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/4Tfk72zdT5SEXJKAploG2g/en-us_image_0000002517200259.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EE98BFCB89D396113654FDCADB6210C99A3BAC024B998A1D97F39C21DF1A2290)
    
     |
    | 
    
    Eating&drinking
    
    Catering and fast food
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/gvg3DKikTZia-5lZUz_jCw/en-us_image_0000002517280247.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8AF3787BA2E3DF51FA78C449CEE88B9548C3ADF67CA83571B945161488BC7FC6)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/kst9_cd1QJCkmv7TXMpxgQ/en-us_image_0000002485000332.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B5B46D091C475CCD20A1FEC9B3907E3145BC2864C2396AC214DA9AFBB7985361)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/4OFKuwvKTRO1HGZzqYPq6g/en-us_image_0000002485000254.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=95586B1EF8AFC84A875E5C91A0DA15146C2C0910A0A82B34E2611FAA998127A5)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/6Ds5GnYKQo-WmpvHdhQTUg/en-us_image_0000002485000242.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B51C09E6618F0F61F0F1B55D05AD90A481D107EBABA8A463136AE560B0F2875F)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/z3pf2xwURQ2pfwTGKh2uhA/en-us_image_0000002485000228.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B13F226F8C5F39BB8D5A13652F73A35099ED7FA6070E33317659ECF6D4FA7C3B)
    
     |
    | 
    
    Health-care
    
    Hospital, clinic, and pharmacy
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/m7p75y-2TLWJE9bdmm9mGQ/en-us_image_0000002517280163.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DD92622E64D2DBF44C22855FD232F0C3F547B68F997047D70282443D5744DE04)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/aNf7cI35QsORo0kMh3rA5A/en-us_image_0000002485000224.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=479DC32834A0C899FE9B209F7D41CB98DE498A7C8876E9A01A632D3504FFF711)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/wmCzagyKSE-Ep7iudtFsrQ/en-us_image_0000002485000246.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DC82537270EAF46FA1806DC0EDE3D9DCD54A7DB031994F2DF09C131E7C8EE60C)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/PAe1YWHkS2yWanMPIt8Q4w/en-us_image_0000002485000252.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CEE8817E8820ABD8A1E9F226A9EE6B117BBCCF828FFECEE1B0972BB8B677D792)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/mbcDHgCOR9G1If_jmXZxig/en-us_image_0000002517200227.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=25D1F5CBFF33DE7CBC64C0123C7DA2D056F06B5F2057AF2246C41640A585AF35)
    
     |
    | 
    
    Leisure
    
    Recreation & Entertainment
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/ccaef_I7TEy_2vyGUf5gkw/en-us_image_0000002517280117.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B2E3D12EA0CF1D1EADC288C4B7A705FFCB96510CF76FE8B342C1ADF59EB97464)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/tXPD5oSXRBuinmz5eRkM6g/en-us_image_0000002517280101.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4B58E98C797489DA80DB41E5E11DE0A9474DDF2528A643019087E348ED804C11)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/hT0W0H4oT5GQdo-TAZ_p8Q/en-us_image_0000002517200197.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2190B702B453CBABE0AA12580024E5A44D45245BB10BB07DFC38AAF2DA8FF497)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/gIevVfnJSAudii5qNUO5Kg/en-us_image_0000002517280143.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=15756BFE989178557F7BDAB93542290EC1CC3F3413DAEB068D55A004EBF065D8)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/QgqekXvnT_WMmejVK6CqhQ/en-us_image_0000002517280221.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3D6FA95BD2609F3F1CBA689EE7EF7882216E4E52E8D6D31AFE4BE1528A31802D)
    
     |
    | 
    
    Lodging
    
    Hotel
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/nakwPNQ6Q1GpR916K8T5gw/en-us_image_0000002485160308.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4F26DAD4774D08F4081DDEE4FE0BD7EFE0F48C8CAB623C3EDCBAD358A3B02D75)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/RdqeJJrFQHuA9Dz5F0Emwg/en-us_image_0000002517280169.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B1A99EF0C7C0BDF6981EE2A2ABD265E1CB54F01B21E6C8F34D7843FA567ACD92)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/jXKMc1F1SQSbq_3jS-GTew/en-us_image_0000002485160282.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BE5E6B53336FE7024B47FC86A503917429E2A266EA7E1AE2CE941BD59FD287CA)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/zBxpWlhTQ7CzBh3Q6wpY9A/en-us_image_0000002517280193.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=880EE023140FF8EC0F547739E5DCBFB2D614442F43AEBAE2AF6B95FD9F8BDDB4)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/0_ddEvmqTsO_Mi_dpc5u-A/en-us_image_0000002485000244.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E4E3C53E2345AC495EE1B6B4441FE9EC56192D74951A99EE1EC0449DA4B5439B)
    
     |
    | 
    
    Miscellaneous
    
    Physical geography
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/EGUTBmPqRZWUsGep-3zK-A/en-us_image_0000002485160258.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3D905DF8676DDBB8BD3A4291D49D086EC9AA97A6B9AB291F786DC46A4D0F7756)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/BecBflAVRBmJR16NMFpqbA/en-us_image_0000002485160248.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=467F7A2E09CD2D7E5331164F45AC61684D9D0A31F11424965D0948533EB2F380)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/p-gIrZ8HS3aEiQj3m1Nm5A/en-us_image_0000002517280255.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=195A32614E27FAF88BC6704C02B5BC9E176384378B260FF5DB61733134C36B39)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/j6lmIZ1WT5KB-dwfpwu2mw/en-us_image_0000002485000322.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=645F9C2C0688B4492DCBFE2D13826F9A9761A232048401B398D373CC58212BAF)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/JxMKlDVCRma1bHp0_NKHmA/en-us_image_0000002517200177.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3E3F01FBD974653A9E4EA63F6C85A62E026F3E12A30A71C6422862014659F165)
    
     |
    | 
    
    Natural
    
    Mountain and forest
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/BpchodCvSfqT3LQXPJq4Tg/en-us_image_0000002485000300.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=008445AEB421F8AD7CB62979D86546381C33D0ED3F1C54D1AF5DF55B3D032C38)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/Wxk-9xwLSuuOryMQFrQVBg/en-us_image_0000002517200169.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6382CF281D2D0A4BBE9759FA2DA17CBED08279B8161E88E62E255F71B95330BC)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/vmXb4tQ7T32sD3O3M0CL1A/en-us_image_0000002517200095.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4321F7D0DD23440EB7F187A119FC1551441EEA2EDAACA64AA2102648BD65C443)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/-yYg-lhPToWlowYaV5TJ9A/en-us_image_0000002517280083.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6C7D2C8D5B51D12BF9E0CF3C405F8B218DC31CC9D3BA48C72733A8F924B4BA63)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/PbrRfr1_Rluah_bMa1dHJA/en-us_image_0000002517280227.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BACC44EBC935A0E70BF9BE8189256DEE825E4B8DF2B9D6116BE499053737C88E)
    
     |
    | 
    
    Public-service
    
    Hospital, clinic, and pharmacy
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/p7zHOIKpSZuPhr7PZwj09w/en-us_image_0000002485000340.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=14C45B9F915DAEF5F72CB0E2778DEBCF62E48E3E5A5CDDB8C95D7C745D05CFDE)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/_IdyAmgLTRKXf8l3gA_adg/en-us_image_0000002517280179.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=822E596D486FAB34013CD78A04BC4B45C4272803AE6CEB106E5022BC8450E061)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/1ABIULIqTeGeyK2VUnV_9g/en-us_image_0000002517200091.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2882416C8A26FB37D09B46A1E8E27A300FE6F0667C44DFBC6687ACE7ADC27BCD)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/ZVhrWKtXQMq2gFNVbrEihw/en-us_image_0000002517200171.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A20EB888E46143FED7AF54D63471EA175344B87ED0553C0B78CEDF440EBFE4F4)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/JtA-lNWVQKGWEcDhLqdW9g/en-us_image_0000002485000282.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=53F2E914064EEF7DE95E800B97EEC4840312B5708140C9902209915E3B336663)
    
     |
    | 
    
    Railway
    
    Railways
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/QR0g-LJwS7KPxBvvwGxylQ/en-us_image_0000002485160222.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C967ED1E1E5A68D37D42E81EB420895B7E734C96A9E5276EAA26DD0C89A83558)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/lnn2Unc4R12JnDemVPFgCA/en-us_image_0000002485000382.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A927DDFF722B4EF130002A47830A7859677A5EC4DA788CA08518C120020F9E95)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/05BstbPZR_W81cLAk0PfXQ/en-us_image_0000002517200103.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C474823A9560B98999E0196D6B5333B7718216F3E9A957418AEAABE8F7BB4736)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/He3HQdpNRLOL2bkV49an2g/en-us_image_0000002517200277.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7EC8001D1B85615C3406050EAA8C608A2289216301823DD78198A967C4D3FC9A)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/l_2s0otBTSyq1WjRbLG7SQ/en-us_image_0000002485000238.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7358E66CA6A43841BEE7A4A5560E5020132D82DEBE49E1BB96CE0A45571005FA)
    
     |
    | 
    
    Shopping
    
    Shopping center and market
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/fz_7A947TkefM6k-UAQIPw/en-us_image_0000002517280249.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8D29C9B601FD57237C73A5E4F70A21A1F6235F3E7827B75BE86F8EE1F651CD1D)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/Gd3uk7uMQNqkb1VuQT9j1Q/en-us_image_0000002485160208.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0996700C94DEE0F426A7F7BCF51C50FB183EC77A0C62A178DD334199D259D351)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/Qe2LRDiyRd6Lc6oD7w1dGA/en-us_image_0000002485000368.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DCF8EEC89A451C33C765DA457ADF0C2B7E5696D76B4CBFB215E4D20E2779E5BA)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/VHg_TsEBTa-ws0gcxEKNxQ/en-us_image_0000002517280209.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=879B01B906734EA3717A1B2422B550ED069E15B1D21145693A728E4A22128A4D)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/Jf4bEUvxQXSk7eUtNUAtsA/en-us_image_0000002485160158.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=90CEDE7F284BDA042AEEF17E03557EAAC52958766FC9BD95A61E7B4A2ECDFA49)
    
     |
    | 
    
    Sports-outdoor
    
    Outdoor sports, mountain climbing, and cycling
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/Bj0hfN7zTHeom3OjNAjtPg/en-us_image_0000002517200159.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F07BDFA3CBD440AB72EE6E7DC2971B0FBC6B8CEDE9F31F53971999B5B0EE645F)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/_QD61ZB2RCiA6A_idqKy5w/en-us_image_0000002485000286.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=87AE8510EB5B69336767BB3BD99C9B65A16B88E239265A61F44EFB63E9704C47)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/RAN_DuhRRPi0OWfFQyNaRg/en-us_image_0000002517280231.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=43E8E811D43A62221F0A71F49F68D40C11C4CAE43E5851D603CEBC5E88F6EFB8)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/mkefIip6RBS1GulOK7v72w/en-us_image_0000002517200241.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4CA01140A3E5FB242835F6213354552CBA7B53874E869982A2ED7738F14AE47D)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/F5-BnJiATJGTIYkzwJbs3w/en-us_image_0000002485160274.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9F506BA6D327BF26589BEEDD7307D07A4B6B4200B7E98F563A9520587DFBAE5A)
    
     |
    | 
    
    Tourism
    
    Tourist attraction, historical relic, and church
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/V_1hVYEdRdSLSGcCz0jp7w/en-us_image_0000002485000240.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1DE39AFA2D70F5F54C9992EDF4F3A8125A806EC366C654673E85BF058958738A)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/kp49GPaHTAuq0d6aNgbI2g/en-us_image_0000002485160226.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AD86BF7A06A130ED0A47C261D919917BC847E486C135662C8A427B45E117C0DE)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/BW19ZpJbT4ec7IKTzzKlYg/en-us_image_0000002485160224.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C0435ED90AD1FFF53D1C039155355D1F77F61DC79710AF99A66386F76B1F5EC7)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/AyUNItiZSjmBccSdf31Acg/en-us_image_0000002517200149.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C216F3E45B823F1F219481344AB53F502BAE810CCE4EDEAB0BA727E0523E9DAA)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/k3EhYU7oQCyENjJ6X_NsTw/en-us_image_0000002485000320.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0FC45D6F760041D7B1E4A37F10477627D020B6E39BE38C3DF2AEDD7106A84285)
    
     |
    
5.  Road
    
    | 
    Element Type
    
    Feature type
    
     | 
    
    Geometry
    
     | 
    
    Labels
    
     | 
    
    Icon
    
     |
    | :-- | :-- | :-- | :-- |
    | 
    
    Fill Color
    
    fill.
    
    color
    
     | 
    
    Filling Width
    
    fill.
    
    weight
    
     | 
    
    Stroke Color
    
    stroke.
    
    color
    
     | 
    
    Stroke Weight
    
    stroke.
    
    weight
    
     | 
    
    Fill Color
    
    fill.
    
    color
    
     | 
    
    Text Size
    
    fill.
    
    weight
    
     | 
    
    Stroke Color
    
    stroke.
    
    color
    
     | 
    
    Stroke Weight
    
    stroke.
    
    weight
    
     | 
    
    Icon Type
    
    icon-type
    
     |
    | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
    | 
    
    City-arterial
    
    Urban trunk road
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/EqRgZuV4RZKaC38eBeRy5w/en-us_image_0000002517280281.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5F3C4CBCD058745A310D6441C56BB6A0896F869BB7EA90F2953964B35236DA79)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/6I2UuHe0Sb2nD_VSP3Yiog/en-us_image_0000002517200097.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=493AAE2D4BA754F628494EFFC7D34E1B7393FCBDAB5A9C6AA0AADB6B3351984D)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/gsS7a-fjQ_mHkb4YGaaJwQ/en-us_image_0000002485000226.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D956D6A70DCD5C880F84F4C4565AD63AD65D2FB88560AF144F37FECE56E204FD)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/NDdMPF9MT5qX_aMxSWOhJg/en-us_image_0000002485000354.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=16AF89CADCAE6CF2AA891CA34C24B38FE1256ED99908F6A9ADACD78507254139)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/zIu3Hs-lQEiBLE11zRAx6Q/en-us_image_0000002517200201.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=87BB7E786A3DD8CAC246758F10E0530D647DFA64763C55E701F924A77C8390B5)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/8GqGwmb6RL2oPTPLg8Dkrw/en-us_image_0000002485160136.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=669D4D15882E8165DBDB030183911411ABBFCFD8505AEBE53D05EA04D2E21E30)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/2E67aJEwQkCOTnrRV4kZpw/en-us_image_0000002485000310.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=78CA1C1C77F0C1AEE799E118794A0DABE8866C86BBC1860944B7DEC6740E9191)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/-jNNXVF6R863RFFq8xVZUg/en-us_image_0000002517200225.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D7EE3A4BB198449BBF5D76B2790F28F7B1729540F93311BCD1B583DE999FB4AF)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/Eyo2IQYpQmy0PELeEIX9Lw/en-us_image_0000002517200165.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=31EE694292A21B5221103750D192BFD812409B4E1731E077EFE007E91BC08B21)
    
     |
    | 
    
    Highway
    
    Urban freeway
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/AURvBDHdRKOaR8TkSi0LQw/en-us_image_0000002485160344.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5A52A30F28E58089DE84CE90551688BE2DEEA4115E6EC5F368586395024A99D6)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/z2dFMDnzQq-9ZisR7nNxiw/en-us_image_0000002485000406.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=122A65CCCC4B7352EE6FC6DCF5D053AB68107A3D982F199CF71F1D8364EC9BD4)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/EIgOjkirT2qVvUjfXMJ2QQ/en-us_image_0000002485000292.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A71732DA1684EF7FA9FAAB720FF7731E5B4487D03720BF18C5814D5EC829388A)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/71BlOaLbS0q-qRGvEjSw6g/en-us_image_0000002517280245.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BB883213DC3207E3208CB3619EA0532AB56D6F7C379D1D4321A26815EA598D20)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/pbPJx32oRSKr6WdeFnd7lg/en-us_image_0000002485160188.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D0FB5C0506E1C024EDF6BAAA48A9E76C172608FDE547B7571B169E8775646AA3)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/kyplGh1aTvWB8YMSACN0qQ/en-us_image_0000002517200237.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9BA258431ED1565C753200503553AC267A212A78B806FE09827B8052C748FD2C)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/JbQFu5kfQ-GbKVTZKgy9oQ/en-us_image_0000002485160254.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8518FC6FADBC583850A2934FA0ADDE1A31C4DEE244EA7CDAAE4D645B384D59A8)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/uuqRM1y2Ra6hYiQLysf6AA/en-us_image_0000002517280223.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F189A88FF7391C55310E44B2F91245EACB0A401604A85E6D4134A7888F6CA216)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/2OgpGvoeQbOyZOinSPQHNQ/en-us_image_0000002485160234.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C43D97DAEC8C96D2E97DEAA41739373AABA3D26741C4C39EB548E7D1A7E59A9A)
    
     |
    | 
    
    Minor-road
    
    Urban branch road
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/enjpn4GvRhSjZ7T2R2TLUQ/en-us_image_0000002517280181.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4BB96F8A471624F181C96E1A3551E8D59055CD28438949885C9AF27D982777FC)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/hMWCbq6DQBSSL5z3BFFC8w/en-us_image_0000002485160250.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F9AEDE5B737A2A228AF8F13C6354F60DF7CC8BCF98C84A45805732E22CF155FE)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/OW0Wakm4QOeqMA-O2_sDuw/en-us_image_0000002517280123.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CD481872C788B987B75A977F8C3C880166556D38E4745D77198396E72C298F41)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/ur3FgXJLTQ2a1qPZ5A4eCw/en-us_image_0000002485000334.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=81DEA3130C034DA5EC21A43425D56D679528477EF1391C3FC6EC06D332B32019)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/j1q4k6Z8RsquOLJoL1AfYg/en-us_image_0000002485000260.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B7E40AC73D3AF35EADFC714E1921B17A4EB17FC85DFFD8D3E16DAF2529E42D48)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/qxDrb_77Q4myBl7OIC_H-Q/en-us_image_0000002517280141.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3A1C66BD31C42174FA2F320064A367F1985B20A2DC5F7D726A18A321D2D41720)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/muSxremKRkOyrH1yEdakVg/en-us_image_0000002485160354.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=234A55E287210B5C9CFB0313A569E5C09BED54890FD9570C749022CA06CFBB5D)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/b1xEhES_SgCkFPLk_1muYA/en-us_image_0000002517200207.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2BB3E68BA8E16BDB8C9DA224F4489D10CE5F250F0174E0ED959DC835B6029924)
    
     | 
    
    \-
    
     |
    | 
    
    National
    
    National road
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/6ubWR1GbQLOqYDXSedQk1w/en-us_image_0000002485160210.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9A52D2B8696B037F6BE103FCA338F28E0174702B7B26ACC377021DDD80E73DCB)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/BacsoYYHRYuwmdHGE2RX8g/en-us_image_0000002517200217.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D719927F207EEEC74AD4B9B8DD6464E84203C82BD43E08BD4567BC3B02031564)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/DfGOO-6sTUSqiL4ratZvIQ/en-us_image_0000002485160366.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ACED6049A8F37ABA9F675322BAF9DBB55693B77AF34E84243159DCC86DC140A0)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/Q4KTjwgOQEGf-YiycGktzw/en-us_image_0000002517280171.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B36FC9E8E93D5BD1322471472ED942C8D20E90B48EB0F1E6C074B0658D4C05CA)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/ZMh5ywbASvmzINtHtkPUdQ/en-us_image_0000002485160288.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=49FDEE2B1300721A9CB223B76FFC8720EF1740E930B1CF38C0E8A35C40E0F1E1)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/PgjQPGjRRq29psZjYh156g/en-us_image_0000002517200251.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=81282236BE57BB3767FD877FA261CB6409C0D0430741FF8F1D71C3A6C59E80AC)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/Ox63I9yxS4mOl2cv2ALuCw/en-us_image_0000002485000280.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=45720B96677ACFBC0543890A9EC290995583AF906BBAEABCC80999497C435DE4)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/eBqrvjEmQrSSMjony5FsqQ/en-us_image_0000002517200205.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5498E71ADDA770DC1FCECA8844D6EE5A2E237CB6F5445EAA05411B88F7C5C0CE)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/j1y-3Pr9TJuEPSUprwmMGQ/en-us_image_0000002517280217.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=48175ADEB981E22573CD669188420BE45253CAA10898DB4696C28CD1139EA1FF)
    
     |
    | 
    
    Province
    
    Provincial road
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/mdEWFAgYTzKYQLb0GchKnQ/en-us_image_0000002517200253.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C7ED9F41E26FE23421D4A6F9DB357A5A792B65A41C0F34CC82635E70831B4256)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/FAWMewZARPqyfE_9OYSk7A/en-us_image_0000002485000230.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=27233C89161754764D78B28D24D2F45A3C09386375FF9E7B6BD9505C7D70AB20)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/BXnT-lkOTqKOIZ3ctjcfPA/en-us_image_0000002517280273.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6BB2634D4D32E872133E2F5659790D3319AF78B65771F04A76023FE536F2FE9E)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/QyvD659LTYKpGHk40W2vyw/en-us_image_0000002517280149.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7B2D3DA8A1C35E14798BFF726F6A3D3BCE8636E184CDED43234DBDC46FC828BF)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/y1uciae2SHSV8g-92Kyw4A/en-us_image_0000002485000222.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B465BD75F09F5C7010AF83BFE4F85A9362B8594AB12759BBF47670EC00BC11D8)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/EeCcLFHmSNGFOFEhFyvXXA/en-us_image_0000002517200153.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B8CC16A912F287501DA3032AF42F5C05E3C89A1B225B56744FC0F4FB012C8461)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/D7g5CBJgTtGeu9ob9uMb1Q/en-us_image_0000002517200233.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BBB947DAD4EA265D17E18F3AA7B7EB28072E94C414847FA1D5A27DE309FD65A8)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/FwZdp8esSfar0UZ3POU_Kg/en-us_image_0000002517200099.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A83380F1A410AE0564A9F9E82D7DBB62A939DF51D2910BFBAB7DB83E7E720FC2)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/RV3uTPSbRdG8BE_8JTOHJA/en-us_image_0000002517200231.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2A6B9F76ED4F61F56C39E3A8B93FE48C3E067AAC0463F1CAF92313D19496525A)
    
     |
    | 
    
    Sidewalk
    
    Sidewalk
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/prKm1sPXSIulv8bCrBCe2A/en-us_image_0000002485160304.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1E4D4FDE7B748727DB73AB1E434A9DBF76756C63C35D481D1CE5FECD1E8D2461)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/TmkMxWEiTgGlcxHSHd4wwQ/en-us_image_0000002517280205.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EFC5F1A221DFA3B673841AF692576F180C7B8C0EB75311C2E97FDEA9BEF2364A)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/WvQQxOi6SCab_3RlxCTNpA/en-us_image_0000002485000304.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B3759500BDDC41CF03EADE31A920EEDCC5365438FEF2F621803F55087CFA09A5)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/-fJb0l3PRBq6SRzEaz3SfQ/en-us_image_0000002485000278.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0271A38108F83C583C41BA9A18FE5E88F0E7FEC445D4741C10E1935FFD211514)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/Rye8un6eSmuPCuVWZKXPFA/en-us_image_0000002485160302.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=662A58BD6A7B495F8740E759518974262052B9899AF012AEE9C1D0FB9B90E429)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/SgKxh0KZSmye2uUWemLTAA/en-us_image_0000002485160264.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0B775A7CF823709EB11DFAC478A64B8C738A67047C8E5588D73AE63E2D0A00F8)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/NxXctPkCT82ntFObe00qLA/en-us_image_0000002485160216.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5B76AC31763908A30DFCE4979C3259CE7C5EDCAB665C417F3293F4AEBAC0DAB4)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/oCz2LtCtReiuM7jFNll9tg/en-us_image_0000002517200263.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6E97B0FD3F0AC8BE5D9CCC7D9945E9CAADEE31EDB3D09CD747B2C6E5252994A7)
    
     | 
    
    \-
    
     |
    
6.  Trafficinfo
    
    | 
    Element Type
    
    Feature type
    
     | 
    
    Geometry
    
     | 
    
    Labels
    
     |
    | :-- | :-- | :-- |
    | 
    
    Fill Color
    
    fill.color
    
     | 
    
    Fill Color
    
    fill.color
    
     | 
    
    Text Size
    
    fill.weight
    
     |
    | :-- | :-- | :-- |
    | 
    
    Closed
    
    Road closure
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/iUYxdwQMTbW_7tbMgRN2hw/en-us_image_0000002485160290.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=45416F97364EC3E1DDDD0DF84F6E1004414717DF99EBECFB2BF289C075F83F06)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/OFx5urzcSTGOJeGsb6dVvA/en-us_image_0000002485160174.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=41863C226D0A533769C2B045D9A1146771EEC4DBF7EBC12838BE42FC2D42350F)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/5JUg3v95QAOP4b7mQwvnMg/en-us_image_0000002517280127.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6477E4D0F4624F444F76E5E66A2ABD9E276D5829E4D4DA5EFC69C5F6DE309BBC)
    
     |
    
7.  Transit
    
    | 
    Element Type
    
    Feature type
    
     | 
    
    Geometry
    
     | 
    
    Labels
    
     | 
    
    Icon
    
     |
    | :-- | :-- | :-- | :-- |
    | 
    
    Fill Color
    
    fill.
    
    color
    
     | 
    
    Filling Width
    
    fill.
    
    weight
    
     | 
    
    Stroke Color
    
    stroke.
    
    color
    
     | 
    
    Stroke Weight
    
    stroke.weight
    
     | 
    
    Fill Color
    
    fill.
    
    color
    
     | 
    
    Text Size
    
    fill.
    
    weight
    
     | 
    
    Stroke Color
    
    stroke.
    
    color
    
     | 
    
    Stroke Weight
    
    stroke.weight
    
     | 
    
    Icon Type
    
    icon-type
    
     |
    | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
    | 
    
    Airport
    
    Airport
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/hcIf53yESIavOpY1UUv10Q/en-us_image_0000002485160310.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2613AA12367D92F8EAB84BB2D16EED9D4D29431918961B3E072365B34329F1A3)
    
     | 
    
    \-
    
     | 
    
    \-
    
     | 
    
    \-
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/xVKdoj-aSWS2WFeBPaRLag/en-us_image_0000002517200239.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=87AC0F2170E3A984AE9D05A414AE2DED141142961048DB01EB6D327247A2ACFE)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/IexfrQWpSUKJfOR8D89Nlw/en-us_image_0000002485160256.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9094D66AB993B5504AEA8C52C03A25AD5B2B82D3D43801F155250935471ED697)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/4BUVcg-eQAWYyw-jjGTy2A/en-us_image_0000002485000290.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0076FF28B1F419D6A2F16B59A8FDA97BD22264F1A5A40EB47E74953889B71456)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/r3miDtVSTe68SKi2Fx-A-w/en-us_image_0000002485160278.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FF3ABD2A028D60630093AF997E0F53725F21EBCAA428E3E2D158B6ED4960974C)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/CNnGlELzTSib9zts4mq_hQ/en-us_image_0000002517200249.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=81974E236ACE37E4D29A3BD8B03897846E8FAAA2E436DCB8D0CF10CD91E83DF6)
    
     |
    | 
    
    Airport Runway
    
    Airport runway
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/Hn1YtOqTQ0WGOQSz3tIhqw/en-us_image_0000002517280145.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C151651A2A2EF6F65FD88CBDC466DC5620283A6C8459B513298FEB7C98FB1F02)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/7rNgFoA2TgSLN-Pn4Xxlaw/en-us_image_0000002485160246.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C0F3D0DCD01202A58EDBAD29B7517F5AC9D7E2B29EC69A0F9D32CF2A137D5F62)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/L-DXay7xQ5-Y7mqknuQB2g/en-us_image_0000002517200157.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=98D404D45A5231893FFACFB784B5BE67030EF9C79295FC0351048C8D7362C7FA)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/9-7ZiKbyRQajestWhkTxuA/en-us_image_0000002517280183.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=29BB883C27ED3E30F88566515120C07997E7C4FDFA2A3519A3F6968994C77219)
    
     | 
    
    \-
    
     | 
    
    \-
    
     | 
    
    \-
    
     | 
    
    \-
    
     | 
    
    \-
    
     |
    | 
    
    Airport Runway Taxiway
    
    Airport runway taxiway
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/FlBtMszRSPS744EvPFiWPQ/en-us_image_0000002485160228.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A0D4A272FF32F853FC678DACABBC9FDC08C98AF094F21834AECB8F0C04F13271)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/ZJcrozrrQXCdUnbLwEZ4lw/en-us_image_0000002517200151.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A0411944D2093C040338D3BE08E66116FA38327F9A3D8C28580C4CB6B1F3F7D4)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/nlpU7gtZTtyC-YKAxSqXXg/en-us_image_0000002517280233.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B166A6C0AA5447B6301445AE04AEC62C0581F9E011AD434460AA263D192F2486)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/rVF4yPaRS52hJqWMC6s94Q/en-us_image_0000002517200093.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E0E6A4C6009910D146A50CDF933F2012DA73E4A4798675A77502BAF848DA6688)
    
     | 
    
    \-
    
     | 
    
    \-
    
     | 
    
    \-
    
     | 
    
    \-
    
     | 
    
    \-
    
     |
    | 
    
    Bus
    
    Bus
    
     | 
    
    \-
    
     | 
    
    \-
    
     | 
    
    \-
    
     | 
    
    \-
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/F6BXAH7WSvmnlVxyhyvdHA/en-us_image_0000002517200199.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=175065B19855625CDC6D7432ED03D83316AD991445EA12F1121733DB1A29DCBD)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/unJPWxI5TmGA6rSxV-FQrA/en-us_image_0000002517280219.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=35E4CFEF63DF24533059CE745D1006F406700F39FF68E3D1F0301E01F2185F6A)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/Nmglnf7XTmO64vFtVEGLtg/en-us_image_0000002485160204.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=45D5D79397A77A5E3EA89B3255F33FB7FA748B62E72FC36967F8D543C6AF2621)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/aypjaL61Rsu5JVV1kUK6jA/en-us_image_0000002485160270.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6DED8B9D3EB82AFBFB1C586AB06F64377D4944E4BF9AC5309FB0472BCA144059)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/o_0-u-rwRGCCfqQRJQH1ww/en-us_image_0000002485000248.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=42E88E9923F1DB8A4418C3831804088F2DC39B8527D46252D4F992CCA8A08FC7)
    
     |
    | 
    
    Ferry-line
    
    Air route
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/xvqbReq_Q2aNIQWsOvZYRA/en-us_image_0000002485160184.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4FCD0E5B7FED020338FE6CC777D44DB307EC5F40896C137223038D94CE080F0D)
    
     | 
    
    \-
    
     | 
    
    \-
    
     | 
    
    \-
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/5EI2TO9rSx6KJiMZ5Ibipg/en-us_image_0000002485160280.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1A651FC22F96EC6AD0F6D49137FF45DEB416BB4105E8911FD8582C394E84DB18)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/LpkyyiBDRfq7Q6wQaW_aCg/en-us_image_0000002517280237.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=76FA3FAF654FD7DEB7743139689EBD92D9A4A722EC6BD90E9211B8230033BF9D)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/5GISLyjWTDOrqANOwMI8UA/en-us_image_0000002517200173.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=61FE289158F5A7200E0384584FB8B356A7536DD9C83770663883EBABC6E891F7)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/RlDOzr-VSGaVeJM1dCdvoQ/en-us_image_0000002517280265.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E4E5834DD8FBCC36554FCA73EDE71681E7B0FD4E1ADF7183C170A9F21A0167E9)
    
     | 
    
    \-
    
     |
    | 
    
    Ferry-terminal
    
    Port
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/4fpqMbPCS2SpFsNSjd8HyA/en-us_image_0000002517280201.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6D168D296DFA8CA6FF1D8348CCFBE8858C2DFA094DCF97D28B2D7F99B50FC22B)
    
     | 
    
    \-
    
     | 
    
    \-
    
     | 
    
    \-
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/gRd1ucVkQA6IH_5Hip1rww/en-us_image_0000002517200195.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1282418393BE5FE329AE5EF197D46A9CA28FFE0759DC69032B4A61EEF7D6208A)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/HjHc4RqjSlKrX-KbZm2BAQ/en-us_image_0000002517280173.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3EED26E714838BBAAAF6B4C2983235E9876B58D8EFC22E36434EFB763E676FA1)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/6vbeskOLQ-ic44EJC6E5kw/en-us_image_0000002485000264.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EE1F5EACCFACE6C701E190CAF857666846AE44EC40CD68D7CA0881EFA3B6599F)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/0lJlVe2SS7S7Q16XH3j3Uw/en-us_image_0000002517200101.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E6EC1115BAA3B69EA496ADAA697B15E777CA6B48C85B672158B692E1C9344C17)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/42fbSM_pRkyXoaeBBgu5KQ/en-us_image_0000002485160242.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=760147FBF9AA37F2D899C4BF6E23003D2F58FEFC687ACE2238FE076036821A13)
    
     |
    | 
    
    Other
    
    Taxi
    
    and entrance and exit
    
     | 
    
    \-
    
     | 
    
    \-
    
     | 
    
    \-
    
     | 
    
    \-
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/H9uVaka4Th2eiGBzAFy0rw/en-us_image_0000002485000294.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B680726A5B9600A5D262C290414981ADBBF0EB795B98CA1274ACE2C38DBB89DE)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/aCk7bsnGQlieSMwh6kdXPA/en-us_image_0000002517200223.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=690967A7E17D2174888C1A244537EA1E98B777840472E2CFA4C4CAB5518E71B2)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/s3Ml9wvIRg-TdrmQll_yqA/en-us_image_0000002517280291.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D493185437FC3DD3407CF05662C4284EE097F70D90444E20AD19706E953E8C32)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/pjXkbGZ0TKqSXDUxqS5hgA/en-us_image_0000002485000394.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F7C98A79A351207525815D6B4AA6046D4854B51CA5B5D4679FBF1DAA4AEFA083)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/ZaAPhXKjTJyvDZk6Ww6exQ/en-us_image_0000002485160252.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CB89EDF2F16787D2D45DF558F524AE248C03CD97A7DFB6F2E3E5B8DE5850713A)
    
     |
    | 
    
    Rail-station
    
    Railway station and
    
    high-speed railway station
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/qjuF-DtCQ4uL7nCIVMY5IQ/en-us_image_0000002517200221.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5A6EA1E715A6718D3E384CCC4FF9C743ECC267F63C38C917D47D15BFA493B16C)
    
     | 
    
    \-
    
     | 
    
    \-
    
     | 
    
    \-
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/Swo8YAdqTNOKXca1XAbxig/en-us_image_0000002517280159.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B457BB8A1F2065ED9DDF367ED7BC0E6EFCA297E31F6EEA2A9BDD2EB3FC751683)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/dWGOR-_uTpyeKPiGbNQt7Q/en-us_image_0000002517200105.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E25AE62F39584D9416E8231C76CC82EF2262A44BEE27D3906660798223578CC8)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/NzhoXLPSSmur9Ioz1g2eBQ/en-us_image_0000002517280199.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A8D11EBAFA4E3550EB9E758F4C4B5E9933382F1CB92DD87F36FE8308AF5D7FFB)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/Bbc-RRSbRAanvmuw0qLofQ/en-us_image_0000002517280207.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=767BFBE826F06E4407F5AAA05760565A325CBB7D4E398D2550BC7001CDA5A51A)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/fns-x4jNTj-VcPLpIgC22A/en-us_image_0000002517280195.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=74287C39725A5D3EE18C26E5DFB83EDE46A7126AC91A19FBEBC2084FF41E8413)
    
     |
    | 
    
    Railway
    
    Railway line and
    
    high-speed railway line
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/ug8YGtdaS3CwhJ8TCIzd0Q/en-us_image_0000002517280203.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B3578804A28E757D7A9950535EA06F3981B18126ED815E22826E8CD8496AFBC7)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/Cbj-779MQ6WuXYYcwwmbzQ/en-us_image_0000002517200285.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=84A8CE4A0D6D2268B82A2A13A91C957E8DCE797D20118ECE618B06F8986BBE21)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/cemEjwEhSOeW41b0I7oPHw/en-us_image_0000002485000314.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3A5043F1186EA1F2D891EA33995472D1C8A9EB31B5EEE4DF8BD138C1B2464ACD)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/A5EsZJLXQsa8_iYrpLO1ow/en-us_image_0000002517280239.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=68984A10EAF79E867D8ED76A572CC38148F91E078A23A3D4C9D8086CA5E858E7)
    
     | 
    
    \-
    
     | 
    
    \-
    
     | 
    
    \-
    
     | 
    
    \-
    
     | 
    
    \-
    
     |
    | 
    
    Subway
    
    Subway
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/yJpgI8XvQ8mKav0c5PAqBw/en-us_image_0000002517200187.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=49977A6C6216B2413ED5F413AB4345B370530C289C7AF91B8001E228C9F57993)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/9Yb8CihAR4y0prrY2Yhwfw/en-us_image_0000002517280185.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C616A91427C0F1220E71F2E1A68FAEF4D730071CBBC41A756E4D53CE02B9905F)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/xN7_rn52S_G9nMdaPov-yw/en-us_image_0000002485000284.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A78F8A47CDEEAED6BF98E00A23F953DFD15C53BCA69174424D88685801758F61)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/3XIPO1xOSwG16Goot-zuaw/en-us_image_0000002485000306.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=10334F12527994C29422A56CC707786E6F20994A17A3B30D6C2ECC2ECB6A3F9F)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/z6QxKk34T_uqnMgt8OwSmQ/en-us_image_0000002485160324.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F35C4B25DE222AAB22BEAE5A9733CB220C21E32BF2172D546D09B20BD7916BD7)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/Zr006GBSRSS-i0GDcIYERA/en-us_image_0000002485160268.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F1A9B0FDC2025CE30942ADC45127C4804B2103A3F23AA51C52D760B9FE728B7B)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/2fpj-uUgR_a5uJnuWg_1Yw/en-us_image_0000002485160198.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D1295FA302A726347AE277F197472B90EB1286F1A45DE23CAA313F3C358D85A1)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/-zX5Gl-5T4ao30gL1xc9sA/en-us_image_0000002517200185.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2A50BEB3C568780642D0F2C9BFC2625F530FD17A54727CC425DA9BF2102248C5)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/AflZDU-dRPyZUJzXPeF8XA/en-us_image_0000002485000256.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BC3F2B01C59DABC4198FB449FD7A553F4B1D49145FEB3E9E5AED07FA66B14D79)
    
     |
    | 
    
    Traffic\_light
    
    Traffic light
    
     | 
    
    \-
    
     | 
    
    \-
    
     | 
    
    \-
    
     | 
    
    \-
    
     | 
    
    \-
    
     | 
    
    \-
    
     | 
    
    \-
    
     | 
    
    \-
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/9BFEfqDJQ168fNqgEYyAEA/en-us_image_0000002517200109.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8D4351E0578F53AAE3957211D9AAD1010A5ABCC745765B8D122F028AD0608D79)
    
     |
    
8.  Water
    
    | 
    Element Type
    
    Feature type
    
     | 
    
    Geometry
    
     | 
    
    Labels
    
     |
    | :-- | :-- | :-- |
    | 
    
    Fill Color
    
    fill.color
    
     | 
    
    Fill Color
    
    fill.color
    
     | 
    
    Text Size
    
    fill.weight
    
     |
    | :-- | :-- | :-- |
    | 
    
    Ocean
    
    Water system, ocean, lake, and river
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/A2iz-wnOQ2q8UiMoEkU0vA/en-us_image_0000002517280129.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E68FC36C91AAF6D5E5790F7889C492B7ACD07E1A1BDE253EF8F729DC375DAF95)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/WnAUemeQRy2JiNPT2Qq-Vg/en-us_image_0000002517200243.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=24DE25BCF528138092A4D16BE1FA425F402F596ECE9EABB90692FF42AE098E9F)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/qkzd-FYUQy-FxCGQ7lHvjA/en-us_image_0000002517200167.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EFF2688628E90E823F88926DE3041019FDC9E5BAA82D478C076B12BDE5A10FD1)
    
     |
