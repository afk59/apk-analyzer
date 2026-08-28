# Global Floating Ball Development

#### When to Use

The floating ball is a non-full-screen application window that hovers over the device screen, providing temporary global capabilities for cross-application interaction.

Applications can display key information (such as price comparison, study assistance, or order grabbing) in a small window (floating ball) mode. Once in this compact mode, users can perform other operations on the screen, enhancing their overall experience.

The floating ball feature is supported since API version 20.

#### Constraints

-   For security purposes, the floating ball can be started only when the application is running in the foreground and has granted the ohos.permission.USE\_FLOAT\_BALL permission.

-   Each application can start one floating ball at a time, and a device can have a maximum of two floating balls at the same time. When the maximum number of floating balls is reached, a new floating ball replaces the oldest one.
-   The floating ball feature is available only for mobile phones and tablets.

#### Available APIs

The following are common APIs for the floating ball feature. For more APIs and their usage, see [@ohos.window.floatingBall (Floating Ball Window)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-floatingball).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

isFloatingBallEnabled(): boolean

 | 

Checks whether the current device supports the floating ball feature.

 |
| 

create(config: FloatingBallConfiguration): Promise<FloatingBallController>

 | 

Creates a floating ball controller.

 |
| 

startFloatingBall(params: FloatingBallParams): Promise<void>

 | 

Starts the floating ball.

 |
| 

updateFloatingBall(params: FloatingBallParams): Promise<void>

 | 

Updates the floating ball.

 |
| 

stopFloatingBall(): Promise<void>

 | 

Stops the floating ball.

 |
| 

on(type: 'stateChange', callback: Callback<FloatingBallState>): void

 | 

Registers a callback to listen for floating ball lifecycle state changes.

 |
| 

off(type: 'stateChange', callback?: Callback<FloatingBallState>): void

 | 

Unregisters the callback used to listen for floating ball lifecycle state changes.

 |
| 

on(type: 'click', callback: Callback<void>): void

 | 

Registers a callback to listen for click events of the floating ball.

 |
| 

off(type: 'click', callback?: Callback<void>): void

 | 

Unregisters the callback used to listen for click events of the floating ball.

 |
| 

getFloatingBallWindowInfo(): Promise<FloatingBallWindowInfo>

 | 

Obtains the window information of the floating ball.

 |
| 

restoreMainWindow(want: Want): Promise<void>

 | 

Restores the main window of the application and loads the specified page.

 |

#### Interaction Modes

The floating ball provides the following interaction modes:

-   Touch: The floating ball click event is triggered.
-   Long press: The floating ball vibrates and enters a deletion-ready state, allowing users to delete individual or all floating balls.
-   Drag: Users can manually drag the floating ball to change its position. While dragging, it automatically avoids the status bar, fixed soft keyboard, navigation bar, and other components. In landscape mode, it does not automatically avoid the input method. (For details about how to change the soft keyboard to fixed or floating state, see [Input Method Service](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inputmethodengine#changeflag10)). When released, the floating ball automatically snaps to the nearest side. To delete the floating ball, drag it to the trash bin area (the middle of the bottom) and release.
-   Position memory: The position of the floating ball is saved when it is closed. When it is started next time, it is displayed at the position where it was closed last time. Screen rotation or device restart resets it to the default position (upper-right side of the screen).

#### Floating Ball Specifications and Layout

Currently, four floating ball template layouts are supported. For details, see [FloatingBallTemplate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-floatingball#floatingballtemplate).

-   Static layout, which provides an icon and a title.
-   Standard text layout, which provides a title and content.
-   Emphasized text layout, which provides an icon, a title, and content.
-   Plain text layout, which provides only a title and can be displayed in two lines.

Currently, the overall width of the floating ball ranges from 70 vp to 98 vp, and the height is 40 vp. The font size of the title and content cannot be customized.

The following diagrams illustrate different template layouts. The actual display may vary by language or content.

**Figure 1** Static layout

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/IW-zEnLURG6McNaOFNKdEg/en-us_image_0000002497901580.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061945Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=62C9C0A2491BA72902E90CCD153BC314F34E093F7DA97447F87D8C914C3AD786)

**Figure 2** Static layout - extra-long title

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/KZ3uFCA0Ql2-GnPgKm9PzQ/en-us_image_0000002497741592.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061945Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=70B04C35CA574D66A25F9163F3D1F72BF72B344FEE15A349FA4EAC814B6D0452)

**Figure 3** Standard text layout

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/eAfK-qVLQNywIG2WmVxkSQ/en-us_image_0000002529701531.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061945Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6D985DA9D27E2F20663A750DF2884651DCD15BC1829D0E2CBDBA9A8FF42508FE)

**Figure 4** Standard text layout - extra-long content

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/VTxW24XXTwuyw--zD1oKeQ/en-us_image_0000002529581567.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061945Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=41EE7DA446301E3B2CAA15BB4569D2D8C53B4CF3592D96812F8AA911778651EB)

**Figure 5** Emphasized text layout

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/2EJdB0uYTgeOR011Pc_LkQ/en-us_image_0000002497901576.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061945Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3EDEB6378AEF57F2A794D64E6FEFD5D9B89BA85278C8B72C518F9DE9F1CDFE6E)

**Figure 6** Emphasized text layout - extra-long content

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/ty_W4KXSQgK6vj_xAUL25Q/en-us_image_0000002529581569.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061945Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=240FF8D0C18B0E2843BD4CC4A7C199A2345209AE5C46984AE356B8DBD70D6650)

