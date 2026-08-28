# Gesture Modifier

With the gesture modifier, you can dynamically set gestures bound to components, complete with the **if/else** syntax.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/rwHZ11OeSzKqvh0XjFi0Cw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DF20823B19C30FAD81DC35FBDAB6ECD9DE7AE155D0CAE9FBE54FE86B039015EA)

This feature is supported since API version 12. Updates will be marked with a superscript to indicate their earliest API version.

#### gestureModifier

gestureModifier(modifier: GestureModifier): T

Creates a gesture modifier.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/Az9iPPbVQWm2GrwfLTLpAg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=00D97E6676764ACEAB8348DF5C81E4F5946318DB50FD40EE246835A6FC26993B)

**gestureModifier** does not support custom components.

This API cannot be called within [attributeModifier](../attribute-modifier/document.md#attributemodifier).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| modifier | [GestureModifier](#gesturemodifier-1) | Yes | 
Modifier for dynamically setting gestures bound to the current component. The **if/else** syntax is supported.

**modifier**: gesture modifier. You need a custom class to implement the **GestureModifier** API.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### GestureModifier

You need a custom class to implement the **GestureModifier** API.

#### \[h2\]applyGesture

applyGesture(event: UIGestureEvent): void

Applies a gesture.

You can customize this API as required. Dynamic configuration using the **if/else** syntax is supported. If gesture switching is triggered during an active gesture operation, the change takes effect in the next gesture operation after the current one completes (when all fingers are lifted).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [UIGestureEvent](../../../gesture-handling/gesture-binding/bound-gesture-configuration/document.md#uigestureevent) | Yes | **UIGestureEvent** object, which is used to set the gesture to be bound to the component. |

#### Example

## Example 1: Dynamically Binding a Gesture

This example demonstrates how to dynamically set the gestures bound to a component using **gestureModifier**.

// xxx.ets
class MyButtonModifier implements GestureModifier {
  supportDoubleTap: boolean = true;

  applyGesture(event: UIGestureEvent): void {
    if (this.supportDoubleTap) {
      event.addGesture(
        new TapGestureHandler({ count: 2, fingers: 1 })
          .tag("aaa")
          .onAction((event: GestureEvent) => {
            console.info('Gesture Info is', JSON.stringify(event));
            console.info('button tap');
          })
      )
    } else {
      event.addGesture(
        new PanGestureHandler()
          .onActionStart(() => {
            console.info('Pan start');
          })
      )
    }
  }
}

@Entry
@Component
struct Index {
  @State modifier: MyButtonModifier = new MyButtonModifier();

  build() {
    Row() {
      Column() {
        Column()
          .gestureModifier(this.modifier)
          .width(500)
          .height(500)
          .backgroundColor(Color.Gray)
        Button('changeGesture')
          .onClick(() => {
            this.modifier.supportDoubleTap = !this.modifier.supportDoubleTap;
          })
          .margin({ top: 10 })
      }
      .width('100%')
    }
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/W192FtO0R32GbyYvBm_DFA/en-us_image_0000002537765484.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C288A9798A71619696D019888E909D278C7485DCF538FD2BBB476DD40DD5F648)

## Example 2: Dynamically Binding a Gesture Group

This example demonstrates how to dynamically set the gesture group bound to a component using **gestureModifier**.

class MyButtonModifier implements GestureModifier {
  isExclusive: boolean = true;

  applyGesture(event: UIGestureEvent): void {
    if (this.isExclusive) {
      // Bind a mutually exclusive gesture group.
      event.addGesture(new GestureGroupHandler({
        mode: GestureMode.Exclusive,
        gestures: \[new TapGestureHandler({ count: 2, fingers: 1 }).onAction((event) => {
          console.info('event info is', JSON.stringify(event));
          console.info('ExclusiveGroupGesture TapGesture is called');
        }), new LongPressGestureHandler({ repeat: true, fingers: 1 }).onAction((event) => {
          console.info('event info is', JSON.stringify(event));
          console.info('ExclusiveGroupGesture LongPressGesture is called');
        }), new PanGestureHandler({ fingers: 1 }).onActionStart((event) => {
          console.info('event info is', JSON.stringify(event));
          console.info('ExclusiveGroupGesture PanGesture onActionStart is called');
        }).onActionEnd((event) => {
          console.info('event info is', JSON.stringify(event));
          console.info('ExclusiveGroupGesture PanGesture onActionEnd is called');
        })\]
      }))
    } else {
      // Bind a parallel gesture group.
      event.addGesture(new GestureGroupHandler({
        mode: GestureMode.Parallel,
        gestures: \[new TapGestureHandler({ count: 2, fingers: 1 }).onAction((event) => {
          console.info('event info is', JSON.stringify(event));
          console.info('ParallelGroupGesture TapGesture is called');
        }), new LongPressGestureHandler({ repeat: true, fingers: 1 }).onAction((event) => {
          console.info('event info is', JSON.stringify(event));
          console.info('ParallelGroupGesture LongPressGesture is called');
        }), new PanGestureHandler({ fingers: 1 }).onActionStart((event) => {
          console.info('event info is', JSON.stringify(event));
          console.info('ParallelGroupGesture PanGesture onActionStart is called');
        }).onActionEnd((event) => {
          console.info('event info is', JSON.stringify(event));
          console.info('ParallelGroupGesture PanGesture onActionEnd is called');
        })\]
      }))
    }
  }
}

@Entry
@Component
struct Index {
  @State modifier: MyButtonModifier = new MyButtonModifier();

  build() {
    Row() {
      Column() {
        Column()
          .gestureModifier(this.modifier)
          .width(500)
          .height(500)
          .backgroundColor(Color.Gray)

        Button('changeGestureGroupType')
          .onClick(() => {
            this.modifier.isExclusive = !this.modifier.isExclusive;
          })
          .margin({ top: 10 })
      }
      .width('100%')
    }
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/3ZkO65m8R-izDgVzeXE9Ng/en-us_image_0000002537925424.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2E96B095FFCC52AD57A762F20AA3426BA1A399EBDE65034B6D0486D96D18FE08)
