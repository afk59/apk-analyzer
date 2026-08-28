# NavPushPathHelper

On the initial launch, the atomic service only downloads and installs the main package and its dependencies. Therefore, if the [NavDestination](../../navigation-and-switching/navdestination/document.md) resides in a different HSP subpackage that is not a dependency of the main package, you'll need to use **NavPushPathHelper** to download and install the corresponding HSP subpackage first. After that, push the specified **NavDestination** page information onto the stack. This way, you enable [Navigation](../../navigation-and-switching/navigation/document.md) to support dynamic loading of the HSP subpackage before the navigation occurs.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/Z_8Nh50GTSac2JAbEqL2DA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062248Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C23652ACBF656CD653CC5EBBA1E149FDC62E16133E8C301B59E23AECA596A228)

This component is supported since API version 12. Updates will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { NavPushPathHelper } from '@kit.ArkUI';

#### Child Components

Not supported

#### Attributes

The [universal attributes](../../universal-attributes/document.md) are not supported.

#### NavPushPathHelper

Encapsulates all navigation APIs for [NavPathStack](../../navigation-and-switching/navigation/document.md#navpathstack10). **NavPushPathHelper** holds a **NavPathStack** object and checks for the existence of a subpackage within its encapsulated navigation APIs. If the subpackage is absent, it dynamically downloads the subpackage. Once the download is complete, it calls the appropriate API of **NavPathStack** to push the specified [NavDestination](../../navigation-and-switching/navdestination/document.md) page onto the stack. For details, see [Example](#example).

#### \[h2\]constructor

constructor(navPathStack: NavPathStack)

A constructor used to create a **NavPushPathHelper** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| navPathStack | [NavPathStack](../../navigation-and-switching/navigation/document.md#navpathstack10) | Yes | [Navigation](../../navigation-and-switching/navigation/document.md) stack. |

#### \[h2\]pushPath

pushPath(moduleName: string, info: NavPathInfo, animated?: boolean): Promise<void>

Checks for the target subpackage and, if it is not present, initiates a download using the specified module name. Once the subpackage is downloaded, the API pushes the [NavDestination](../../navigation-and-switching/navdestination/document.md) page specified by the **info** parameter onto the navigation stack. This API uses a promise to handle asynchronous operations.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| moduleName | string | Yes | Module name of the package where the [NavDestination](../../navigation-and-switching/navdestination/document.md) page is located. |
| info | [NavPathInfo](../../navigation-and-switching/navigation/document.md#navpathinfo10) | Yes | Information about the [NavDestination](../../navigation-and-switching/navdestination/document.md) page. |
| animated | boolean | No | 
Whether to support the transition animation.

Default value: **true**

**true**: The transition animation is supported.

**false**: The transition animation is not supported.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Router Error Codes](../../../error-codes/ui/router-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 300001 | hsp silent install fail. |

#### \[h2\]pushPath

pushPath(moduleName: string, info: NavPathInfo, options?: NavigationOptions): Promise<void>

Checks for the target subpackage and, if it is not present, initiates a download using the specified module name. Once the subpackage is downloaded, the API pushes the [NavDestination](../../navigation-and-switching/navdestination/document.md) page specified by the **info** parameter onto the navigation stack. This API uses a promise to handle asynchronous operations.

Depending on the [LaunchMode](../../navigation-and-switching/navigation/document.md#launchmode12) specified in the **options** parameter, different behaviors will be triggered.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| moduleName | string | Yes | Module name of the package where the [NavDestination](../../navigation-and-switching/navdestination/document.md) page is located. |
| info | [NavPathInfo](../../navigation-and-switching/navigation/document.md#navpathinfo10) | Yes | Information about the [NavDestination](../../navigation-and-switching/navdestination/document.md) page. |
| options | [NavigationOptions](../../navigation-and-switching/navigation/document.md#navigationoptions12) | No | 
Navigation options.

Default value: **{ launchMode: LaunchMode.STANDARD, animated: true }**

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Router Error Codes](../../../error-codes/ui/router-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 300001 | hsp silent install fail. |

#### \[h2\]pushPathByName

pushPathByName(moduleName: string, name: string, param: Object, animated?: boolean): Promise<void>

Checks for the target subpackage and, if it is not present, initiates a download using the specified module name. Once the subpackage is downloaded, the API pushes the [NavDestination](../../navigation-and-switching/navdestination/document.md) page specified by the **name** parameter onto the navigation stack, along with the data specified by **param**. This API uses a promise to handle asynchronous operations.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| moduleName | string | Yes | Module name of the package where the [NavDestination](../../navigation-and-switching/navdestination/document.md) page is located. |
| name | string | Yes | Name of the [NavDestination](../../navigation-and-switching/navdestination/document.md) page. |
| param | Object | Yes | Settings of the [NavDestination](../../navigation-and-switching/navdestination/document.md) page. |
| animated | boolean | No | 
Whether to support the transition animation.

Default value: **true**

**true**: The transition animation is supported.

**false**: The transition animation is not supported.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Router Error Codes](../../../error-codes/ui/router-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 300001 | hsp silent install fail. |

#### \[h2\]pushPathByName

pushPathByName(moduleName: string, name: string, param: Object, onPop: Callback<PopInfo>, animated?: boolean): Promise<void>

Checks for the target subpackage and, if it is not present, initiates a download using the specified module name. Once the subpackage is downloaded, the API pushes the [NavDestination](../../navigation-and-switching/navdestination/document.md) page specified by the **name** parameter onto the navigation stack, along with the data specified by **param**. The **onPop** callback handles the return results when the page is popped from the stack. This API uses a promise to handle asynchronous operations.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| moduleName | string | Yes | Module name of the package where the [NavDestination](../../navigation-and-switching/navdestination/document.md) page is located. |
| name | string | Yes | Name of the [NavDestination](../../navigation-and-switching/navdestination/document.md) page. |
| param | Object | Yes | Settings of the [NavDestination](../../navigation-and-switching/navdestination/document.md) page. |
| onPop | Callback<[PopInfo](../../navigation-and-switching/navigation/document.md#popinfo11)\> | Yes | Callback used to receive the result. |
| animated | boolean | No | 
Whether to support the transition animation.

Default value: **true**

**true**: The transition animation is supported.

**false**: The transition animation is not supported.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Router Error Codes](../../../error-codes/ui/router-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 300001 | hsp silent install fail. |

#### \[h2\]pushDestination

pushDestination(moduleName: string, info: NavPathInfo, animated?: boolean): Promise<void>

Checks for the target subpackage and, if it is not present, initiates a download using the specified module name. Once the subpackage is downloaded, the API pushes the [NavDestination](../../navigation-and-switching/navdestination/document.md) page specified by the **info** parameter onto the navigation stack. This API uses a promise to handle asynchronous operations.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| moduleName | string | Yes | Module name of the package where the [NavDestination](../../navigation-and-switching/navdestination/document.md) page is located. |
| info | [NavPathInfo](../../navigation-and-switching/navigation/document.md#navpathinfo10) | Yes | Information about the [NavDestination](../../navigation-and-switching/navdestination/document.md) page. |
| animated | boolean | No | 
Whether to support the transition animation.

Default value: **true**

**true**: The transition animation is supported.

**false**: The transition animation is not supported.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md), [Router Error Codes](../../../error-codes/ui/router-error-codes/document.md), and [API Call Error Codes](../../../error-codes/ui/api-call-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameters types. 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100005 | Builder function not registered. |
| 100006 | NavDestination not found. |
| 300001 | hsp silent install fail. |

#### \[h2\]pushDestination

pushDestination(moduleName: string, info: NavPathInfo, options?: NavigationOptions): Promise<void>

Checks for the target subpackage and, if it is not present, initiates a download using the specified module name. Once the subpackage is downloaded, the API pushes the [NavDestination](../../navigation-and-switching/navdestination/document.md) page specified by the **info** parameter onto the navigation stack. This API uses a promise to handle asynchronous operations.

Depending on the [LaunchMode](../../navigation-and-switching/navigation/document.md#launchmode12) specified in the **options** parameter, different behaviors will be triggered.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| moduleName | string | Yes | Module name of the package where the [NavDestination](../../navigation-and-switching/navdestination/document.md) page is located. |
| info | [NavPathInfo](../../navigation-and-switching/navigation/document.md#navpathinfo10) | Yes | Information about the [NavDestination](../../navigation-and-switching/navdestination/document.md) page. |
| options | [NavigationOptions](../../navigation-and-switching/navigation/document.md#navigationoptions12) | No | 
Navigation options.

Default value: **{ launchMode: LaunchMode.STANDARD, animated: true }**

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md), [Router Error Codes](../../../error-codes/ui/router-error-codes/document.md), and [API Call Error Codes](../../../error-codes/ui/api-call-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameters types. 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100005 | Builder function not registered. |
| 100006 | NavDestination not found. |
| 300001 | hsp silent install fail. |

#### \[h2\]pushDestinationByName

pushDestinationByName(moduleName: string, name: string, param: Object, animated?: boolean): Promise<void>

Checks for the target subpackage and, if it is not present, initiates a download using the specified module name. Once the subpackage is downloaded, the API pushes the [NavDestination](../../navigation-and-switching/navdestination/document.md) page specified by the **name** parameter onto the navigation stack, along with the data specified by **param**. This API uses a promise to handle asynchronous operations.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| moduleName | string | Yes | Module name of the package where the [NavDestination](../../navigation-and-switching/navdestination/document.md) page is located. |
| name | string | Yes | Name of the [NavDestination](../../navigation-and-switching/navdestination/document.md) page. |
| param | Object | Yes | Settings of the [NavDestination](../../navigation-and-switching/navdestination/document.md) page. |
| animated | boolean | No | 
Whether to support the transition animation.

Default value: **true**

**true**: The transition animation is supported.

**false**: The transition animation is not supported.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md), [Router Error Codes](../../../error-codes/ui/router-error-codes/document.md), and [API Call Error Codes](../../../error-codes/ui/api-call-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameters types. 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100005 | Builder function not registered. |
| 100006 | NavDestination not found. |
| 300001 | hsp silent install fail. |

#### \[h2\]pushDestinationByName

pushDestinationByName(moduleName: string, name: string, param: Object, onPop: Callback<PopInfo>, animated?: boolean): Promise<void>

Checks for the target subpackage and, if it is not present, initiates a download using the specified module name. Once the subpackage is downloaded, the API pushes the [NavDestination](../../navigation-and-switching/navdestination/document.md) page specified by the **name** parameter onto the navigation stack, along with the data specified by **param**. The **onPop** callback handles the return results when the page is popped from the stack. This API uses a promise to handle asynchronous operations.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| moduleName | string | Yes | Module name of the package where the [NavDestination](../../navigation-and-switching/navdestination/document.md) page is located. |
| name | string | Yes | Name of the [NavDestination](../../navigation-and-switching/navdestination/document.md) page. |
| param | Object | Yes | Settings of the [NavDestination](../../navigation-and-switching/navdestination/document.md) page. |
| onPop | Callback<[PopInfo](../../navigation-and-switching/navigation/document.md#popinfo11)\> | Yes | Callback used to handle the result returned when the page is popped out of the stack. |
| animated | boolean | No | 
Whether to support the transition animation.

Default value: **true**

**true**: The transition animation is supported.

**false**: The transition animation is not supported.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md), [Router Error Codes](../../../error-codes/ui/router-error-codes/document.md), and [API Call Error Codes](../../../error-codes/ui/api-call-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameters types. 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100005 | Builder function not registered. |
| 100006 | NavDestination not found. |
| 300001 | hsp silent install fail. |

#### \[h2\]replacePath

replacePath(moduleName: string, info: NavPathInfo, animated?: boolean): Promise<void>

Checks for the target subpackage and, if it is not present, initiates a download using the specified module name. Once the subpackage is downloaded, the API pops the top page from the current navigation stack and pushes the [NavDestination](../../navigation-and-switching/navdestination/document.md) page specified by the **info** parameter onto the stack. This API uses a promise to handle asynchronous operations.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| moduleName | string | Yes | Module name of the package where the [NavDestination](../../navigation-and-switching/navdestination/document.md) page is located. |
| info | [NavPathInfo](../../navigation-and-switching/navigation/document.md#navpathinfo10) | Yes | Parameters of the page to replace the top of the navigation stack. |
| animated | boolean | No | 
Whether to support the transition animation.

Default value: **true**

**true**: The transition animation is supported.

**false**: The transition animation is not supported.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Router Error Codes](../../../error-codes/ui/router-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 300001 | hsp silent install fail. |

#### \[h2\]replacePath

replacePath(moduleName: string, info: NavPathInfo, options?: NavigationOptions): Promise<void>

Checks for the target subpackage and, if it is not present, initiates a download using the specified module name. Once the subpackage is downloaded, the API pops the top page from the current navigation stack. This API uses a promise to handle asynchronous operations.

Depending on the [LaunchMode](../../navigation-and-switching/navigation/document.md#launchmode12) specified in the **options** parameter, different behaviors will be triggered.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| moduleName | string | Yes | Module name of the package where the [NavDestination](../../navigation-and-switching/navdestination/document.md) page is located. |
| info | [NavPathInfo](../../navigation-and-switching/navigation/document.md#navpathinfo10) | Yes | Parameters of the page to replace the top of the navigation stack. |
| options | [NavigationOptions](../../navigation-and-switching/navigation/document.md#navigationoptions12) | No | 
Navigation options.

Default value: **{ launchMode: LaunchMode.STANDARD, animated: true }**

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Router Error Codes](../../../error-codes/ui/router-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 300001 | hsp silent install fail. |

#### \[h2\]replacePathByName

replacePathByName(moduleName: string, name: string, param: Object, animated?: boolean): Promise<void>

Checks for the target subpackage and, if it is not present, initiates a download using the specified module name. Once the subpackage is downloaded, the API pops the top page from the current navigation stack and pushes the [NavDestination](../../navigation-and-switching/navdestination/document.md) page specified by the **name** parameter onto the stack. This API uses a promise to handle asynchronous operations.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| moduleName | string | Yes | Module name of the package where the [NavDestination](../../navigation-and-switching/navdestination/document.md) page is located. |
| name | string | Yes | Name of the [NavDestination](../../navigation-and-switching/navdestination/document.md) page. |
| param | Object | Yes | Settings of the [NavDestination](../../navigation-and-switching/navdestination/document.md) page. |
| animated | boolean | No | 
Whether to support the transition animation.

Default value: **true**

**true**: The transition animation is supported.

**false**: The transition animation is not supported.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Router Error Codes](../../../error-codes/ui/router-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 300001 | hsp silent install fail. |

#### Events

The [universal events](../../universal-events/document.md) are not supported.

#### Example

Main package:

// Index.ets
import { NavPushPathHelper } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
@Entry
@Component
struct NavigationExample {
  pageInfo: NavPathStack = new NavPathStack();
  helper: NavPushPathHelper = new NavPushPathHelper(this.pageInfo);

  build() {
    Navigation(this.pageInfo) {
      Column() {
        Button('StartTest', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.helper.pushPath('hsptest1', { name: 'pageOne' }, false)
              .catch((error: BusinessError) => {
              console.error(\`\[pushPath\]failed, error code = ${error.code}, error.message = ${error.message}.\`);
            }).then(() => {
              console.error(\`\[pushPath\]success.\`);
            }); // Push the NavDestination page specified by name to the navigation stack.
          })
      }
    }.title('NavIndex')
  }
}

Subpackage **hsptest1**:

// PageOne.ets
import { NavPushPathHelper } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

class TmpClass {
  count: number = 10;
}

class ParamWithOp {
  operation: number = 1;
  count: number = 10;
}

@Builder
export function PageOneBuilder(name: string, param: Object) {
  PageOne();
}

@Component
export struct PageOne {
  pageInfo: NavPathStack = new NavPathStack();
  helper: NavPushPathHelper = new NavPushPathHelper(this.pageInfo);
  @State message: string = 'Hello World';

  build() {
    NavDestination() {
      Column() {
        Text(this.message)
          .width('80%')
          .height(50)
          .margin(10)

        Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(35)
          .margin(10)
          .onClick(() => {
            this.helper.pushPath('hsptest2', { name: 'pageTwo', param: new ParamWithOp(), onPop: (popInfo: PopInfo) => {
              this.message = '\[pushPath\]last page is: ' + popInfo.info.name + ', result: ' + JSON.stringify(popInfo.result);
            }}).catch((error: BusinessError) => {
              console.error(\`\[pushPath\]failed, error code = ${error.code}, error.message = ${error.message}.\`);
            }).then(() => {
              console.info(\`\[pushPath\]success.\`);
            });
          })

        Button('pushPath with NavigationOptions', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(35)
          .margin(10)
          .onClick(() => {
            this.helper.pushPath('hsptest2', { name: 'pageTwo', param: new ParamWithOp(), onPop: (popInfo: PopInfo) => {
              this.message = '\[pushPath with NavigationOptions\]last page is: ' + popInfo.info.name + ', result: ' + JSON.stringify(popInfo.result);
            }}, {launchMode:0, animated:true}).catch((error: BusinessError) => {
              console.error(\`\[pushPath with NavigationOptions\]failed, error code = ${error.code}, error.message = ${error.message}.\`);
            }).then(() => {
              console.info(\`\[pushPath with NavigationOptions\]success.\`);
            });
          })

        Button('pushPathByName', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(35)
          .margin(10)
          .onClick(() => {
            let tmp = new TmpClass();
            this.helper.pushPathByName('hsptest2', 'pageTwo', tmp, (popInfo) => {
              this.message = '\[pushPathByName\]last page is: ' + popInfo.info.name + ', result: ' + JSON.stringify(popInfo.result);
            }).catch((error: BusinessError) => {
              console.error(\`\[pushPathByName\]failed, error code = ${error.code}, error.message = ${error.message}.\`);
            }).then(() => {
              console.info(\`\[pushPathByName\]success.\`);
            });
          })

        Button('pushPathByNameWithoutOnPop', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(35)
          .margin(10)
          .onClick(() => {
            let tmp = new TmpClass();
            this.helper.pushPathByName('hsptest2', 'pageTwo', tmp, true)
            .catch((error: BusinessError) => {
              console.error(\`\[pushPathByNameWithoutOnPop\]failed, error code = ${error.code}, error.message = ${error.message}.\`);
            }).then(() => {
              console.info(\`\[pushPathByNameWithoutOnPop\]success.\`);
            });
          })

        Button('pushDestination', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(35)
          .margin(10)
          .onClick(() => {
            let tmp = new TmpClass()
            this.helper.pushDestination('hsptest2', { name: 'pageTwo', param: new ParamWithOp(), onPop: (popInfo: PopInfo) => {
              this.message = '\[pushDestination\]last page is: ' + popInfo.info.name + ', result: ' + JSON.stringify(popInfo.result);
            }}).catch((error: BusinessError) => {
              console.error(\`\[pushDestination\]failed, error code = ${error.code}, error.message = ${error.message}.\`);
            }).then(() => {
              console.error(\`\[pushDestination\]success.\`);
            });
          })

        Button('pushDestination with NavigationOptions', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(35)
          .margin(10)
          .onClick(() => {
            let tmp = new TmpClass();
            this.helper.pushDestination('hsptest2', { name: 'pageTwo', param: new ParamWithOp(), onPop: (popInfo: PopInfo) => {
              this.message = '\[pushDestination with NavigationOptions\]last page is: ' + popInfo.info.name + ', result: ' + JSON.stringify(popInfo.result);
            }}, {launchMode:0, animated:true}).catch((error: BusinessError) => {
              console.error(\`\[pushDestination with NavigationOptions\]failed, error code = ${error.code}, error.message = ${error.message}.\`);
            }).then(() => {
              console.error(\`\[pushDestination with NavigationOptions\]success.\`);
            });
          })

        Button('pushDestinationByName', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(35)
          .margin(10)
          .onClick(() => {
            let tmp = new TmpClass()
            this.helper.pushDestinationByName('hsptest2','pageTwo', tmp, (popInfo) => {
              this.message = '\[pushDestinationByName\]last page is: ' + popInfo.info.name + ', result: ' + JSON.stringify(popInfo.result);
            }).catch((error: BusinessError) => {
              console.error(\`\[pushDestinationByName\]failed, error code = ${error.code}, error.message = ${error.message}.\`);
            }).then(() => {
              console.error(\`\[pushDestinationByName\]success.\`);
            });
          })

        Button('pushDestinationByNameWithoutOnPop', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(35)
          .margin(10)
          .onClick(() => {
            let tmp = new TmpClass()
            this.helper.pushDestinationByName('hsptest2','pageTwo', tmp, true)
              .catch((error: BusinessError) => {
                console.error(\`\[pushDestinationByNameWithoutOnPop\]failed, error code = ${error.code}, error.message = ${error.message}.\`);
              }).then(() => {
              console.error(\`\[pushDestinationByNameWithoutOnPop\]success.\`);
            });
          })

        Button('replacePath', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(35)
          .margin(10)
          .onClick(() => {
            this.helper.replacePath('hsptest2', { name: 'pageTwo', param: new ParamWithOp(), onPop: (popInfo: PopInfo) => {
              this.message = '\[replacePath\]last page is: ' + popInfo.info.name + ', result: ' + JSON.stringify(popInfo.result);
            }}).catch((error: BusinessError) => {
              console.error(\`\[replacePath\]failed, error code = ${error.code}, error.message = ${error.message}.\`);
            }).then(() => {
              console.info(\`\[replacePath\]success.\`);
            });
          })

        Button('replacePath with NavigationOptions', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(35)
          .margin(10)
          .onClick(() => {
            this.helper.replacePath('hsptest2', { name: 'pageTwo', param: new ParamWithOp(), onPop: (popInfo: PopInfo) => {
              this.message = '\[replacePath with NavigationOptions\]last page is: ' + popInfo.info.name + ', result: ' + JSON.stringify(popInfo.result);
            }}, {launchMode:0, animated:true}).catch((error: BusinessError) => {
              console.error(\`\[replacePath with NavigationOptions\]failed, error code = ${error.code}, error.message = ${error.message}.\`);
            }).then(() => {
              console.info(\`\[replacePath with NavigationOptions\]success.\`);
            });
          })

        Button('replacePathByName', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(35)
          .margin(10)
          .onClick(() => {
            let tmp = new TmpClass();
            this.helper.replacePathByName('hsptest2', 'pageTwo', tmp)
              .catch((error: BusinessError) => {
              console.error(\`\[replacePathByName\]failed, error code = ${error.code}, error.message = ${error.message}.\`);
            }).then(() => {
              console.info(\`\[replacePathByName\]success.\`);
            });
          })

      }.width('100%').height('100%')
    }.title('pageOne')
    .onBackPressed(() => {
      this.pageInfo.pop({ number: 1 }) // Pop the top element out of the navigation stack.
      return true;
    }).onReady((context: NavDestinationContext) => {
      this.pageInfo = context.pathStack;
      this.helper = new NavPushPathHelper(this.pageInfo);
    })
  }
}

Configure **{"routerMap": "$profile:route\_map"}** in the project configuration file **module.json5**. The configuration in the **route\_map.json** file is as follows:

{
  "routerMap": \[
    {
      "name": "pageOne",
      "pageSourceFile": "src/main/ets/pages/PageOne.ets",
      "buildFunction": "PageOneBuilder",
      "data": {
        "description": "this is pageOne"
      }
    }
  \]
}

Subpackage **hsptest2**:

// PageTwo.ets

class resultClass {
  constructor(count: number) {
    this.count = count;
  }
  count: number = 10
}

@Builder
export function PageTwoBuilder() {
  PageTwo()
}

@Component
export struct PageTwo {
  pathStack: NavPathStack = new NavPathStack()

  build() {
    NavDestination() {
      Column() {
        Button('pop', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pathStack.pop(new resultClass(1)); // Return to the previous page and pass in the processing result to the onPop callback of push.
          })
      }.width('100%').height('100%')
    }.title('pageTwo')
    .onBackPressed(() => {
      this.pathStack.pop(new resultClass(0)); // Return to the previous page and pass in the processing result to the onPop callback of push.
      return true;
    }).onReady((context: NavDestinationContext) => {
      this.pathStack = context.pathStack
    })
  }
}

Configure **{"routerMap": "$profile:route\_map"}** in the project configuration file **module.json5**. The configuration in the **route\_map.json** file is as follows:

{
  "routerMap": \[
    {
      "name": "pageTwo",
      "pageSourceFile": "src/main/ets/pages/PageTwo.ets",
      "buildFunction": "PageTwoBuilder",
      "data": {
        "description": "this is pageTwo"
      }
    }
  \]
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/iBKaJn2kTaeEWfBiDVXydQ/en-us_image_0000002537925892.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062248Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E2AEAB56093AE8C435B7F9418AD0A436CA4F2852499E1E1BAFF6F6FB20BD14E5)
