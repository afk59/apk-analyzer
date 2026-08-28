# native\_interface.h

#### Overview

Provides a unified entry for the native module APIs.

**File to include**: <arkui/native\_interface.h>

**Library**: libace\_ndk.z.so

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Since**: 12

**Related module**: [ArkUI\_NativeModule](../../modules/arkui-nativemodule/document.md)

**Sample**: [NativeNodeInterfaceSample](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/ArkUISample/NativeType/NativeNodeInterfaceSample)

#### Summary

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [ArkUI\_NativeAPIVariantKind](#arkui_nativeapivariantkind) | ArkUI\_NativeAPIVariantKind | Enumerates the types of native API collections. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [void\* OH\_ArkUI\_QueryModuleInterfaceByName(ArkUI\_NativeAPIVariantKind type, const char\* structName)](#oh_arkui_querymoduleinterfacebyname) | Initializes the C API environment and obtains the native module API collection of the specified type. |

#### \[h2\]Macros

| Name | Description |
| :-- | :-- |
| [OH\_ArkUI\_GetModuleInterface(nativeAPIVariantKind, structType, structPtr)](#oh_arkui_getmoduleinterface) | Obtains the corresponding struct pointer based on the struct type. |

#### Enum Description

#### \[h2\]ArkUI\_NativeAPIVariantKind

enum ArkUI\_NativeAPIVariantKind

**Description**

Enumerates the types of native API collections.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_NATIVE\_NODE = 0 | API related to UI components. For details, see the [struct](../native-node-h/document.md#structs) definition in [native\_node.h](../native-node-h/document.md). |
| ARKUI\_NATIVE\_DIALOG = 1 | API related to dialog boxes. For details, see the [struct](../native-dialog-h/document.md#structs) definition in [native\_dialog.h](../native-dialog-h/document.md). |
| ARKUI\_NATIVE\_GESTURE = 2 | API related to gestures. For details, see the [struct](../native-gesture-h/document.md#structs) definition in [native\_gesture.h](../native-gesture-h/document.md). |
| ARKUI\_NATIVE\_ANIMATE = 3 | API related to animations. For details, see the [struct](../native-animate-h/document.md#structs) definition in [native\_animate.h](../native-animate-h/document.md). |
| ARKUI\_MULTI\_THREAD\_NATIVE\_NODE = 4 | 
API related to multi-threaded UI components. For details, see the [struct](../native-node-h/document.md#structs) definition in [native\_node.h](../native-node-h/document.md).

**Since**: 22

 |

#### Function Description

#### \[h2\]OH\_ArkUI\_QueryModuleInterfaceByName()

void\* OH\_ArkUI\_QueryModuleInterfaceByName(ArkUI\_NativeAPIVariantKind type, const char\* structName)

**Description**

Initializes the C API environment and obtains the native module API collection of the specified type.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NativeAPIVariantKind](#arkui_nativeapivariantkind) type | Type of the native API collection provided by ArkUI, for example, **ARKUI\_NATIVE\_NODE** or **ARKUI\_NATIVE\_GESTURE**. |
| const char\* structName | Name of a native struct, obtained by querying the struct definitions in the corresponding header file, for example, **ArkUI\_NativeNodeAPI\_1** in [native\_node.h](../native-node-h/document.md). |

**Return value**

| Type | Description |
| :-- | :-- |
| void\* | Pointer to the native API abstraction, which must be cast to the specific type for use. |

#### \[h2\]OH\_ArkUI\_GetModuleInterface()

#define OH\_ArkUI\_GetModuleInterface(nativeAPIVariantKind, structType, structPtr)                     \\
do {                                                                                                 \\
        void\* anyNativeAPI = OH\_ArkUI\_QueryModuleInterfaceByName(nativeAPIVariantKind, #structType); \\
        if (anyNativeAPI) {                                                                          \\
            structPtr = (structType\*)(anyNativeAPI);                                                 \\
        }                                                                                            \\
    } while (0)

**Description**

Obtains the corresponding struct pointer based on the struct type. This API takes parameters of **nativeAPIVariantKind** (an enumeration of type [ArkUI\_NativeAPIVariantKind](#arkui_nativeapivariantkind)), **structType** (of type const char\*), **structPtr** (of type structType\*). It calls [OH\_ArkUI\_QueryModuleInterfaceByName](#oh_arkui_querymoduleinterfacebyname) to obtain a native API pointer, casts it to structType\*, and assigns the result to **structPtr**.

**Since**: 12
