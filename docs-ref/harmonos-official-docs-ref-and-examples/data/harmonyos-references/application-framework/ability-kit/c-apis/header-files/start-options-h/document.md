# start\_options.h

#### Overview

The file declares the [AbilityRuntime\_StartOptions](../../structs/abilityruntime-startoptions/document.md) struct for application startup parameters and the functions for setting and obtaining data.

**File to include**: <AbilityKit/ability\_runtime/start\_options.h>

**Library**: libability\_runtime.so

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Since**: 17

**Related module**: [AbilityRuntime](../../modules/abilityruntime/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [AbilityRuntime\_StartOptions](../../structs/abilityruntime-startoptions/document.md) | AbilityRuntime\_StartOptions | StartOptions struct. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [AbilityRuntime\_StartOptions\* OH\_AbilityRuntime\_CreateStartOptions(void)](#oh_abilityruntime_createstartoptions) | Creates an AbilityRuntime\_StartOptions object. |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_DestroyStartOptions(AbilityRuntime\_StartOptions \*\*startOptions)](#oh_abilityruntime_destroystartoptions) | Destroys an AbilityRuntime\_StartOptions object. |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsWindowMode(AbilityRuntime\_StartOptions \*startOptions,AbilityRuntime\_WindowMode windowMode)](#oh_abilityruntime_setstartoptionswindowmode) | Sets the window mode for starting an ability. |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsWindowMode(AbilityRuntime\_StartOptions \*startOptions,AbilityRuntime\_WindowMode &windowMode)](#oh_abilityruntime_getstartoptionswindowmode) | Obtains the window mode for starting an ability. |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsDisplayId(AbilityRuntime\_StartOptions \*startOptions,int32\_t displayId)](#oh_abilityruntime_setstartoptionsdisplayid) | Sets the ID of the display where the window is launched when the ability is started. |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsDisplayId(AbilityRuntime\_StartOptions \*startOptions,int32\_t &displayId)](#oh_abilityruntime_getstartoptionsdisplayid) | Obtains the ID of the display where the window is launched when the ability is started. |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsWithAnimation(AbilityRuntime\_StartOptions \*startOptions,bool withAnimation)](#oh_abilityruntime_setstartoptionswithanimation) | Sets whether to use animation effects when an ability is started. |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsWithAnimation(AbilityRuntime\_StartOptions \*startOptions,bool &withAnimation)](#oh_abilityruntime_getstartoptionswithanimation) | Checks whether animation effects are used when an ability is started. |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsWindowLeft(AbilityRuntime\_StartOptions \*startOptions,int32\_t windowLeft)](#oh_abilityruntime_setstartoptionswindowleft) | Sets the left position of the window when the ability is started, in px. |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsWindowLeft(AbilityRuntime\_StartOptions \*startOptions,int32\_t &windowLeft)](#oh_abilityruntime_getstartoptionswindowleft) | Obtains the left position of the window when the ability is started, in px. |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsWindowTop(AbilityRuntime\_StartOptions \*startOptions,int32\_t windowTop)](#oh_abilityruntime_setstartoptionswindowtop) | Sets the top position of the window when the ability is started, in px. |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsWindowTop(AbilityRuntime\_StartOptions \*startOptions,int32\_t &windowTop)](#oh_abilityruntime_getstartoptionswindowtop) | Obtains the top position of the window when the ability is started, in px. |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsWindowHeight(AbilityRuntime\_StartOptions \*startOptions,int32\_t windowHeight)](#oh_abilityruntime_setstartoptionswindowheight) | Sets the height of the window when the ability is started, in px. |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsWindowHeight(AbilityRuntime\_StartOptions \*startOptions,int32\_t &windowHeight)](#oh_abilityruntime_getstartoptionswindowheight) | Obtains the height of the window when the ability is started, in px. |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsWindowWidth(AbilityRuntime\_StartOptions \*startOptions,int32\_t windowWidth)](#oh_abilityruntime_setstartoptionswindowwidth) | Sets the width of the window when the ability is started, in px. |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsWindowWidth(AbilityRuntime\_StartOptions \*startOptions,int32\_t &windowWidth)](#oh_abilityruntime_getstartoptionswindowwidth) | Obtains the width of the window when the ability is started, in px. |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsStartVisibility(AbilityRuntime\_StartOptions \*startOptions,AbilityRuntime\_StartVisibility startVisibility)](#oh_abilityruntime_setstartoptionsstartvisibility) | Sets the visibility of the window and dock bar icons when the ability is started. |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsStartVisibility(AbilityRuntime\_StartOptions \*startOptions,AbilityRuntime\_StartVisibility &startVisibility)](#oh_abilityruntime_getstartoptionsstartvisibility) | Obtains the visibility of the window and dock bar icons when the ability is started. |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsStartWindowIcon(AbilityRuntime\_StartOptions \*startOptions,OH\_PixelmapNative \*startWindowIcon)](#oh_abilityruntime_setstartoptionsstartwindowicon) | Sets the startup icon of the window when the ability is started. The maximum size of an image used as the startup icon is 600 MB. |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsStartWindowIcon(AbilityRuntime\_StartOptions \*startOptions,OH\_PixelmapNative \*\*startWindowIcon)](#oh_abilityruntime_getstartoptionsstartwindowicon) | Obtains the startup icon of the window when the ability is started. |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsStartWindowBackgroundColor(AbilityRuntime\_StartOptions \*startOptions, const char \*startWindowBackgroundColor)](#oh_abilityruntime_setstartoptionsstartwindowbackgroundcolor) | Sets the background color of the window when the ability is started. If this function is not called, the value of **startWindowBackground** configured under **abilities** in the **module.json5** file corresponding to the UIAbility is used by default. |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsStartWindowBackgroundColor(AbilityRuntime\_StartOptions \*startOptions, char \*\*startWindowBackgroundColor, size\_t &size)](#oh_abilityruntime_getstartoptionsstartwindowbackgroundcolor) | Obtains the background color of the window when the ability is started. |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsSupportedWindowModes(AbilityRuntime\_StartOptions \*startOptions, AbilityRuntime\_SupportedWindowMode \*supportedWindowModes,size\_t size)](#oh_abilityruntime_setstartoptionssupportedwindowmodes) | Sets the window modes supported by the ability when it is started. If this function is not called, the value of **supportWindowMode** configured under **abilities** in the **module.json5** file corresponding to the UIAbility is used by default. |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsSupportedWindowModes(AbilityRuntime\_StartOptions \*startOptions, AbilityRuntime\_SupportedWindowMode \*\*supportedWindowModes,size\_t &size)](#oh_abilityruntime_getstartoptionssupportedwindowmodes) | Obtains the window modes supported by the ability when it is started. |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsMinWindowWidth(AbilityRuntime\_StartOptions \*startOptions, int32\_t minWindowWidth)](#oh_abilityruntime_setstartoptionsminwindowwidth) | Sets the minimum width of the window when the ability is started, in vp. |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsMinWindowWidth(AbilityRuntime\_StartOptions \*startOptions, int32\_t &minWindowWidth)](#oh_abilityruntime_getstartoptionsminwindowwidth) | Obtains the minimum width of the window when the ability is started, in vp. |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsMaxWindowWidth(AbilityRuntime\_StartOptions \*startOptions, int32\_t maxWindowWidth)](#oh_abilityruntime_setstartoptionsmaxwindowwidth) | Sets the maximum width of the window when the ability is started, in vp. |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsMaxWindowWidth(AbilityRuntime\_StartOptions \*startOptions, int32\_t &maxWindowWidth)](#oh_abilityruntime_getstartoptionsmaxwindowwidth) | Obtains the maximum width of the window when the ability is started, in vp. |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsMinWindowHeight(AbilityRuntime\_StartOptions \*startOptions, int32\_t minWindowHeight)](#oh_abilityruntime_setstartoptionsminwindowheight) | Sets the minimum height of the window when the ability is started, in vp. |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsMinWindowHeight(AbilityRuntime\_StartOptions \*startOptions, int32\_t &minWindowHeight)](#oh_abilityruntime_getstartoptionsminwindowheight) | Obtains the minimum height of the window when the ability is started, in vp. |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsMaxWindowHeight(AbilityRuntime\_StartOptions \*startOptions, int32\_t maxWindowHeight)](#oh_abilityruntime_setstartoptionsmaxwindowheight) | Sets the maximum height of the window when the ability is started, in vp. |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsMaxWindowHeight(AbilityRuntime\_StartOptions \*startOptions, int32\_t &maxWindowHeight)](#oh_abilityruntime_getstartoptionsmaxwindowheight) | Obtains the maximum height of the window when the ability is started, in vp. |

#### Function Description

#### \[h2\]OH\_AbilityRuntime\_CreateStartOptions()

AbilityRuntime\_StartOptions\* OH\_AbilityRuntime\_CreateStartOptions(void)

**Description**

Creates an [AbilityRuntime\_StartOptions](../../structs/abilityruntime-startoptions/document.md) object.

**Since**: 17

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](../../structs/abilityruntime-startoptions/document.md)\* | Pointer to the AbilityRuntime\_StartOptions object created. |

**Example**

#include <AbilityKit/ability\_runtime/start\_options.h>

void createStartOptionsTest()
{
    AbilityRuntime\_StartOptions\* options = OH\_AbilityRuntime\_CreateStartOptions();
    if (options == nullptr) {
        // Record error logs and other service processing.
        return;
    }

    // Destroy options to prevent memory leakage.
    OH\_AbilityRuntime\_DestroyStartOptions(&options);
}

#### \[h2\]OH\_AbilityRuntime\_DestroyStartOptions()

AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_DestroyStartOptions(AbilityRuntime\_StartOptions \*\*startOptions)

**Description**

Destroys an [AbilityRuntime\_StartOptions](../../structs/abilityruntime-startoptions/document.md) object.

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](../../structs/abilityruntime-startoptions/document.md) \*\*startOptions | Double pointer to the AbilityRuntime\_StartOptions object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](../ability-runtime-common-h/document.md#abilityruntime_errorcode) | 
**ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR**: The call is successful.

**ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID**: The input parameter **StartOptions** is nullptr.

 |

**Example**

#include <AbilityKit/ability\_runtime/start\_options.h>

void destroyStartOptionsTest()
{
    AbilityRuntime\_StartOptions\* options = OH\_AbilityRuntime\_CreateStartOptions();
    if (options == nullptr) {
        // Record error logs and other service processing.
        return;
    }

    // Destroy options to prevent memory leakage.
    OH\_AbilityRuntime\_DestroyStartOptions(&options);
}

#### \[h2\]OH\_AbilityRuntime\_SetStartOptionsWindowMode()

AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsWindowMode(AbilityRuntime\_StartOptions \*startOptions,AbilityRuntime\_WindowMode windowMode)

**Description**

Sets the window mode for starting an ability.

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](../../structs/abilityruntime-startoptions/document.md) \*startOptions | Pointer to an AbilityRuntime\_StartOptions object. |
| [AbilityRuntime\_WindowMode](../context-constant-h/document.md#abilityruntime_windowmode) windowMode | Window mode. For details about the available options, see **AbilityRuntime\_WindowMode**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](../ability-runtime-common-h/document.md#abilityruntime_errorcode) | 
**ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR**: The call is successful.

**ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID**: The input parameter **StartOptions** is nullptr, or **WindowMode** is invalid.

 |

**Example**

#include <AbilityKit/ability\_runtime/start\_options.h>

void demo()
{
    AbilityRuntime\_StartOptions\* options = OH\_AbilityRuntime\_CreateStartOptions();
    if (options == nullptr) {
        // Record error logs and other service processing.
        return;
    }

    AbilityRuntime\_ErrorCode err = OH\_AbilityRuntime\_SetStartOptionsWindowMode(options,
        ABILITY\_RUNTIME\_WINDOW\_MODE\_FULL\_SCREEN);
    if (err != ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR) {
        // Record error logs and other service processing.
    }
    // Destroy options to prevent memory leakage.
    OH\_AbilityRuntime\_DestroyStartOptions(&options);
}

#### \[h2\]OH\_AbilityRuntime\_GetStartOptionsWindowMode()

AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsWindowMode(AbilityRuntime\_StartOptions \*startOptions,AbilityRuntime\_WindowMode &windowMode)

**Description**

Obtains the window mode for starting an ability.

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](../../structs/abilityruntime-startoptions/document.md) \*startOptions | Pointer to an AbilityRuntime\_StartOptions object. |
| [AbilityRuntime\_WindowMode](../context-constant-h/document.md#abilityruntime_windowmode) windowMode | Window mode. For details about the available options, see **AbilityRuntime\_WindowMode**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](../ability-runtime-common-h/document.md#abilityruntime_errorcode) | 
**ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR**: The call is successful.

**ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID**: The input parameter **StartOptions** is nullptr.

 |

**Example**

#include <AbilityKit/ability\_runtime/start\_options.h>

void demo()
{
    AbilityRuntime\_StartOptions\* options = OH\_AbilityRuntime\_CreateStartOptions();
    if (options == nullptr) {
        // Record error logs and other service processing.
        return;
    }

    AbilityRuntime\_WindowMode windowMode = ABILITY\_RUNTIME\_WINDOW\_MODE\_UNDEFINED;
    AbilityRuntime\_ErrorCode err = OH\_AbilityRuntime\_GetStartOptionsWindowMode(options, windowMode);
    if (err != ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR) {
        // Record error logs and other service processing.
    }
    // Destroy options to prevent memory leakage.
    OH\_AbilityRuntime\_DestroyStartOptions(&options);
}

#### \[h2\]OH\_AbilityRuntime\_SetStartOptionsDisplayId()

AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsDisplayId(AbilityRuntime\_StartOptions \*startOptions,int32\_t displayId)

**Description**

Sets the ID of the display where the window is launched when the ability is started.

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](../../structs/abilityruntime-startoptions/document.md) \*startOptions | Pointer to an AbilityRuntime\_StartOptions object. |
| int32\_t displayId | Display ID. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](../ability-runtime-common-h/document.md#abilityruntime_errorcode) | 
**ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR**: The call is successful.

**ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID**: The input parameter **StartOptions** is nullptr.

 |

**Example**

#include <AbilityKit/ability\_runtime/start\_options.h>

void demo()
{
    AbilityRuntime\_StartOptions\* options = OH\_AbilityRuntime\_CreateStartOptions();
    if (options == nullptr) {
        // Record error logs and other service processing.
        return;
    }

    AbilityRuntime\_ErrorCode err = OH\_AbilityRuntime\_SetStartOptionsDisplayId(options, 1);
    if (err != ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR) {
        // Record error logs and other service processing.
    }
    // Destroy options to prevent memory leakage.
    OH\_AbilityRuntime\_DestroyStartOptions(&options);
}

#### \[h2\]OH\_AbilityRuntime\_GetStartOptionsDisplayId()

AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsDisplayId(AbilityRuntime\_StartOptions \*startOptions,int32\_t &displayId)

**Description**

Obtains the ID of the display where the window is launched when the ability is started.

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](../../structs/abilityruntime-startoptions/document.md) \*startOptions | Pointer to an AbilityRuntime\_StartOptions object. |
| int32\_t &displayId | Display ID. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](../ability-runtime-common-h/document.md#abilityruntime_errorcode) | 
**ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR**: The call is successful.

**ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID**: The input parameter **StartOptions** is nullptr.

 |

**Example**

#include <AbilityKit/ability\_runtime/start\_options.h>

void demo()
{
    AbilityRuntime\_StartOptions\* options = OH\_AbilityRuntime\_CreateStartOptions();
    if (options == nullptr) {
        // Record error logs and other service processing.
        return;
    }

    int32\_t displayId = 0;
    AbilityRuntime\_ErrorCode err = OH\_AbilityRuntime\_GetStartOptionsDisplayId(options, displayId);
    if (err != ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR) {
        // Record error logs and other service processing.
    }
    // Destroy options to prevent memory leakage.
    OH\_AbilityRuntime\_DestroyStartOptions(&options);
}

#### \[h2\]OH\_AbilityRuntime\_SetStartOptionsWithAnimation()

AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsWithAnimation(AbilityRuntime\_StartOptions \*startOptions,bool withAnimation)

**Description**

Sets whether to use animation effects when an ability is started.

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](../../structs/abilityruntime-startoptions/document.md) \*startOptions | Pointer to an AbilityRuntime\_StartOptions object. |
| bool withAnimation | 
Whether to use animation effects.

