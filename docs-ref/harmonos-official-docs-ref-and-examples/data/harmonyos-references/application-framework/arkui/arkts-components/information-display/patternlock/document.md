# PatternLock

The **PatternLock** component allows users to use a pattern password for authentication. It enters the input state once a finger is pressed against it, and exits the input state and completes the input once the finger leaves the screen.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/sSjy71M2SG27b8BVPEQ7PA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9B263DC2E3E46712B940312342B1F03C056B9FDABDDD8C8C358C0CF1A415290F)

-   This component is supported since API version 9. Updates will be marked with a superscript to indicate their earliest API version.
    
-   If you require additional features, use [custom components](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-create-custom-components). For example, the custom component [CustomPatternLock](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/UI/CustomPatternLock) implements the pattern lock function using the [Canvas](../../canvas-drawing/canvas/document.md) component. You can extend its functionality as required.
    

#### Child Components

Not supported

#### APIs

PatternLock(controller?: PatternLockController)

Creates a pattern lock component.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| controller | [PatternLockController](#patternlockcontroller) | No | Controller of a component to reset the component status. |

#### Attributes

In addition to the [universal attributes](../../universal-attributes/document.md), the following attributes are supported.

#### \[h2\]sideLength

sideLength(value: Length)

Sets the width and height (same value) of the component. If this attribute is set to **0** or a negative number, the component is not displayed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/6AMdG2tURA6TIDTaCW3SmA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F0E9355AF792469932BB77739CEBAB478606C358631A89ADF2F1F162D3D64069)

When the **PatternLock** component has the universal attribute [aspectRatio](../../universal-attributes/layout-and-borders/layout-constraints/document.md#aspectratio) set and the ratio is not equal to 1 (the component is constrained to a rectangle), the nine‑grid pattern is still drawn as a square, which exceeds the component's bounds.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Length](../../common-definitions/basic-types/document.md#length) | Yes | Width and height of the component. Default value: **288vp** |

#### \[h2\]circleRadius

circleRadius(value: Length)

Sets the radius of the dots in a grid. If this attribute is set to **0** or a negative value, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Length](../../common-definitions/basic-types/document.md#length) | Yes | 
Radius of the dots in a grid.

Default value: **6vp**

Value range: (0, sideLength/11\]. If the value is less than or equal to **0**, the default value is used. If the value exceeds the maximum value, the maximum value is used.

 |

#### \[h2\]backgroundColor

backgroundColor(value: ResourceColor)

Sets the background color.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/FG_hJBHRR0K-cXRPw8yF_w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FD5A356E3A0FB1DD3B435049194748C7FCA5CAEBFF90574706F274A3B05D973C)

This API can be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | Background color. |

#### \[h2\]regularColor

regularColor(value: ResourceColor)

Sets the fill color of the grid dot in the unselected state.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | 
Fill color of the grid dot in the unselected state.

Default value: **'#ff182431'**

 |

#### \[h2\]selectedColor

selectedColor(value: ResourceColor)

Fill color of the grid dot in the selected state.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | 
Fill color of the grid dot in the selected state.

Default value: **'#ff182431'**

 |

#### \[h2\]activeColor

activeColor(value: ResourceColor)

Sets the fill color of the grid dot in the activated state, which is when the dot is highlighted but not selected.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | 
Fill color of the grid dot in the activated state.

Default value: **'#ff182431'**

 |

#### \[h2\]pathColor

pathColor(value: ResourceColor)

Sets the path color.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | 
Path color.

Default value: **'#33182431'**

 |

#### \[h2\]pathStrokeWidth

pathStrokeWidth(value: number | string)

Sets the width of the path stroke. If this attribute is set to **0** or a negative value, the path stroke is not displayed.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | string | Yes | 
Width of the path stroke.

Default value: **12vp**

Value range: (0, sideLength/3\]. If the value is set to **0** or a negative number, the line is not displayed. If the value exceeds the maximum value, the maximum value is used.

 |

#### \[h2\]autoReset

