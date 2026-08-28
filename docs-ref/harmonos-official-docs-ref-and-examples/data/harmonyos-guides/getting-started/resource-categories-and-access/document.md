# Resource Categories and Access

#### Function Description

In application development, it is common to use resources such as strings, colors, fonts, spacing, and icons. To ensure the application delivers an optimal experience across different devices (e.g., mobile phones, tablets, vehicle head units) and configurations (e.g., languages, screen densities, color modes), the system supports an automatic resource dynamic matching mechanism that selects the most appropriate resources for various scenarios. This section describes resource types and organization methods, and provides guidance for resource development.

Based on source differences, resources are categorized into system resources and application resources. System resources are provided by the system. You can retrieve system symbol icons, colors, spacing, characters, and other resource information from [global\_system\_resources](https://gitcode.com/openharmony/global_system_resources/tree/master/systemres/main/resources/base/element). Among these system resources, symbol icons can be further customized via [SymbolGlyph](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-symbolglyph). Application resources are custom-defined within the application, and resource files can be used to manage how resources behave across different devices or configurations.

#### Resource Categories

Resource files used during application development must be stored in specified directories for management. There are two types of resource directories, namely, resource directories and resource group directories. The resource directories are the **base**, qualifiers, **rawfile**, and **resfile** directories. The resource group directories are the **element**, **media**, and **profile** directories.

resources
|---base  // Default directory.
|   |---element
|   |   |---string.json // String resource file.
|   |---media
|   |   |---icon.png // Media resource file, which can be an image or a video.
|   |---profile
|   |   |---test\_profile.json // User-defined profile.
|---en\_GB-vertical-car-mdpi // Example of a qualifiers subdirectory, which needs to be created on your own.
|   |---element
|   |   |---string.json
|   |---media
|   |   |---icon.png
|   |---profile
|   |   |---test\_profile.json
|---rawfile // Other types of files are saved as raw files and will not be integrated into the resources.index file. You can customize the file name as needed.
|---resfile // Other types of files are saved as raw files and will not be integrated into the resources.index file. You can customize the file name as needed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/jKCx42-DQ5msYm7lQByWVg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061913Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3EFEA318D5C4EBD286C63587A6C4EAFEED7CCA068601EC3DDF9865DC95859A7D)

-   Files in resource directories and resource group directories are considered as resource files and will not be obfuscated during application packaging.
    
-   The common resource files used across projects in the stage model are stored in the **resources** directory under **AppScope**.
    
-   The resource files in the **AppScope** directory are merged into the **resources** directory. If files with the same name exist in these two directories, the ones in the **AppScope** directory are retained after build and packaging.
    
-   For details about the resource packaging policies in directories other than **resources**, see [copyCodeResource](../../building-an-app/configuration-files/module-level-build-profile-json5-file/document.md#table1476161719356).
    

## Resource Directories

Table 1 Description of resource directories

| Directory | Description |
| :-- | :-- |
| base directory | 
The **base** directory is provided by default. Under this directory, the **element** subdirectory stores basic elements such as strings, colors, and Boolean values, and the **media** and **profile** subdirectories store resource files such as media, animations, and layouts.

Resource files in the directories are compiled into binary files, and each resource file is assigned an ID. Access resource files in the directories based on the resource type and resource name.

 |
| Qualifiers directory | 

The qualifiers directory needs to be created as required. Under this directory, the **element** subdirectory stores basic elements such as strings, colors, and Boolean values, and the **media** and **profile** subdirectories store resource files such as media, animations, and layouts.

Similarly, resource files in the directories are compiled into binary files, and each resource file is assigned an ID. Access resource files in the directories based on the resource type and resource name. For details about the meaning and value range of qualifiers and the naming rules of this directory, see [Qualifiers Directory](#qualifiers-directory).

 |
| rawfile directory | 

You can create multiple levels of subdirectories with custom names to store various resource files.

Resource files in the subdirectory are directly packed into the application without being compiled, and no IDs will be assigned to the resource files. Access the directories based on the specified file path and file name.

 |
| resfile directory | 

You can create multiple levels of subdirectories with custom names to store various resource files.

Resource files in the subdirectory are directly packed into the application without being compiled, and no IDs will be assigned to the resource files. After the application is installed, resources in the **resfile** repository are decompressed to the application sandbox path. After the **resfile** directory is obtained through the **Context** attribute [resourceDir](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-context#properties), the resources can be accessed through the file path in read-only mode.

 |

## Resource Group Directories

Table 2 Resource group directories

| Directory | Description | Resource File |
| :-- | :-- | :-- |
| element | 
Indicates element resources. Each type of data is represented by a JSON file. (Only files are supported in this directory.) The options are as follows.

\- **boolean**: boolean data

\- **color**: color data

\- **float**: floating point number, ranging from -2^128 to 2^128

\- **intarray**: array of integers

\- **integer**: integer, ranging from -2^31 to 2^31-1

\- **plural**: plural form data

\- **strarray**: array of strings

\- **string**: string. For details about how to format strings, see [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-resource-manager#getstringsync10).

 | 

It is recommended that files in the **element** subdirectory be named the same as the following files, each of which can contain only data of the same type:

\- boolean.json

\- color.json

\- float.json

\- intarray.json

\- integer.json

\- plural.json

\- strarray.json

\- string.json

 |
| media | 

Indicates media resources, including non-text files such as images, audios, and videos. (Only files are supported in this directory.)

Table 3 and Table 4 describe the types of images, audios, and videos.

 | The file name can be customized, for example, **icon.png**. |
| profile | Indicates a custom configuration file. You can obtain the file content by using the [getProfileByAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-bundlemanager#bundlemanagergetprofilebyability) API. (Only JSON files are supported in this directory.) | The file name can be customized, for example, **test\_profile.json**. |

**Media Resource Types**

Table 3 Image resource types

| Format | File Name Extension |
| :-- | :-- |
| JPEG | .jpg |
| PNG | .png |
| GIF | .gif |
| SVG | .svg |
| WEBP | .webp |
| BMP | .bmp |

Table 4 Audio and video resource types

| Format | File Name Extension |
| :-- | :-- |
| H.264 AVC | .3gp |
| Baseline Profile (BP) | .mp4 |

## Qualifiers Directory

The name of a qualifiers directory consists of one or more qualifiers that represent the application scenarios or device characteristics. Qualifiers include the mobile country code (MCC), mobile network code (MNC), language, script, country or region, screen orientation, device type, night mode, and screen density. Underscores (\_) or hyphens (-) are used to separate qualifiers. Before creating a qualifiers directory, familiarize yourself with the following directory naming conventions:

-   Qualifiers are ordered in the following sequence: MCC\_MNC-language\_script\_country/region-screen orientation-device type-night mode-screen density. You can select one or multiple qualifiers to name your subdirectory based on your application scenarios and device characteristics.
    
-   Separation between qualifiers: the MCC and MNC qualifiers are separated by underscores (\_); the language, script, and country/region qualifiers are separated by underscores (\_); other qualifiers are separated by hyphens (-). For example, **mcc460\_mnc00-zh\_Hant\_CN** and **zh\_CN-car-ldpi**.
    
-   Value range of qualifiers: The value of each qualifier must meet the requirements specified in the following table. Otherwise, the resource files in the resources directory cannot be matched.
    

Table 5 Requirements for qualifier values

| Qualifier Type | Description and Value Range |
| :-- | :-- |
| MCC&MNC | 
Indicates the MCC and MNC, which are obtained from the network where the device is registered.

The MCC can be either followed by the MNC with an underscore (\_) in between or be used independently. For example, **mcc460** represents China, and **mcc460\_mnc00** represents China Mobile.

For details about the value range, see [ITU-T E.212](https://www.itu.int/rec/T-REC-E.212) (the international identification plan for public networks and subscriptions).

 |
| Language | 

Indicates the language used by the device. The value consists of two or three lowercase letters. For example, **zh** indicates Chinese, **en** indicates English, and **mai** indicates Maithili.

For details about the value range, see [ISO 639](https://www.iso.org/iso-639-language-code) (codes for the representation of names of languages).

 |
| Text | 

Indicates the script type used by the device. The value starts with one uppercase letter followed by three lowercase letters. For example, **Hans** indicates simplified Chinese, and **Hant** indicates traditional Chinese.

For details about the value range, see [ISO 15924](https://www.iso.org/standard/81905.html) (codes for the representation of names of scripts).

 |
| Country/Region | 

Indicates the country or region where the user is located. The value consists of two or three uppercase letters or three digits. For example, **CN** indicates China, and **GB** indicates the United Kingdom.

For details about the value range, see [ISO 3166-1](https://www.iso.org/iso-3166-country-codes.html) (codes for the representation of names of countries and their subdivisions).

 |
| Screen orientation | 

Indicates the screen orientation of the device. The value can be:

\- **vertical**: portrait orientation

\- **horizontal**: landscape orientation

 |
| Device type | 

Indicates the type of device, with the following values:

\- **phone**: Mobile phone

\- **tablet**: Tablet

\- **car**: Telematics device

\- **tv**: Smart screen

\- **wearable**: Smart watch

\- **2in1**: PCs/2-in-1 Devices

 |
| Color mode | 

Indicates the color mode of the device. The value can be:

\- **dark**: dark mode

\- **light**: light mode

 |
| Screen density | 

Indicates the screen density of the device, in dpi. The value can be:

\- **sdpi**: small-scale DPI. This value is applicable to devices with a DPI range of (0, 120\].

\- **mdpi**: medium-scale DPI. This value is applicable to devices with a DPI range of (120, 160\].

\- **ldpi**: large-scale DPI. This value is applicable to devices with a DPI range of (160, 240\].

\- **xldpi**: extra-large-scale DPI. This value is applicable to devices with a DPI range of (240, 320\].

\- **xxldpi**: extra-extra-large-scale DPI. This value is applicable to devices with a DPI range of (320, 480\].

\- **xxxldpi**: extra-extra-extra-large-scale DPI. This value is applicable to devices with a DPI range of (480, 640\].

 |

## Resource File Examples

The content of the **color.json** file is as follows.

The standard hexadecimal color value consists of eight hexadecimal digits. The first two digits indicate the opacity and the last six digits indicate the color value.

{
  "color": \[
    {
      "name": "color\_hello",
      "value": "#ffff0000"
    },
    {
      "name": "color\_world",
      "value": "#ff0000ff"
    }
  \]
}

The content of the **float.json** file is as follows.

{
  "float": \[
    {
      "name": "font\_hello",
      "value": "28.0fp"
    },
    {
      "name": "font\_world",
      "value": "20.0fp"
    }
  \]
}

The content of the **string.json** file is as follows.

{
  "string": \[
    {
      "name": "string\_hello",
      "value": "Hello"
    },
    {
      "name": "string\_world",
      "value": "World"
    },
    {
      "name": "message\_arrive",
      "value": "We will arrive at %1$s."
    },
    {
      "name": "message\_notification",
      "value": "Hello, %1$s!,You have %2$d new messages."
    }
  \]
}

The content of the **plural.json** file is as follows.

{
  "plural": \[
    {
      "name": "eat\_apple",
      "value": \[
        {
          "quantity": "one",
          "value": "%d apple"
        },
        {
          "quantity": "other",
          "value": "%d apples"
        }
      \]
    }
  \]
}

#### Creating a Resource Directory and Resource File

You can create a directory and its files under the **resources** directory based on the naming rules of the qualifiers directory and file types supported by resource group directories. DevEco Studio provides a wizard for you to create resource directories and resource files.

## Creating a Resource Directory and Resource File

Right-click the **resources** directory and choose **New** > **Resource File**. By default, the file is created in a resource group directory under **base**. If one or more qualifiers are selected, the system automatically generates a subdirectory and creates the file in this subdirectory.

Qualifiers of different types can be combined. For example, if **Locale** is set to **zh\_CN** and **ColorMode** is set to **Dark**, the qualifiers directory name will be **zh\_CN-dark**. For details about the combination rules, see [Qualifiers Directory](#qualifiers-directory).

In **File name**, enter the name of the resource file to create. In **Resource type**, select the type of the resource group, which is **element** by default. In **Root Element**, select a resource type. To select a qualifier, highlight it under **Available qualifiers** and click the right arrow. To deselect a qualifier, highlight it under **Selected qualifiers** and click the left arrow.

The created directory is automatically named in the format of Qualifiers.Resource group type. For example, if you create a directory by setting **Color Mode** to **Dark** and **Resource type** to **Element**, the system automatically generates a directory named **dark/element**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/axe2_OdvQOK0lt0UNgaPag/en-us_image_0000002568684055.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061913Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=86308995AE3B4235C9A03FA196EB43AF5B5820036D30B115C733D043F4FE67A9)

## Creating a Resource Directory

Right-click the **resources** directory and choose **New** > **Resource Directory** to create a directory only. By default, the **base** directory is created. If one or more qualifiers are selected, the system automatically generates the qualifiers directories and resource group directories. After specifying the qualifier, select a resource group type. Currently, the supported resource group types are **Element**, **Media**, and **Profile**. A resource directory will be generated upon creation.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/D32xIrSAQkacacy_jypgfA/en-us_image_0000002568764065.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061913Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FCF7E8C9D2E4074C5C4B5B0EA6D36F5595524C4214039666081BCBDCD319CFBC)

## Creating a Resource File

Right-click a resource group directory (**element**, **media**, or **profile**) and choose **New** > **XXX Resource File**. A resource file under this directory is then created. For example, you can create an element resource file in the **element** subdirectory.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/ip5FtEEcQ7i8a2c3J2tyIw/en-us_image_0000002537764340.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061913Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AD260E856BE89F06C0019BAC098F40BA31FC88B831634C0E63B5E9A5461BBADC)

## Example

The following takes the Chinese and English string resource files as examples to describe how to create resources with different qualifiers.

1.  Right-click the **resources** directory and choose **New** > **Resource File** from the shortcut menu. Set **File name** to **string\_sample**, **Resource type** to **Element**, **Root Element** to **string**, and **Available qualifiers** to **Locale**. Select **zh** from the language list and **CN** from the country/region list. After all is set, the **zh\_CN/element/string\_sample.json** file is created in the **resources** directory.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/S_RLIsmQSU2Pmqd1LIqr5g/en-us_image_0000002537924280.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061913Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1EEBE5AD7DE899C0370738BCA286531FDE5CC68918251DCA99FE1EF07BAEDE05)
    
2.  Similarly, select **en** for language and **US** for country/region to create the **en\_US/element/string\_sample.json** file.
    
    The following figure shows the created resource files. For details about how to access the created resource files, see [Accessing Resources](#accessing-resources).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/_ZHWpo71SG2ePGUFro1cSw/en-us_image_0000002568684057.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061913Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EDE2BA84999DF065F1D0E07AC45F8DFA4070780EB16754F700258DC36EBCB69C)
    

#### Using the attr Attribute for Resource Translation

## Function Description

If the string resource referenced by an application needs to support multi-language adaptation, the **attr** attribute can be used to mark the translation scope and status of the string. The **attr** attribute is not involved in resource compilation.

If the **attr** attribute is not configured, a string is translated by default.

**Parameters of attr**

| Name | Type | Description |
| :-- | :-- | :-- |
| translatable | boolean | 
Whether the string needs to be translated.

**true**: The string needs to be translated.

**false**: The string does not need to be translated.

 |
| priority | string | 

Translation status of the string.

**code**: untranslated

**translate**: translated but not verified

**LT**: translated and verified

**customer**: custom

 |

## Constraints

The **attr** attribute applies to the string, strarray, and plural resources in the **base** directory.

resources
|---base
|   |---element
|   |   |---string.json
|   |   |---strarray.json
|   |   |---plural.json

## Example

The following shows the **attr** attribute configured in **string**. The **string1** string is marked as not to be translated, and the **string2** string is marked as to be translated and the translation has been verified.

{
  "string": \[
    {
      "name": "string1",
      "value": "1",
      "attr": {
        "translatable": false
      }
    },
    {
      "name": "string2",
      "value": "Hello world!",
      "attr": {
        "translatable": true,
        "priority": "LT"
      }
    }
  \]
}

#### Accessing Resources

## HAP Resources

-   Access resources through $r or $rawfile.
    
    Resources of the color, float, string, plural, media and profile types are accessed through $r('app.type.name'), in which **app** indicates the resource defined in the **resources** directory, **type** indicates the resource type, and **name** indicates the resource name.
    
    To access strings with multiple placeholders in the **string.json** file, for example, %1$s and %2$d in a value, use the $r('app.string.label', 'aaa', 444) format, where **label** indicates the resource name, and **'aaa'** and **444** are used to replace placeholders.
    
    To access resources in the **rawfile** subdirectory, use the $rawfile('filename') format. **filename** indicates the relative path of a file in the **rawfile** subdirectory, which must contain the file name extension and cannot start with a slash (/).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/nFrjwsNxRL-15ZYUDOuWJw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061913Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=524AEF8F6CF0E5071DB3814DF188611B64965C21BCCEF1FED54435D9F64BA09E)
    
    For details about how to use native APIs to access raw files, see [Raw File Development](../../ndk-development/code-development/resource-management/raw-file-development/document.md).
    

[Resource file examples](#resource-file-examples) show different .json files, including **color.json**, **string.json**, and **plural.json**. Before accessing application resources, you need to learn the usage specifications of the .json files.

The usage is as follows.

// Access the resource through $r('app.type.name').
// The resource name is an example. Replace it with the actual resource.
Text($r('app.string.string\_hello'))
  .id('app\_resource')
  .fontColor($r('app.color.color\_emphasize'))
  .fontSize($r('app.float.text\_size\_headline1'))
  .fontFamily($r('app.string.font\_family\_medium'))
  .backgroundColor($r('app.color.color\_palette\_aux1'))

// The resource name is an example. Replace it with the actual resource.
Image($r('app.media.app\_icon'))
  .border({
    color: $r('app.color.color\_palette\_aux1'),
    radius: $r('app.float.corner\_radius\_button'), width: 2
  })
  .margin({
    top: $r('app.float.elements\_margin\_horizontal\_m'),
    bottom: $r('app.float.elements\_margin\_horizontal\_l')
  })
  .height(100)
  .width(100)

// For a string in string.json whose name is "message\_notification", its value is "Hello, %1$s!,You have %2$d new messages."
// Replace the placeholders %1$s and %2$d with 'LiHua' and 2, respectively. Access the resource as follows.
// The resource name is an example. Replace it with the actual resource.
Text($r('app.string.message\_notification', 'LiHua', 2)).id('app\_string\_resource')

// For a string in plural.json whose name is "eat\_apple", its value of the singular form is "%d apple" and that of the plural form is "%d apples".
// You can access the plural.json resources. The first parameter determines whether a string is displayed in the singular or plural form. The value 1 indicates the singular form, and a value greater than 1 indicates the plural form.
// The resource has one placeholder %d, which should be replaced with 2. You can access the resource in the following way:
// The resource name is an example. Replace it with the actual resource.
Text($r('app.plural.eat\_apple', 2, 2)).id('app\_plural\_resource')

-   After obtaining a **ResourceManager** object through the application context, call APIs of [resource management](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-resource-manager) to access different resources. Example:
    
    Call **getContext().resourceManager.getStringByNameSync('test')** to obtain string resources.
    
    Call **getContext().resourceManager.getRawFd('rawfilepath')** to obtain the descriptor information of the HAP where the raw file is located, and then use **{fd, offset, length}** to access the raw file.
    

## Cross-HAP/HSP Resources

**Inter-Bundle, Cross-Module Access**

-   Create the context of the corresponding module through the [createModuleContext(context, moduleName)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-application#applicationcreatemodulecontext) API. After obtaining the **resourceManager** object, call different APIs of [resource management](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-resource-manager) to access various resources by resource ID or resource name.
    
-   Access resources through $r or $rawfile. Specifically, perform either of the following:
    
    1.  Add dependencies to the **oh-package.json5** file in the **entry** directory. For example, **"dependencies": {"library": "file:../library"}**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/0n5-bXK5RXaK6P0IRDwVoA/en-us_image_0000002568764067.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061913Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=73BF1215E1AAC8F33201B7936AE7466055B6549DC7161695921EC9A61F8B8A61)
    
    1.  Obtain resources using variables or the literal **\[Module name\].type.name**, where **module name** indicates the name of the HSP module, **type** indicates the resource type, and **name** indicates the resource name. The following is an example:
    
    @Entry
    @Component
    struct Second {
      // \[library\] is an example module name. Replace it with the actual module name.
      // The resource name is an example. Replace it with the actual resource.
      text: string = '\[library\].string.test\_string';
      fontSize: string = '\[library\].float.font\_size';
      fontColor: string = '\[library\].color.font\_color';
      image: string = '\[library\].media.image';
      rawfile: string = '\[library\].icon.png';
    
      build() {
        Column() {
          // Use the literal \[module name\].type.name to obtain resources.
          // The resource name is an example. Replace it with the actual resource.
          Text($r('\[library\].string.test\_string'))
            .id('hsp\_resource\_one')
            .fontSize($r('\[library\].float.font\_size'))
            .fontColor($r('\[library\].color.font\_color'))
          Image($rawfile('\[library\].icon.png'))
            .height(100)
            .width(100)
    
          // Use variables to obtain resources.
          Text($r(this.text))
            .id('hsp\_resource\_two')
            .fontSize($r(this.fontSize))
            .fontColor($r(this.fontColor))
    
          Image($r(this.image))
            .height(100)
            .width(100)
    
          Image($rawfile(this.rawfile))
            .height(100)
            .width(100)
        }
        .height('100%')
        .width('100%')
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/PEQ5aEGhSVyAPCRvsPjSgQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061913Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CDCE66F71A059CC4A250678FA8A4931337A6115C7ACF65B52923E38BBCFF440A)
    
    The HSP module name must be placed in the brackets (\[\]). If the **rawfile** directory contains multiple levels of folders, the path must start from the first level, for example, $rawfile('\[hsp\].firstDir/secondDir/icon.png'). When **$r** or **$rawfile** is used for cross-HSP resource access, resource verification is not available at compile time, and you need to manually check that the target resources exist in the corresponding location.
    

## System Resources

To access system resources, use the $r('sys.type.name') format, where **sys** indicates the system resource, **type** indicates the resource type, such as color, float, string, media, or symbol, and **name** indicates the resource name.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/MxG7RAlcREebovnoZGX4vA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061913Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8DBD38138A3281CDE9CF0486A936DFF5023294F2736E9F0344C662758D6BDE57)

-   For preset applications, you are advised to use system resources. For third-party applications, you can choose to use system resources or custom application resources as required.
    
-   The use of system resources is only supported in the declarative development paradigm.
    
-   The default system font used on the UI is HarmonyOS Sans, and the supported character range follows the standards in [Information technology—Chinese coded character set GB18030-2022](https://openstd.samr.gov.cn/bzgk/gb/newGbInfo?hcno=A1931A578FE14957104988029B0833D3). If the characters cannot be displayed in HarmonyOS Sans, the system uses another font with the highest priority to display the characters. For details about the priority of the system fonts, see the **/system/etc/fontconfig.json** configuration file on the device.
    

Text('Hello')
  .fontColor($r('sys.color.ohos\_id\_color\_emphasize'))
  .fontSize($r('sys.float.ohos\_id\_text\_size\_headline1'))
  .fontFamily($r('sys.string.ohos\_id\_text\_font\_family\_medium'))
  .backgroundColor($r('sys.color.ohos\_id\_color\_palette\_aux1'))

Image($r('sys.media.ohos\_app\_icon'))
  .border({
    color: $r('sys.color.ohos\_id\_color\_palette\_aux1'),
    radius: $r('sys.float.ohos\_id\_corner\_radius\_button'), width: 2
  })
  .margin({
    top: $r('sys.float.ohos\_id\_elements\_margin\_horizontal\_m'),
    bottom: $r('sys.float.ohos\_id\_elements\_margin\_horizontal\_l')
  })
  .height(100)
  .width(100)

#### Matching Resources

When your application needs to use a resource, the system preferentially searches the qualifiers subdirectories that match the current device state. The system searches the **base** subdirectory for the target resource only when the **resources** directory does not contain any qualifiers subdirectories that match the current device state or the target resource is not found in the qualifiers subdirectories. **rawfile** and **resfile** are raw file directories, which will not match resources based on the device status.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/W2CPzAZMTOS8biN8Md3bsg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061913Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2F1B1E12500F1F7CF6085F110B65510444CCC61202C27F39E6CD325144684ED3)

-   The resource files in the **AppScope** directory are merged into the **resources** directory. If files with the same name exist in these two directories, the ones in the **AppScope** directory are retained after build and packaging.

## Rules for Matching Qualifiers Subdirectories and Device Resources

-   Qualifiers are matched with the device resources in the following priorities: MCC&MNC > locale (options: language, language\_script, language\_country/region, and language\_script\_country/region) > screen orientation > device type > color mode > screen density
    
-   If the qualifiers subdirectories contain the MCC, MNC, language, script, screen orientation, device type, and color mode qualifiers, their values must be consistent with the current device status so that the subdirectories can be used for matching the device resources. For example, the qualifiers directory **zh\_CN-car-ldpi** cannot be used for matching the resource files labeled **en\_US**.
    
-   If there are multiple qualifiers subdirectories for the screen density, the closest qualifiers are matched upwards; otherwise, downwards. For example, if qualifiers directories **xldpi** and **xxldpi** exist and the device screen density is **xxldpi**, the qualifier directory **xxldpi** will be matched.
    

For details about the rules for loading resources on the application UI, see [Overview of Internationalization and Localization](../../application-framework/localization-kit/about-this-kit/document.md).

## Obtaining Resources for a Specific Configuration

**Basic Concepts**

You can add qualifiers to the project-level **resources** directory to meet different system settings such as multi-language support and dark and light color modes. However, some directory resources fail to be obtained due to matching rules of the qualifiers directories.

If this is the case, you can use the following APIs to obtain resources for a specific configuration.

**Available APIs**

| API | Description |
| :-- | :-- |
| [getOverrideResourceManager](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-resource-manager#getoverrideresourcemanager12)(configuration?: [Configuration](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-resource-manager#configuration)) : [ResourceManager](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-resource-manager#resourcemanager) | Obtains a **ResourceManager** object for loading resources for a specific configuration. This API returns the result synchronously. |
| [getOverrideConfiguration](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-resource-manager#getoverrideconfiguration12)() : [Configuration](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-resource-manager#configuration) | Obtains the specified configuration. This API returns the result synchronously. |
| [updateOverrideConfiguration](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-resource-manager#updateoverrideconfiguration12)(configuration: [Configuration](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-resource-manager#configuration)) : void | Updates the specified configuration. |

**Example**

The following example demonstrates how to obtain the specified resources for languages other than the one in use. Assume that the following resource files with the same name are defined in the **resources** directories for Chinese, English, and Japanese:

-   entry/src/main/resources/zh\_CN/element/string.json

{
  "string": \[
    {
      "name": "greetings",
      "value": "你好，世界"
    }
  \]
}

-   entry/src/main/resources/en\_US/element/string.json

{
  "string": \[
    {
      "name": "greetings",
      "value": "Hello, world"
    }
  \]
}

-   entry/src/main/resources/ja\_JP/element/string.json

{
  "string": \[
    {
      "name": "greetings",
      "value": "こんにちは、世界"
    }
  \]
}

In **Index.ets**, add code to obtain the resources of the three languages and display them in the text box. The current system language is Chinese. The following is sample code in **entry/src/main/ets/pages/Index.ets**:

import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  @State englishString: string = '';
  @State japaneseString: string = '';

  build() {
    Column() {
    // ...
      Text(this.getString())
        .id('config\_resource\_one')
        .fontSize(30)
        .fontWeight(FontWeight.Bold)
      Text(this.englishString)
        .id('config\_resource\_two')
        .fontSize(30)
        .fontWeight(FontWeight.Bold)
      Text(this.japaneseString)
        .id('config\_resource\_three')
        .fontSize(30)
        .fontWeight(FontWeight.Bold)
    // ...
    }
    .height('100%')
    .width('100%')
  }

  getString(): string {
    let resMgr = this.getUIContext().getHostContext()?.resourceManager;
    if (!resMgr) {
      return '';
    }
    let currentLanguageString: string = '';
    try {
      // The resource name is an example. Replace it with the actual resource.
      let resId = $r('app.string.greetings').id;

      // Obtain resources that match the current system configuration, including the color mode and resolution, for the current system language.
      currentLanguageString = resMgr.getStringSync(resId);

      // Obtain resources that match the current system configuration, including the color mode and resolution, for the English language.
      let overrideConfig = resMgr.getOverrideConfiguration();
      overrideConfig.locale = 'en\_US'; // Set the language to English and locale to en\_US.
      let overrideResMgr = resMgr.getOverrideResourceManager(overrideConfig);
      this.englishString = overrideResMgr.getStringSync(resId);

      // Obtain resources that match the current system configuration, including the color mode and resolution, for the Japanese language.
      overrideConfig.locale = 'ja\_JP'; // Set the language to Japanese and locale to ja\_JP.
      // Equivalent to resMgr.updateOverrideConfiguration(overrideConfig)
      overrideResMgr.updateOverrideConfiguration(overrideConfig);
      this.japaneseString = overrideResMgr.getStringSync(resId);
    } catch (err) {
      const code = (err as BusinessError).code;
      const message = (err as BusinessError).message;
      console.error(\`get override resource failed, error code: ${code}, error msg: ${message}\`);
    }
    return currentLanguageString;
  }
}

#### Overlay Mechanism

Overlay is a resource replacement mechanism. With overlay resource packages, you can enable your application UI to adapt to different styles of various brands and products, without having to repack your application HAPs. The overlay mechanism works in dynamic and static modes. Overlay resource packages contain only resource files, resource index files, and configuration files.

## Using overlay in dynamic mode

1.  Place the overlay resource package in the target application installation path. For example, for the com.example.overlay application, place the overlay resource package in **data/app/el1/bundle/public/com.example.overlay/**.
2.  The application uses [addResource(path)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-resource-manager#addresource10) to load overlay resources and uses [removeResource(path)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-resource-manager#removeresource10) to remove overlay resources. The path to an overlay resource consists of the application's sandbox root directory (obtained through **getContext().bundleCodeDir**) and the overlay resource bundle name. For example, **let path = getContext().bundleCodeDir + "overlay resource bundle name"**, such as **/data/storage/el1/bundle/overlayResourceBundleName**.

## Using overlay in static mode

This feature is enabled by default. For details about how to enable and disable this feature, see [@ohos.bundle.overlay (overlay Module)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-overlay).

The **app.json5** file in the inter-application overlay resource package supports the following fields:

{
  "app":{
    "bundleName": "com.example.myapplication.overlay",
    "vendor" : "example",
    "versionCode": "1000000",
    "versionName": "1.0.0.1",
    "icon": "$media:app\_icon",
    "label": "$string:app\_name"
  }
}

The **module.json5** file in the inter-application overlay resource package supports the following fields:

{
  "module":{
    "name": "entry\_overlay\_module\_name",
    "type": "shared",
    "description": "$string:entry\_overlay\_desc",
    "deviceTypes": \[
      "default",
      "tablet"
    \],
    "deliveryWithInstall": true,
    "targetModuleName": "entry\_module\_name",
    "targetPriority": 1
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/kDMngSdAS72NZqGa8jNO1g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061913Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C99F78603C0AF160F50EAA99D16376CDE8CB9AE2FD9F6228E92FA66D7397CEAA)

-   **targetModuleName**: name of the target module to apply the overlay feature. The value is a string.
    
-   **targetPriority**: overlay priority. The value is an integer.
    
-   Other fields such as **Ability**, **ExtensionAbility**, and **Permission** are not supported.
    
-   The overlay feature does not support JSON images.
    

If the **module.json5** file of a module contains the **targetModuleName** and **targetPriority fields** during project creation on DevEco Studio, the module is identified as a module with the overlay feature in the installation phase. Modules with the overlay feature generally provide an overlay resource file for other modules on the device, so that the module specified by **targetModuleName** can display different colors, labels, themes, and the like by using the overlay resource file in a running phase.
