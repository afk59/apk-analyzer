# @ohos.app.ability.Want (Want)

Want is a carrier for information transfer between objects (application components).

A typical scenario is when a UIAbility (for example, UIAbility A) needs to launch another UIAbility (for example, UIAbility B) and pass some data along. In this case, a Want can be used as the medium. For example, in the **want** parameter of the **startAbility** API, you can specify the target ability using the **abilityName** field or include additional data via the **parameters** field.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/Qk7O53uPQrOjvVr4UdTUQg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062208Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E66C8BF92FDE3AE3D63CFC4B5C8FE59860D34772AB0F6E7EB9B212F5EE2667F8)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Constraints

Launching an ability is subject to IPC limitations. The maximum data supported in the **Want** field is 100 KB.

#### Modules to Import

import { Want } from '@kit.AbilityKit';

#### Want

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityBase

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | string | No | Yes | Device ID. It indicates the device ID of the target application in the application launch scenario. If not specified, it defaults to the current device. |
| bundleName | string | No | Yes | Bundle name of the application. It represents the bundle name of the target application in the application launch scenario. |
| moduleName | string | No | Yes | 
Module name of the application. It represents the module name of the target application in the application launch scenario.

**NOTE**

If the ability belongs to a [HAR](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/har-package) module, **moduleName** must be set to the name of the [HAP](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/hap-package) or [HSP](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/in-app-hsp) module that depends on this HAR.

 |
