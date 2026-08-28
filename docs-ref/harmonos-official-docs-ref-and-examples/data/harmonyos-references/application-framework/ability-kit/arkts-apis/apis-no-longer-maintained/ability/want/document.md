# Want

Want is a carrier for information transfer between objects (application components). Want can be used as a parameter of [startAbility](../../../dependent-elements-and-definitions/application/uiabilitycontext/document.md#startability) to specify a startup target and information that needs to be carried during startup, for example, **bundleName** and **abilityName**, which respectively indicate the bundle name of the target ability and the ability name in the bundle. When ability A needs to start ability B and transfer some data to ability B, it can use Want a carrier to transfer the data.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/IMzYjLQBSlCvxh02REhHyA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F6A2B153E4683CF347B519963BCA54EFDE8E767436EC4B8445949D693CCEB448)

The APIs of this module are supported since API version 6 and deprecated since API version 9. You are advised to use [@ohos.app.ability.Want](../../../both-models-recommended/ohos-app-ability-want-want/document.md) instead. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import Want from '@ohos.app.ability.Want';

#### Attributes

**System capability**: SystemCapability.Ability.AbilityBase

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | string | No | Yes | ID of the device running the ability. If this field is unspecified, the local device is used. |
| bundleName | string | No | Yes | Bundle name. |
| abilityName | string | No | Yes | Name of the ability. If both **bundleName** and **abilityName** are specified in a Want object, the Want object can match a specific ability. The value of **abilityName** must be unique in an application. |
| uri | string | No | Yes | URI. If **uri** is specified in a Want object, the Want object will match the specified URI information, including **scheme**, **schemeSpecificPart**, **authority**, and **path**. |
| type | string | No | Yes | MIME type, that is, the type of the file to open, for example, **'text/xml'** and **'image/\*'**. For details about the MIME type definition, see [https://www.iana.org/assignments/media-types/media-types.xhtml?utm\_source=ld246.com](https://www.iana.org/assignments/media-types/media-types.xhtml?utm_source=ld246.com). |
| flags | number | No | Yes | How the Want object will be handled. By default, numbers are passed in. For details, see [flags](../../ohos-ability-wantconstant-wantconstant/document.md#flags). |
| action | string | No | Yes | Action to take, such as viewing and sharing application details. In implicit Want, you can define this field and use it together with **uri** or **parameters** to specify the operation to be performed on the data. For details, see [action](../../ohos-ability-wantconstant-wantconstant/document.md#action). For details about the definition and matching rules of implicit Want, see [Matching Rules of Explicit Want and Implicit Want](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/explicit-implicit-want-mappings). |
| parameters | { \[key: string\]: any } | No | Yes | 
Want parameters in the form of custom key-value (KV) pairs. By default, the following keys are carried:

**ohos.aafwk.callerPid**: PID of the caller.

**ohos.aafwk.param.callerToken**: token of the caller.

**ohos.aafwk.param.callerUid**: UID in [bundleInfo](../../bundle/bundleinfo/document.md#bundleinfodeprecated), that is, the application UID in the bundle information.

\- **component.startup.newRules**: whether to enable the new control rule.

\- **moduleName**: module name of the caller. No matter what this field is set to, the correct module name will be sent to the peer.

\- **ohos.dlp.params.sandbox**: available only for DLP files.

 |
| entities | Array<string> | No | Yes | Additional category information (such as browser and video player) of the target ability. It is a supplement to **action** in implicit Want and is used to filter ability types. |

**Example**

-   Basic usage (called in a UIAbility object, where context in the example is the context object of the UIAbility).
    
    import AbilityConstant from '@ohos.app.ability.AbilityConstant';
    import UIAbility from '@ohos.app.ability.UIAbility';
    import Want from '@ohos.app.ability.Want';
    import { BusinessError } from '@ohos.base';
    
    let want: Want = {
      deviceId: '', // An empty deviceId indicates the local device.
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility',
      moduleName: 'entry' // moduleName is optional.
    };
    class MyAbility extends UIAbility{
      onCreate(want: Want, launchParam: AbilityConstant.LaunchParam){
        this.context.startAbility(want, (error: BusinessError) => {
          // Start an ability explicitly. The bundleName, abilityName, and moduleName parameters work together to uniquely identify an ability.
          console.error(\`error.code = ${error.code}\`);
        });
      }
    }
    
-   Passing a file descriptor (FD) (called in a UIAbility object, where context in the example is the context object of the UIAbility):
    
    import fs from '@ohos.file.fs';
    import Want from '@ohos.app.ability.Want';
    import { BusinessError } from '@ohos.base';
    import AbilityConstant from '@ohos.app.ability.AbilityConstant';
    import UIAbility from '@ohos.app.ability.UIAbility';
    
    // ...
    let fd: number = 0;
    try {
      fd = fs.openSync('/data/storage/el2/base/haps/pic.png').fd;
    } catch(e) {
      console.error(\`openSync fail: ${JSON.stringify(e)}\`);
    }
    
    
    let want: Want = {
      deviceId: '', // An empty deviceId indicates the local device.
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility',
      moduleName: 'entry', // moduleName is optional.
      parameters: {
        'keyFd':{'type':'FD', 'value':fd}
      }
    };
    class MyAbility extends UIAbility{
      onCreate(want: Want, launchParam: AbilityConstant.LaunchParam){
        this.context.startAbility(want, (error: BusinessError) => {
          // Start an ability explicitly. The bundleName, abilityName, and moduleName parameters work together to uniquely identify an ability.
          console.error(\`error.code = ${error.code}\`);
        });
      }
    }
    // ...
