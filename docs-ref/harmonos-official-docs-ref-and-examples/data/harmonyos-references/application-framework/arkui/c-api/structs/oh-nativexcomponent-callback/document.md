# OH\_NativeXComponent\_Callback

typedef struct OH\_NativeXComponent\_Callback {...} OH\_NativeXComponent\_Callback

#### Overview

Registers callbacks for the surface lifecycle and touch event.

**Since**: 8

**Related module**: [OH\_NativeXComponent Native XComponent](../../modules/oh-nativexcomponent-native-xcomponent/document.md)

**Header file**: [native\_interface\_xcomponent.h](../../header-files/native-interface-xcomponent-h/document.md)

#### Summary

#### \[h2\]Member Functions

| Name | Description |
| :-- | :-- |
| [void (\*OnSurfaceCreated)(OH\_NativeXComponent\* component, void\* window)](#onsurfacecreated) | Invoked when a surface is created. |
| [void (\*OnSurfaceChanged)(OH\_NativeXComponent\* component, void\* window)](#onsurfacechanged) | Invoked when the surface changes. |
| [void (\*OnSurfaceDestroyed)(OH\_NativeXComponent\* component, void\* window)](#onsurfacedestroyed) | Invoked when the surface is destroyed. |
| [void (\*DispatchTouchEvent)(OH\_NativeXComponent\* component, void\* window)](#dispatchtouchevent) | Invoked when a touch event is triggered. |

#### Member Function Description

#### \[h2\]OnSurfaceCreated()

void (\*OnSurfaceCreated)(OH\_NativeXComponent\* component, void\* window)

**Description**

Invoked when a surface is created.

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeXComponent](../oh-nativexcomponent/document.md)\* component | Pointer to an [OH\_NativeXComponent](../oh-nativexcomponent/document.md) instance. |
| void\* window | Handle to the **NativeWindow** instance. |

#### \[h2\]OnSurfaceChanged()

void (\*OnSurfaceChanged)(OH\_NativeXComponent\* component, void\* window)

**Description**

Invoked when the surface changes.

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeXComponent](../oh-nativexcomponent/document.md)\* component | Pointer to an [OH\_NativeXComponent](../oh-nativexcomponent/document.md) instance. |
| void\* window | 
Handle to the **NativeWindow** instance.

The **NativeWindow** instance obtained through the **XComponent** lifecycle callback is held by the system side with a reference count. After the **OnSurfaceDestroyed** callback is triggered, the reference count is decreased by one. After the reference count reaches zero, the **NativeWindow** instance will be released.

 |

#### \[h2\]OnSurfaceDestroyed()

void (\*OnSurfaceDestroyed)(OH\_NativeXComponent\* component, void\* window)

**Description**

Invoked when the surface is destroyed.

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeXComponent](../oh-nativexcomponent/document.md)\* component | Pointer to an [OH\_NativeXComponent](../oh-nativexcomponent/document.md) instance. |
| void\* window | Handle to the **NativeWindow** instance. |

#### \[h2\]DispatchTouchEvent()

void (\*DispatchTouchEvent)(OH\_NativeXComponent\* component, void\* window)

**Description**

Invoked when a touch event is triggered.

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeXComponent](../oh-nativexcomponent/document.md)\* component | Pointer to an [OH\_NativeXComponent](../oh-nativexcomponent/document.md) instance. |
| void\* window | Handle to the **NativeWindow** instance. |