**true** to use, **false** otherwise.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](../ability-runtime-common-h/document.md#abilityruntime_errorcode) | 
**ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR**: The call is successful.

**ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID**: The input parameter **StartOptions** is nullptr.

 |

**Example**

#include <AbilityKit/ability\_runtime/start\_options.h>

void demo()
{
    AbilityRuntime\_StartOptions\* options = OH\_AbilityRuntime\_CreateStartOptions();
    if (options == nullptr) {
        // Record error logs and other service processing.
        return;
    }

    AbilityRuntime\_ErrorCode err = OH\_AbilityRuntime\_SetStartOptionsWithAnimation(options, true);
    if (err != ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR) {
        // Record error logs and other service processing.
    }
    // Destroy options to prevent memory leakage.
    OH\_AbilityRuntime\_DestroyStartOptions(&options);
}

#### \[h2\]OH\_AbilityRuntime\_GetStartOptionsWithAnimation()

AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsWithAnimation(AbilityRuntime\_StartOptions \*startOptions,bool &withAnimation)

**Description**

Checks whether animation effects are used when an ability is started.

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](../../structs/abilityruntime-startoptions/document.md) \*startOptions | Pointer to an AbilityRuntime\_StartOptions object. |
| bool &withAnimation | 
Whether animation effects are used.

