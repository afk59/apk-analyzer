# SwipeRefresher

The swipe refresher is a component used to obtain and load content, typically with a pull-down gesture.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/jE03aX8oS2-rNUSmAHleYA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9034FA3AD3420B2F595AAA5A47023CA74F005EEB93B7A758C80157CB6B3CD94F)

This component and its child components are supported since API version 10. Updates will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { SwipeRefresher } from '@kit.ArkUI';

#### Child Components

Not supported

#### Attributes

The [universal attributes](../../universal-attributes/document.md) are not supported.

#### SwipeRefresher

SwipeRefresher ({content?: ResourceStr, isLoading: boolean})

Implements the pull-down refresh function. When a user pulls down the page, it triggers a content loading operation, fetching new content from the data source and dynamically displaying it on the page.

**Decorator**: @Component

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Mandatory | Decorator | Description |
| :-- | :-- | :-- | :-- | :-- |
| content | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | @Prop | 
Text displayed when the content is loaded.

The default value is an empty string.

**NOTE**

If the text length exceeds the column width, it will be truncated. The Resource type is supported since API version 20.

 |
| isLoading | boolean | Yes | @Prop | 

Whether content is being loaded.

**true**: Content is being loaded.

**false**: Content is not being loaded.

 |

#### Events

The [universal events](../../universal-events/document.md) are not supported.

#### Example

This example demonstrates how setting the **content** parameter to empty or non-empty strings and toggling the **isLoading** parameter between **true** and **false** affects the loading effect.

import { SwipeRefresher } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    Column() {
      SwipeRefresher({
        content: 'Loading',
        isLoading: true
      })
      SwipeRefresher({
        content: '',
        isLoading: true
      })
      SwipeRefresher({
        content: 'Loading',
        isLoading: false
      })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/JiTiujS_R8SHP9FPqx4pGQ/en-us_image_0000002537925938.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=35DB08505AD255395BEA71C4CCC095FA73C090371BDFBDE9DD601387CA03E7B0)