autoReset(value: boolean)

Sets whether to allow the user to reset the component status (that is, clear the input) by touching the component again after the input is complete.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether to allow the user to reset the component status (that is, clear the input) by touching the component again after the input is complete.

**true**: yes; **false**: no

Default value: **true**

 |

#### \[h2\]activateCircleStyle12+

activateCircleStyle(options: Optional<CircleStyleOptions>)

Sets the background circle style for the dots in a grid when they are in the activated state.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | Optional<[CircleStyleOptions](#circlestyleoptions12)\> | Yes | Background circle style of the dots in the activated state. |

#### \[h2\]skipUnselectedPoint15+

skipUnselectedPoint(skipped: boolean)

Sets whether unselected dots in the grid are automatically skipped when the password path passes over them.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| skipped | boolean | Yes | 
Whether unselected dots in the grid are automatically skipped when the password path passes over them.

**true** to skip the unselected dots when the password path passes over them; **false** otherwise. Default value: **false**

 |

#### Events

In addition to the [universal events](../../universal-events/document.md), the following events are supported.

#### \[h2\]onPatternComplete

onPatternComplete(callback: (input: Array<number>) => void)

Invoked when the pattern password input is complete.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| input | Array<number> | Yes | Array of digits representing the indices of the selected grid dots, in the order they were connected. Grid dots are indexed row-wise from top to bottom, left to right: The first row contains indices 0, 1, 2; the second row 3, 4, 5; and the third row 6, 7, 8. |

#### \[h2\]onDotConnect11+

onDotConnect(callback: [Callback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<number>)

Invoked when a grid dot is connected during pattern password input.

The callback parameter is an array of digits, where each digit represents the index of a selected grid dot, listed in the order they were connected. Grid dots are indexed row-wise from top to bottom, left to right: The first row contains indices 0, 1, 2; the second row 3, 4, 5; and the third row 6, 7, 8.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/ncsIx7UKRZ2bVflLCyVM7w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=123709535488FD13009BB0B5509D25704798FE6A0DA457FE46D80033A3A462E3)

This API can be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [Callback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<number> | Yes | Invoked when a grid dot is connected during pattern password input. |

#### CircleStyleOptions12+

Describes the parameters of the ring style.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| color | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 
Color of the background circle.

Default value: **'#33182431'**

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| radius | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | Yes | 

Radius of the background circle.

Default value: 1.833 times (that is, 11/6) of the value of [circleRadius](#circleradius)

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| enableWaveEffect | boolean | No | Yes | 

Whether to enable the wave effect after a grid dot is selected.

**true** to enable; **false** otherwise.

Default value: **true**

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| enableForeground15+ | boolean | No | Yes | 

Whether the background circle is displayed above the grid dot.

**true**: The background ring is displayed above the grid dot to cover the grid dot. **false**: The background ring is displayed below the grid dot and does not cover the grid dot.

Default value: **false**

**Atomic service API**: This API can be used in atomic services since API version 15.

 |

#### PatternLockController

Controller of the **PatternLock** component, which is used to reset the component status.

## Objects to Import

let patternLockController: PatternLockController = new PatternLockController()

#### \[h2\]constructor

constructor()

A constructor used to create a **PatternLockController** instance.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]reset

reset()

Resets the component status.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]setChallengeResult11+

setChallengeResult(result: PatternLockChallengeResult): void

Challenge result of the pattern password.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| result | [PatternLockChallengeResult](#patternlockchallengeresult11) | Yes | Authentication challenge result of the pattern password. The status can be correct or incorrect. |

#### PatternLockChallengeResult11+

Authentication challenge result of the pattern password.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| CORRECT | 1 | The pattern password is correct. |
| WRONG | 2 | The pattern password is incorrect. |

#### Example

## Example 1: Creating a Pattern Lock

This example shows the basic usage of the **PatternLock** component.

// xxx.ets
@Entry
@Component
struct PatternLockExample {
  @State passwords: number\[\] = \[\];
  @State message: string = 'please input password!';
  private patternLockController: PatternLockController = new PatternLockController();

  build() {
    Column() {
      Text(this.message).textAlign(TextAlign.Center).margin(20).fontSize(20)
      PatternLock(this.patternLockController)
        .sideLength(200)
        .circleRadius(9)
        .pathStrokeWidth(5)
        .activeColor('#707070')
        .selectedColor('#707070')
        .pathColor('#707070')
        .backgroundColor('#F5F5F5')
        .regularColor(Color.Black)
        .skipUnselectedPoint(false)
        .autoReset(true)
        .onDotConnect((index: number) => {
          console.info('onDotConnect index: ' + index);
        })
    }.width('100%').height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/zPOyl3GySt2Ejp_OIHzR5w/en-us_image_0000002568685503.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B5F24E1FF13838584EFE56F15038039CA34125572EF49B1F9BA53DF5BB557378)

## Example 2: Verifying the Password

This example demonstrates how to use the [sideLength](#sidelength) attribute to set the grid size, how to use the [circleRadius](#circleradius) attribute to set the grid dot style, and how to use the [onPatternComplete](#onpatterncomplete) attribute to set the callback for password input.

When the user completes the password input, different responses are given based on the input:

\- If the password length is less than 5, a message is displayed to prompt the user to re-enter the password.

\- After the first input, a message is displayed to prompt the user to enter the password again.

\- After the second input, the system checks whether the two inputs match. If they match, a message is displayed to indicate that the password setup is successful; otherwise, the user is prompted to re-enter the password.

The user can click **Reset PatternLock** to reset the password lock.

// xxx.ets
import { LengthUnit } from '@kit.ArkUI';

@Entry
@Component
struct PatternLockExample {
  @State passwords: number\[\] = \[\];
  @State message: string = 'please input password!';
  private patternLockController: PatternLockController = new PatternLockController();

  build() {
    Column() {
      Text(this.message).textAlign(TextAlign.Center).margin(20).fontSize(20)
      PatternLock(this.patternLockController)
        .sideLength(200)
        .circleRadius(9)
        .pathStrokeWidth(5)
        .activeColor('#707070')
        .selectedColor('#707070')
        .pathColor('#707070')
        .backgroundColor('#F5F5F5')
        .autoReset(true)
        .activateCircleStyle({
          color: '#707070',
          radius: { value: 16, unit: LengthUnit.VP },
          enableWaveEffect: true
        })
        .onDotConnect((index: number) => {
          console.info('onDotConnect index: ' + index);
        })
        .onPatternComplete((input: Array<number>) => {
          // If the length of the entered password is less than 5, the system prompts the user to enter the password again.
          if (input.length < 5) {
            this.message = 'The password length needs to be greater than 5, please enter again.';
            return;
          }
          // Check whether the password length is greater than 0.
          if (this.passwords.length > 0) {
            // Check whether the two passwords are the same. If yes, the system displays a message indicating that the password is set successfully. If no, the system prompts the user to enter the password again.
            if (this.passwords.toString() === input.toString()) {
              this.passwords = input;
              this.message = 'Set password successfully: ' + this.passwords.toString();
              this.patternLockController.setChallengeResult(PatternLockChallengeResult.CORRECT);
            } else {
              this.message = 'Inconsistent passwords, please enter again.';
              this.patternLockController.setChallengeResult(PatternLockChallengeResult.WRONG);
            }
          } else {
            // The system prompts the user to enter the password again.
            this.passwords = input;
            this.message = 'Please enter again.';
          }
        })
      Button('Reset PatternLock').margin(30).onClick(() => {
        // Reset the pattern lock.
        this.patternLockController.reset();
        this.passwords = \[\];
        this.message = 'Please input password';
      })
    }.width('100%').height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/aRji_nveT9qRjv5TPHpyaQ/en-us_image_0000002568765513.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=87B4F505B19C1832EAD11180E919D9DD7CF345C44382C62794EBE72F88041F70)
