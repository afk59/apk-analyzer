# visionImageAnalyzer (AI Image Recognition Control)

AI image recognition provides scenario-based text recognition, subject segmentation, and image search functions by aggregating AI capabilities such as Optical Character Recognition (OCR), subject segmentation, entity recognition, and multi-object recognition.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/HrZtLE56TaC6Ue51jQItjw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062525Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=151FE356A3B47F3802391763E1A11B537FF26E568B29E119954B7F62C8FE2A7C)

Exceptions need to be captured when an API is called.

**Start version**: 5.0.0(12)

#### Module Import

import { visionImageAnalyzer } from '@kit.VisionKit';

#### Menu

AI image recognition menu.

**System capability**: SystemCapability.AI.VisionImageAnalyzer

**Start version**: 5.0.0(12)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

value

 | 

[ResourceStr](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr)

 | 

No

 | 

No

 | 

Menu content.

 |
| 

action

 | 

[Callback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<string | [Subject](#section242033555713)\[\]>

 | 

No

 | 

No

 | 

Menu result callback, including the text selection result and clipping result.

 |

#### Rect

Rectangular data structure.

**System capability**: SystemCapability.AI.VisionImageAnalyzer

**Start version**: 5.0.0(12)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

left

 | 

number

 | 

No

 | 

Yes

 | 

Left position of a rectangle. The value ranges from the left boundary to the right boundary of an image. The unit is vp.

 |
| 

top

 | 

number

 | 

No

 | 

Yes

 | 

Top position of a rectangle. The value ranges from the top boundary to the bottom boundary of an image. The unit is vp.

 |
| 

right

 | 

number

 | 

No

 | 

Yes

 | 

Right position of a rectangle. The value ranges from the left boundary to the right boundary of an image. The unit is vp.

 |
| 

bottom

 | 

number

 | 

No

 | 

Yes

 | 

Bottom position of a rectangle. The value ranges from the top boundary to the bottom boundary of an image. The unit is vp.

 |

#### Subject

Subject recognition result.

**System capability**: SystemCapability.AI.VisionImageAnalyzer

**Start version**: 5.0.0(12)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

id

 | 

number

 | 

No

 | 

No

 | 

Subject ID. Value range: \[0, 6\]

 |
| 

image

 | 

[PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)

 | 

No

 | 

No

 | 

Image from which a subject is recognized.

 |
| 

boundingBox

 | 

[Rect](#section47991924195714)

 | 

No

 | 

No

 | 

Bounding box of a recognized subject.

 |
| 

maskData

 | 

Int32Array

 | 

No

 | 

Yes

 | 

1D array based on the original image size, which represents the subject mask. The value ranges from 0 to 255. The value **0** indicates the background, the value **255** indicates a subject, and the values between **0** and **255** indicate the probability of a salient subject.

**Start version**: 5.1.0(18)

CAUTION:

The **maskData** parameter might contain a large amount of data. Parsing and logging it using **JSON.stringify()** can be time-consuming, potentially affecting the API performance. Log this parameter based on your needs.

 |

#### SelectedStatus

Enumerated values of the object selection status during image recognition.

**System capability**: SystemCapability.AI.VisionImageAnalyzer

**Start version**: 5.0.0(12)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

SELECTED

 | 

0

 | 

Selected.

 |
| 

UNSELECTED

 | 

1

 | 

Unselected.

 |

#### ImageAnalyzerVisibility

Enumerated values of the AI image recognition control visibility.

**System capability**: SystemCapability.AI.VisionImageAnalyzer

**Start version**: 5.0.0(12)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

SHOWN

 | 

0

 | 

Visible.

 |
| 

HIDDEN

 | 

1

 | 

Invisible.

 |

#### AIButtonStatus

Enumerated values of the AIButton status.

**System capability**: SystemCapability.AI.VisionImageAnalyzer

**Start version**: 5.0.0(12)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

SELECTED

 | 

0

 | 

Selected.

 |
| 

UNSELECTED

 | 

1

 | 

Unselected.

 |
| 

HIDDEN

 | 

2

 | 

Hidden.

 |

#### ObjectSearchPanelVisibility

Enumerated values of the image search screen visibility.

**System capability**: SystemCapability.AI.VisionImageAnalyzer

**Start version**: 5.0.1(13)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

SHOW

 | 

0

 | 

Visible.

 |
| 

HIDE

 | 

1

 | 

Invisible.

 |

#### ImageAnalyzerUIStatus

Enumerated values of the image analysis screen status.

**System capability**: SystemCapability.AI.VisionImageAnalyzer

**Start version**: 5.0.2(14)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

INITIAL

 | 

0

 | 

Initial.

 |
| 

AI\_BUTTON\_SELECTED

 | 

1

 | 

AIButton selected.

 |
| 

TEXT\_SELECTED

 | 

2

 | 

Text selected.

 |
| 

SUBJECT\_SELECTED

 | 

3

 | 

Subject selected.

 |
| 

OBJECT\_SEARCH

 | 

4

 | 

Visual search.

 |

#### VisionImageAnalyzerController

Visual image controller used for controlling interactions. It inherits from the [ImageAnalyzerController](../../../../application-framework/arkui/arkts-components/images-and-videos/image-analysis-types/document.md#imageanalyzercontroller12) class.

**System capability**: SystemCapability.AI.VisionImageAnalyzer

**Start version**: 5.0.0(12)

#### \[h2\]setImageAnalyzerVisibility

setImageAnalyzerVisibility(visibility: ImageAnalyzerVisibility): void

Sets the visibility of the AI image recognition control.

**System capability**: SystemCapability.AI.VisionImageAnalyzer

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

visibility

 | 

[ImageAnalyzerVisibility](#section7314173721119)

 | 

Yes

 | 

Visibility of the AI image recognition control.

 |

**Example**:

import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear() {
    this.visionImageAnalyzerController.setImageAnalyzerVisibility(visionImageAnalyzer.ImageAnalyzerVisibility.HIDDEN)
  }
  build() {
    Stack() {
      // Set the image separately and add it to the **src/main/resources/base/media** directory.
      Image($r('app.media.img'), {
          types: \[ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT\_LOOKUP\],
          aiController: this.visionImageAnalyzerController
        })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
}

#### \[h2\]setAIButtonPosition

setAIButtonPosition(position: Rect): void

Sets the position of AIButton.

**System capability**: SystemCapability.AI.VisionImageAnalyzer

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

position

 | 

[Rect](#section47991924195714)

 | 

Yes

 | 

Position of AIButton relative to the four sides of the AI image recognition control, in vp. By default, it is displayed in the lower right corner.

If some parameters in **Rect** are passed, use the passed parameters preferentially for position matching. If the **position** parameter is abnormal, the default position will be used for display.

If both the **top** and **bottom** parameters are set, only the **top** parameter takes effect when the **setAIButtonPosition** API is called.

 |

**Example**:

import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear() {
    let position: visionImageAnalyzer.Rect = {
      bottom: 300
    }
    this.visionImageAnalyzerController.setAIButtonPosition(position)
    this.visionImageAnalyzerController.setAIButtonVisibility(true)
  }
  build() {
    Stack() {
      // Set the image separately and add it to the **src/main/resources/base/media** directory.
      Image($r('app.media.6'), {
        types: \[ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT\_LOOKUP\],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
}

#### \[h2\]setAIButtonVisibility

setAIButtonVisibility(visible: boolean): void

Sets the visibility of AIButton. When AIButton is set to visible, images are pre-analyzed. AIButton is displayed only when the images contain text and the text region occupies more than 5% of space in the image region. Enabling AIButton will trigger image pre-analysis, which causes certain power consumption. Therefore, you are advised to assess the context and enable AIButton only in scenarios where text content in images is of high importance. In this way, you can ensure an excellent image browsing experience for users while minimizing unnecessary power consumption.

**System capability**: SystemCapability.AI.VisionImageAnalyzer

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

visible

 | 

boolean

 | 

Yes

 | 

Indicates whether AIButton is visible. The value **true** indicates yes, and the value **false** indicates no.

The default value is **false**.

 |

**Example**:

import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear() {
    this.visionImageAnalyzerController.setAIButtonVisibility(true)
  }
  build() {
    Stack() {
      // Set the image separately and add it to the **src/main/resources/base/media** directory.
      Image($r('app.media.img'), {
          types: \[ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT\_LOOKUP\],
          aiController: this.visionImageAnalyzerController
        })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
}

#### \[h2\]setCustomTextMenuItems

setCustomTextMenuItems(menus: Menu\[\]): void

Sets customized menu items for text analysis.

**System capability**: SystemCapability.AI.VisionImageAnalyzer

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

menus

 | 

[Menu](#section12912173105717)\[\]

 | 

Yes

 | 

Customized menu items to be added for selected text. The callback contains the selected text.

A maximum of three menu items can be displayed. If there are more than three menu items, the first three are displayed.

 |

**Example**:

import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear() {
    this.visionImageAnalyzerController.setAIButtonVisibility(true)
    this.visionImageAnalyzerController.setCustomTextMenuItems(\[
      {
        value: "menu2",
        action: (param: string | visionImageAnalyzer.Subject\[\]) => {
          console.info("DEMO\_TAG", "text menu clicked")
        }
      }
    \]
    )
  }
  build() {
    Stack() {
      // Set the image separately and add it to the **src/main/resources/base/media** directory.
      Image($r('app.media.img'), {
        types: \[ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT\_LOOKUP\],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
}

#### \[h2\]startSubjectAnalyzer

startSubjectAnalyzer(): void

Enables subject recognition. Before performing this operation, ensure that the current device supports subject recognition. You can obtain subject data through the **subjectAnalysis** event callback. Note: Add a timeout mechanism to prevent your app from waiting indefinitely for subject data if no subject is identified.

**System capability**: SystemCapability.AI.VisionImageAnalyzer

**Start version**: 5.0.0(12)

**Example**:

import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear() {
    let supportTypes = this.visionImageAnalyzerController.getImageAnalyzerSupportTypes();
    if (supportTypes.includes(ImageAnalyzerType.SUBJECT)) {
       this.visionImageAnalyzerController.startSubjectAnalyzer()
    }
  }
  build() {
    Stack() {
      // Set the image separately and add it to the **src/main/resources/base/media** directory.
      Image($r('app.media.img'), {
        types: \[ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT\_LOOKUP\],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
}

#### \[h2\]setCustomSubjectMenuItems

setCustomSubjectMenuItems(menus: Menu\[\]): void

Sets customized menu items for subject analysis.

**System capability**: SystemCapability.AI.VisionImageAnalyzer

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

menus

 | 

[Menu](#section12912173105717)\[\]

 | 

Yes

 | 

Customized menu items to be added for selected subjects. The callback contains the selected subjects.

A maximum of three menu items can be displayed. If there are more than three menu items, the first three are displayed.

 |

**Example**:

import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear() {
    this.visionImageAnalyzerController.setCustomSubjectMenuItems(\[
      {
        value: "menu2",
        action: (param: string | visionImageAnalyzer.Subject\[\]) => {
          console.info("DEMO\_TAG", "subject menu clicked")
        }
      }
    \]
    )
  }
  build() {
    Stack() {
      // Set the image separately and add it to the **src/main/resources/base/media** directory.
      Image($r('app.media.img'), {
        types: \[ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT\_LOOKUP\],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
}

#### \[h2\]setSelectedSubjects

setSelectedSubjects(subjectIds: number\[\]): void

Sets selected subjects based on the subject ID list.

**System capability**: SystemCapability.AI.VisionImageAnalyzer

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

subjectIds

 | 

number\[\]

 | 

Yes

 | 

ID list of subjects to be selected. The value is obtained through [getSubject](#section7245340164614). Only the IDs of subjects contained in the image recognition result are valid.

 |

**Example**:

import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct SingleImageTest2 {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear() {
    this.visionImageAnalyzerController.on('subjectAnalysis', (subjects: visionImageAnalyzer.Subject\[\]) => {
      console.info("DEMO\_TAG", \`subjectAnalysis result: ${JSON.stringify(subjects)}\`)
      if(subjects.length > 0) {
        this.visionImageAnalyzerController.setSelectedSubjects(\[subjects\[0\].id\])
      }
    })
  }
  build() {
    Stack() {
      // Set the image separately and add it to the **src/main/resources/base/media** directory.
      Image($r('app.media.img'), {
        types: \[ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT\_LOOKUP\],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
}

#### \[h2\]getSelectedSubjects

getSelectedSubjects(): Promise<Subject\[\] | null>

Obtains the selected subjects. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.AI.VisionImageAnalyzer

**Start version**: 5.0.0(12)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[Subject](#section242033555713)\[\] | null>

 | 

Selected subjects, which are returned through a promise.

 |

**Example**:

import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  getSelectedSubjects() {
    this.visionImageAnalyzerController.getSelectedSubjects().then((subjects: visionImageAnalyzer.Subject\[\] | null) => {
      console.info("DEMO\_TAG", \`getSelectedSubjects result: ${JSON.stringify(subjects)}\`)
    })
  }
  build() {
    Stack() {
      // Set the image separately and add it to the **src/main/resources/base/media** directory.
      Image($r('app.media.img'), {
        types: \[ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT\_LOOKUP\],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
}

#### \[h2\]getSubject

getSubject(point: visionBase.Point): Promise<Subject | null>

Obtains a subject corresponding to a point position. This API returns the result asynchronously through a promise. Before calling this API, call [startSubjectAnalyzer](#section2238839144418) to enable subject recognition.

**System capability**: SystemCapability.AI.VisionImageAnalyzer

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

point

 | 

[visionBase.Point](../../../core-vision-kit/arkts-apis/visionbase-core-vision-kit-base-class/document.md#section1465431712919)

 | 

Yes

 | 

Point position relative to the upper left corner of an image, in px.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[Subject](#section242033555713) | null>

 | 

Subject corresponding to a point position, which is returned through a promise.

 |

**Example**:

import { visionImageAnalyzer } from '@kit.VisionKit';
import { visionBase } from '@kit.CoreVisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController = new visionImageAnalyzer.VisionImageAnalyzerController()
  getSelectedSubjects() {
    let searchPoint: visionBase.Point = { x: 100, y: 100 }
    this.visionImageAnalyzerController.getSubject(searchPoint).then((subjects: visionImageAnalyzer.Subject | null) => {
      console.info("DEMO\_TAG", \`getSubject result: ${JSON.stringify(subjects)}\`)
    })
  }
  build() {
    Stack() {
      // Set the image separately and add it to the **src/main/resources/base/media** directory.
      Image($r('app.media.img'), {
        types: \[ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT\_LOOKUP\],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
}

#### \[h2\]getSubjectsImage

getSubjectsImage(subjectIds: number\[\]): Promise<PixelMap | null>

Obtains an image assembled based on subjects corresponding to specified subject IDs. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.AI.VisionImageAnalyzer

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

subjectIds

 | 

number\[\]

 | 

Yes

 | 

Subject ID list. The value is obtained through [getSubject](#section7245340164614).

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | null>

 | 

Image assembled based on subjects corresponding to specified subject IDs, which is returned through a promise.

 |

**Example**:

import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  getSubjectsImage() {
    this.visionImageAnalyzerController.on('subjectAnalysis', (subjects: visionImageAnalyzer.Subject\[\]) => {
      console.info("DEMO\_TAG", \`subjectAnalysis result: ${JSON.stringify(subjects)}\`)
      if(subjects.length > 0) {
        let ids: number\[\] = \[subjects\[0\].id\]
        this.visionImageAnalyzerController.getSubjectsImage(ids).then((image: PixelMap | null) => {
          console.info('Image data obtained successfully:', image);
        }).catch((error: Error) => {
          console.error('Failed to obtain image data:', error);
        })
      }
    })
  }
  build() {
    Stack() {
      // Set the image separately and add it to the **src/main/resources/base/media** directory.
      Image($r('app.media.img'), {
        types: \[ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT\_LOOKUP\],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
}

#### \[h2\]getImageAnalyzerUIStatus

getImageAnalyzerUIStatus(): Promise<ImageAnalyzerUIStatus>

Obtains the current image analysis screen status. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.AI.VisionImageAnalyzer

**Start version**: 5.0.2(14)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[ImageAnalyzerUIStatus](#section1079155235910)\>

 | 

Current image analysis screen status, which is returned through a promise.

 |

**Example**:

import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear() {
    this.visionImageAnalyzerController.setAIButtonVisibility(true);
    this.visionImageAnalyzerController.on('objectSearchPanelVisibilityChange', (objectSearchPanelVisibility: visionImageAnalyzer.ObjectSearchPanelVisibility) => {
      this.visionImageAnalyzerController.getImageAnalyzerUIStatus().then((status: visionImageAnalyzer.ImageAnalyzerUIStatus) => {
        console.info('Image data obtained successfully:', status);
      }).catch((error: Error) => {
        console.error('Failed to obtain image data:', error);
      })
    })
  }
  build() {
    Stack() {
      Image($r('app.media.img'), {
        types: \[ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT\_LOOKUP\],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('60%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)

      Button('Obtain current image analysis screen status', { stateEffect: true, type: ButtonType.Capsule })
        .width('80%')
        .height(40)
        .onClick(() => {
          this.visionImageAnalyzerController.getImageAnalyzerUIStatus()
            .then((status: visionImageAnalyzer.ImageAnalyzerUIStatus) => {
              console.info('Image data obtained successfully:', status);
            })
            .catch((error: Error) => {
              console.error('Failed to obtain image data:', error);
            })
        })
        .id('getImageAnalyzerUIStatus')
        .width('40%')
    }.width('100%').height('100%')
  }
}

#### \[h2\]startObjectSearch

startObjectSearch(): Promise<boolean>

Enables visual search. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.AI.VisionImageAnalyzer

**Device behavior differences**: This API has no effect on PCs/2-in-1 devices, but works properly on other devices.

**Start version**: 5.0.0(12)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<boolean>

 | 

Indicates whether visual search is enabled, which is returned through a promise. The value **true** indicates yes, and the value **false** indicates no. The return value is **false** if the API is called during text selection or subject recognition.

CAUTION:

If visual search fails to work in the image switching scenario within the [Swiper](../../../../application-framework/arkui/arkts-components/scroll-and-swipe/swiper/document.md) container, you need to reset the index to null in [onAnimationStart](../../../../application-framework/arkui/arkts-components/scroll-and-swipe/swiper/document.md#onanimationstart9), and then set the index in [onAnimationEnd](../../../../application-framework/arkui/arkts-components/scroll-and-swipe/swiper/document.md#onanimationend9) to the index of the newly selected image. This ensures that the overlay follows the image changes correctly.

 |

**Example**:

import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  startObjectSearch() {
    this.visionImageAnalyzerController.startObjectSearch()
  }
  build() {
    Stack() {
      // Set the image separately and add it to the **src/main/resources/base/media** directory.
      Image($r('app.media.img'), {
        types: \[ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT\_LOOKUP\],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
}

#### \[h2\]stopObjectSearch

stopObjectSearch(): void

Disables visual search. The function cannot be disabled if the visual search interaction is in progress.

**System capability**: SystemCapability.AI.VisionImageAnalyzer

**Device behavior differences**: This API has no effect on PCs/2-in-1 devices, but works properly on other devices.

**Start version**: 5.0.0(12)

**Example**:

import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  stopObjectSearch() {
    this.visionImageAnalyzerController.stopObjectSearch()
  }
  build() {
    Stack() {
      // Set the image separately and add it to the **src/main/resources/base/media** directory.
      Image($r('app.media.img'), {
        types: \[ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT\_LOOKUP\],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
}

#### \[h2\]setSubjectMenuVisibility

setSubjectMenuVisibility(visible: boolean): void

Sets whether to display the image segmentation menu.

**System capability**: SystemCapability.AI.VisionImageAnalyzer

**Start version**: 5.0.1(13)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

visible

 | 

boolean

 | 

Yes

 | 

Indicates whether to display the image segmentation menu.

The value **true** indicates yes, and the value **false** indicates no.

The default value is **true**.

 |

import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  setSubjectMenuVisibility(visible: boolean) {
    this.visionImageAnalyzerController.setSubjectMenuVisibility(visible)
  }
  build() {
    Stack() {
      // Set the image separately and add it to the **src/main/resources/base/media** directory.
      Image($r('app.media.img'), {
        types: \[ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT\_LOOKUP\],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
}

#### \[h2\]on(type: 'aiButtonStatusChange')

on(type: 'aiButtonStatusChange', callback: Callback<AIButtonStatus>): void

Listens to the AIButton display status.

**System capability**: SystemCapability.AI.VisionImageAnalyzer

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

The value is **aiButtonStatusChange**, indicating listening to the AIButton display status.

 |
| 

callback

 | 

[Callback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<[AIButtonStatus](#section1612865961116)\>

 | 

Yes

 | 

Callback function. It receives the AIButton display status.

 |

**Example**:

import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear(): void {
    this.visionImageAnalyzerController?.setAIButtonVisibility(true)
    this.visionImageAnalyzerController.on('aiButtonStatusChange', (aiButtonState: visionImageAnalyzer.AIButtonStatus) => {
      console.info("DEMO\_TAG", \`aiButtonStatusChange result: ${JSON.stringify(aiButtonState)}\`)
    })
  }
  build() {
    Stack() {
      // Set the image separately and add it to the **src/main/resources/base/media** directory.
      Image($r('app.media.img'), {
        types: \[ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT\_LOOKUP\],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
}

#### \[h2\]off(type: 'aiButtonStatusChange')

off(type: 'aiButtonStatusChange', callback?: Callback<AIButtonStatus>): void

Cancels the listening to the AIButton display status.

**System capability**: SystemCapability.AI.VisionImageAnalyzer

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

The value is **aiButtonStatusChange**, indicating canceling the listening to the AIButton display status.

 |
| 

callback

 | 

[Callback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<[AIButtonStatus](#section1612865961116)\>

 | 

No

 | 

Callback function to be unregistered, which must be the same as that passed upon subscription. If this parameter is not passed, all callback functions will be unregistered.

 |

**Example**:

import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear(): void {
    this.visionImageAnalyzerController?.setAIButtonVisibility(true)
    this.visionImageAnalyzerController.on('aiButtonStatusChange', (aiButtonState: visionImageAnalyzer.AIButtonStatus) => {
      console.info("DEMO\_TAG", \`aiButtonStatusChange result: ${JSON.stringify(aiButtonState)}\`)
    })
  }
  aboutToDisappear(): void {
    this.visionImageAnalyzerController.off('aiButtonStatusChange')
  }
  build() {
    Stack() {
      // Set the image separately and add it to the **src/main/resources/base/media** directory.
      Image($r('app.media.img'), {
        types: \[ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT\_LOOKUP\],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
}

#### \[h2\]on(type: 'imageAnalyzerVisibilityChange')

on(type: 'imageAnalyzerVisibilityChange', callback: Callback<ImageAnalyzerVisibility>): void

Listens to the visibility of the AI image recognition control.

**System capability**: SystemCapability.AI.VisionImageAnalyzer

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

The value is **imageAnalyzerVisibilityChange**, indicating listening to the visibility of the AI image recognition control.

 |
| 

callback

 | 

[Callback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<[ImageAnalyzerVisibility](#section7314173721119)\>

 | 

Yes

 | 

Callback function. It receives the visibility of the AI image recognition control.

 |

**Example**:

import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear(): void {
    this.visionImageAnalyzerController?.setAIButtonVisibility(true)
    this.visionImageAnalyzerController.on('imageAnalyzerVisibilityChange', (visibility: visionImageAnalyzer.ImageAnalyzerVisibility) => {
      console.info("DEMO\_TAG", \`imageAnalyzerVisibilityChange result: ${JSON.stringify(visibility)}\`)
    })
  }
  aboutToDisappear(): void {
    this.visionImageAnalyzerController.off('imageAnalyzerVisibilityChange')
  }
  build() {
    Stack() {
      // Set the image separately and add it to the **src/main/resources/base/media** directory.
      Image($r('app.media.img'), {
        types: \[ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT\_LOOKUP\],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
}

#### \[h2\]off(type: 'imageAnalyzerVisibilityChange')

off(type: 'imageAnalyzerVisibilityChange', callback?: Callback<ImageAnalyzerVisibility>): void

Cancels the listening to the visibility of the AI image recognition control.

**System capability**: SystemCapability.AI.VisionImageAnalyzer

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

The value is **imageAnalyzerVisibilityChange**, indicating canceling the listening to the visibility of the AI image recognition control.

 |
| 

callback

 | 

[Callback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<[ImageAnalyzerVisibility](#section7314173721119)\>

 | 

No

 | 

Callback function to be unregistered, which must be the same as that passed upon subscription. If this parameter is not passed, all callback functions will be unregistered.

 |

**Example**:

import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear(): void {
    this.visionImageAnalyzerController?.setAIButtonVisibility(true)
    this.visionImageAnalyzerController.on('imageAnalyzerVisibilityChange', (visibility: visionImageAnalyzer.ImageAnalyzerVisibility) => {
      console.info("DEMO\_TAG", \`imageAnalyzerVisibilityChange result: ${JSON.stringify(visibility)}\`)
    })
  }
  aboutToDisappear(): void {
    this.visionImageAnalyzerController.off('imageAnalyzerVisibilityChange')
  }
  build() {
    Stack() {
      // Set the image separately and add it to the **src/main/resources/base/media** directory.
      Image($r('app.media.img'), {
        types: \[ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT\_LOOKUP\],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
}

#### \[h2\]on(type: 'textAnalysis')

on(type: 'textAnalysis', callback: Callback<string>): void

Listens to the text analysis result. By default, text analysis is triggered when the image text is pressed and held for the first time. On PCs/2-in-1 devices, text analysis is triggered when an image is loaded for the first time.

**System capability**: SystemCapability.AI.VisionImageAnalyzer

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

The value is **textAnalysis**, indicating listening to the text analysis result.

 |
| 

callback

 | 

[Callback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<string>

 | 

Yes

 | 

Callback function. It receives the text analysis result.

 |

**Example**:

import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear(): void {
    this.visionImageAnalyzerController.on('textAnalysis', (text: string) => {
      console.info("DEMO\_TAG", \`textAnalysis result: ${JSON.stringify(text)}\`)
    })
  }
  aboutToDisappear(): void {
    this.visionImageAnalyzerController.off('textAnalysis')
  }
  build() {
    Stack() {
      // Set the image separately and add it to the **src/main/resources/base/media** directory.
      Image($r('app.media.img'), {
        types: \[ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT\_LOOKUP\],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
}

#### \[h2\]off(type: 'textAnalysis')

off(type: 'textAnalysis', callback?: Callback<string>): void

Cancels the listening to the text analysis result.

**System capability**: SystemCapability.AI.VisionImageAnalyzer

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

The value is **textAnalysis**, indicating canceling the listening to the text analysis result.

 |
| 

callback

 | 

[Callback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<string>

 | 

No

 | 

Callback function to be unregistered, which must be the same as that passed upon subscription. If this parameter is not passed, all callback functions will be unregistered.

 |

**Example**:

import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear(): void {
    this.visionImageAnalyzerController.on('textAnalysis', (text: string) => {
      console.info("DEMO\_TAG", \`textAnalysis result: ${JSON.stringify(text)}\`)
    })
  }
  aboutToDisappear(): void {
    this.visionImageAnalyzerController.off('textAnalysis')
  }
  build() {
    Stack() {
      // Set the image separately and add it to the **src/main/resources/base/media** directory.
      Image($r('app.media.img'), {
        types: \[ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT\_LOOKUP\],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
}

#### \[h2\]on(type: 'selectedTextChange')

on(type: 'selectedTextChange', callback: Callback<string>): void

Listens to the text selection result.

**System capability**: SystemCapability.AI.VisionImageAnalyzer

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

The value is **selectedTextChange**, indicating listening to the text selection result.

 |
| 

callback

 | 

[Callback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<string>

 | 

Yes

 | 

Callback function. It receives the text selection result.

 |

**Example**:

import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear(): void {
    this.visionImageAnalyzerController.on('selectedTextChange', (selectedText: string) => {
      console.info("DEMO\_TAG", \`selectedTextChange result: ${JSON.stringify(selectedText)}\`)
    })
  }
  aboutToDisappear(): void {
    this.visionImageAnalyzerController.off('selectedTextChange')
  }
  build() {
    Stack() {
      // Set the image separately and add it to the **src/main/resources/base/media** directory.
      Image($r('app.media.img'), {
        types: \[ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT\_LOOKUP\],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
}

#### \[h2\]off(type: 'selectedTextChange')

off(type: 'selectedTextChange', callback?: Callback<string>): void

Cancels the listening to the text selection result.

**System capability**: SystemCapability.AI.VisionImageAnalyzer

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

The value is **selectedTextChange**, indicating canceling the listening to the text selection result.

 |
| 

callback

 | 

[Callback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<string>

 | 

No

 | 

Callback function to be unregistered, which must be the same as that passed upon subscription. If this parameter is not passed, all callback functions will be unregistered.

 |

**Example**:

import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear(): void {
    this.visionImageAnalyzerController.on('selectedTextChange', (selectedText: string) => {
      console.info("DEMO\_TAG", \`selectedTextChange result: ${JSON.stringify(selectedText)}\`)
    })
  }
  aboutToDisappear(): void {
    this.visionImageAnalyzerController.off('selectedTextChange')
  }
  build() {
    Stack() {
      // Set the image separately and add it to the **src/main/resources/base/media** directory.
      Image($r('app.media.img'), {
        types: \[ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT\_LOOKUP\],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
}

#### \[h2\]on(type: 'subjectAnalysis')

on(type: 'subjectAnalysis', callback: Callback<Subject\[\]>): void

Listens to the subject analysis result and returns all subject information.

**System capability**: SystemCapability.AI.VisionImageAnalyzer

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

The value is **subjectAnalysis**, indicating listening to the subject analysis result and returning all subject information.

 |
| 

callback

 | 

[Callback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<[Subject](#section242033555713)\[\]>

 | 

Yes

 | 

Callback function. It receives the subject analysis result and returns all subject information.

 |

**Example**:

import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear(): void {
    this.visionImageAnalyzerController.on('subjectAnalysis', (subjects: visionImageAnalyzer.Subject\[\]) => {
      console.info("DEMO\_TAG", \`subjectAnalysis result: ${JSON.stringify(subjects)}\`)
    })
  }
  aboutToDisappear(): void {
    this.visionImageAnalyzerController.off('subjectAnalysis')
  }
  build() {
    Stack() {
      // Set the image separately and add it to the **src/main/resources/base/media** directory.
      Image($r('app.media.img'), {
        types: \[ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT\_LOOKUP\],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
}

#### \[h2\]off(type: 'subjectAnalysis')

off(type: 'subjectAnalysis', callback?: Callback<Subject\[\]>): void

Cancels the listening to the subject analysis result.

**System capability**: SystemCapability.AI.VisionImageAnalyzer

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

The value is **subjectAnalysis**, indicating canceling the listening to the subject analysis result.

 |
| 

callback

 | 

[Callback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<[Subject](#section242033555713)\[\]>

 | 

No

 | 

Callback function to be unregistered, which must be the same as that passed upon subscription. If this parameter is not passed, all callback functions will be unregistered.

 |

**Example**:

import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear(): void {
    this.visionImageAnalyzerController.on('subjectAnalysis', (subjects: visionImageAnalyzer.Subject\[\]) => {
      console.info("DEMO\_TAG", \`subjectAnalysis result: ${JSON.stringify(subjects)}\`)
    })
  }
  aboutToDisappear(): void {
    this.visionImageAnalyzerController.off('subjectAnalysis')
  }
  build() {
    Stack() {
      // Set the image separately and add it to the **src/main/resources/base/media** directory.
      Image($r('app.media.img'), {
        types: \[ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT\_LOOKUP\],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
}

#### \[h2\]on(type: 'selectedSubjectsChange')

on(type: 'selectedSubjectsChange', callback: Callback<Subject\[\]>): void

Listens to selected subjects.

**System capability**: SystemCapability.AI.VisionImageAnalyzer

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

The value is **selectedSubjectsChange**, indicating listening to selected subjects.

 |
| 

callback

 | 

[Callback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<[Subject](#section242033555713)\[\]>

 | 

Yes

 | 

Callback function. It receives information about selected subjects.

 |

**Example**:

import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear(): void {
    this.visionImageAnalyzerController.on('selectedSubjectsChange', (subjects: visionImageAnalyzer.Subject\[\]) => {
      console.info("DEMO\_TAG", \`selectedSubjectsChange result: ${JSON.stringify(subjects)}\`)
    })
  }
  aboutToDisappear(): void {
    this.visionImageAnalyzerController.off('selectedSubjectsChange')
  }
  build() {
    Stack() {
      // Set the image separately and add it to the **src/main/resources/base/media** directory.
      Image($r('app.media.img'), {
        types: \[ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT\_LOOKUP\],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
}

#### \[h2\]off(type: 'selectedSubjectsChange')

off(type: 'selectedSubjectsChange', callback?: Callback<Subject\[\]>): void

Cancels the listening to selected subjects.

**System capability**: SystemCapability.AI.VisionImageAnalyzer

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

The value is **selectedSubjectsChange**, indicating canceling the listening to selected subjects.

 |
| 

callback

 | 

[Callback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<[Subject](#section242033555713)\[\]>

 | 

No

 | 

Callback function to be unregistered, which must be the same as that passed upon subscription. If this parameter is not passed, all callback functions will be unregistered.

 |

**Example**:

import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear(): void {
    this.visionImageAnalyzerController.on('selectedSubjectsChange', (subjects: visionImageAnalyzer.Subject\[\]) => {
      console.info("DEMO\_TAG", \`selectedSubjectsChange result: ${JSON.stringify(subjects)}\`)
    })
  }
  aboutToDisappear(): void {
    this.visionImageAnalyzerController.off('selectedSubjectsChange')
  }
  build() {
    Stack() {
      // Set the image separately and add it to the **src/main/resources/base/media** directory.
      Image($r('app.media.img'), {
        types: \[ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT\_LOOKUP\],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
}

#### \[h2\]on(type: 'objectSearchPanelVisibilityChange')

on(type: 'objectSearchPanelVisibilityChange', callback: Callback<ObjectSearchPanelVisibility>): void

Listens to image search events.

**System capability**: SystemCapability.AI.VisionImageAnalyzer

**Start version**: 5.0.1(13)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

The value is **objectSearchPanelVisibilityChange**, indicating listening to image search events.

 |
| 

callback

 | 

[Callback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<[ObjectSearchPanelVisibility](#section7671145547)\>

 | 

Yes

 | 

Callback function. It receives image search event information.

 |

import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear(): void {
    this.visionImageAnalyzerController.on('objectSearchPanelVisibilityChange', (status: visionImageAnalyzer.ObjectSearchPanelVisibility) => {
      console.info("DEMO\_TAG", \`objectSearchPanelVisibilityChange result: ${JSON.stringify(status)}\`)
    })
  }
  aboutToDisappear(): void {
    this.visionImageAnalyzerController.off('objectSearchPanelVisibilityChange')
  }
  build() {
    Stack() {
      // Set the image separately and add it to the **src/main/resources/base/media** directory.
      Image($r('app.media.img'), {
        types: \[ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT\_LOOKUP\],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
}

#### \[h2\]off(type: 'objectSearchPanelVisibilityChange')

off(type: 'objectSearchPanelVisibilityChange', callback?: Callback<ObjectSearchPanelVisibility>): void

Cancels the listening to image search events.

**System capability**: SystemCapability.AI.VisionImageAnalyzer

**Start version**: 5.0.1(13)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

The value is **objectSearchPanelVisibilityChange**, indicating canceling the listening to image search events.

 |
| 

callback

 | 

[Callback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<[ObjectSearchPanelVisibility](#section7671145547)\>

 | 

No

 | 

Callback function to be unregistered, which must be the same as that passed upon subscription. If this parameter is not passed, all callback functions will be unregistered.

 |

import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear(): void {
    this.visionImageAnalyzerController.on('objectSearchPanelVisibilityChange', (status: visionImageAnalyzer.ObjectSearchPanelVisibility) => {
      console.info("DEMO\_TAG", \`objectSearchPanelVisibilityChange result: ${JSON.stringify(status)}\`)
    })
  }
  aboutToDisappear(): void {
    this.visionImageAnalyzerController.off('objectSearchPanelVisibilityChange')
  }
  build() {
    Stack() {
      // Set the image separately and add it to the **src/main/resources/base/media** directory.
      Image($r('app.media.img'), {
        types: \[ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT\_LOOKUP\],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
}

#### \[h2\]on(type: 'cursorMoveInText')

on(type: 'cursorMoveInText', callback: Callback<void>): void

Listens to the event of moving the cursor into the text area in an image.

**System capability**: SystemCapability.AI.VisionImageAnalyzer

**Start version**: 5.1.0(18)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

The value is **cursorMoveInText**, indicating listening to the event of moving the cursor into the text area in an image.

 |
| 

callback

 | 

[Callback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<void>

 | 

Yes

 | 

Callback function. It receives information about the event of moving the cursor into the text area in an image.

 |

import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear(): void {
    this.visionImageAnalyzerController.on('cursorMoveInText', () => {
      console.info("DEMO\_TAG", \`cursorMoveInText on\`)
    })
  }
  aboutToDisappear(): void {
    this.visionImageAnalyzerController.off('cursorMoveInText')
  }
  build() {
    Stack() {
      // Set the image separately and add it to the **src/main/resources/base/media** directory.
      Image($r('app.media.img'), {
        types: \[ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT\_LOOKUP\],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
}

#### \[h2\]off(type: 'cursorMoveInText')

off(type: 'cursorMoveInText', callback?: Callback<void>): void

Cancels the listening to the event of moving the cursor into the text area in an image.

**System capability**: SystemCapability.AI.VisionImageAnalyzer

**Start version**: 5.1.0(18)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

The value is **cursorMoveInText**, indicating canceling the listening to the event of moving the cursor into the text area in an image.

 |
| 

callback

 | 

[Callback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<void>

 | 

No

 | 

Callback function to be unregistered, which must be the same as that passed upon subscription. If this parameter is not passed, all callback functions will be unregistered.

 |

import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear(): void {
    this.visionImageAnalyzerController.on('cursorMoveInText', () => {
      console.info("DEMO\_TAG", \`cursorMoveInText on\`)
    })
  }
  aboutToDisappear(): void {
    this.visionImageAnalyzerController.off('cursorMoveInText')
  }
  build() {
    Stack() {
      // Set the image separately and add it to the **src/main/resources/base/media** directory.
      Image($r('app.media.img'), {
        types: \[ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT\_LOOKUP\],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
}

#### \[h2\]on(type: 'cursorMoveOutText')

on(type: 'cursorMoveOutText', callback: Callback<void>): void

Listens to the event of moving the cursor out of the text area in an image.

**System capability**: SystemCapability.AI.VisionImageAnalyzer

**Start version**: 5.1.0(18)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

The value is **cursorMoveOutText**, indicating listening to the event of moving the cursor out of the text area in an image.

 |
| 

callback

 | 

[Callback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<void>

 | 

Yes

 | 

Callback function. It receives information about the event of moving the cursor out of the text area in an image.

 |

import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear(): void {
    this.visionImageAnalyzerController.on('cursorMoveOutText', () => {
      console.info("DEMO\_TAG", \`cursorMoveOutText on\`)
    })
  }
  aboutToDisappear(): void {
    this.visionImageAnalyzerController.off('cursorMoveOutText')
  }
  build() {
    Stack() {
      // Set the image separately and add it to the **src/main/resources/base/media** directory.
      Image($r('app.media.img'), {
        types: \[ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT\_LOOKUP\],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
}

#### \[h2\]off(type: 'cursorMoveOutText')

off(type: 'cursorMoveOutText', callback?: Callback<void>): void

Cancels the listening to the event of moving the cursor out of the text area in an image.

**System capability**: SystemCapability.AI.VisionImageAnalyzer

**Start version**: 5.1.0(18)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

The value is **cursorMoveOutText**, indicating canceling the listening to the event of moving the cursor out of the text area in an image.

 |
| 

callback

 | 

[Callback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<void>

 | 

No

 | 

Callback function to be unregistered, which must be the same as that passed upon subscription. If this parameter is not passed, all callback functions will be unregistered.

 |

import { visionImageAnalyzer } from '@kit.VisionKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear(): void {
    this.visionImageAnalyzerController.on('cursorMoveOutText', () => {
      console.info("DEMO\_TAG", \`cursorMoveOutText on\`)
    })
  }
  aboutToDisappear(): void {
    this.visionImageAnalyzerController.off('cursorMoveOutText')
  }
  build() {
    Stack() {
      // Set the image separately and add it to the **src/main/resources/base/media** directory.
      Image($r('app.media.img'), {
        types: \[ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT\_LOOKUP\],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
}

#### \[h2\]on(type: 'analyzerFailed')

on(type: 'analyzerFailed', callback: ErrorCallback): void

Listens to abnormal scenarios of AI image recognition.

**System capability**: SystemCapability.AI.VisionImageAnalyzer

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

The value is **analyzerFailed**, indicating listening to abnormal scenarios of AI image recognition.

 |
| 

callback

 | 

[ErrorCallback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#errorcallback)

 | 

Yes

 | 

Callback function. It receives information about abnormal scenarios of AI image recognition.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.

 |
| 

1013700002

 | 

The service is abnormal.

 |

**Example**:

import { visionImageAnalyzer } from '@kit.VisionKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear(): void {
    this.visionImageAnalyzerController.on('analyzerFailed', (error: BusinessError) => {
      console.error("DEMO\_TAG", \`analyzerFailed result: ${JSON.stringify(error)}\`)
    })
  }
  aboutToDisappear(): void {
    this.visionImageAnalyzerController.off('analyzerFailed')
  }
  build() {
    Stack() {
      // Set the image separately and add it to the **src/main/resources/base/media** directory.
      Image($r('app.media.img'), {
        types: \[ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT\_LOOKUP\],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
}

#### \[h2\]off(type: 'analyzerFailed')

off(type: 'analyzerFailed', callback?: ErrorCallback): void

Cancels the listening to abnormal scenarios of AI image recognition.

**System capability**: SystemCapability.AI.VisionImageAnalyzer

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

The value is **analyzerFailed**, indicating canceling the listening to abnormal scenarios of AI image recognition.

 |
| 

callback

 | 

[ErrorCallback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#errorcallback)

 | 

No

 | 

Callback function to be unregistered, which must be the same as that passed upon subscription. If this parameter is not passed, all callback functions will be unregistered.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.

 |
| 

1013700002

 | 

The service is abnormal.

 |

**Example**:

import { visionImageAnalyzer } from '@kit.VisionKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController()
  aboutToAppear(): void {
    this.visionImageAnalyzerController.on('analyzerFailed', (error: BusinessError) => {
      console.error("DEMO\_TAG", \`analyzerFailed result: ${JSON.stringify(error)}\`)
    })
  }
  aboutToDisappear(): void {
    this.visionImageAnalyzerController.off('analyzerFailed')
  }
  build() {
    Stack() {
      // Set the image separately and add it to the **src/main/resources/base/media** directory.
      Image($r('app.media.img'), {
        types: \[ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT\_LOOKUP\],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
}
