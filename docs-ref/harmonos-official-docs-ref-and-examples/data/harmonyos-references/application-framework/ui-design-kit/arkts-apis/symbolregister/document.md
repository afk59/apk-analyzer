# symbolRegister

This module provides the capability of registering and loading custom symbol icon and animation parameter resources.

**Start version**: 5.1.1(19)

#### Module Import

import { symbolRegister } from '@kit.UIDesignKit';

#### symbolRegister.registerSymbol

registerSymbol(ttfSrc: resourceManager.Resource, jsonSrc: resourceManager.Resource): boolean

Registers custom symbol resources.

**System capability**: SystemCapability.UIDesign.Core

**Start version**: 5.1.1(19)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

ttfSrc

 | 

[resourceManager.Resource](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resource)

 | 

Yes

 | 

Custom symbol icon resource.

 |
| 

jsonSrc

 | 

[resourceManager.Resource](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resource)

 | 

Yes

 | 

Custom symbol animation parameter resource.

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

boolean

 | 

Registration result. The options are **true** (successful) and **false** (failed).

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

801

 | 

Device Type error.

 |
| 

1012600002

 | 

TTF or JSON resource out of size.

 |
| 

1012600003

 | 

TTF or JSON resource content error.

 |

**Example**:

import { symbolRegister } from '@kit.UIDesignKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct test {
  aboutToAppear(): void {
    try {
      // Register custom symbol resources and configure the icon resources in the **resource/rawfile** directory.
      let result = symbolRegister.registerSymbol($rawfile("symbol/symbol\_register.ttf"), $rawfile("symbol/symbol\_register.json"));
    } catch (error) {
      let err = error as BusinessError;
      console.error("errCode:" + err.code)
      console.error("error " + err.message);
    }
  }
  build() {
    Column(){
      SymbolGlyph($r('app.string.symbol\_custom\_phone\_fill\_1'))
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/UXAlq5lqT02JMw1dObMezg/en-us_image_0000002500424078.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062328Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AC4F3CA2BDC5E6E99FD4D51AF48E2B2A43B4A5F70C1C4FA063159295DAC39296)