| abilityName | string | No | Yes | Ability name of the application. It represents the ability name of the target application in the application launch scenario. If both **bundleName** and **abilityName** are specified in a Want object, the Want object can match a specific ability. The value of **abilityName** must be unique in an application. |
| action | string | No | Yes | Action to take, such as viewing and sharing application details. In implicit Want, you can define this field and use it together with **uri** or **parameters** to specify the operation to be performed on the data. For details about the definition and matching rules of implicit Want, see [Matching Rules of Explicit Want and Implicit Want](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/explicit-implicit-want-mappings). |
| entities | Array<string> | No | Yes | Additional category information (such as browser and video player) of the ability. It is a supplement to the **action** field for implicit Want. and is used to filter ability types. |
| uri | string | No | Yes | URI, which is used with **type** to specify the data type to be processed in the application launch scenario. If **uri** is specified in a Want, the Want will match the specified URI information, including **scheme**, **schemeSpecificPart**, **authority**, and **path**. |
| type | string | No | Yes | MIME type, that is, the type of the file to open, for example, **'text/xml'** and **'image/\*'**. For details about the MIME type definition, see [Media Types](https://www.iana.org/assignments/media-types/media-types.xhtml?utm_source=ld246.com). |
| parameters | Record<string, Object> | No | Yes | 

List of parameters in the Want object.

1\. The values of the following keys are assigned by the system. Manual settings do not take effect, since the system automatically changes the values to the actual values during data transfer.

\- **ohos.aafwk.param.callerPid**: PID of the caller. The value is a string.

\- **ohos.aafwk.param.callerBundleName**: bundle name of the caller. The value is a string.

\- **ohos.aafwk.param.callerAbilityName**: ability name of the caller. The value is a string.

\- **ohos.aafwk.param.callerNativeName**: process name of the caller when the native method is called. The value is a string.

\- **ohos.aafwk.param.callerAppId**: appId of the caller. The value is a string.

\- **ohos.aafwk.param.callerAppIdentifier**: appIdentifier of the caller. The value is a string.

\- **ohos.aafwk.param.callerToken**: token of the caller. The value is a string.

\- **ohos.aafwk.param.callerUid**: UID in [BundleInfo](../../dependent-elements-and-definitions/bundlemanager/bundleinfo/document.md#bundleinfo-1), that is, the application's UID in the bundle information. The value is a number.

\- **ohos.param.callerAppCloneIndex**: clone index of the caller. The value is of the numeric type.

\- **component.startup.newRules**: enabled status of the new control rule. The value is of the Boolean type.

\- **moduleName**: module name of the caller. The value is a string.

\- **ohos.ability.params.abilityRecoveryRestart**: support for ability restart upon fault recovery. The value is of the Boolean type.

\- **ohos.extra.param.key.showMode**: mode to show the atomic service startup. The value is an enumerated value of [wantConstant.ShowMode](../ohos-app-ability-wantconstant-want-constants/document.md#showmode12).

**NOTE**

In cross-device scenarios, the following fields do not take effect and cannot be used for identity or permission verification: **ohos.aafwk.param.callerPid**, **ohos.aafwk.param.callerToken**, and **ohos.aafwk.param.callerUid**.

2\. Certain keys are defined by the system, and their values need to be manually assigned. For details about the keys and their values, see [wantConstant.Params](../ohos-app-ability-wantconstant-want-constants/document.md#params).

3\. In addition to the foregoing cases, applications may further agree on the key-value pairs to transfer.

**NOTE**

For details about the constants of **Params** in **want**, see [wantConstant](../ohos-app-ability-wantconstant-want-constants/document.md).

Note that a maximum of 100 KB data that can be transferred by using **WantParams**. If the data volume exceeds 100 KB, transfer data in [WriteRawDataBuffer](../../../../ipc-kit/arkts-apis/ohos-rpc-rpc/document.md#writerawdatabuffer11) or [uri](../../../../arkts/arkts-apis/ohos-uri-uri-string-parsing/document.md) mode.

The values of **parameters** must be of the following basic data types: String, Number, Boolean, Object, undefined, and null. Functions in an object cannot be transferred.

 |
| flags | number | No | Yes | 

How the Want object will be handled. The value is of the enumeration type [Flags](../ohos-app-ability-wantconstant-want-constants/document.md#flags). A numeric value should be passed by default.

For example, if the value is 0x00000001 (**wantConstant.Flags.FLAG\_AUTH\_READ\_URI\_PERMISSION**), the receiver is temporarily granted the permission to read the data pointed to by the URI.

 |
| fds15+ | Record<string, number> | Yes | Yes | 

File descriptor (FD). The FD written by the launcher in the application launch scenario is set to this parameter.

**Atomic service API**: This API can be used in atomic services since API version 15.

 |

**Example**

-   Basic usage: called in a UIAbility object, as shown in the example below. For details about how to obtain the context, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).
    
    import { UIAbility, Want } from '@kit.AbilityKit';
    import { window } from '@kit.ArkUI';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    export default class EntryAbility extends UIAbility {
      onWindowStageCreate(windowStage: window.WindowStage): void {
        let want: Want = {
          deviceId: '', // An empty deviceId indicates the local device.
          bundleName: 'com.example.myapplication',
          abilityName: 'FuncAbility',
          moduleName: 'entry' // moduleName is optional.
        };
    
        this.context.startAbility(want, (err: BusinessError) => {
          if (err.code) {
            // Start an ability explicitly. The bundleName, abilityName, and moduleName parameters work together to uniquely identify an ability.
            console.error(\`Failed to startAbility. Code: ${err.code}, message: ${err.message}\`);
          }
        });
      }
    }
    
-   Currently, the following data types are supported: string, number, Boolean, object, array, and file descriptor (FD).
    
    -   String
        
        import { UIAbility, Want } from '@kit.AbilityKit';
        import { window } from '@kit.ArkUI';
        import { BusinessError } from '@kit.BasicServicesKit';
        
        export default class EntryAbility extends UIAbility {
          onWindowStageCreate(windowStage: window.WindowStage): void {
            let want: Want = {
              bundleName: 'com.example.myapplication',
              abilityName: 'FuncAbility',
              parameters: {
                keyForString: 'str',
              },
            };
        
            this.context.startAbility(want, (err: BusinessError) => {
              if (err.code) {
                console.error(\`Failed to startAbility. Code: ${err.code}, message: ${err.message}\`);
              }
            });
          }
        }
        
    -   Number
        
        import { UIAbility, Want } from '@kit.AbilityKit';
        import { window } from '@kit.ArkUI';
        import { BusinessError } from '@kit.BasicServicesKit';
        
        export default class EntryAbility extends UIAbility {
          onWindowStageCreate(windowStage: window.WindowStage): void {
            let want: Want = {
              bundleName: 'com.example.myapplication',
              abilityName: 'FuncAbility',
              parameters: {
                keyForInt: 100,
                keyForDouble: 99.99,
              },
            };
        
            this.context.startAbility(want, (err: BusinessError) => {
              if (err.code) {
                console.error(\`Failed to startAbility. Code: ${err.code}, message: ${err.message}\`);
              }
            });
          }
        }
        
    -   Boolean
        
        import { UIAbility, Want } from '@kit.AbilityKit';
        import { window } from '@kit.ArkUI';
        import { BusinessError } from '@kit.BasicServicesKit';
        
        export default class EntryAbility extends UIAbility {
          onWindowStageCreate(windowStage: window.WindowStage): void {
            let want: Want = {
              bundleName: 'com.example.myapplication',
              abilityName: 'FuncAbility',
              parameters: {
                keyForBool: true,
              },
            };
        
            this.context.startAbility(want, (err: BusinessError) => {
              if (err.code) {
                console.error(\`Failed to startAbility. Code: ${err.code}, message: ${err.message}\`);
              }
            });
          }
        }
        
    -   Object
        
        import { UIAbility, Want } from '@kit.AbilityKit';
        import { window } from '@kit.ArkUI';
        import { BusinessError } from '@kit.BasicServicesKit';
        
        export default class EntryAbility extends UIAbility {
          onWindowStageCreate(windowStage: window.WindowStage): void {
            let want: Want = {
              bundleName: 'com.example.myapplication',
              abilityName: 'FuncAbility',
              parameters: {
                keyForObject: {
                  keyForObjectString: 'str',
                  keyForObjectInt: -200,
                  keyForObjectDouble: 35.5,
                  keyForObjectBool: false,
                },
              },
            };
        
            this.context.startAbility(want, (err: BusinessError) => {
              if (err.code) {
                console.error(\`Failed to startAbility. Code: ${err.code}, message: ${err.message}\`);
              }
            });
          }
        }
        
    -   Array
        
        import { UIAbility, Want } from '@kit.AbilityKit';
        import { window } from '@kit.ArkUI';
        import { BusinessError } from '@kit.BasicServicesKit';
        
        export default class EntryAbility extends UIAbility {
          onWindowStageCreate(windowStage: window.WindowStage): void {
            let want: Want = {
              bundleName: 'com.example.myapplication',
              abilityName: 'FuncAbility',
              parameters: {
                keyForArrayString: \['str1', 'str2', 'str3'\],
                keyForArrayInt: \[100, 200, 300, 400\],
                keyForArrayDouble: \[0.1, 0.2\],
                keyForArrayObject: \[{ obj1: 'aaa' }, { obj2: 100 }\],
              },
            };
        
            this.context.startAbility(want, (err: BusinessError) => {
              if (err.code) {
                console.error(\`Failed to startAbility. Code: ${err.code}, message: ${err.message}\`);
              }
            });
          }
        }
        
    -   FD
        
        import { UIAbility, Want } from '@kit.AbilityKit';
        import { window } from '@kit.ArkUI';
        import { BusinessError } from '@kit.BasicServicesKit';
        import { fileIo } from '@kit.CoreFileKit';
        
        export default class EntryAbility extends UIAbility {
          onWindowStageCreate(windowStage: window.WindowStage): void {
            let fd: number = 0;
        
            try {
              fd = fileIo.openSync('/data/storage/el2/base/haps/pic.png').fd;
            } catch (err) {
              let code = (err as BusinessError).code;
              let message = (err as BusinessError).message;
              console.error(\`Failed to openSync. Code: ${code}, message: ${message}\`);
            }
            let want: Want = {
              deviceId: '', // An empty deviceId indicates the local device.
              bundleName: 'com.example.myapplication',
              abilityName: 'FuncAbility',
              moduleName: 'entry', // moduleName is optional.
              parameters: {
                'keyFd': { 'type': 'FD', 'value': fd } // {'type':'FD', 'value':fd} is a fixed usage, indicating that the data is a file descriptor.
              }
            };
        
            this.context.startAbility(want, (err: BusinessError) => {
              if (err.code) {
                console.error(\`Failed to startAbility. Code: ${err.code}, message: ${err.message}\`);
              }
            });
          }
        }
        
    -   **parameters** usage: **parameters** carries custom parameters. It is transferred by UIAbilityA to UIAbilityB and obtained from UIAbilityB.
        
        // (1) UIAbilityA calls startAbility to start UIAbilityB.
        import { UIAbility, Want } from '@kit.AbilityKit';
        import { window } from '@kit.ArkUI';
        import { BusinessError } from '@kit.BasicServicesKit';
        
        export default class EntryAbility extends UIAbility {
          onWindowStageCreate(windowStage: window.WindowStage): void {
            let want: Want = {
              bundleName: 'com.example.myapplication',
              abilityName: 'UIAbilityB',
              parameters: {
                developerParameters: 'parameters',
              },
            };
        
            this.context.startAbility(want, (err: BusinessError) => {
              if (err.code) {
                console.error(\`Failed to startAbility. Code: ${err.code}, message: ${err.message}\`);
              }
            });
          }
        }
        
        // (2) If the UIAbilityB instance is started for the first time, it enters the onCreate lifecycle.
        import { UIAbility, Want, AbilityConstant } from '@kit.AbilityKit';
        
        class UIAbilityB extends UIAbility {
          onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
            console.info(\`onCreate, want parameters: ${want.parameters?.developerParameters}\`);
          }
        }
        
    -   Usage of the keys of [wantConstant](../ohos-app-ability-wantconstant-want-constants/document.md) in **parameters**.
        
        import { UIAbility, Want, wantConstant } from '@kit.AbilityKit';
        import { window } from '@kit.ArkUI';
        import { BusinessError } from '@kit.BasicServicesKit';
        
        export default class EntryAbility extends UIAbility {
          onWindowStageCreate(windowStage: window.WindowStage): void {
            let want: Want = {
              bundleName: 'com.example.myapplication',
              abilityName: 'FuncAbility',
              parameters: {
                \[wantConstant.Params.CONTENT\_TITLE\_KEY\]: 'contentTitle',
              },
            };
        
            this.context.startAbility(want, (err: BusinessError) => {
              if (err.code) {
                console.error(\`Failed to startAbility. Code: ${err.code}, message: ${err.message}\`);
              }
            });
          }
        }
        
    -   Obtain the information about the party that starts the UIAbility from **parameters**.
        
        For details, see [Obtaining Information About the UIAbility Launcher](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-information-about-the-uiability-launcher).
