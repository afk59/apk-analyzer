# Creating an ArkTS Widget

You can create an ArkTS widget package in either of the following ways:

Method 1: Create a shared package. For details, see [Creating a Shared Package](#method-1-creating-a-shared-package). The widget UI and application code are in the same module, and the final compilation product is in the same HAP.

Method 2: Create a standalone package. For details, see [Creating a Standalone Package](#method-2-creating-a-standalone-package). The widget UI and application code are in different modules, and the final compilation products are in separate widget and application packages. The initial APIs of this module are supported since API version 20.

After an ArkTS widget is created, you can preview the widget in real time during development. For details, see [Previewing a Service Widget](../../../../environment-setup/creating-a-project/managing-modules/creating-a-service-widget/document.md#section18171652015).

#### Method 1: Creating a Shared Package

## Procedure

**1\. Create a project.**

In DevEco Studio, create an application or atomic service project. Both types of projects support widget creation. For details about how to create a project, see [Creating a Project](../../../../environment-setup/creating-a-project/creating-a-project/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/hDVDWZ5EQ6WWpplQwUOzdQ/en-us_image_0000002537765050.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061952Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C0040E119C071A67E813B712243FCBE33CC40515D2CCD0E6BCADB3B5EECA846F)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/vrMGGOH1Sye83n-0UVwXLQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061952Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3CB5967E8697F67BC31FA8AE1DFC6CAA759A3E8FE5E0EDC608D95A9A402F9BE0)

The UI may be different in DevEco Studio of a different version.

**2\. Create a widget.**

In an existing application project, right-click to create an ArkTS widget. The procedure is as follows:

-   Right-click the **entry** directory and choose **New** > **Service Widget** > **Dynamic Widget** from the shortcut menu. In a project using the stage model of API version 10 or later, you can directly create dynamic widgets or static widgets through the **Service Widget** menu. After a widget is created, you can modify the widget type by setting the **isDynamic** parameter in the [form\_config.json file](../configuring-arkts-widget-configuration-files/document.md#fields-in-configuration-file) of the widget. If **isDynamic** is left empty or set to **true**, the widget is a [dynamic widget](../arkts-widget-overview/document.md#dynamic-widget). If **isDynamic** is set to **false**, the widget is a [static widget](../arkts-widget-overview/document.md#static-widget). After the static widget and dynamic widget are switched, the user interaction implementation needs to be modified. For details, see [Dynamic Widget](../arkts-widget-overview/document.md#dynamic-widget) and [Static Widget](../arkts-widget-overview/document.md#static-widget) in ArkTS widget overview.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/V-SuLZc5RLGCzDNCAEj3tg/en-us_image_0000002537924990.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061952Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B712A0756C67F72DFEB94943AF94BB822B6B39BFFF1178081059A21416203AFA)
    
-   Select a template and click **Next**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/d1JdPsC5QKWYy0GVDI3bqw/en-us_image_0000002568684767.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061952Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4D734D3840E9EB8EAC8211B2E2951F2CE1E07F5D0BAF72103E359975F2B8E15A)
    
-   Set **Language** to **ArkTS**, **Support dimension** to the desired widget size, and **Default dimension** to the default widget dimension. Then click **Finish** to create an ArkTS widget. You can refer to or modify the widget dimension in the [form\_config.json](../configuring-arkts-widget-configuration-files/document.md#fields-in-configuration-file) file.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/fna_bDQNSM6Q8-BkFXiQaA/en-us_image_0000002568764777.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061952Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BB756CAFFAD085AFF1A11A6A19A7324016BC89D6EFAA31D3B22047794D0C3861)
    
    You are advised to name the widget based on the actual scenario. After an ArkTS widget is created, the following widget-related files are automatically added to the project directory: **EntryFormAbility.ets** (widget lifecycle management file), **WidgetCard.ets** (widget page file), and **form\_config.json** (widget configuration file). You can enter the widget configuration information and click **Finish**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/7eCniLd6TKm9Q2P9XpAXjA/en-us_image_0000002537765052.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061952Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FF672E75DA52D4CE5635939DDE40345743D3DF6EC206C1EC4C13C598111D7C05)
    

## Project Structure

**Figure 1** ArkTS widget project directory and related modules

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/ZOZPCnWETdG8TXHiJk6K7w/en-us_image_0000002537924992.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061952Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A865AE9C34B2E7931DF9D68A317653F448343219A62BF71C68F23A20115C8E5E)

-   [FormExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-form-formextensionability): provides lifecycle callbacks invoked when a widget is created, destroyed, or updated.
    
-   [FormExtensionContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-formextensioncontext): provides context for FormExtensionAbilities. You can use the APIs of this module to start FormExtensionAbilities.
    
-   [formProvider](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-form-formprovider): provides capabilities such as obtaining widget information, updating widgets, and setting the widget update time.
    
-   [formInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-form-forminfo): provides types and enums related to the widget information and state.
    
-   [formBindingData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-form-formbindingdata): provides APIs for widget data binding. You can use the APIs to create a **FormBindingData** object and obtain related information.
    
-   [Page layout (WidgetCard.ets)](../arkts-widget-provider-development/arkts-widget-ui-development/overview-of-arkts-widget-ui-development/document.md): provides the widget UI development capability based on ArkUI.
    
    -   [General capabilities of ArkTS widgets](../arkts-widget-provider-development/arkts-widget-ui-development/overview-of-arkts-widget-ui-development/document.md#page-capabilities-supported-by-arkts-widgets): provide components, attributes, and APIs that can be used in ArkTS widgets.
    -   [Capabilities exclusive to ArkTS widgets](../arkts-widget-provider-development/arkts-widget-page-interaction/overview-of-arkts-widget-page-interaction/document.md): include the **postCardAction** API used for interaction between the widget internal and the provider application and can be called only in the widget.
-   [Widget configuration](../configuring-arkts-widget-configuration-files/document.md): includes FormExtensionAbility configuration and widget configuration.
    
    -   Configure the FormExtensionAbility information under **extensionAbilities** in the [module.json5 file](../../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md).
    -   Configure **WidgetCard.ets** in the [form\_config.json](../configuring-arkts-widget-configuration-files/document.md#fields-in-configuration-file) file under the **resources/base/profile/** directory.

#### Method 2: Creating a Standalone Package

## Procedure

**1\. Create a project.**

In DevEco Studio, create an application or atomic service project. Both types of projects support widget creation. For details about how to create a project, see [Creating a Project](../../../../environment-setup/creating-a-project/creating-a-project/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/dXauPfGHTZuRIx8Dg5KPlA/en-us_image_0000002537765050.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061952Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3C12A63388F3B9FED335F7C72ABA6F1ECFFCCA9B69DC380371CC8AE6BAE40F1D)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/Vu1q4-vZT9yQ-M0z9IgcdA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061952Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=126A104495A30C0259DDAF5607C0632EFAECCF91C5365F5FAA5CA4FFFCBF05D6)

The UI may be different in DevEco Studio of a different version.

**2\. Create a widget.**

-   Right-click the **entry** directory and choose **New** > **Service Widget** > **Dynamic Widget(Standalone)** from the shortcut menu. On the **Service Widget** menu, you can directly select **Dynamic Widget(standalone)** or **Static Widget(standalone)** to create a standalone package. After a widget is created, you can modify the widget type by setting the **isDynamic** parameter in the [form\_config.json file](../configuring-arkts-widget-configuration-files/document.md#fields-in-configuration-file) of the widget. If **isDynamic** is left empty or set to **true**, the widget is a [dynamic widget](../arkts-widget-overview/document.md#dynamic-widget). If **isDynamic** is set to **false**, the widget is a [static widget](../arkts-widget-overview/document.md#static-widget). After the static widget and dynamic widget are switched, the user interaction implementation needs to be modified. For details, see [Dynamic Widget](../arkts-widget-overview/document.md#dynamic-widget) and [Static Widget](../arkts-widget-overview/document.md#static-widget) in ArkTS widget overview.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/CSvYkNhoSPiUbMdDQhKgYw/en-us_image_0000002568684769.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061952Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BDA1DE07535AD4CF6E346BA616D234F2F16FB34C1D801BBCD9AFC8754E0F198D)
    
-   Select a template and click **Next**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/zQD_s7UGSEma0UwaeiYx4A/en-us_image_0000002568684767.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061952Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0233E5F3A2539F755327537781BEFC2E7E78B0B259793E6846098024955CA1E5)
    
-   You can enter the widget configuration information and click **Finish**. After the widget is created, the entry package contains the application and widget backend capabilities, and the library package contains the widget UI capabilities. In the module.json5 configuration file of the entry module, the formWidgetModule field must be associated with the library module; conversely, the formExtensionModule field in the module.json5 of the library module must be linked to the entry module. This mutual association ensures the widget package and application bundle are properly connected. After the creation is complete, the configuration file is automatically generated and configured. You can also configure the file according to [widget configuration files](../configuring-arkts-widget-configuration-files/document.md).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/kf8kcRpGS3uulq0gsm-NCg/en-us_image_0000002568764779.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061952Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=617A45AA13B9B19C2C95C08465A427D7FF5FE735A594D76F53E4C7EB15406B23)
    

## Project Structure

If a widget is created using a standalone widget package or a shared widget package, the project structure is different but the generated files are the same. For details about the files, see [Project Structure in a Shared Package](#project-structure).

**Figure 2** Project directory of a standalone widget package

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/4r9ygP45SAG-QKSpA_IcNg/en-us_image_0000002537765054.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061952Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C6B8C0D338461F25CC1DF4B6FCF1A1D3BD0BC3DCED89CA59D07DA329DD4718DE)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/cpnMRArqRAihoDaJ_XamGw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061952Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F73AFCF12B6539C58E5DAD2CE04308396AB76B3BDAB31B50DF8C54611D583E64)

The application package and widget package in a standalone widget package are two independent modules. Therefore, you need to ensure that the application package and widget package installed at the same time have the same version number.
