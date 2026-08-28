# native\_node\_napi.h

#### Overview

Provides the APIs used to convert [FrameNode](../../../arkts-api/ui/arkui/framenode/document.md) on the ArkTS side to [NodeHandle](../../structs/arkui-node--00020177/document.md).

**File to include**: <arkui/native\_node\_napi.h>

**Library**: libace\_ndk.z.so

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Since**: 12

**Related module**: [ArkUI\_NativeModule](../../modules/arkui-nativemodule/document.md)

**Sample**: [native\_node\_napi](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/ArkUISample/NativeNodeNapi/native_node_napi)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [int32\_t OH\_ArkUI\_GetNodeHandleFromNapiValue(napi\_env env, napi\_value frameNode, ArkUI\_NodeHandle\* handle)](#oh_arkui_getnodehandlefromnapivalue) | Obtains an **ArkUI\_NodeHandle** object on the native side mapped from the **FrameNode** object created on the ArkTS side. |
| [int32\_t OH\_ArkUI\_GetContextFromNapiValue(napi\_env env, napi\_value value, ArkUI\_ContextHandle\* context)](#oh_arkui_getcontextfromnapivalue) | Obtains an **ArkUI\_ContextHandle** object on the native side mapped from the **UIContext** object created on the ArkTS side. |
| [int32\_t OH\_ArkUI\_GetNodeContentFromNapiValue(napi\_env env, napi\_value value, ArkUI\_NodeContentHandle\* content)](#oh_arkui_getnodecontentfromnapivalue) | Obtains an **ArkUI\_NodeContentHandle** object on the native side mapped from the **NodeContent** object created on the ArkTS side. |
| [int32\_t OH\_ArkUI\_GetDrawableDescriptorFromNapiValue(napi\_env env, napi\_value value, ArkUI\_DrawableDescriptor\*\* drawableDescriptor)](#oh_arkui_getdrawabledescriptorfromnapivalue) | Maps a **DrawableDescriptor** object on the ArkTS side to an **ArkUI\_DrawableDescriptor** object on the native side. |
| [int32\_t OH\_ArkUI\_GetDrawableDescriptorFromResourceNapiValue(napi\_env env, napi\_value value, ArkUI\_DrawableDescriptor\*\* drawableDescriptor)](#oh_arkui_getdrawabledescriptorfromresourcenapivalue) | Maps an $r resource object on the ArkTS side to an **ArkUI\_DrawableDescriptor** object on the native side. |
| [ArkUI\_ErrorCode OH\_ArkUI\_GetNavigationId(ArkUI\_NodeHandle node, char\* buffer, int32\_t bufferSize, int32\_t\* writeLength)](#oh_arkui_getnavigationid) | Obtains the ID of the **Navigation** component where the specified node is located. |
| [ArkUI\_ErrorCode OH\_ArkUI\_GetNavDestinationName(ArkUI\_NodeHandle node, char\* buffer, int32\_t bufferSize, int32\_t\* writeLength)](#oh_arkui_getnavdestinationname) | Obtains the name of the **NavDestination** component where the specified node is located. |
| [ArkUI\_ErrorCode OH\_ArkUI\_GetNavStackLength(ArkUI\_NodeHandle node, int32\_t\* length)](#oh_arkui_getnavstacklength) | Obtains the length of the **Navigation** stack where the specified node is located. |
| [ArkUI\_ErrorCode OH\_ArkUI\_GetNavDestinationNameByIndex(ArkUI\_NodeHandle node, int32\_t index, char\* buffer, int32\_t bufferSize, int32\_t\* writeLength)](#oh_arkui_getnavdestinationnamebyindex) | Obtains the page name that matches the specified index in the navigation stack where the specified node is located. The index starts from 0, which indicates the bottom of the stack. |
| [ArkUI\_ErrorCode OH\_ArkUI\_GetNavDestinationId(ArkUI\_NodeHandle node, char\* buffer, int32\_t bufferSize, int32\_t\* writeLength)](#oh_arkui_getnavdestinationid) | Obtains the ID of the **NavDestination** component where the specified node is located. |
| [ArkUI\_ErrorCode OH\_ArkUI\_GetNavDestinationState(ArkUI\_NodeHandle node, ArkUI\_NavDestinationState\* state)](#oh_arkui_getnavdestinationstate) | Obtains the state of the **NavDestination** component where the specified node is located. |
| [ArkUI\_ErrorCode OH\_ArkUI\_GetNavDestinationIndex(ArkUI\_NodeHandle node, int32\_t\* index)](#oh_arkui_getnavdestinationindex) | Obtains the index of the **NavDestination** component where the specified node is located in the navigation stack. |
| [napi\_value OH\_ArkUI\_GetNavDestinationParam(ArkUI\_NodeHandle node)](#oh_arkui_getnavdestinationparam) | Obtains the parameters of the **NavDestination** component where the specified node is located. |
| [ArkUI\_ErrorCode OH\_ArkUI\_GetRouterPageIndex(ArkUI\_NodeHandle node, int32\_t\* index)](#oh_arkui_getrouterpageindex) | Obtains the index of the page where the specified node is located in the page stack for routing. |
| [ArkUI\_ErrorCode OH\_ArkUI\_GetRouterPageName(ArkUI\_NodeHandle node, char\* buffer, int32\_t bufferSize, int32\_t\* writeLength)](#oh_arkui_getrouterpagename) | Obtains the name of the page where the specified node is located. |
| [ArkUI\_ErrorCode OH\_ArkUI\_GetRouterPagePath(ArkUI\_NodeHandle node, char\* buffer, int32\_t bufferSize, int32\_t\* writeLength)](#oh_arkui_getrouterpagepath) | Obtains the path to the page where the specified node is located. |
| [ArkUI\_ErrorCode OH\_ArkUI\_GetRouterPageState(ArkUI\_NodeHandle node, ArkUI\_RouterPageState\* state)](#oh_arkui_getrouterpagestate) | Obtains the state of the page where the specified node is located. |
| [ArkUI\_ErrorCode OH\_ArkUI\_GetRouterPageId(ArkUI\_NodeHandle node, char\* buffer, int32\_t bufferSize, int32\_t\* writeLength)](#oh_arkui_getrouterpageid) | Obtains the ID of the page where the specified node is located. |
| [ArkUI\_ErrorCode OH\_ArkUI\_InitModuleForArkTSEnv(napi\_env env)](#oh_arkui_initmoduleforarktsenv) | Initializes ArkUI-related APIs for the specified context environment. This function must not be called from a non-UI thread; otherwise, the program will actively abort. |
| [void OH\_ArkUI\_NotifyArkTSEnvDestroy(napi\_env env)](#oh_arkui_notifyarktsenvdestroy) | Notifies that the specified context environment has been destroyed. This function must not be called from a non-UI thread; otherwise, the program will actively abort. |
| [int32\_t OH\_ArkUI\_PostFrameCallback(ArkUI\_ContextHandle uiContext, void\* userData,void (\*callback)(uint64\_t nanoTimestamp, uint32\_t frameCount, void\* userData))](#oh_arkui_postframecallback) | Registers a callback function to be executed during the next frame rendering. This function must not be called from a non-UI thread; otherwise, the program will actively abort. |
| [int32\_t OH\_ArkUI\_PostIdleCallback(ArkUI\_ContextHandle uiContext, void\* userData,void (\*callback)(uint64\_t nanoTimeLeft, uint32\_t frameCount, void\* userData))](#oh_arkui_postidlecallback) | Registers a callback function that will be executed after the rendering of the next frame is completed if there is more than 1 ms of idle time remaining before the next VSync signal arrives. If the remaining time is less than 1 ms, the callback will be deferred until a subsequent frame where more than 1 ms of idle time is available. If there is no next frame scheduled, one will be automatically requested. |

#### Function Description

#### \[h2\]OH\_ArkUI\_GetNodeHandleFromNapiValue()

int32\_t OH\_ArkUI\_GetNodeHandleFromNapiValue(napi\_env env, napi\_value frameNode, ArkUI\_NodeHandle\* handle)

**Description**

Obtains an **ArkUI\_NodeHandle** object on the native side mapped from the **FrameNode** object created on the ArkTS side.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| napi\_env env | Pointer to the Node-API environment. |
| napi\_value frameNode | **FrameNode** object created on the ArkTS side. |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md)\* handle | Pointer to the **ArkUI\_NodeHandle**. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_GetContextFromNapiValue()

int32\_t OH\_ArkUI\_GetContextFromNapiValue(napi\_env env, napi\_value value, ArkUI\_ContextHandle\* context)

**Description**

Obtains an **ArkUI\_ContextHandle** object on the native side mapped from a [UIContext](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md) object created on the ArkTS side.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| napi\_env env | Pointer to the Node-API environment. |
| napi\_value value | **UIContext** object created on the ArkTS side. |
| [ArkUI\_ContextHandle](../../structs/arkui-context--00020177/document.md)\* context | Pointer to the **ArkUI\_ContextHandle**. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_GetNodeContentFromNapiValue()

int32\_t OH\_ArkUI\_GetNodeContentFromNapiValue(napi\_env env, napi\_value value, ArkUI\_NodeContentHandle\* content)

**Description**

Obtains an **ArkUI\_NodeContentHandle** object on the native side mapped from the **NodeContent** object created on the ArkTS side.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| napi\_env env | Pointer to the Node-API environment. |
| napi\_value value | **NodeContent** object created on the ArkTS side. |
| [ArkUI\_NodeContentHandle](../../structs/arkui-nodecontent/document.md)\* content | Pointer to the **ArkUI\_NodeContentHandle**. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_GetDrawableDescriptorFromNapiValue()

int32\_t OH\_ArkUI\_GetDrawableDescriptorFromNapiValue(napi\_env env, napi\_value value, ArkUI\_DrawableDescriptor\*\* drawableDescriptor)

**Description**

Maps the [DrawableDescriptor](../../../arkts-components/images-and-videos/image/document.md#drawabledescriptor10) object created on the ArkTS side to the [ArkUI\_DrawableDescriptor](../../structs/arkui-drawabledescriptor/document.md) object on the native side.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| napi\_env env | Pointer to the Node-API environment. |
| napi\_value value | [DrawableDescriptor](../../../arkts-components/images-and-videos/image/document.md#drawabledescriptor10) object created on the ArkTS side. |
| [ArkUI\_DrawableDescriptor](../../structs/arkui-drawabledescriptor/document.md)\*\* drawableDescriptor | Double pointer used to receive the **ArkUI\_DrawableDescriptor** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_GetDrawableDescriptorFromResourceNapiValue()

int32\_t OH\_ArkUI\_GetDrawableDescriptorFromResourceNapiValue(napi\_env env, napi\_value value, ArkUI\_DrawableDescriptor\*\* drawableDescriptor)

**Description**

Converts the resource object obtained by **$r()** on the ArkTS side to the [ArkUI\_DrawableDescriptor](../../structs/arkui-drawabledescriptor/document.md) object that can be used on the native side.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| napi\_env env | Pointer to the Node-API environment. |
| napi\_value value | **$r** resource object created on the ArkTS side. |
| [ArkUI\_DrawableDescriptor](../../structs/arkui-drawabledescriptor/document.md)\*\* drawableDescriptor | Double pointer used to receive the **ArkUI\_DrawableDescriptor** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_GetNavigationId()

ArkUI\_ErrorCode OH\_ArkUI\_GetNavigationId(ArkUI\_NodeHandle node, char\* buffer, int32\_t bufferSize, int32\_t\* writeLength)

**Description**

Obtains the ID of the [Navigation](../../../arkts-components/navigation-and-switching/navigation/document.md) component where the specified node is located.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Target node. |
| char\* buffer | Buffer to which the obtained ID is written. |
| int32\_t bufferSize | Buffer size. |
| int32\_t\* writeLength | Length of the string written to the buffer when [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) is returned; Minimum size of the buffer required to hold the target when [ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](../native-type-h/document.md#arkui_errorcode) is returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](../native-type-h/document.md#arkui_errorcode) | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_GET\_INFO\_FAILED](../native-type-h/document.md#arkui_errorcode) if information fails to be obtained, possibly because the specified node is not in the navigation stack.

Returns [ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](../native-type-h/document.md#arkui_errorcode) if the data size exceeds the specified buffer size.

 |

#### \[h2\]OH\_ArkUI\_GetNavDestinationName()

ArkUI\_ErrorCode OH\_ArkUI\_GetNavDestinationName(ArkUI\_NodeHandle node, char\* buffer, int32\_t bufferSize, int32\_t\* writeLength)

**Description**

Obtains the name of the [NavDestination](../../../arkts-components/navigation-and-switching/navdestination/document.md) component where the specified node is located.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Target node. |
| char\* buffer | Buffer to which the obtained name is written. |
| int32\_t bufferSize | Buffer size. |
| int32\_t\* writeLength | Length of the string written to the buffer when [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) is returned; Minimum size of the buffer required to hold the target when [ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](../native-type-h/document.md#arkui_errorcode) is returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](../native-type-h/document.md#arkui_errorcode) | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_GET\_INFO\_FAILED](../native-type-h/document.md#arkui_errorcode) if information fails to be obtained, possibly because the specified node is not in the navigation stack.

Returns [ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](../native-type-h/document.md#arkui_errorcode) if the specified buffer size is smaller than the minimum buffer size required to hold the target.

 |

#### \[h2\]OH\_ArkUI\_GetNavStackLength()

ArkUI\_ErrorCode OH\_ArkUI\_GetNavStackLength(ArkUI\_NodeHandle node, int32\_t\* length)

**Description**

Obtains the length of the **Navigation** stack where the specified node is located.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Target node. |
| int32\_t\* length | Length of the navigation stack. The result, if obtained successfully, is written back to this parameter. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](../native-type-h/document.md#arkui_errorcode) | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_GET\_INFO\_FAILED](../native-type-h/document.md#arkui_errorcode) if information fails to be obtained, possibly because the specified node is not in the navigation stack.

 |

#### \[h2\]OH\_ArkUI\_GetNavDestinationNameByIndex()

ArkUI\_ErrorCode OH\_ArkUI\_GetNavDestinationNameByIndex(ArkUI\_NodeHandle node, int32\_t index, char\* buffer, int32\_t bufferSize, int32\_t\* writeLength)

**Description**

Obtains the name of the page in the navigation stack where the specified node is located based on the given index. The index starts from 0, which indicates the bottom of the stack.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Target node. |
| int32\_t index | Index of the target page in the navigation stack. |
| char\* buffer | Buffer to which the obtained name is written. |
| int32\_t bufferSize | Buffer size. |
| int32\_t\* writeLength | Length of the string written to the buffer when [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) is returned; Minimum size of the buffer required to hold the target when [ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](../native-type-h/document.md#arkui_errorcode) is returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](../native-type-h/document.md#arkui_errorcode) | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_NODE\_INDEX\_INVALID](../native-type-h/document.md#arkui_errorcode) if the index is invalid.

Returns [ARKUI\_ERROR\_CODE\_GET\_INFO\_FAILED](../native-type-h/document.md#arkui_errorcode) if information fails to be obtained, possibly because the specified node is not in the navigation stack.

Returns [ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](../native-type-h/document.md#arkui_errorcode) if the specified buffer size is smaller than the minimum buffer size required to hold the target.

 |

#### \[h2\]OH\_ArkUI\_GetNavDestinationId()

ArkUI\_ErrorCode OH\_ArkUI\_GetNavDestinationId(ArkUI\_NodeHandle node, char\* buffer, int32\_t bufferSize, int32\_t\* writeLength)

**Description**

Obtains the ID of the **NavDestination** component where the specified node is located.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Target node. |
| char\* buffer | Buffer to which the obtained ID is written. |
| int32\_t bufferSize | Buffer size. |
| int32\_t\* writeLength | Length of the string written to the buffer when [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) is returned; Minimum size of the buffer required to hold the target when [ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](../native-type-h/document.md#arkui_errorcode) is returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](../native-type-h/document.md#arkui_errorcode) | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_GET\_INFO\_FAILED](../native-type-h/document.md#arkui_errorcode) if information fails to be obtained, possibly because the specified node is not in the navigation stack.

Returns [ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](../native-type-h/document.md#arkui_errorcode) if the data size exceeds the specified buffer size.

 |

#### \[h2\]OH\_ArkUI\_GetNavDestinationState()

ArkUI\_ErrorCode OH\_ArkUI\_GetNavDestinationState(ArkUI\_NodeHandle node, ArkUI\_NavDestinationState\* state)

**Description**

Obtains the state of the **NavDestination** component where the specified node is located.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Target node. |
| [ArkUI\_NavDestinationState](../native-type-h/document.md#arkui_navdestinationstate)\* state | State of the **NavDestination** component. The result, if obtained successfully, is written back to this parameter. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](../native-type-h/document.md#arkui_errorcode) | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_GET\_INFO\_FAILED](../native-type-h/document.md#arkui_errorcode) if information fails to be obtained, possibly because the specified node is not in the navigation stack.

 |

#### \[h2\]OH\_ArkUI\_GetNavDestinationIndex()

ArkUI\_ErrorCode OH\_ArkUI\_GetNavDestinationIndex(ArkUI\_NodeHandle node, int32\_t\* index)

**Description**

Obtains the index of the **NavDestination** component where the specified node is located in the navigation stack.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Target node. |
| int32\_t\* index | Zero-based index. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](../native-type-h/document.md#arkui_errorcode) | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_GET\_INFO\_FAILED](../native-type-h/document.md#arkui_errorcode) if information fails to be obtained, possibly because the specified node is not in the navigation stack.

 |

#### \[h2\]OH\_ArkUI\_GetNavDestinationParam()

napi\_value OH\_ArkUI\_GetNavDestinationParam(ArkUI\_NodeHandle node)

**Description**

Obtains the parameters of the **NavDestination** component where the specified node is located.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Target node. |

**Return value**

| Type | Description |
| :-- | :-- |
| napi\_value | Parameter object. Returns an empty value if the parameters do not exist or the specified node is null. |

#### \[h2\]OH\_ArkUI\_GetRouterPageIndex()

ArkUI\_ErrorCode OH\_ArkUI\_GetRouterPageIndex(ArkUI\_NodeHandle node, int32\_t\* index)

**Description**

Obtains the index of the [Router](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-router/document.md) page stack where the specified node is located.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Target node. |
| int32\_t\* index | One-based index. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](../native-type-h/document.md#arkui_errorcode) | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if the node or index specified is invalid.

Returns [ARKUI\_ERROR\_CODE\_GET\_INFO\_FAILED](../native-type-h/document.md#arkui_errorcode) if information fails to be obtained, possibly because the specified node is not in the navigation stack.

 |

#### \[h2\]OH\_ArkUI\_GetRouterPageName()

ArkUI\_ErrorCode OH\_ArkUI\_GetRouterPageName(ArkUI\_NodeHandle node, char\* buffer, int32\_t bufferSize, int32\_t\* writeLength)

**Description**

Obtains the name of the **Router** page where the specified node is located.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Target node. |
| char\* buffer | Buffer to which the obtained name is written. |
| int32\_t bufferSize | Buffer size. |
| int32\_t\* writeLength | Length of the string written to the buffer when [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) is returned; Minimum size of the buffer required to hold the target when [ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](../native-type-h/document.md#arkui_errorcode) is returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](../native-type-h/document.md#arkui_errorcode) | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_GET\_INFO\_FAILED](../native-type-h/document.md#arkui_errorcode) if information fails to be obtained.

Returns [ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](../native-type-h/document.md#arkui_errorcode) if the specified buffer size is smaller than the minimum buffer size required to hold the target.

 |

#### \[h2\]OH\_ArkUI\_GetRouterPagePath()

ArkUI\_ErrorCode OH\_ArkUI\_GetRouterPagePath(ArkUI\_NodeHandle node, char\* buffer, int32\_t bufferSize, int32\_t\* writeLength)

**Description**

Obtains the path of the **Router** page where the specified node is located.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Target node. |
| char\* buffer | Buffer to which the page path is written. |
| int32\_t bufferSize | Buffer size. |
| int32\_t\* writeLength | Length of the string written to the buffer when [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) is returned; Minimum size of the buffer required to hold the target when [ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](../native-type-h/document.md#arkui_errorcode) is returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](../native-type-h/document.md#arkui_errorcode) | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_GET\_INFO\_FAILED](../native-type-h/document.md#arkui_errorcode) if information fails to be obtained.

Returns [ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](../native-type-h/document.md#arkui_errorcode) if the specified buffer size is smaller than the minimum buffer size required to hold the target.

 |

#### \[h2\]OH\_ArkUI\_GetRouterPageState()

ArkUI\_ErrorCode OH\_ArkUI\_GetRouterPageState(ArkUI\_NodeHandle node, ArkUI\_RouterPageState\* state)

**Description**

Obtains the status of the **Router** page where the specified node is located.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Target node. |
| [ArkUI\_RouterPageState](../native-type-h/document.md#arkui_routerpagestate)\* state | Status of the **Router** page. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](../native-type-h/document.md#arkui_errorcode) | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_GET\_INFO\_FAILED](../native-type-h/document.md#arkui_errorcode) if information fails to be obtained.

 |

#### \[h2\]OH\_ArkUI\_GetRouterPageId()

ArkUI\_ErrorCode OH\_ArkUI\_GetRouterPageId(ArkUI\_NodeHandle node, char\* buffer, int32\_t bufferSize, int32\_t\* writeLength)

**Description**

Obtains the ID of the **Router** page where the specified node is located.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Target node. |
| char\* buffer | Buffer to which the page ID is written. |
| int32\_t bufferSize | Buffer size. |
| int32\_t\* writeLength | Length of the string written to the buffer when [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) is returned; Minimum size of the buffer required to hold the target when [ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](../native-type-h/document.md#arkui_errorcode) is returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](../native-type-h/document.md#arkui_errorcode) | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_GET\_INFO\_FAILED](../native-type-h/document.md#arkui_errorcode) if information fails to be obtained.

Returns [ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](../native-type-h/document.md#arkui_errorcode) if the data size exceeds the specified buffer size.

 |

#### \[h2\]OH\_ArkUI\_InitModuleForArkTSEnv()

ArkUI\_ErrorCode OH\_ArkUI\_InitModuleForArkTSEnv(napi\_env env)

**Description**

Initializes ArkUI-related APIs for the specified context environment. This function must not be called from a non-UI thread; otherwise, the program will actively abort.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| napi\_env env | Pointer to the Node-API environment. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](../native-type-h/document.md#arkui_errorcode) | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if the parameter is invalid. Examples of invalid parameters include a null env pointer or failure to configure the trustlist.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

 |

#### \[h2\]OH\_ArkUI\_NotifyArkTSEnvDestroy()

void OH\_ArkUI\_NotifyArkTSEnvDestroy(napi\_env env)

**Description**

Notifies that the specified context environment has been destroyed. This function must not be called from a non-UI thread; otherwise, the program will actively abort.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| napi\_env env | Pointer to the Node-API environment. |

#### \[h2\]OH\_ArkUI\_PostFrameCallback()

int32\_t OH\_ArkUI\_PostFrameCallback(ArkUI\_ContextHandle uiContext, void\* userData,void (\*callback)(uint64\_t nanoTimestamp, uint32\_t frameCount, void\* userData))

**Description**

Registers a callback function to be executed during the next frame rendering. This function must not be called from a non-UI thread; otherwise, the program will actively abort.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ContextHandle](../../structs/arkui-context--00020177/document.md) uiContext | Pointer to the [UIContext](../../../arkts-components/custom-components/custom-component-built-in-apis/document.md#uicontext) object, which is used to bind an instance. |
| void\* userData | Custom event parameter, which is passed in the callback when the event is triggered. |
| callback | Custom callback function. |
| uint64\_t nanoTimestamp | Timestamp of the frame signal. |
| uint32\_t frameCount | Frame number. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_UI\_CONTEXT\_INVALID](../native-type-h/document.md#arkui_errorcode) if the **uiContext** object is invalid.

Returns [ARKUI\_ERROR\_CODE\_CALLBACK\_INVALID](../native-type-h/document.md#arkui_errorcode) if the callback function is invalid.

 |

#### \[h2\]OH\_ArkUI\_PostIdleCallback()

int32\_t OH\_ArkUI\_PostIdleCallback(ArkUI\_ContextHandle uiContext, void\* userData,void (\*callback)(uint64\_t nanoTimeLeft, uint32\_t frameCount, void\* userData))

**Description**

Registers a callback function that will be executed after the rendering of the next frame is completed if there is more than 1 ms of idle time remaining before the next frame arrives. If the remaining time is less than 1 ms, the callback will be deferred until a subsequent frame where more than 1 ms of idle time is available. If there is no next frame scheduled, one will be automatically requested.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ContextHandle](../../structs/arkui-context--00020177/document.md) uiContext | **UIContext** object used to bind the instance. |
| void\* userData | Custom event parameter, which is passed in the callback when the custom callback is triggered. |
| callback | Custom callback function, which is executed when the remaining time until the next frame event exceeds 1 ms. |
| uint64\_t nanoTimeLeft | Remaining time after the next frame is rendered. |
| uint32\_t frameCount | Frame number. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_UI\_CONTEXT\_INVALID](../native-type-h/document.md#arkui_errorcode) if the **uiContext** object is invalid.

Returns [ARKUI\_ERROR\_CODE\_CALLBACK\_INVALID](../native-type-h/document.md#arkui_errorcode) if the callback function is invalid.

 |
