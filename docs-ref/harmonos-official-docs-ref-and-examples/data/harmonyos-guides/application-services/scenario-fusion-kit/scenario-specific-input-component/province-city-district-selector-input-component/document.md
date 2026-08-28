# Province/City/District Selector Input Component

#### Use Case

The province/city/district selector input component is supported since version 5.1.0(18).

You can call the FunctionalInput component to use the province/city/district selector input function so your app can quickly display a region selection page for users to select a region.

Run the sample code, and tap the **Region** input box. The **Select region** page is displayed for you. After you select a region, the selected information will be filled in the input box.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/yLCdDfJJRGajPTK2oZlCwg/en-us_image_0000002503572051.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062119Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A69D95C736D388A47F70BEBA0B6BE3C04DD1A96B3C4D6E99299AFD8BB22F7ED1 "Click to enlarge")

#### Prerequisites

For details, please refer to [Preparations](../../../map-kit/preparations/document.md).

#### Development Procedure

1.  Import the Scenario Fusion Kit module and related common modules.
    
    import { FunctionalInput, functionalInputComponentManager } from '@kit.ScenarioFusionKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { SymbolGlyphModifier, TextInputModifier } from '@kit.ArkUI';
    
2.  Declare FunctionalInput in the container, set **inputType** for the FunctionalInput component, and configure the callback.
    
    @Entry
    @Component
    struct Index {
      @State inputContent: string = '';
    
      build() {
        Column() {
          Row() {
            Text('Region').width(64)
            // Declare FunctionalInput.
            FunctionalInput({
              params: {
                // **InputType.SELECT\_DISTRICT** indicates the province/city/district selector input type.
                inputType: functionalInputComponentManager.InputType.SELECT\_DISTRICT,
                textInputValue: {
                  text: this.inputContent,
                  placeholder: 'Province, city, district, street',
                },
                // Adjust the TextInput style.
                inputAttributeModifier: new TextInputModifier()
                  .fontColor($r('sys.color.ohos\_id\_color\_badge\_red'))
                  .onChange((value) => {
                    if (value !== this.inputContent) {
                      this.inputContent = value;
                    }
                  }),
                // Place the icon at the end.
                icon: $r('sys.symbol.xmark'),
                // Set the event and style of the icon.
                iconSymbolModifier: new SymbolGlyphModifier()
                  .onClick(() => {
                    this.inputContent = '';
                  })
                  .fontSize(32),
              },
              // When **InputType** is set to **SELECT\_DISTRICT**, the callback must be **onSelectDistrict**.
              controller: new functionalInputComponentManager.FunctionalInputController().onSelectDistrict((err,
                data: functionalInputComponentManager.DistrictSelectResult) => {
                if (err) {
                  // Error processing.
                  hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
                  return;
                }
                // Success processing.
                hilog.info(0x0000, "testTag", "succeeded in selecting district");
                // Display the selected region information in the input component.
                this.inputContent = data.inputContent;
              })
            })
              .layoutWeight(1)
          }.height('100%')
        }.width('100%')
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/Y6igZB-lT12zOUDiA1V3pw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062119Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A3D6CED49769FBC34AF8D0400191FFBAC78E1BE91CCBAAFAC303B5DE6DE18958)
    
    -   Set **inputType** to **functionalInputComponentManager.InputType.SELECT\_DISTRICT** to specify the purpose of the input component as a province/city/district selector.
    -   Set **controller** to **new functionalInputComponentManager.FunctionalInputController().onSelectDistrict**.
    -   You can process the returned result and fill it back to the input component by yourself.
    -   The input component supports two types of icons: symbol and image. If the icon is of the symbol type, call [iconSymbolModifier](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scenario-fusion-functionalinputcomponentmanager#section19784874147) to set the icon event and style. If the icon is of the image type, call [iconImgModifier](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scenario-fusion-functionalinputcomponentmanager#section19784874147) to set the icon event and style.
    -   The functionalInput component supports [SmartFill](../../smartfill/document.md), in which case, [ContentType](../../smartfill/contenttype-scenarios/document.md) is set to **ADDRESS\_CITY\_AND\_STATE**.
    
    For details about other parameters, please refer to [FunctionalInput (Input Component)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scenario-fusion-functionalinput).
