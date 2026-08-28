# @ohos.web.WebNativeMessagingExtensionContext (Web Native Messaging Extension Context)

WebNativeMessagingExtensionContext is the context of web native message extension and is inherited from ExtensionContext. It provides the capability of exchanging messages with WebNativeMessagingExtension.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/0MuWs5AyTd2y6js4URjstQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062314Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=583A5EC7B38891556310E10B15A935FFEA8CF57543BC2E026B20949CF8CA8332)

The initial APIs of this module are supported since API version 21. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module can be used only in the stage model.

#### Modules to Import

import { WebNativeMessagingExtensionAbility, ConnectionInfo } from '@kit.ArkWeb';

#### WebNativeMessagingExtensionContext

Represents the context of web native message extension, including the required interaction capabilities.

#### \[h2\]startAbility

startAbility(want: Want, options?: StartOptions): Promise<void>

Starts an ability using a promise.

**System capability**: SystemCapability.Web.Webview.Core

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | [Want](../../../ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | Information about the ability to start. |
| options | [StartOptions](../../../ability-kit/arkts-apis/stage-model/ohos-app-ability-startoptions-optional-parameters-of-startability/document.md) | No | Startup options. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../ability-kit/error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The application does not have permission to call the interface. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000008 | The crowdtesting application expires. |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000010 | The call with the continuation and prepare continuation flag is forbidden. |
| 16000011 | The context does not exist. |
| 16000012 | The application is controlled. |
| 16000013 | The application is controlled by EDM. |
| 16000019 | No matching ability is found. |
| 16000050 | Internal error. Possible causes: 1. Failed to connect to the system service; 2. The system service failed to communicate with dependency module. |
| 16000055 | Installation-free timed out. |
| 16000071 | App clone is not supported. |
| 16000072 | App clone or multi-instance is not supported. |
| 16000073 | The app clone index is invalid. |
| 16000076 | The app instance key is invalid. |
| 16000077 | The number of app instances reaches the limit. |
| 16000078 | The multi-instance is not supported. |
| 16000079 | The APP\_INSTANCE\_KEY cannot be specified. |
| 16000080 | Creating a new instance is not supported. |

**Example**

import { WebNativeMessagingExtensionAbility, ConnectionInfo } from '@kit.ArkWeb';
import { Want } from '@kit.AbilityKit';

export class MyWebNativeMessagingExtension extends WebNativeMessagingExtensionAbility {
  onConnectNative(info: ConnectionInfo): void {
    const abilityWant: Want = {
    bundleName: 'com.example.mybundle',
    abilityName: 'MainAbility'
    };
    try {
        const context = this.context; // Obtain the WebNativeMessagingExtensionContext instance.
        context.startAbility(abilityWant);
        console.info('Ability started successfully');
    } catch (err) {
        console.error(\`Failed to start ability. Code: ${err.code}, Message: ${err.message}\`);
    }
  }
}

#### \[h2\]terminateSelf

terminateSelf(): Promise<void>

Destroys the current native web message extension. This method returns a promise for asynchronous processing.

**System capability**: SystemCapability.Web.Webview.Core

**Model restriction**: This API can be used only in the stage model.

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Ability Error Codes](../../../ability-kit/error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. Possible causes: 1. Failed to connect to the system service; 2. The system service failed to communicate with dependency module. |

**Example**

import { WebNativeMessagingExtensionAbility, ConnectionInfo } from '@kit.ArkWeb';

export class MyWebNativeMessagingExtension extends WebNativeMessagingExtensionAbility {
  onConnectNative(info: ConnectionInfo): void {
    try {
        const context = this.context; // Obtain the WebNativeMessagingExtensionContext instance.
        context.terminateSelf();
        console.info('Extension terminated successfully');
    } catch (err) {
        console.error(\`Failed to terminate extension. Code: ${err.code}, Message: ${err.message}\`);
    }
  }
}

#### \[h2\]stopNativeConnection

stopNativeConnection(connectionId: number): Promise<void>

Stops a native connection. This API uses a promise to return the result.

**System capability**: SystemCapability.Web.Webview.Core

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| connectionId | number | Yes | ID of the connection to stop. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The application does not have permission to call the interface. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. Possible causes: 1. Failed to connect to the system service; 2. The system service failed to communicate with dependency module. |

**Example**

import { WebNativeMessagingExtensionAbility, ConnectionInfo } from '@kit.ArkWeb';

export class MyWebNativeMessagingExtension extends WebNativeMessagingExtensionAbility {
  onConnectNative(info: ConnectionInfo): void {
    const CONNECTION\_ID = 12345; // Actual connection ID.
    try {
        const context = this.context;// Obtain the WebNativeMessagingExtensionContext instance.
        context.stopNativeConnection(CONNECTION\_ID);
        console.info('Native connection stopped successfully');
    } catch (err) {
        console.error(\`Failed to stop native connection. Code: ${err.code}, Message: ${err.message}\`);
    }
  }
}