**Figure 7** Emphasized text layout - icon

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/lTM8HsrlT-WN_r80kHHj1Q/en-us_image_0000002497901578.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061945Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CD9FE9C781F15BB27F4A24E2EB336B9DACB7FF2F7C22772E2D85232535B16D16)

**Figure 8** Emphasized text layout - icon and extra-long content  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/cG-5-4TDQuqEXREf_deWSQ/en-us_image_0000002529581565.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061945Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=072BB0F96A6B42375A359DC81A972896A61ACDA55D88CA11F10C5D1E4C7E88DC)

**Figure 9** Plain text layout  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/VEAnOoR_TKC3tl5Y9PvG-g/en-us_image_0000002497741588.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061945Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9BCEAB0F8D03447EA33572CADDF02F4C7A7084314FB9B4E7C9ED3B2100F7F4C4)

**Figure 10** Plain text layout - extra-long title  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/MNbb5Iu_SzeanhnfQRh8nw/en-us_image_0000002529701533.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061945Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=31B4D5753AAB5E16E6DA6C202DA7A7740DDB28806EE36437C6CADB2A9A5BD7C2)

When two applications start the floating ball, they merge, as shown below. The overall height is 76 vp.

**Figure 11** Merged floating ball display  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/uWCIP9E8RmawlC-kk71h5g/en-us_image_0000002497741590.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061945Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=92A81312B6ADBCED19C3B4A5665386A592EF6487A1C216166B2B83BD6090FDE0)

#### How to Develop

1.  Import the module and declare the floating ball controller.
2.  Use [create()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-floatingball#floatingballcreate) to create a floating ball controller instance, register the click event callback and state change event callback, and use [startFloatingBall()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-floatingball#startfloatingball) to start the floating ball.
3.  Use [updateFloatingBall()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-floatingball#updatefloatingball) to update the information about the floating ball to control the content displayed.
4.  Use [stopFloatingBall()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-floatingball#stopfloatingball) to stop the floating ball. When there is no need to display the floating ball, you can stop it as required.
    
    // Index.ets
    // This page uses the button click event to display the basic operations of the floating ball.
    import { floatingBall } from '@kit.ArkUI';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { Want } from '@kit.AbilityKit';
    
    @Entry
    @Component
    struct Index {
      // Declare the floating ball controller.
      private floatingBallController: floatingBall.FloatingBallController | undefined = undefined;
      build() {
        Row({ space: 6 }) {
          Button('Create').onClick(async () => {
            // Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
            if (!this.floatingBallController) {
              this.floatingBallController = await floatingBall.create({
                context: this.getUIContext().getHostContext()
              });
            }
            if (this.floatingBallController) {
              // Register the touch callback event.
              this.floatingBallController?.on('click', () => {
                console.info('Floating-ball onClickEvent');
                let want: Want = {
                  // Replace it with the actual bundle name.
                  bundleName: 'xxx.xxx.xxx',
                  abilityName: 'MainAbility'
                };
                // Use Promise for asynchronous callback.
                this.floatingBallController?.restoreMainWindow(want)
                .then(() => {
                  console.info('Success in restoring floating-ball main window. ');
                }).catch((err: BusinessError) => {
                  console.error(\`Failed to restore floating-ball main window. Cause code: ${err.code}, message: ${err.message}\`);
                });
              });
              // Register a listener for state change events.
              this.floatingBallController?.on('stateChange', (state: floatingBall.FloatingBallState) => {
                console.info('Floating-ball stateChange: ' + state);
                if (state === floatingBall.FloatingBallState.STOPPED) {
                  this.floatingBallController?.off('stateChange');
                  this.floatingBallController?.off('click');
                  this.floatingBallController = undefined;
                }
              });
              // Start the floating ball.
              let startParams: floatingBall.FloatingBallParams = {
                template: floatingBall.FloatingBallTemplate.EMPHATIC,
                title: 'title',
                content: 'content'
              };
              this.floatingBallController?.startFloatingBall(startParams)
              .then(() => {
                console.info(\`Succeeded in starting floating-ball.\`);
              }).catch((err: BusinessError) => {
                console.error(\`Failed to start floating-ball. Cause:${err.code}, message:${err.message}\`);
              });
            }
          })
          // Update the floating ball information.
          Button('Update').onClick(() => {
            const arr = \['aa', 'bb', 'cc', 'dd'\]
            let updateParams: floatingBall.FloatingBallParams = {
              template: floatingBall.FloatingBallTemplate.EMPHATIC,
              title: 'title2' + arr\[Math.floor(Math.random() \* 3)\],
              content: 'content2'
            };
            this.floatingBallController?.updateFloatingBall(updateParams).then(() => {
              console.info(\`Succeeded in updating floating-ball.\`);
            }).catch((err: BusinessError) => {
              console.error(\`Failed to update floating-ball. Cause:${err.code}, message:${err.message}\`);
            });
          })
          // Stop the floating ball.
          Button('Stop').onClick(() => {
            // stop is an asynchronous process. The actual deletion result needs to be obtained through the stateChange callback.
            this.floatingBallController?.stopFloatingBall().then(() => {
              console.info(\`Succeeded in stopping floating-ball.\`);
            }).catch((err: BusinessError) => {
              console.error(\`Failed to stop floating-ball. Cause:${err.code}, message:${err.message}\`);
            });
          })
        }
        .width('100%')
        .height('100%')
        .justifyContent(FlexAlign.Center)
      }
    }