**true** to use, **false** otherwise.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](../ability-runtime-common-h/document.md#abilityruntime_errorcode) | 
**ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR**: The call is successful.

**ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID**: The input parameter **StartOptions** is nullptr.

 |

**Example**

#include <AbilityKit/ability\_runtime/start\_options.h>

void demo()
{
    AbilityRuntime\_StartOptions\* options = OH\_AbilityRuntime\_CreateStartOptions();
    if (options == nullptr) {
        // Record error logs and other service processing.
        return;
    }

    bool withAnimation = false;
    AbilityRuntime\_ErrorCode err = OH\_AbilityRuntime\_GetStartOptionsWithAnimation(options, withAnimation);
    if (err != ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR) {
        // Record error logs and other service processing.
    }
    // Destroy options to prevent memory leakage.
    OH\_AbilityRuntime\_DestroyStartOptions(&options);
}

#### \[h2\]OH\_AbilityRuntime\_SetStartOptionsWindowLeft()

AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsWindowLeft(AbilityRuntime\_StartOptions \*startOptions,int32\_t windowLeft)

**Description**

Sets the left position of the window when the ability is started, in px.

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](../../structs/abilityruntime-startoptions/document.md) \*startOptions | Pointer to an AbilityRuntime\_StartOptions object. |
| int32\_t windowLeft | Left position of the window, in px. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](../ability-runtime-common-h/document.md#abilityruntime_errorcode) | 
**ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR**: The call is successful.

**ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID**: The input parameter **StartOptions** is nullptr.

 |

**Example**

#include <AbilityKit/ability\_runtime/start\_options.h>

void demo()
{
    AbilityRuntime\_StartOptions\* options = OH\_AbilityRuntime\_CreateStartOptions();
    if (options == nullptr) {
        // Record error logs and other service processing.
        return;
    }

    AbilityRuntime\_ErrorCode err = OH\_AbilityRuntime\_SetStartOptionsWindowLeft(options, 200);
    if (err != ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR) {
        // Record error logs and other service processing.
    }
    // Destroy options to prevent memory leakage.
    OH\_AbilityRuntime\_DestroyStartOptions(&options);
}

#### \[h2\]OH\_AbilityRuntime\_GetStartOptionsWindowLeft()

AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsWindowLeft(AbilityRuntime\_StartOptions \*startOptions,int32\_t &windowLeft)

**Description**

Obtains the left position of the window when the ability is started, in px.

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](../../structs/abilityruntime-startoptions/document.md) \*startOptions | Pointer to an AbilityRuntime\_StartOptions object. |
| int32\_t &windowLeft | Left position of the window, in px. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](../ability-runtime-common-h/document.md#abilityruntime_errorcode) | 
**ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR**: The call is successful.

**ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID**: The input parameter **StartOptions** is nullptr.

 |

**Example**

#include <AbilityKit/ability\_runtime/start\_options.h>

void demo()
{
    AbilityRuntime\_StartOptions\* options = OH\_AbilityRuntime\_CreateStartOptions();
    if (options == nullptr) {
        // Record error logs and other service processing.
        return;
    }

    int32\_t windowLeft = 0;
    AbilityRuntime\_ErrorCode err = OH\_AbilityRuntime\_GetStartOptionsWindowLeft(options, windowLeft);
    if (err != ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR) {
        // Record error logs and other service processing.
    }
    // Destroy options to prevent memory leakage.
    OH\_AbilityRuntime\_DestroyStartOptions(&options);
}

#### \[h2\]OH\_AbilityRuntime\_SetStartOptionsWindowTop()

AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsWindowTop(AbilityRuntime\_StartOptions \*startOptions,int32\_t windowTop)

**Description**

Sets the top position of the window when the ability is started, in px.

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](../../structs/abilityruntime-startoptions/document.md) \*startOptions | Pointer to an AbilityRuntime\_StartOptions object. |
| int32\_t windowTop | Top position of the window, in px. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](../ability-runtime-common-h/document.md#abilityruntime_errorcode) | 
**ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR**: The call is successful.

**ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID**: The input parameter **StartOptions** is nullptr.

 |

**Example**

#include <AbilityKit/ability\_runtime/start\_options.h>

void demo()
{
    AbilityRuntime\_StartOptions\* options = OH\_AbilityRuntime\_CreateStartOptions();
    if (options == nullptr) {
        // Record error logs and other service processing.
        return;
    }

    AbilityRuntime\_ErrorCode err = OH\_AbilityRuntime\_SetStartOptionsWindowTop(options, 500);
    if (err != ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR) {
        // Record error logs and other service processing.
    }
    // Destroy options to prevent memory leakage.
    OH\_AbilityRuntime\_DestroyStartOptions(&options);
}

#### \[h2\]OH\_AbilityRuntime\_GetStartOptionsWindowTop()

AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsWindowTop(AbilityRuntime\_StartOptions \*startOptions,int32\_t &windowTop)

**Description**

Obtains the top position of the window when the ability is started, in px.

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](../../structs/abilityruntime-startoptions/document.md) \*startOptions | Pointer to an AbilityRuntime\_StartOptions object. |
| int32\_t &windowTop | Top position of the window, in px. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](../ability-runtime-common-h/document.md#abilityruntime_errorcode) | 
**ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR**: The call is successful.

**ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID**: The input parameter **StartOptions** is nullptr.

 |

**Example**

#include <AbilityKit/ability\_runtime/start\_options.h>

void demo()
{
    AbilityRuntime\_StartOptions\* options = OH\_AbilityRuntime\_CreateStartOptions();
    if (options == nullptr) {
        // Record error logs and other service processing.
        return;
    }

    int32\_t windowTop = 0;
    AbilityRuntime\_ErrorCode err = OH\_AbilityRuntime\_GetStartOptionsWindowTop(options, windowTop);
    if (err != ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR) {
        // Record error logs and other service processing.
    }
    // Destroy options to prevent memory leakage.
    OH\_AbilityRuntime\_DestroyStartOptions(&options);
}

#### \[h2\]OH\_AbilityRuntime\_SetStartOptionsWindowHeight()

AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsWindowHeight(AbilityRuntime\_StartOptions \*startOptions,int32\_t windowHeight)

**Description**

Sets the height of the window when the ability is started, in px.

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](../../structs/abilityruntime-startoptions/document.md) \*startOptions | Pointer to an AbilityRuntime\_StartOptions object. |
| int32\_t windowHeight | Window height, in px. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](../ability-runtime-common-h/document.md#abilityruntime_errorcode) | 
**ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR**: The call is successful.

**ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID**: The input parameter **StartOptions** is nullptr.

 |

**Example**

#include <AbilityKit/ability\_runtime/start\_options.h>

void demo()
{
    AbilityRuntime\_StartOptions\* options = OH\_AbilityRuntime\_CreateStartOptions();
    if (options == nullptr) {
        // Record error logs and other service processing.
        return;
    }

    AbilityRuntime\_ErrorCode err = OH\_AbilityRuntime\_SetStartOptionsWindowHeight(options, 500);
    if (err != ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR) {
        // Record error logs and other service processing.
    }
    // Destroy options to prevent memory leakage.
    OH\_AbilityRuntime\_DestroyStartOptions(&options);
}

#### \[h2\]OH\_AbilityRuntime\_GetStartOptionsWindowHeight()

AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsWindowHeight(AbilityRuntime\_StartOptions \*startOptions,int32\_t &windowHeight)

**Description**

Obtains the height of the window when the ability is started, in px.

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](../../structs/abilityruntime-startoptions/document.md) \*startOptions | Pointer to an AbilityRuntime\_StartOptions object. |
| int32\_t &windowHeight | Window height, in px. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](../ability-runtime-common-h/document.md#abilityruntime_errorcode) | 
**ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR**: The call is successful.

**ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID**: The input parameter **StartOptions** is nullptr.

 |

**Example**

#include <AbilityKit/ability\_runtime/start\_options.h>

void demo()
{
    AbilityRuntime\_StartOptions\* options = OH\_AbilityRuntime\_CreateStartOptions();
    if (options == nullptr) {
        // Record error logs and other service processing.
        return;
    }

    int32\_t windowHeight = 0;
    AbilityRuntime\_ErrorCode err = OH\_AbilityRuntime\_GetStartOptionsWindowHeight(options, windowHeight);
    if (err != ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR) {
        // Record error logs and other service processing.
    }
    // Destroy options to prevent memory leakage.
    OH\_AbilityRuntime\_DestroyStartOptions(&options);
}

#### \[h2\]OH\_AbilityRuntime\_SetStartOptionsWindowWidth()

AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsWindowWidth(AbilityRuntime\_StartOptions \*startOptions,int32\_t windowWidth)

**Description**

Sets the width of the window when the ability is started, in px.

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](../../structs/abilityruntime-startoptions/document.md) \*startOptions | Pointer to an AbilityRuntime\_StartOptions object. |
| int32\_t windowWidth | Window width, in px. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](../ability-runtime-common-h/document.md#abilityruntime_errorcode) | 
**ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR**: The call is successful.

**ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID**: The input parameter **StartOptions** is nullptr.

 |

**Example**

#include <AbilityKit/ability\_runtime/start\_options.h>

void demo()
{
    AbilityRuntime\_StartOptions\* options = OH\_AbilityRuntime\_CreateStartOptions();
    if (options == nullptr) {
        // Record error logs and other service processing.
        return;
    }

    AbilityRuntime\_ErrorCode err = OH\_AbilityRuntime\_SetStartOptionsWindowWidth(options, 500);
    if (err != ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR) {
        // Record error logs and other service processing.
    }
    // Destroy options to prevent memory leakage.
    OH\_AbilityRuntime\_DestroyStartOptions(&options);
}

#### \[h2\]OH\_AbilityRuntime\_GetStartOptionsWindowWidth()

AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsWindowWidth(AbilityRuntime\_StartOptions \*startOptions,int32\_t &windowWidth)

**Description**

Obtains the width of the window when the ability is started, in px.

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](../../structs/abilityruntime-startoptions/document.md) \*startOptions | Pointer to an AbilityRuntime\_StartOptions object. |
| int32\_t &windowWidth | Window width, in px. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](../ability-runtime-common-h/document.md#abilityruntime_errorcode) | 
**ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR**: The call is successful.

**ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID**: The input parameter **StartOptions** is nullptr.

 |

**Example**

#include <AbilityKit/ability\_runtime/start\_options.h>

void demo()
{
    AbilityRuntime\_StartOptions\* options = OH\_AbilityRuntime\_CreateStartOptions();
    if (options == nullptr) {
        // Record error logs and other service processing.
        return;
    }

    int32\_t windowWidth = 0;
    AbilityRuntime\_ErrorCode err = OH\_AbilityRuntime\_GetStartOptionsWindowWidth(options, windowWidth);
    if (err != ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR) {
        // Record error logs and other service processing.
    }
    // Destroy options to prevent memory leakage.
    OH\_AbilityRuntime\_DestroyStartOptions(&options);
}

#### \[h2\]OH\_AbilityRuntime\_SetStartOptionsStartVisibility()

AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsStartVisibility(AbilityRuntime\_StartOptions \*startOptions,AbilityRuntime\_StartVisibility startVisibility)

**Description**

Sets the visibility of the window and dock bar icons when the ability is started.

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](../../structs/abilityruntime-startoptions/document.md) \*startOptions | Pointer to the StartOptions struct. |
| [AbilityRuntime\_StartVisibility](../context-constant-h/document.md#abilityruntime_startvisibility) startVisibility | Visibility. For details about the available options, see **AbilityRuntime\_StartVisibility**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](../ability-runtime-common-h/document.md#abilityruntime_errorcode) | 
**ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR**: The setting is successful.

**ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID**: The input parameter **StartOptions** is nullptr, or **startVisibility** is not an enumerated value of **AbilityRuntime\_StartVisibility**.

 |

**Example**

#include <AbilityKit/ability\_runtime/start\_options.h>

void demo()
{
    AbilityRuntime\_StartOptions\* options = OH\_AbilityRuntime\_CreateStartOptions();
    if (options == nullptr) {
        // Record error logs and other service processing.
        return;
    }

    AbilityRuntime\_StartVisibility visibility = AbilityRuntime\_StartVisibility::ABILITY\_RUNTIME\_SHOW\_UPON\_START;
    AbilityRuntime\_ErrorCode err = OH\_AbilityRuntime\_SetStartOptionsStartVisibility(options, visibility);
    if (err != ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR) {
        // Record error logs and other service processing.
    }
    // Destroy options to prevent memory leakage.
    OH\_AbilityRuntime\_DestroyStartOptions(&options);
}

#### \[h2\]OH\_AbilityRuntime\_GetStartOptionsStartVisibility()

AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsStartVisibility(AbilityRuntime\_StartOptions \*startOptions,AbilityRuntime\_StartVisibility &startVisibility)

**Description**

Obtains the visibility of the window and dock bar icons when the ability is started.

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](../../structs/abilityruntime-startoptions/document.md) \*startOptions | Pointer to the StartOptions struct. |
| [AbilityRuntime\_StartVisibility](../context-constant-h/document.md#abilityruntime_startvisibility) &startVisibility | Visibility. For details about the available options, see **AbilityRuntime\_StartVisibility**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](../ability-runtime-common-h/document.md#abilityruntime_errorcode) | 
**ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR**: The retrieval is successful.

**ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID**: The input parameter **StartOptions** is nullptr, or **startVisibility** is empty.

 |

**Example**

#include <AbilityKit/ability\_runtime/start\_options.h>

void demo()
{
    AbilityRuntime\_StartOptions\* options = OH\_AbilityRuntime\_CreateStartOptions();
    if (options == nullptr) {
        // Record error logs and other service processing.
        return;
    }

    AbilityRuntime\_StartVisibility visibility;
    AbilityRuntime\_ErrorCode err = OH\_AbilityRuntime\_GetStartOptionsStartVisibility(options, visibility);
    if (err != ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR) {
        // Record error logs and other service processing.
    }
    // Destroy options to prevent memory leakage.
    OH\_AbilityRuntime\_DestroyStartOptions(&options);
}

#### \[h2\]OH\_AbilityRuntime\_SetStartOptionsStartWindowIcon()

AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsStartWindowIcon(AbilityRuntime\_StartOptions \*startOptions,OH\_PixelmapNative \*startWindowIcon)

**Description**

Sets the startup icon of the window when the ability is started. The maximum size of an image used as the startup icon is 600 MB.

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](../../structs/abilityruntime-startoptions/document.md) \*startOptions | Pointer to an AbilityRuntime\_StartOptions object. |
| OH\_PixelmapNative \*startWindowIcon | Pointer to the startup icon of the window. The maximum size of an image used as the startup icon is 600 MB. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](../ability-runtime-common-h/document.md#abilityruntime_errorcode) | 
**ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR**: The call is successful.

**ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID**: The input parameter **StartOptions** is nullptr, or **OH\_PixelmapNative** is not nullptr.

 |

**Example**

#include <AbilityKit/ability\_runtime/start\_options.h>

void demo()
{
    uint8\_t data\[96\];
    size\_t dataSize = 96;
    for (int i = 0; i < dataSize; i++) {
        data\[i\] = i + 1;
    }

    // Create a parameter structure instance and set parameters.
    OH\_Pixelmap\_InitializationOptions \*createOpts = nullptr;
    OH\_PixelmapInitializationOptions\_Create(&createOpts);
    OH\_PixelmapInitializationOptions\_SetWidth(createOpts, 6);
    OH\_PixelmapInitializationOptions\_SetHeight(createOpts, 4);
    OH\_PixelmapInitializationOptions\_SetPixelFormat(createOpts, PIXEL\_FORMAT\_RGBA\_8888);
    OH\_PixelmapInitializationOptions\_SetAlphaType(createOpts, PIXELMAP\_ALPHA\_TYPE\_UNKNOWN);

    // Create a PixelMap instance.
    OH\_PixelmapNative \*startWindowIcon = nullptr;
    Image\_ErrorCode errCode = OH\_PixelmapNative\_CreatePixelmap(data, dataSize, createOpts, &startWindowIcon);
    if (errCode != IMAGE\_SUCCESS) {
        // Record error logs and other service processing.

        // Destroy createOpts to prevent memory leakage.
        OH\_PixelmapInitializationOptions\_Release(createOpts);
        return;
    }

    AbilityRuntime\_StartOptions\* options = OH\_AbilityRuntime\_CreateStartOptions();
    if (options == nullptr) {
        // Record error logs and other service processing.

        // Destroy createOpts to prevent memory leakage.
        OH\_PixelmapInitializationOptions\_Release(createOpts);

        // Destroy startWindowIcon to prevent memory leakage.
        OH\_PixelmapNative\_Release(startWindowIcon);
        return;
    }

    AbilityRuntime\_ErrorCode err = OH\_AbilityRuntime\_SetStartOptionsStartWindowIcon(options, startWindowIcon);
    if (err != ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR) {
        // Record error logs and other service processing.
    }
    // Destroy createOpts to prevent memory leakage.
    OH\_PixelmapInitializationOptions\_Release(createOpts);

    // Destroy startWindowIcon to prevent memory leakage.
    OH\_PixelmapNative\_Release(startWindowIcon);

    // Destroy options to prevent memory leakage.
    OH\_AbilityRuntime\_DestroyStartOptions(&options);
}

#### \[h2\]OH\_AbilityRuntime\_GetStartOptionsStartWindowIcon()

AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsStartWindowIcon(AbilityRuntime\_StartOptions \*startOptions,OH\_PixelmapNative \*\*startWindowIcon)

**Description**

Obtains the startup icon of the window when the ability is started.

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](../../structs/abilityruntime-startoptions/document.md) \*startOptions | Pointer to an AbilityRuntime\_StartOptions object. |
| OH\_PixelmapNative \*\*startWindowIcon | Double pointer to the startup icon of the window. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](../ability-runtime-common-h/document.md#abilityruntime_errorcode) | 
**ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR**: The call is successful.

**ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID**: The input parameter **StartOptions** or **StartWindowBackgroundColor** is nullptr.

 |

**Example**

#include <AbilityKit/ability\_runtime/start\_options.h>

void demo()
{
    AbilityRuntime\_StartOptions\* options = OH\_AbilityRuntime\_CreateStartOptions();
    if (options == nullptr) {
        // Record error logs and other service processing.
        return;
    }

    OH\_PixelmapNative \*startWindowIcon = nullptr;
    AbilityRuntime\_ErrorCode err = OH\_AbilityRuntime\_GetStartOptionsStartWindowIcon(options, &startWindowIcon);
    if (err != ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR) {
        // Record error logs and other service processing.
    }

    // Destroy startWindowIcon to prevent memory leakage.
    OH\_PixelmapNative\_Release(startWindowIcon);

    // Destroy options to prevent memory leakage.
    OH\_AbilityRuntime\_DestroyStartOptions(&options);
}

#### \[h2\]OH\_AbilityRuntime\_SetStartOptionsStartWindowBackgroundColor()

AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsStartWindowBackgroundColor(AbilityRuntime\_StartOptions \*startOptions, const char \*startWindowBackgroundColor)

**Description**

Sets the background color of the window when the ability is started. If this property is not set, the value of **startWindowBackground** configured under [abilities](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#abilities) in the [module.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file) file corresponding to the UIAbility is used by default.

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](../../structs/abilityruntime-startoptions/document.md) \*startOptions | Pointer to an AbilityRuntime\_StartOptions object. |
| const char \*startWindowBackgroundColor | Pointer to the background color of the window. The value is in ARGB format, for example, **#E5FFFFFF**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](../ability-runtime-common-h/document.md#abilityruntime_errorcode) | 
**ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR**: The call is successful.

**ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID**: The input parameter **StartOptions** is nullptr, or **StartWindowBackgroundColor** is not nullptr.

 |

**Example**

#include <AbilityKit/ability\_runtime/start\_options.h>

void demo()
{
    AbilityRuntime\_StartOptions\* options = OH\_AbilityRuntime\_CreateStartOptions();
    if (options == nullptr) {
        // Record error logs and other service processing.
        return;
    }

    AbilityRuntime\_ErrorCode err = OH\_AbilityRuntime\_SetStartOptionsStartWindowBackgroundColor(options, "#00000000");
    if (err != ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR) {
        // Record error logs and other service processing.
    }

    // Destroy options to prevent memory leakage.
    OH\_AbilityRuntime\_DestroyStartOptions(&options);
}

#### \[h2\]OH\_AbilityRuntime\_GetStartOptionsStartWindowBackgroundColor()

AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsStartWindowBackgroundColor(AbilityRuntime\_StartOptions \*startOptions, char \*\*startWindowBackgroundColor, size\_t &size)

**Description**

Obtains the background color of the window when the ability is started.

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](../../structs/abilityruntime-startoptions/document.md) \*startOptions | Pointer to an AbilityRuntime\_StartOptions object. |
| char \*\*startWindowBackgroundColor | Double pointer to the background color of the window. The value is in ARGB format, for example, **#E5FFFFFF**. |
| size\_t &size | Size of the background color. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](../ability-runtime-common-h/document.md#abilityruntime_errorcode) | 
**ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR**: The call is successful.

**ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID**: The input parameter **StartOptions** or **SupportedWindowModes** is nullptr, or **Size** is **0**.

**ABILITY\_RUNTIME\_ERROR\_CODE\_INTERNAL**: An internal error that cannot be rectified, such as internal malloc error or string copy function error, occurs.

 |

**Example**

#include <cstdlib>

#include <AbilityKit/ability\_runtime/start\_options.h>

void demo()
{
    AbilityRuntime\_StartOptions\* options = OH\_AbilityRuntime\_CreateStartOptions();
    if (options == nullptr) {
        // Record error logs and other service processing.
        return;
    }

    char \*startWindowBackgroundColor = nullptr;
    size\_t size = 0;
    AbilityRuntime\_ErrorCode err = OH\_AbilityRuntime\_GetStartOptionsStartWindowBackgroundColor(options,
        &startWindowBackgroundColor, size);
    if (err != ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR) {
        // Record error logs and other service processing.
    }

    if (startWindowBackgroundColor != nullptr) {
        // Destroy startWindowBackgroundColor to prevent memory leakage.
        free(startWindowBackgroundColor);
        startWindowBackgroundColor = nullptr;
    }

    // Destroy options to prevent memory leakage.
    OH\_AbilityRuntime\_DestroyStartOptions(&options);
}

#### \[h2\]OH\_AbilityRuntime\_SetStartOptionsSupportedWindowModes()

AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsSupportedWindowModes(AbilityRuntime\_StartOptions \*startOptions, AbilityRuntime\_SupportedWindowMode \*supportedWindowModes,size\_t size)

**Description**

Sets the window modes supported by the ability when it is started.

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](../../structs/abilityruntime-startoptions/document.md) \*startOptions | Pointer to an AbilityRuntime\_StartOptions object. |
| [AbilityRuntime\_SupportedWindowMode](../context-constant-h/document.md#abilityruntime_supportedwindowmode) \*supportedWindowModes | Pointer to the window modes supported. For details about the available options, see **AbilityRuntime\_SupportedWindowMode**. |
| size\_t size | Size of the window modes supported. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](../ability-runtime-common-h/document.md#abilityruntime_errorcode) | 
**ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR**: The call is successful.

**ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID**: The input parameter **StartOptions** or **SupportedWindowModes** is nullptr, or **Size** is **0**.

 |

**Example**

#include <AbilityKit/ability\_runtime/start\_options.h>

void demo()
{
    AbilityRuntime\_StartOptions\* options = OH\_AbilityRuntime\_CreateStartOptions();
    if (options == nullptr) {
        // Record error logs and other service processing.
        return;
    }

    size\_t supportedWindowModesSize = 3;
    AbilityRuntime\_SupportedWindowMode supportedWindowModes\[3\] = {
        ABILITY\_RUNTIME\_SUPPORTED\_WINDOW\_MODE\_FULL\_SCREEN,
        ABILITY\_RUNTIME\_SUPPORTED\_WINDOW\_MODE\_SPLIT,
        ABILITY\_RUNTIME\_SUPPORTED\_WINDOW\_MODE\_FLOATING,
    };
    AbilityRuntime\_ErrorCode err = OH\_AbilityRuntime\_SetStartOptionsSupportedWindowModes(options,
        supportedWindowModes, supportedWindowModesSize);
    if (err != ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR) {
        // Record error logs and other service processing.
    }

    // Destroy options to prevent memory leakage.
    OH\_AbilityRuntime\_DestroyStartOptions(&options);
}

#### \[h2\]OH\_AbilityRuntime\_GetStartOptionsSupportedWindowModes()

AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsSupportedWindowModes(AbilityRuntime\_StartOptions \*startOptions, AbilityRuntime\_SupportedWindowMode \*\*supportedWindowModes,size\_t &size)

**Description**

Obtains the window modes supported by the ability when it is started.

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](../../structs/abilityruntime-startoptions/document.md) \*startOptions | Pointer to an AbilityRuntime\_StartOptions object. |
| [AbilityRuntime\_SupportedWindowMode](../context-constant-h/document.md#abilityruntime_supportedwindowmode) \*\*supportedWindowModes | Double pointer to the window modes supported. For details about the available options, see **AbilityRuntime\_SupportedWindowMode**. |
| size | Size of the window modes supported. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](../ability-runtime-common-h/document.md#abilityruntime_errorcode) | 
**ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR**: The call is successful.

**ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID**: The input parameter **StartOptions** is nullptr, or **SupportWindowMode** is not nullptr.

**ABILITY\_RUNTIME\_ERROR\_CODE\_INTERNAL**: An internal error that cannot be rectified, such as internal malloc error, occurs.

 |

**Example**

#include <cstdlib>

#include <AbilityKit/ability\_runtime/start\_options.h>

void demo()
{
    AbilityRuntime\_StartOptions\* options = OH\_AbilityRuntime\_CreateStartOptions();
    if (options == nullptr) {
        // Record error logs and other service processing.
        return;
    }

    AbilityRuntime\_SupportedWindowMode \*supportedWindowModes = nullptr;
    size\_t size = 0;
    AbilityRuntime\_ErrorCode err = OH\_AbilityRuntime\_GetStartOptionsSupportedWindowModes(options,
        &supportedWindowModes, size);
    if (err != ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR) {
        // Record error logs and other service processing.
    }

    if (supportedWindowModes != nullptr) {
        // Destroy supportedWindowModes to prevent memory leakage.
        free(supportedWindowModes);
    }

    // Destroy options to prevent memory leakage.
    OH\_AbilityRuntime\_DestroyStartOptions(&options);
}

#### \[h2\]OH\_AbilityRuntime\_SetStartOptionsMinWindowWidth()

AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsMinWindowWidth(AbilityRuntime\_StartOptions \*startOptions, int32\_t minWindowWidth)

**Description**

Sets the minimum width of the window when the ability is started, in vp.

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](../../structs/abilityruntime-startoptions/document.md) \*startOptions | Pointer to an AbilityRuntime\_StartOptions object. |
| int32\_t minWindowWidth | Minimum width of the window, in vp. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](../ability-runtime-common-h/document.md#abilityruntime_errorcode) | 
**ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR**: The call is successful.

**ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID**: The input parameter **StartOptions** is nullptr.

 |

**Example**

#include <AbilityKit/ability\_runtime/start\_options.h>

void demo()
{
    AbilityRuntime\_StartOptions\* options = OH\_AbilityRuntime\_CreateStartOptions();
    if (options == nullptr) {
        // Record error logs and other service processing.
        return;
    }

    AbilityRuntime\_ErrorCode err = OH\_AbilityRuntime\_SetStartOptionsMinWindowWidth(options, 100);
    if (err != ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR) {
        // Record error logs and other service processing.
    }

    // Destroy options to prevent memory leakage.
    OH\_AbilityRuntime\_DestroyStartOptions(&options);
}

#### \[h2\]OH\_AbilityRuntime\_GetStartOptionsMinWindowWidth()

AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsMinWindowWidth(AbilityRuntime\_StartOptions \*startOptions, int32\_t &minWindowWidth)

**Description**

Obtains the minimum width of the window when the ability is started, in vp.

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](../../structs/abilityruntime-startoptions/document.md) \*startOptions | Pointer to an AbilityRuntime\_StartOptions object. |
| int32\_t &minWindowWidth | Minimum width of the window, in vp. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](../ability-runtime-common-h/document.md#abilityruntime_errorcode) | 
**ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR**: The call is successful.

**ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID**: The input parameter **StartOptions** is nullptr.

 |

**Example**

#include <AbilityKit/ability\_runtime/start\_options.h>

void demo()
{
    AbilityRuntime\_StartOptions\* options = OH\_AbilityRuntime\_CreateStartOptions();
    if (options == nullptr) {
        // Record error logs and other service processing.
        return;
    }

    int32\_t minWindowWidth = 0;
    AbilityRuntime\_ErrorCode err = OH\_AbilityRuntime\_GetStartOptionsMinWindowWidth(options, minWindowWidth);
    if (err != ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR) {
        // Record error logs and other service processing.
    }

    // Destroy options to prevent memory leakage.
    OH\_AbilityRuntime\_DestroyStartOptions(&options);
}

#### \[h2\]OH\_AbilityRuntime\_SetStartOptionsMaxWindowWidth()

AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsMaxWindowWidth(AbilityRuntime\_StartOptions \*startOptions, int32\_t maxWindowWidth)

**Description**

Sets the maximum width of the window when the ability is started, in vp.

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](../../structs/abilityruntime-startoptions/document.md) \*startOptions | Pointer to an AbilityRuntime\_StartOptions object. |
| int32\_t maxWindowWidth | Maximum width of the window, in vp. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](../ability-runtime-common-h/document.md#abilityruntime_errorcode) | 
**ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR**: The call is successful.

**ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID**: The input parameter **StartOptions** is nullptr.

 |

**Example**

#include <AbilityKit/ability\_runtime/start\_options.h>

void demo()
{
    AbilityRuntime\_StartOptions\* options = OH\_AbilityRuntime\_CreateStartOptions();
    if (options == nullptr) {
        // Record error logs and other service processing.
        return;
    }

    AbilityRuntime\_ErrorCode err = OH\_AbilityRuntime\_SetStartOptionsMaxWindowWidth(options, 100);
    if (err != ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR) {
        // Record error logs and other service processing.
    }

    // Destroy options to prevent memory leakage.
    OH\_AbilityRuntime\_DestroyStartOptions(&options);
}

#### \[h2\]OH\_AbilityRuntime\_GetStartOptionsMaxWindowWidth()

AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsMaxWindowWidth(AbilityRuntime\_StartOptions \*startOptions, int32\_t &maxWindowWidth)

**Description**

Obtains the maximum width of the window when the ability is started, in vp.

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](../../structs/abilityruntime-startoptions/document.md) \*startOptions | Pointer to an AbilityRuntime\_StartOptions object. |
| int32\_t &maxWindowWidth | Maximum width of the window, in vp. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](../ability-runtime-common-h/document.md#abilityruntime_errorcode) | 
**ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR**: The call is successful.

**ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID**: The input parameter **StartOptions** is nullptr.

 |

**Example**

#include <AbilityKit/ability\_runtime/start\_options.h>

void demo()
{
    AbilityRuntime\_StartOptions\* options = OH\_AbilityRuntime\_CreateStartOptions();
    if (options == nullptr) {
        // Record error logs and other service processing.
        return;
    }

    int32\_t maxWindowWidth = 0;
    AbilityRuntime\_ErrorCode err = OH\_AbilityRuntime\_GetStartOptionsMaxWindowWidth(options, maxWindowWidth);
    if (err != ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR) {
        // Record error logs and other service processing.
    }

    // Destroy options to prevent memory leakage.
    OH\_AbilityRuntime\_DestroyStartOptions(&options);
}

#### \[h2\]OH\_AbilityRuntime\_SetStartOptionsMinWindowHeight()

AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsMinWindowHeight(AbilityRuntime\_StartOptions \*startOptions, int32\_t minWindowHeight)

**Description**

Sets the minimum height of the window when the ability is started, in vp.

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](../../structs/abilityruntime-startoptions/document.md) \*startOptions | Pointer to an AbilityRuntime\_StartOptions object. |
| int32\_t minWindowHeight | Minimum height of the window, in vp. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](../ability-runtime-common-h/document.md#abilityruntime_errorcode) | 
**ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR**: The call is successful.

**ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID**: The input parameter **StartOptions** is nullptr.

 |

**Example**

#include <AbilityKit/ability\_runtime/start\_options.h>

void demo()
{
    AbilityRuntime\_StartOptions\* options = OH\_AbilityRuntime\_CreateStartOptions();
    if (options == nullptr) {
        // Record error logs and other service processing.
        return;
    }

    AbilityRuntime\_ErrorCode err = OH\_AbilityRuntime\_SetStartOptionsMinWindowHeight(options, 100);
    if (err != ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR) {
        // Record error logs and other service processing.
    }

    // Destroy options to prevent memory leakage.
    OH\_AbilityRuntime\_DestroyStartOptions(&options);
}

#### \[h2\]OH\_AbilityRuntime\_GetStartOptionsMinWindowHeight()

AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsMinWindowHeight(AbilityRuntime\_StartOptions \*startOptions, int32\_t &minWindowHeight)

**Description**

Obtains the minimum height of the window when the ability is started, in vp.

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](../../structs/abilityruntime-startoptions/document.md) \*startOptions | Pointer to an AbilityRuntime\_StartOptions object. |
| int32\_t &minWindowHeight | Minimum height of the window, in vp. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](../ability-runtime-common-h/document.md#abilityruntime_errorcode) | 
**ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR**: The call is successful.

**ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID**: The input parameter **StartOptions** is nullptr.

 |

**Example**

#include <AbilityKit/ability\_runtime/start\_options.h>

void demo()
{
    AbilityRuntime\_StartOptions\* options = OH\_AbilityRuntime\_CreateStartOptions();
    if (options == nullptr) {
        // Record error logs and other service processing.
        return;
    }

    int32\_t minWindowHeight = 0;
    AbilityRuntime\_ErrorCode err = OH\_AbilityRuntime\_GetStartOptionsMinWindowHeight(options, minWindowHeight);
    if (err != ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR) {
        // Record error logs and other service processing.
    }

    // Destroy options to prevent memory leakage.
    OH\_AbilityRuntime\_DestroyStartOptions(&options);
}

#### \[h2\]OH\_AbilityRuntime\_SetStartOptionsMaxWindowHeight()

AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsMaxWindowHeight(AbilityRuntime\_StartOptions \*startOptions, int32\_t maxWindowHeight)

**Description**

Sets the maximum height of the window when the ability is started, in vp.

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](../../structs/abilityruntime-startoptions/document.md) \*startOptions | Pointer to an AbilityRuntime\_StartOptions object. |
| int32\_t maxWindowHeight | Maximum height of the window, in vp. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](../ability-runtime-common-h/document.md#abilityruntime_errorcode) | 
**ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR**: The call is successful.

**ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID**: The input parameter **StartOptions** is nullptr.

 |

**Example**

#include <AbilityKit/ability\_runtime/start\_options.h>

void demo()
{
    AbilityRuntime\_StartOptions\* options = OH\_AbilityRuntime\_CreateStartOptions();
    if (options == nullptr) {
        // Record error logs and other service processing.
        return;
    }

    AbilityRuntime\_ErrorCode err = OH\_AbilityRuntime\_SetStartOptionsMaxWindowHeight(options, 100);
    if (err != ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR) {
        // Record error logs and other service processing.
    }

    // Destroy options to prevent memory leakage.
    OH\_AbilityRuntime\_DestroyStartOptions(&options);
}

#### \[h2\]OH\_AbilityRuntime\_GetStartOptionsMaxWindowHeight()

AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsMaxWindowHeight(AbilityRuntime\_StartOptions \*startOptions, int32\_t &maxWindowHeight)

**Description**

Obtains the maximum height of the window when the ability is started, in vp.

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](../../structs/abilityruntime-startoptions/document.md) \*startOptions | Pointer to an AbilityRuntime\_StartOptions object. |
| int32\_t &maxWindowHeight | Maximum height of the window, in vp. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](../ability-runtime-common-h/document.md#abilityruntime_errorcode) | 
**ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR**: The call is successful.

**ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID**: The input parameter **StartOptions** is nullptr.

 |

**Example**

#include <AbilityKit/ability\_runtime/start\_options.h>

void demo()
{
    AbilityRuntime\_StartOptions\* options = OH\_AbilityRuntime\_CreateStartOptions();
    if (options == nullptr) {
        // Record error logs and other service processing.
        return;
    }

    int32\_t maxWindowHeight = 0;
    AbilityRuntime\_ErrorCode err = OH\_AbilityRuntime\_GetStartOptionsMaxWindowHeight(options, maxWindowHeight);
    if (err != ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR) {
        // Record error logs and other service processing.
    }

    // Destroy options to prevent memory leakage.
    OH\_AbilityRuntime\_DestroyStartOptions(&options);
}
