# Configuring ArkTS Widget Configuration Files

Widget-related configuration includes [FormExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-form-formextensionability) configuration and widget configuration. A [standalone widget package](../creating-an-arkts-widget/document.md) includes the [standalone widget package configuration](#standalone-widget-package-configuration).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/eRZ7RgrVSwyUBVhxlQuAdw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061952Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=822BC93FF371CBB89EB023F83AD90498160BB2121DF6456BB3946669C4850201)

-   The widget five-tuple comprises the unique identifiers of a widget, including **bundleName**, **moduleName**, **abilityName**, **formName**, and **formDimension**. Specifically, **bundleName** maps to the **bundleName** tag in the [app.json5 file](../../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/app-json5-configuration-file/document.md#tags-in-the-configuration-file), **moduleName** corresponds to the **name** tag in the [module.json5 file](../../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md#tags-in-the-configuration-file), **abilityName** refers to the **name** property in the [abilities tag](../../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md#abilities), **formName** denotes the **name** field specified in the [widget configuration file](#fields-in-configuration-file), and **formDimension** refers to the **supportDimensions** field in the [widget configuration file](#fields-in-configuration-file).
-   Importing the five-tuple configuration via resource files is not recommended. Should the IDs of new fields in the resource file change, the five-tuple will be deemed modified as a result.
-   If the five-tuple is modified following an application upgrade, the corresponding system widget will be deleted and disappear.

#### FormExtensionAbility Configuration

Configure FormExtensionAbility information under extensionAbilities in the [module.json5 file](../../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md). For FormExtensionAbility, you must specify metadata. Specifically, set **name** to **ohos.extension.form** (fixed), and set **resource** to the [index of the widget configuration information](#widget-configuration).

Example:

{
  "module": {
    // ...
    "extensionAbilities": \[
      {
        "name": "EntryFormAbility",
        "srcEntry": "./ets/entryformability/EntryFormAbility.ets",
        "label": "$string:EntryFormAbility\_label",
        "description": "$string:EntryFormAbility\_desc",
        "type": "form",
        "metadata": \[
          {
            "name": "ohos.extension.form",
            "resource": "$profile:form\_config"
          }
        \]
      }
    \],
    // This configuration is only applicable to the standalone widget package form and is used to associate the corresponding widget package module.
    "formWidgetModule": "library"
  }
}

#### Standalone Widget Package Configuration

In the [module.json5 file](../../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md) of a widget package, the formExtensionModule field is used to associate with the module of the application bundle.

Example:

{
  "module": {
    "name": "library",
    "type": "shared",
    "description": "$string:shared\_desc",
    "deviceTypes": \[
      "phone"
    \],
    "deliveryWithInstall": true,
    // This configuration is only applicable to the standalone widget package form and is used to associate the corresponding application bundle module.
    "formExtensionModule": "entry"
  }
}

#### Widget Configuration

In the **metadata** configuration item of FormExtensionAbility, you can specify the resource index of specific configuration information of the widget. For example, if **resource** is set to **$profile:form\_config**, **form\_config.json** in the **resources/base/profile/** directory of the development view is used as the profile configuration file of the widget. The **form\_config.json** configuration file is automatically generated when you [create a widget](../creating-an-arkts-widget/document.md).

## Fields in Configuration File

**Table 1** form\_config.json file

| Field | Description | Data Type | Default Value Allowed |
| :-- | :-- | :-- | :-- |
| forms | 
Configuration about all application widgets.

A maximum of 16 widgets can be configured. If more than 16 widgets are configured, the first 16 widgets are retained.

 | Array | No |
| name | 

Name of the widget. The value is a string with a maximum of 127 bytes. It is used to distinguish different widgets.

**Note**:

You are not advised to reference resource files for this field.

 | String | No |
| displayName | Display name of the widget. It is mainly displayed on the [widget management page](../../about-this-kit/document.md#scenarios-for-widget-usage) and corresponds to "cardName" in the preview. It is recommended that the name reflect the core functionalities or usage of the widget. The value can be a string or a resource index to the name in multiple languages, with the resource index recommended. The string must contain 1 to 30 bytes. | String | No |
| description | Description of the widget. It is used to display the widget description on the [widget management page](../../about-this-kit/document.md#scenarios-for-widget-usage) and corresponds to "This is a service widget." in the preview. The value can be a string or a resource index to the name in multiple languages, with the resource index recommended. The value is a string with a maximum of 255 bytes. | String | Yes (initial value: left empty) |
| src | Full path of the UI code corresponding to the widget. For an ArkTS widget, the full path must contain the widget file name extension, for example, **./ets/widget/pages/WidgetCard.ets**. For a JS widget, the full path does not need to contain the widget file name extension, for example, **./js/widget/pages/WidgetCard**. | String | No |
| uiSyntax | 

Type of the widget.

\- **arkts**: ArkTS widget

\- **hml**: JS widget

 | String | Yes (initial value: **hml**) |
| window | 

Window-related configurations.

**Note**:

This field takes effect only for JS widgets.

 | Object | Yes. For details about the default value, see the [window](#window-field) field. |
| isDefault | 

Whether the widget is the default one (the widget that appears first in the widget center). Each application supports only one default widget.

\- **true**: The widget is the default one.

\- **false**: The widget is not the default one.

**Note**:

When an application is released, only one default widget can be configured for the application.

 | Boolean | No |
| colorMode(deprecated) | 

Color mode of the widget.

\- **auto**: following the system color mode

\- **dark**: dark color mode

\- **light**: light color mode

**Note**:

1\. This configuration item is supported since API version 12 and deprecated since API version 20. The color mode follows the system color mode.

2\. This field takes effect only for JS widgets.

 | String | Yes (initial value: **auto**) |
| supportDimensions | 

Supported widget dimensions. The options are as follows:

\- 1 \* 1: indicates a grid with one row and one column.

\- **1 \* 2**: indicates a grid with one row and two columns.

\- **2 \* 2**: indicates a grid with two rows and two columns.

\- **2 \* 4**: indicates a grid with two rows and four columns.

\- **2 \* 3**: indicates a grid with two rows and three columns.

\- **3 \* 3**: indicates a grid with three rows and three columns.

\- **4 \* 4**: indicates a grid with four rows and four columns.

\- **6 \* 4**: indicates a grid with six rows and four columns.

**Note**: **2 \* 3** and **3 \* 3** support only watches, and 1 \* 1 can be used only on a lock screen.

 | String array | No |
| defaultDimension | Default dimensions of the widget. The value must be available in the **supportDimensions** array of the widget. | String | No |
| updateEnabled | 

Whether the widget can be updated periodically.

\- **true**: The widget can be updated at a specified interval (**updateDuration**) or at the scheduled time (**scheduledUpdateTime**). **updateDuration** takes precedence over **scheduledUpdateTime**. If both are specified, the value specified by **updateDuration** is used.

\- **false**: The widget cannot be updated periodically.

 | Boolean | No |
| scheduledUpdateTime | 

[Scheduled time](../arkts-widget-provider-development/arkts-widget-update/passive-update-of-arkts-widgets/document.md#time-specific-update) to update the widget. The value is in 24-hour format and accurate to minute, for example, 10:30.

**Note**:

**updateDuration** takes precedence over **scheduledUpdateTime**. If both are specified, the value specified by **updateDuration** is used.

 | String | Yes (initial value: **0:0**). By default, the widget is not updated at the scheduled time. |
| updateDuration | 

[Interval to update](../arkts-widget-provider-development/arkts-widget-update/passive-update-of-arkts-widgets/document.md#interval-based-update) the widget. The value is a natural number, in the unit of 30 minutes.

If the value is **0**, this field does not take effect.

If the value is a positive integer N, the interval is calculated by multiplying N and 30 minutes.

**Note**:

**updateDuration** takes precedence over **scheduledUpdateTime**. If both are specified, the value specified by **updateDuration** is used.

 | Number | Yes (initial value: **0**) |
| formConfigAbility | Ability path to be opened after the widget is tapped for editing. The value is in URI format. | String | Yes (initial value: left empty) |
| metadata | Metadata of the widget. For details, see [Metadata](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-bundlemanager-metadata). | Object | Yes (initial value: left empty) |
| isDynamic | 

Whether the widget is a dynamic widget. This field applies only to ArkTS widgets.

\- **true**: [dynamic widget](../arkts-widget-overview/document.md#dynamic-widget).

\- **false**: [static widget](../arkts-widget-overview/document.md#static-widget).

 | Boolean | Yes (initial value: **true**) |
| fontScaleFollowSystem | 

Whether the font size of the widget changes with the system font size.

\- **true**: The font size varies with the system font size.

\- **false**: The font size cannot change with the system font size.

 | Boolean | Yes (initial value: **true**) |
| supportShapes | 

Shapes that the widget can be displayed. The options are as follows:

\- **rect**: rectangular widget.

\- **circle**: circular widget.

 | String array | Yes (initial value: **\["rect"\]**) |
| previewImages | Preview images of the widget, corresponding to the supportDimensions parameter. It is mandatory for smart wearables and currently valid only for wearables. | String array | Yes (initial value: **\[\]**) |
| transparencyEnabled | 

Whether a transparent background is enabled for the widget. (valid only for system applications or ArkTS widgets that have requested the background transparency capability).

\- **true**: A transparent background is enabled.

\- **false**: A transparent background is disabled.

 | Boolean | Yes (initial value: **false**) |
| enableBlurBackground | 

Whether a blur background is enabled for the widget.

\- **true**: A blur background is enabled.

\- **false**: A blur background is disabled.

 | Boolean | Yes (initial value: **false**) |
| renderingMode | 

Rendering mode of the widget.

\- **autoColor**: automatic mode. The display effect can be determined by the widget host as either full-color or monochrome. For details, see [Widget Color](https://developer.huawei.com/consumer/en/doc/design-guides/system-features-service-widget-0000002087671904#section295mcpsimp). In this mode, the colors and images in the widget can be modified by the widget host. The widget can be added to the home screen or lock screen.

\- **fullColor**: full-color mode. For details, see [Widget Color](https://developer.huawei.com/consumer/en/doc/design-guides/system-features-service-widget-0000002087671904#section295mcpsimp). In this mode, the colors and images in the widget cannot be modified by the widget host. The widget can be added to the home screen.

\- **singleColor**: monochrome mode. Elements are distinguished by opacity and blur but not by hue. For details, see [Widget Color](https://developer.huawei.com/consumer/en/doc/design-guides/system-features-service-widget-0000002087671904#section295mcpsimp). In this mode, the colors and images in the widget can be modified by the widget host. The widget can be added to the lock screen.

**Note**:

This field is supported since API version 15.

 | String | Yes (initial value: **fullColor**) |
| multiScheduledUpdateTime | 

Times for updating the widget. As an additional parameter for single-point update, it follows the 24-hour format, precise to the minute. It allows up to 24 distinct times, with every two times separated by a comma (,).

**Note**:

This field is supported since API version 18. It must be used together with **scheduledUpdateTime**.

 | String | Yes (initial value: The widget is not updated at the scheduled times.) |
| conditionUpdate | 

Conditional update capabilities supported by the widget (valid only for ArkTS widgets of system applications). The value can be:

\- **network**: Network update is supported.

**Note**:

This field is supported since API version 18.

 | String array | Yes (initial value: an empty string array) |
| [funInteractionParams](#funinteractionparams-field) | Extended field of the fun-based widget. This field is supported since API version 20. | Object | Yes (initial value: left empty) If **funInteractionParams** and **sceneAnimationParams** are both configured, the interactive widget is a fun-based widget. |
| [sceneAnimationParams](#sceneanimationparams-field) | Extended field of the [scene-based widgets](../interactive-widget-development/scene-based-widget/overview-of-scene-based-widgets/document.md). This field is supported since API version 20. | Object | Yes (initial value: left empty) If **funInteractionParams** and **sceneAnimationParams** are both configured, the interactive widget is a fun-based widget. |
| resizable | 

Whether the widget can be resized by dragging. The value must be in the **supportDimensions** configuration list of the widget or the widget with the same **groupId**.

\- **true**: The widget can be resized.

\- **false**: The widget cannot be resized.

**Note**:

This field is supported since API version 20.

 | Boolean | Yes (initial value: **false**) |
| groupId | 

Shared ID for a group of widgets. When multiple widgets have the same **groupId** and their **resizable** is set to **true**, they share the **supportDimensions** configuration. This configuration is recommended when multiple widgets with the same functionality need to be resized.

Example 1: For widget A, **groupId** is set to **'1'**, **resizable** is set to **true**, and **supportDimensions** is set to **2\*2**. For widget B, **groupId** is set to **'1'**, **resizable** is set to **true**, and **supportDimensions** is set to **2\*4**. Resizing between widget A and widget B is supported in this scenario.

Example 2: If multiple values are set for **supportDimensions** and **resizable** is **true**, resizing takes priority within the same widget. For widget A, **resizable** is set to **true** and **supportDimensions** is set to **2\*2** and **2\*4**, so resizing between these two dimensions is supported.

Example 3: For widget A, **groupId** is set to **'1'**, **resizable** is set to **true**, and **supportDimensions** is set to **1\*2**. For widget B, **groupId** is set to **'1'**, **resizable** is set to **true**, and **supportDimensions** is set to **2\*2**, **2\*4**, and **4\*4**. Widget A can be resized to the default dimensions of widget B, while widget B only supports resizing across its three supported dimensions and cannot be resized to match widget A's dimensions.

**Note**:

This field is supported since API version 20.

 | String | Yes (initial value: an empty string) |
| [supportDeviceTypes](#supportdevicetypes-field) | 

Device type supported by a widget. For example, if **supportDeviceTypes** is set to **phone**, **tablet**, and **tv**, the widget can be displayed on smartphones, tablets, and Visions.

**Note**:

This field is supported since API version 22.

 | String array | Yes (initial value: **\["phone", "tablet", "tv", "wearable", "car", "2in1"\]**) |
| [supportDevicePerformanceClasses](#supportdeviceperformanceclasses-field) | 

Device performance class supported by a widget. For example, if **supportDevicePerformanceClasses** is set to **high**, **medium**, and **low**, the widget can be displayed on devices with the performance class of high, medium, and low.

**Note**:

This field is supported since API version 22.

 | String array | Yes (initial value: **\["high", "medium", "low"\]**) |

## supportDeviceTypes Field

Specifies the device type supported by the widget.

| Field | Description | Data Type |
| :-- | :-- | :-- |
| phone | Smartphone | String |
| tablet | Tablet | String |
| tv | Vision | String |
| wearable | Wearable | String |
| car | Head unit | String |
| 2in1 | PC/2-in-1 device | String |

## supportDevicePerformanceClasses Field

Specifies the device performance class supported by the widget.

| Field | Description | Data Type |
| :-- | :-- | :-- |
| high | High | String |
| medium | Medium | String |
| low | Low | String |

## window Field

Defines the internal structure of the **window** object. This field is supported only in JS widgets.

| Field | Description | Data Type | Default Value Allowed |
| :-- | :-- | :-- | :-- |
| designWidth | Baseline width for page design. The size of an element is scaled by the actual device width. | Number | Yes (initial value: **720px**) |
| autoDesignWidth | Whether to automatically calculate the baseline width for page design. If it is set to **true**, the **designWidth** attribute will be ignored, and the baseline width will be calculated based on the device width and screen density. | Boolean | Yes (initial value: **false**) |

## funInteractionParams Field

Specifies a fun-based widget. If **funInteractionParams** and **sceneAnimationParams** are both configured, the interactive widget is a fun-based widget.

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| abilityName | String | No | LiveFormExtensionAbility name. This parameter is left empty by default. |
| targetBundleName | String | Yes | Main bundle name. |
| subBundleName | String | No | Sub bundle name. |
| keepStateDuration | Number | No | Duration of the activated state when there is no interaction. The default value is **10000**, in ms. The value should be an integer within the range \[0, 10000\]. If the value exceeds this range, it defaults to 10000 milliseconds. |

{
  "forms": \[
    {
       // ...
      "funInteractionParams": {
         "targetBundleName": "com.example.funInteraction",
         "subBundleName": "com.example.subFunInteraction"
      }
    }
  \]
}

## sceneAnimationParams Field

Specifies a scene-based widget. If **funInteractionParams** and **sceneAnimationParams** are both configured, the interactive widget is a fun-based widget.

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| abilityName | String | Yes | LiveFormExtensionAbility name of the scene-based widget. |

   {
     "forms": \[
       {
          // ...
         "sceneAnimationParams": {
            "abilityName": "MyLiveFormExtensionAbility"
         }
       }
     \]
   }

## Configuration File Example

   {
     "forms": \[
       {
         "name": "widget",
         "displayName": "$string:widget\_display\_name",
         "description": "$string:widget\_desc",
         "src": "./ets/widget/pages/WidgetCard.ets",
         "uiSyntax": "arkts",
         "window": {
           "designWidth": 720,
           "autoDesignWidth": true
         },
         "renderingMode": "fullColor",
         "isDefault": true,
         "updateEnabled": true,
         "scheduledUpdateTime": "10:30",
         "updateDuration": 1,
         "defaultDimension": "2\*2",
         "supportDimensions": \[
           "2\*2"
         \],
         "formConfigAbility": "ability://EntryAbility",
         "isDynamic": true,
         "metadata": \[\]
       }
     \]
   }
