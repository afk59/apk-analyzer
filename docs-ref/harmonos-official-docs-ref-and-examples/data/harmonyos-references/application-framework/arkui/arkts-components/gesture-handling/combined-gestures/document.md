# Combined Gestures

Combined gestures integrate two or more gestures into a compound gesture, supporting sequential recognition, parallel recognition, and exclusive recognition.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/K_L827EUQ9CyTeqUNZ49gA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062237Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=78D53C97476A79B7DDFC37185DFD45B31C54773D1264A58967D4700937410C67)

The initial APIs of this module are supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.

#### APIs

GestureGroup(mode: GestureMode, ...gesture: GestureType\[\])

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [GestureMode](#gesturemode) | Yes | 
Recognition mode of combined gestures.

Default value: **GestureMode.Sequence**

 |
| gesture | [GestureType](../gesture-common-apis/document.md#gesturetype)\[\] | No | 

One or more basic gestures to be recognized simultaneously. If this parameter is left empty, simultaneous recognition will not take effect.

**NOTE**

To add both single-tap and double-tap gestures for a component, add two [TapGesture](../basic-gestures/tapgesture/document.md) instances, with the double-tap gesture preceding the single-tap gesture. The gestures will not work correctly if this order is reversed.

 |

#### GestureMode

Defines the recognition mode of a gesture group.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| Sequence | \- | 
Sequential recognition. Gestures are recognized in the registration sequence until all gestures are recognized successfully. If any gesture in the sequence fails recognition, subsequent gestures will not be recognized.

Only the last gesture in a sequentially recognized gesture group can trigger **onActionEnd**.

 |
| Parallel | \- | Parallel recognition. Registered gestures are recognized concurrently until all gestures are recognized. The recognition result of each gesture does not affect each other. |
| Exclusive | \- | Exclusive recognition. All registered gestures are processed simultaneously. Once any gesture is recognized successfully, the recognition process ends, and all other gestures are deemed unrecognized. |

#### Events

#### \[h2\]onCancel

onCancel(event: () => void)

Triggered when a tap cancellation event is received after a gesture is recognized.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | () => void | Yes | Callback for the gesture event. |

#### Example

This example demonstrates the sequential recognition of combined gestures, specifically long press and pan gestures, using **GestureGroup**.

// xxx.ets
@Entry
@Component
struct GestureGroupExample {
  @State count: number = 0;
  @State offsetX: number = 0;
  @State offsetY: number = 0;
  @State positionX: number = 0;
  @State positionY: number = 0;
  @State borderStyles: BorderStyle = BorderStyle.Solid;

  build() {
    Column() {
      Text('sequence gesture\\n' + 'LongPress onAction:' + this.count + '\\nPanGesture offset:\\nX: ' + this.offsetX + '\\n' + 'Y: ' + this.offsetY)
        .fontSize(15)
    }
    .translate({ x: this.offsetX, y: this.offsetY, z: 0 })
    .height(150)
    .width(200)
    .padding(20)
    .margin(20)
    .border({ width: 3, style: this.borderStyles })
    .gesture(
      // The following combined gestures are recognized in sequential recognition mode. If the long press gesture event is not triggered correctly, the pan gesture event will not be triggered.
      GestureGroup(GestureMode.Sequence,
        LongPressGesture({ repeat: true })
          .onAction((event?: GestureEvent) => {
            if (event && event.repeat) {
              this.count++
            }
            console.info('LongPress onAction')
          }),
        PanGesture()
          .onActionStart(() => {
            this.borderStyles = BorderStyle.Dashed
            console.info('pan start')
          })
          .onActionUpdate((event?: GestureEvent) => {
            if (event) {
              this.offsetX = this.positionX + event.offsetX
              this.offsetY = this.positionY + event.offsetY
            }
            console.info('pan update')
          })
          .onActionEnd(() => {
            this.positionX = this.offsetX
            this.positionY = this.offsetY
            this.borderStyles = BorderStyle.Solid
            console.info('pan end')
          })
      )
        .onCancel(() => {
          console.info('sequence gesture canceled')
        })
    )
  }
}

Diagram:

In sequence recognition mode, the long press gesture event is triggered first.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/aKcET1MxSXCIP7GIHShOrQ/en-us_image_0000002568685209.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062237Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0C9727245029898640F69C9C0F9663C552D07C866E1BEB66398B266F31E3BE92)

After the long press gesture is recognized, the pan gesture event is triggered.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/AEAWKyBvTWmiboVfaIF4NQ/en-us_image_0000002568765219.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062237Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=93FC790593D520DE08B410AC3689634D20EC873B8DE5D858BD718B8E61291ABC)
