# Registering Resources

#### Use Case

The function of registering resources is available since version 5.1.1(19)).

Resources can be registered to facilitate rapid, app-specific [symbol icon](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ui-design-symbolregister) customization, without relying on symbol icon resources preset in the system.

#### Constraints

The resource registration function supports phones, tablets, PCs/2-in-1 devices, and (since 5.1.1(19)) TVs.

#### Development Procedure

1.  Place the symbol icon resource (TTF file) and animation parameter resource (JSON file) developed by your UX designer under **entry/src/main/resources/rawfile**. You can also place the files in a new directory under this path.
    
    For details, please refer to the [symbol resource design specifications](https://developer.huawei.com/consumer/en/doc/design-guides/system-icons-0000001929854962).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/cMf4wccaQ6muV6jWA7_bzw/en-us_image_0000002532144131.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061957Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3ECF02DC56FFEE5E1E227541FD569C4C54A666D401B911DF9C9057B909B3E66A "Click to enlarge")
    
2.  To support multilingual scenarios, configure the Unicode value for a symbol icon in the **string.json** file within the specific language subdirectory under the **entry/src/main/resources** directory.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/UqEfNMTDQ36Z05DqZyaGqg/en-us_image_0000002500424060.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061957Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=87466520C9B6B08419C77F19D8018F0BE760A5479BBD841B00227F109DBC1C23)
    
    {
      "string": \[
        {
          "name": "symbol\_custom\_phone\_fill\_1",
          "value": "0x100016"
        }
      \]
    }
    
3.  Import required modules.
    
    import { symbolRegister } from '@kit.UIDesignKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
4.  Register and load the symbol icon and animation parameter resources before displaying the custom symbol icon using **SymbolGlyph/SymbolSpan**.
    
    try {
      let result = symbolRegister.registerSymbol($rawfile("symbol/symbol\_register.ttf"), $rawfile("symbol/symbol\_register.json"));
    } catch (error) {
      let err = error as BusinessError;
      console.error("errCode: " + err.code)
      console.error("error: " + err.message);
    }
    
5.  Display the symbol icon on the target page using the **SymbolGlyph/SymbolSpan** component.
    
    struct test {
      build() {
        Column(){
          SymbolGlyph($r('app.string.symbol\_custom\_phone\_fill\_1'))
        }
      }
    }
    

#### Development Example

import { symbolRegister } from '@kit.UIDesignKit';
import { BusinessError } from '@ohos.base';

@Entry
@Component
struct test {
  aboutToAppear(): void {
    try {
      let result = symbolRegister.registerSymbol($rawfile("symbol/symbol\_register.ttf"), $rawfile("symbol/symbol\_register.json"));
    } catch (error) {
      let err = error as BusinessError;
      console.error("errCode: " + err.code)
      console.error("error: " + err.message);
    }
  }
  build() {
    Column(){
      SymbolGlyph($r('app.string.symbol\_custom\_phone\_fill\_1'))
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/lc7qhf_UQPO8Db7-XYYsvA/en-us_image_0000002500304210.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061957Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3221491CDC573197975A2ACF48C81D6F8CA8D1CB3867BA532683625A0B4B2173)
