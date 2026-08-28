# uds.h

#### Overview

Defines the APIs and structs related to the uniform data structs.

**File to include**: <database/udmf/uds.h>

**Library**: libudmf.so

**System capability**: SystemCapability.DistributedDataManager.UDMF.Core

**Since**: 12

**Related module**: [UDMF](../../modules/udmf/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_UdsPlainText](../../structs/oh-udsplaintext/document.md) | OH\_UdsPlainText | Defines a struct for the unified data of the plaintext type. |
| [OH\_UdsHyperlink](../../structs/oh-udshyperlink/document.md) | OH\_UdsHyperlink | Defines a struct for the unified data of the hyperlink type. |
| [OH\_UdsHtml](../../structs/oh-udshtml/document.md) | OH\_UdsHtml | Defines a struct for the unified data of the Hypertext Markup Language (HTML) type. |
| [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) | OH\_UdsAppItem | Defines a struct for the unified data of the home screen icon type. |
| [OH\_UdsFileUri](../../structs/oh-udsfileuri/document.md) | OH\_UdsFileUri | Defines a struct for the unified data of the file URI type. |
| [OH\_UdsPixelMap](../../structs/oh-udspixelmap/document.md) | OH\_UdsPixelMap | Defines a struct for the unified data of the pixel map type. |
| [OH\_UdsArrayBuffer](../../structs/oh-udsarraybuffer/document.md) | OH\_UdsArrayBuffer | Defines a struct for the unified data of the ArrayBuffer type. |
| [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md) | OH\_UdsContentForm | Defines a struct for the unified data of the content card type. |
| [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) | OH\_UdsDetails | Defines a struct for the unified data of the dictionary type. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_UdsPlainText\* OH\_UdsPlainText\_Create()](#oh_udsplaintext_create) | Creates an [OH\_UdsPlainText](../../structs/oh-udsplaintext/document.md) instance and a pointer to it. If this pointer is no longer required, use [OH\_UdsPlainText\_Destroy](#oh_udsplaintext_destroy) to destroy it. Otherwise, memory leaks may occur. |
| [void OH\_UdsPlainText\_Destroy(OH\_UdsPlainText\* pThis)](#oh_udsplaintext_destroy) | Destroys an [OH\_UdsPlainText](../../structs/oh-udsplaintext/document.md) instance. |
| [const char\* OH\_UdsPlainText\_GetType(OH\_UdsPlainText\* pThis)](#oh_udsplaintext_gettype) | Obtains the type ID from an [OH\_UdsPlainText](../../structs/oh-udsplaintext/document.md) instance. |
| [const char\* OH\_UdsPlainText\_GetContent(OH\_UdsPlainText\* pThis)](#oh_udsplaintext_getcontent) | Obtains the plaintext from an [OH\_UdsPlainText](../../structs/oh-udsplaintext/document.md) instance. |
| [const char\* OH\_UdsPlainText\_GetAbstract(OH\_UdsPlainText\* pThis)](#oh_udsplaintext_getabstract) | Obtains the abstract from an [OH\_UdsPlainText](../../structs/oh-udsplaintext/document.md) instance. |
| [int OH\_UdsPlainText\_SetContent(OH\_UdsPlainText\* pThis, const char\* content)](#oh_udsplaintext_setcontent) | Sets the plaintext content for an [OH\_UdsPlainText](../../structs/oh-udsplaintext/document.md) instance. |
| [int OH\_UdsPlainText\_SetAbstract(OH\_UdsPlainText\* pThis, const char\* abstract)](#oh_udsplaintext_setabstract) | Sets the abstract for an [OH\_UdsPlainText](../../structs/oh-udsplaintext/document.md) instance. |
| [OH\_UdsHyperlink\* OH\_UdsHyperlink\_Create()](#oh_udshyperlink_create) | Creates an [OH\_UdsHyperlink](../../structs/oh-udshyperlink/document.md) instance and a pointer to it. If this pointer is no longer required, use [OH\_UdsHyperlink\_Destroy](#oh_udshyperlink_destroy) to destroy it. Otherwise, memory leaks may occur. |
| [void OH\_UdsHyperlink\_Destroy(OH\_UdsHyperlink\* pThis)](#oh_udshyperlink_destroy) | Destroys an [OH\_UdsHyperlink](../../structs/oh-udshyperlink/document.md) instance. |
| [const char\* OH\_UdsHyperlink\_GetType(OH\_UdsHyperlink\* pThis)](#oh_udshyperlink_gettype) | Obtains the type ID from an [OH\_UdsHyperlink](../../structs/oh-udshyperlink/document.md) instance. |
| [const char\* OH\_UdsHyperlink\_GetUrl(OH\_UdsHyperlink\* pThis)](#oh_udshyperlink_geturl) | Obtains the URL from an [OH\_UdsHyperlink](../../structs/oh-udshyperlink/document.md) instance. |
| [const char\* OH\_UdsHyperlink\_GetDescription(OH\_UdsHyperlink\* pThis)](#oh_udshyperlink_getdescription) | Obtains the description from an [OH\_UdsHyperlink](../../structs/oh-udshyperlink/document.md) instance. |
| [int OH\_UdsHyperlink\_SetUrl(OH\_UdsHyperlink\* pThis, const char\* url)](#oh_udshyperlink_seturl) | Sets the URL for an [OH\_UdsHyperlink](../../structs/oh-udshyperlink/document.md) instance. |
| [int OH\_UdsHyperlink\_SetDescription(OH\_UdsHyperlink\* pThis, const char\* description)](#oh_udshyperlink_setdescription) | Sets the description for an [OH\_UdsHyperlink](../../structs/oh-udshyperlink/document.md) instance. |
| [OH\_UdsHtml\* OH\_UdsHtml\_Create()](#oh_udshtml_create) | Creates an [OH\_UdsHtml](../../structs/oh-udshtml/document.md) instance and a pointer to it. If this pointer is no longer required, use [OH\_UdsHtml\_Destroy](#oh_udshtml_destroy) to destroy it. Otherwise, memory leaks may occur. |
| [void OH\_UdsHtml\_Destroy(OH\_UdsHtml\* pThis)](#oh_udshtml_destroy) | Destroys an [OH\_UdsHtml](../../structs/oh-udshtml/document.md) instance. |
| [const char\* OH\_UdsHtml\_GetType(OH\_UdsHtml\* pThis)](#oh_udshtml_gettype) | Obtains the type ID from an [OH\_UdsHtml](../../structs/oh-udshtml/document.md) instance. |
| [const char\* OH\_UdsHtml\_GetContent(OH\_UdsHtml\* pThis)](#oh_udshtml_getcontent) | Obtains the HTML content from an [OH\_UdsHtml](../../structs/oh-udshtml/document.md) instance. |
| [const char\* OH\_UdsHtml\_GetPlainContent(OH\_UdsHtml\* pThis)](#oh_udshtml_getplaincontent) | Obtains the plaintext content from an [OH\_UdsHtml](../../structs/oh-udshtml/document.md) instance. |
| [int OH\_UdsHtml\_SetContent(OH\_UdsHtml\* pThis, const char\* content)](#oh_udshtml_setcontent) | Sets the HTML content for an [OH\_UdsHtml](../../structs/oh-udshtml/document.md) instance. |
| [int OH\_UdsHtml\_SetPlainContent(OH\_UdsHtml\* pThis, const char\* plainContent)](#oh_udshtml_setplaincontent) | Sets the plaintext content for an [OH\_UdsHtml](../../structs/oh-udshtml/document.md) instance. |
| [OH\_UdsAppItem\* OH\_UdsAppItem\_Create()](#oh_udsappitem_create) | Creates an [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) instance and a pointer to it. If this pointer is no longer required, use [OH\_UdsAppItem\_Destroy](#oh_udsappitem_destroy) to destroy it. Otherwise, memory leaks may occur. |
| [void OH\_UdsAppItem\_Destroy(OH\_UdsAppItem\* pThis)](#oh_udsappitem_destroy) | Destroys an [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) instance. |
| [const char\* OH\_UdsAppItem\_GetType(OH\_UdsAppItem\* pThis)](#oh_udsappitem_gettype) | Obtains the type ID from an [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) instance. |
| [const char\* OH\_UdsAppItem\_GetId(OH\_UdsAppItem\* pThis)](#oh_udsappitem_getid) | Obtains the application ID from an [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) instance. |
| [const char\* OH\_UdsAppItem\_GetName(OH\_UdsAppItem\* pThis)](#oh_udsappitem_getname) | Obtains the application name from an [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) instance. |
| [const char\* OH\_UdsAppItem\_GetIconId(OH\_UdsAppItem\* pThis)](#oh_udsappitem_geticonid) | Obtains the image ID from an [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) instance. |
| [const char\* OH\_UdsAppItem\_GetLabelId(OH\_UdsAppItem\* pThis)](#oh_udsappitem_getlabelid) | Obtains the label ID from an [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) instance. |
| [const char\* OH\_UdsAppItem\_GetBundleName(OH\_UdsAppItem\* pThis)](#oh_udsappitem_getbundlename) | Obtains the bundle name from an [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) instance. |
| [const char\* OH\_UdsAppItem\_GetAbilityName(OH\_UdsAppItem\* pThis)](#oh_udsappitem_getabilityname) | Obtains the ability name from an [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) instance. |
| [int OH\_UdsAppItem\_SetId(OH\_UdsAppItem\* pThis, const char\* appId)](#oh_udsappitem_setid) | Sets the application ID for an [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) instance. |
| [int OH\_UdsAppItem\_SetName(OH\_UdsAppItem\* pThis, const char\* appName)](#oh_udsappitem_setname) | Sets the application name for an [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) instance. |
| [int OH\_UdsAppItem\_SetIconId(OH\_UdsAppItem\* pThis, const char\* appIconId)](#oh_udsappitem_seticonid) | Sets the image ID for an [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) instance. |
| [int OH\_UdsAppItem\_SetLabelId(OH\_UdsAppItem\* pThis, const char\* appLabelId)](#oh_udsappitem_setlabelid) | Sets the label ID for an [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) instance. |
| [int OH\_UdsAppItem\_SetBundleName(OH\_UdsAppItem\* pThis, const char\* bundleName)](#oh_udsappitem_setbundlename) | Sets the bundle name for an [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) instance. |
| [int OH\_UdsAppItem\_SetAbilityName(OH\_UdsAppItem\* pThis, const char\* abilityName)](#oh_udsappitem_setabilityname) | Sets the ability name for an [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) instance. |
| [OH\_UdsFileUri\* OH\_UdsFileUri\_Create()](#oh_udsfileuri_create) | Creates an [OH\_UdsFileUri](../../structs/oh-udsfileuri/document.md) instance and a pointer to it. If this pointer is no longer required, use [OH\_UdsFileUri\_Destroy](#oh_udsfileuri_destroy) to destroy it. Otherwise, memory leaks may occur. |
| [void OH\_UdsFileUri\_Destroy(OH\_UdsFileUri\* pThis)](#oh_udsfileuri_destroy) | Destroys an [OH\_UdsFileUri](../../structs/oh-udsfileuri/document.md) instance. |
| [const char\* OH\_UdsFileUri\_GetType(OH\_UdsFileUri\* pThis)](#oh_udsfileuri_gettype) | Obtains the type ID from an [OH\_UdsFileUri](../../structs/oh-udsfileuri/document.md) instance. |
| [const char\* OH\_UdsFileUri\_GetFileUri(OH\_UdsFileUri\* pThis)](#oh_udsfileuri_getfileuri) | Obtains the file URI from an [OH\_UdsFileUri](../../structs/oh-udsfileuri/document.md) instance. |
| [const char\* OH\_UdsFileUri\_GetFileType(OH\_UdsFileUri\* pThis)](#oh_udsfileuri_getfiletype) | Obtains the file type from an [OH\_UdsFileUri](../../structs/oh-udsfileuri/document.md) instance. |
| [int OH\_UdsFileUri\_SetFileUri(OH\_UdsFileUri\* pThis, const char\* fileUri)](#oh_udsfileuri_setfileuri) | Sets the URI information for an [OH\_UdsFileUri](../../structs/oh-udsfileuri/document.md) instance. |
| [int OH\_UdsFileUri\_SetFileType(OH\_UdsFileUri\* pThis, const char\* fileType)](#oh_udsfileuri_setfiletype) | Sets the file type for an [OH\_UdsFileUri](../../structs/oh-udsfileuri/document.md) instance. |
| [OH\_UdsPixelMap\* OH\_UdsPixelMap\_Create()](#oh_udspixelmap_create) | Creates an [OH\_UdsPixelMap](../../structs/oh-udspixelmap/document.md) instance and a pointer to it. If this pointer is no longer required, use [OH\_UdsPixelMap\_Destroy](#oh_udspixelmap_destroy) to destroy it. Otherwise, memory leaks may occur. |
| [void OH\_UdsPixelMap\_Destroy(OH\_UdsPixelMap\* pThis)](#oh_udspixelmap_destroy) | Destroys an [OH\_UdsPixelMap](../../structs/oh-udspixelmap/document.md) instance. |
| [const char\* OH\_UdsPixelMap\_GetType(OH\_UdsPixelMap\* pThis)](#oh_udspixelmap_gettype) | Obtains the type ID from an [OH\_UdsPixelMap](../../structs/oh-udspixelmap/document.md) instance. |
| [void OH\_UdsPixelMap\_GetPixelMap(OH\_UdsPixelMap\* pThis, OH\_PixelmapNative\* pixelmapNative)](#oh_udspixelmap_getpixelmap) | Obtains the pointer to the [OH\_PixelmapNative](../../../../../media/image-kit/c-apis/header-files/pixelmap-native-h/document.md#oh_pixelmapnative_antialiasinglevel) instance from an [OH\_UdsPixelMap](../../structs/oh-udspixelmap/document.md) instance. |
| [int OH\_UdsPixelMap\_SetPixelMap(OH\_UdsPixelMap\* pThis, OH\_PixelmapNative\* pixelmapNative)](#oh_udspixelmap_setpixelmap) | Sets the pixel image content for an [OH\_UdsPixelMap](../../structs/oh-udspixelmap/document.md) instance. |
| [OH\_UdsArrayBuffer\* OH\_UdsArrayBuffer\_Create()](#oh_udsarraybuffer_create) | Creates an [OH\_UdsArrayBuffer](../../structs/oh-udsarraybuffer/document.md) instance and a pointer to it. If this pointer is no longer required, use [OH\_UdsArrayBuffer\_Destroy](#oh_udsarraybuffer_destroy) to destroy it. Otherwise, memory leaks may occur. |
| [int OH\_UdsArrayBuffer\_Destroy(OH\_UdsArrayBuffer\* buffer)](#oh_udsarraybuffer_destroy) | Destroys an [OH\_UdsArrayBuffer](../../structs/oh-udsarraybuffer/document.md) instance. |
| [int OH\_UdsArrayBuffer\_SetData(OH\_UdsArrayBuffer\* buffer, unsigned char\* data, unsigned int len)](#oh_udsarraybuffer_setdata) | Sets the data content for an [OH\_UdsArrayBuffer](../../structs/oh-udsarraybuffer/document.md) instance. |
| [int OH\_UdsArrayBuffer\_GetData(OH\_UdsArrayBuffer\* buffer, unsigned char\*\* data, unsigned int\* len)](#oh_udsarraybuffer_getdata) | Obtains the custom ArrayBuffer data from an [OH\_UdsArrayBuffer](../../structs/oh-udsarraybuffer/document.md) instance. |
| [OH\_UdsContentForm\* OH\_UdsContentForm\_Create()](#oh_udscontentform_create) | Creates an [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md) instance and a pointer to it. |
| [void OH\_UdsContentForm\_Destroy(OH\_UdsContentForm\* pThis)](#oh_udscontentform_destroy) | Destroys an [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md) instance. |
| [const char\* OH\_UdsContentForm\_GetType(OH\_UdsContentForm\* pThis)](#oh_udscontentform_gettype) | Obtains the type ID from an [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md) instance. |
| [int OH\_UdsContentForm\_GetThumbData(OH\_UdsContentForm\* pThis, unsigned char\*\* thumbData, unsigned int\* len)](#oh_udscontentform_getthumbdata) | Obtains the image data from an [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md) instance. |
| [const char\* OH\_UdsContentForm\_GetDescription(OH\_UdsContentForm\* pThis)](#oh_udscontentform_getdescription) | Obtains the description from an [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md) instance. |
| [const char\* OH\_UdsContentForm\_GetTitle(OH\_UdsContentForm\* pThis)](#oh_udscontentform_gettitle) | Obtains the title from an [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md) instance. |
| [int OH\_UdsContentForm\_GetAppIcon(OH\_UdsContentForm\* pThis, unsigned char\*\* appIcon, unsigned int\* len)](#oh_udscontentform_getappicon) | Obtains the application icon data from an [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md) instance. |
| [const char\* OH\_UdsContentForm\_GetAppName(OH\_UdsContentForm\* pThis)](#oh_udscontentform_getappname) | Obtains the application name from an [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md) instance. |
| [const char\* OH\_UdsContentForm\_GetLinkUri(OH\_UdsContentForm\* pThis)](#oh_udscontentform_getlinkuri) | Obtains the hyperlink from an [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md) instance. |
| [int OH\_UdsContentForm\_SetThumbData(OH\_UdsContentForm\* pThis, const unsigned char\* thumbData, unsigned int len)](#oh_udscontentform_setthumbdata) | Sets the image data for an [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md) instance. |
| [int OH\_UdsContentForm\_SetDescription(OH\_UdsContentForm\* pThis, const char\* description)](#oh_udscontentform_setdescription) | Sets the description for an [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md) instance. |
| [int OH\_UdsContentForm\_SetTitle(OH\_UdsContentForm\* pThis, const char\* title)](#oh_udscontentform_settitle) | Sets the title for an [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md) instance. |
| [int OH\_UdsContentForm\_SetAppIcon(OH\_UdsContentForm\* pThis, const unsigned char\* appIcon, unsigned int len)](#oh_udscontentform_setappicon) | Sets the application icon data for an [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md) instance. |
| [int OH\_UdsContentForm\_SetAppName(OH\_UdsContentForm\* pThis, const char\* appName)](#oh_udscontentform_setappname) | Sets the application name for an [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md) instance. |
| [int OH\_UdsContentForm\_SetLinkUri(OH\_UdsContentForm\* pThis, const char\* linkUri)](#oh_udscontentform_setlinkuri) | Sets the hyperlink for an [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md) instance. |
| [int OH\_UdsPlainText\_GetDetails(OH\_UdsPlainText\* pThis, OH\_UdsDetails\* details)](#oh_udsplaintext_getdetails) | Obtains the pointer to the [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) instance from an [OH\_UdsPlainText](../../structs/oh-udsplaintext/document.md) instance. |
| [int OH\_UdsPlainText\_SetDetails(OH\_UdsPlainText\* pThis, const OH\_UdsDetails\* details)](#oh_udsplaintext_setdetails) | Sets the [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) parameter for an [OH\_UdsPlainText](../../structs/oh-udsplaintext/document.md) instance. |
| [int OH\_UdsHyperlink\_GetDetails(OH\_UdsHyperlink\* pThis, OH\_UdsDetails\* details)](#oh_udshyperlink_getdetails) | Obtains the pointer to the [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) instance from an [OH\_UdsHyperlink](../../structs/oh-udshyperlink/document.md) instance. |
| [int OH\_UdsHyperlink\_SetDetails(OH\_UdsHyperlink\* pThis, const OH\_UdsDetails\* details)](#oh_udshyperlink_setdetails) | Sets the [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) parameter for an [OH\_UdsHyperlink](../../structs/oh-udshyperlink/document.md) instance. |
| [int OH\_UdsHtml\_GetDetails(OH\_UdsHtml\* pThis, OH\_UdsDetails\* details)](#oh_udshtml_getdetails) | Obtains the pointer to the [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) instance from an [OH\_UdsHtml](../../structs/oh-udshtml/document.md) instance. |
| [int OH\_UdsHtml\_SetDetails(OH\_UdsHtml\* pThis, const OH\_UdsDetails\* details)](#oh_udshtml_setdetails) | Sets the [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) parameter for an [OH\_UdsHtml](../../structs/oh-udshtml/document.md) instance. |
| [int OH\_UdsAppItem\_GetDetails(OH\_UdsAppItem\* pThis, OH\_UdsDetails\* details)](#oh_udsappitem_getdetails) | Obtains the pointer to the [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) instance from an [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) object. |
| [int OH\_UdsAppItem\_SetDetails(OH\_UdsAppItem\* pThis, const OH\_UdsDetails\* details)](#oh_udsappitem_setdetails) | Sets the [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) parameter for an [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) instance. |
| [int OH\_UdsFileUri\_GetDetails(OH\_UdsFileUri\* pThis, OH\_UdsDetails\* details)](#oh_udsfileuri_getdetails) | Obtains the pointer to the [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) instance from an [OH\_UdsFileUri](../../structs/oh-udsfileuri/document.md) instance. |
| [int OH\_UdsFileUri\_SetDetails(OH\_UdsFileUri\* pThis, const OH\_UdsDetails\* details)](#oh_udsfileuri_setdetails) | Sets the [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) parameter for an [OH\_UdsFileUri](../../structs/oh-udsfileuri/document.md) instance. |
| [int OH\_UdsPixelMap\_GetDetails(OH\_UdsPixelMap\* pThis, OH\_UdsDetails\* details)](#oh_udspixelmap_getdetails) | Obtains the pointer to the [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) instance from an [OH\_UdsPixelMap](../../structs/oh-udspixelmap/document.md) instance. |
| [int OH\_UdsPixelMap\_SetDetails(OH\_UdsPixelMap\* pThis, const OH\_UdsDetails\* details)](#oh_udspixelmap_setdetails) | Sets the [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) parameter for an [OH\_UdsPixelMap](../../structs/oh-udspixelmap/document.md) instance. |
| [OH\_UdsDetails\* OH\_UdsDetails\_Create()](#oh_udsdetails_create) | 
Creates an [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) instance and a pointer to it.

If this pointer is no longer required, use [OH\_UdsDetails\_Destroy](#oh_udsdetails_destroy) to destroy it. Otherwise, memory leaks may occur.

 |
| [void OH\_UdsDetails\_Destroy(OH\_UdsDetails\* pThis)](#oh_udsdetails_destroy) | Destroys an [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) instance. |
| [bool OH\_UdsDetails\_HasKey(const OH\_UdsDetails\* pThis, const char\* key)](#oh_udsdetails_haskey) | Checks whether the [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) instance contains the specified key. |
| [int OH\_UdsDetails\_Remove(OH\_UdsDetails\* pThis, const char\* key)](#oh_udsdetails_remove) | Deletes the specified KV pair from the [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) instance. |
| [int OH\_UdsDetails\_Clear(OH\_UdsDetails\* pThis)](#oh_udsdetails_clear) | Clears all data from the [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) instance. |
| [int OH\_UdsDetails\_SetValue(OH\_UdsDetails\* pThis, const char\* key, const char\* value)](#oh_udsdetails_setvalue) | Adds a KV pair to an [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) instance. |
| [const char\* OH\_UdsDetails\_GetValue(const OH\_UdsDetails\* pThis, const char\* key)](#oh_udsdetails_getvalue) | Obtains the value of a specified key from an [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) instance. |
| [char\*\* OH\_UdsDetails\_GetAllKeys(OH\_UdsDetails\* pThis, unsigned int\* count)](#oh_udsdetails_getallkeys) | Obtains the result set of all keys from an [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) instance. |

#### Function Description

#### \[h2\]OH\_UdsPlainText\_Create()

OH\_UdsPlainText\* OH\_UdsPlainText\_Create()

**Description**

Creates an [OH\_UdsPlainText](../../structs/oh-udsplaintext/document.md) instance and a pointer to it. If this pointer is no longer required, use [OH\_UdsPlainText\_Destroy](#oh_udsplaintext_destroy) to destroy it. Otherwise, memory leaks may occur.

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_UdsPlainText](../../structs/oh-udsplaintext/document.md)\* | Returns a pointer to the [OH\_UdsPlainText](../../structs/oh-udsplaintext/document.md) instance created if the operation is successful; returns **nullptr** otherwise. |

#### \[h2\]OH\_UdsPlainText\_Destroy()

void OH\_UdsPlainText\_Destroy(OH\_UdsPlainText\* pThis)

**Description**

Destroys an [OH\_UdsPlainText](../../structs/oh-udsplaintext/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsPlainText](../../structs/oh-udsplaintext/document.md)\* pThis | Pointer to the [OH\_UdsPlainText](../../structs/oh-udsplaintext/document.md) instance. |

#### \[h2\]OH\_UdsPlainText\_GetType()

const char\* OH\_UdsPlainText\_GetType(OH\_UdsPlainText\* pThis)

**Description**

Obtains the type ID from an [OH\_UdsPlainText](../../structs/oh-udsplaintext/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsPlainText](../../structs/oh-udsplaintext/document.md)\* pThis | Pointer to the [OH\_UdsPlainText](../../structs/oh-udsplaintext/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Returns a pointer to the type ID obtained if the operation is successful; returns **nullptr** otherwise. |

#### \[h2\]OH\_UdsPlainText\_GetContent()

const char\* OH\_UdsPlainText\_GetContent(OH\_UdsPlainText\* pThis)

**Description**

Obtains the plaintext from an [OH\_UdsPlainText](../../structs/oh-udsplaintext/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsPlainText](../../structs/oh-udsplaintext/document.md)\* pThis | Pointer to the [OH\_UdsPlainText](../../structs/oh-udsplaintext/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Returns a pointer to the plaintext obtained if the operation is successful; returns **nullptr** otherwise. |

#### \[h2\]OH\_UdsPlainText\_GetAbstract()

const char\* OH\_UdsPlainText\_GetAbstract(OH\_UdsPlainText\* pThis)

**Description**

Obtains the abstract from an [OH\_UdsPlainText](../../structs/oh-udsplaintext/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsPlainText](../../structs/oh-udsplaintext/document.md)\* pThis | Pointer to the [OH\_UdsPlainText](../../structs/oh-udsplaintext/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Returns a pointer to the abstract obtained if the operation is successful; returns **nullptr** otherwise. |

OH\_UdsPlainText

#### \[h2\]OH\_UdsPlainText\_SetContent()

int OH\_UdsPlainText\_SetContent(OH\_UdsPlainText\* pThis, const char\* content)

**Description**

Sets the plaintext content for an [OH\_UdsPlainText](../../structs/oh-udsplaintext/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsPlainText](../../structs/oh-udsplaintext/document.md)\* pThis | Pointer to the [OH\_UdsPlainText](../../structs/oh-udsplaintext/document.md) instance. |
| const char\* content | Pointer to the plain text content to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdsPlainText\_SetAbstract()

int OH\_UdsPlainText\_SetAbstract(OH\_UdsPlainText\* pThis, const char\* abstract)

**Description**

Sets the abstract for an [OH\_UdsPlainText](../../structs/oh-udsplaintext/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsPlainText](../../structs/oh-udsplaintext/document.md)\* pThis | Pointer to the [OH\_UdsPlainText](../../structs/oh-udsplaintext/document.md) instance. |
| const char\* abstract | Pointer to the abstract to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdsHyperlink\_Create()

OH\_UdsHyperlink\* OH\_UdsHyperlink\_Create()

**Description**

Creates an [OH\_UdsHyperlink](../../structs/oh-udshyperlink/document.md) instance and a pointer to it. If this pointer is no longer required, use [OH\_UdsHyperlink\_Destroy](#oh_udshyperlink_destroy) to destroy it. Otherwise, memory leaks may occur.

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_UdsHyperlink\* | Returns a pointer to the [OH\_UdsHyperlink](../../structs/oh-udshyperlink/document.md) instance created if the operation is successful; returns **nullptr** otherwise. |

#### \[h2\]OH\_UdsHyperlink\_Destroy()

void OH\_UdsHyperlink\_Destroy(OH\_UdsHyperlink\* pThis)

**Description**

Destroys an [OH\_UdsHyperlink](../../structs/oh-udshyperlink/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsHyperlink](../../structs/oh-udshyperlink/document.md)\* pThis | Pointer to the [OH\_UdsHyperlink](../../structs/oh-udshyperlink/document.md) instance. |

#### \[h2\]OH\_UdsHyperlink\_GetType()

const char\* OH\_UdsHyperlink\_GetType(OH\_UdsHyperlink\* pThis)

**Description**

Obtains the type ID from an [OH\_UdsHyperlink](../../structs/oh-udshyperlink/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsHyperlink](../../structs/oh-udshyperlink/document.md)\* pThis | Pointer to the [OH\_UdsHyperlink](../../structs/oh-udshyperlink/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Returns a pointer to the type ID obtained if the operation is successful; returns **nullptr** otherwise. |

#### \[h2\]OH\_UdsHyperlink\_GetUrl()

const char\* OH\_UdsHyperlink\_GetUrl(OH\_UdsHyperlink\* pThis)

**Description**

Obtains the URL from an [OH\_UdsHyperlink](../../structs/oh-udshyperlink/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsHyperlink](../../structs/oh-udshyperlink/document.md)\* pThis | Pointer to the [OH\_UdsHyperlink](../../structs/oh-udshyperlink/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Returns a pointer to the URL obtained if the operation is successful; returns **nullptr** otherwise. |

#### \[h2\]OH\_UdsHyperlink\_GetDescription()

const char\* OH\_UdsHyperlink\_GetDescription(OH\_UdsHyperlink\* pThis)

**Description**

Obtains the description from an [OH\_UdsHyperlink](../../structs/oh-udshyperlink/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsHyperlink](../../structs/oh-udshyperlink/document.md)\* pThis | Pointer to the [OH\_UdsHyperlink](../../structs/oh-udshyperlink/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Returns a pointer to the description obtained if the operation is successful; returns **nullptr** otherwise. |

#### \[h2\]OH\_UdsHyperlink\_SetUrl()

int OH\_UdsHyperlink\_SetUrl(OH\_UdsHyperlink\* pThis, const char\* url)

**Description**

Sets the URL for an [OH\_UdsHyperlink](../../structs/oh-udshyperlink/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsHyperlink](../../structs/oh-udshyperlink/document.md)\* pThis | Pointer to the [OH\_UdsHyperlink](../../structs/oh-udshyperlink/document.md) instance. |
| const char\* url | Pointer to the URL to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdsHyperlink\_SetDescription()

int OH\_UdsHyperlink\_SetDescription(OH\_UdsHyperlink\* pThis, const char\* description)

**Description**

Sets the description for an [OH\_UdsHyperlink](../../structs/oh-udshyperlink/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsHyperlink](../../structs/oh-udshyperlink/document.md)\* pThis | Pointer to the [OH\_UdsHyperlink](../../structs/oh-udshyperlink/document.md) instance. |
| const char\* description | Pointer to the description to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdsHtml\_Create()

OH\_UdsHtml\* OH\_UdsHtml\_Create()

**Description**

Creates an [OH\_UdsHtml](../../structs/oh-udshtml/document.md) instance and a pointer to it. If this pointer is no longer required, use [OH\_UdsHtml\_Destroy](#oh_udshtml_destroy) to destroy it. Otherwise, memory leaks may occur.

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_UdsHtml](../../structs/oh-udshtml/document.md)\* | Returns a pointer to the [OH\_UdsHtml](../../structs/oh-udshtml/document.md) instance created if the operation is successful; returns **nullptr** otherwise. |

#### \[h2\]OH\_UdsHtml\_Destroy()

void OH\_UdsHtml\_Destroy(OH\_UdsHtml\* pThis)

**Description**

Destroys an [OH\_UdsHtml](../../structs/oh-udshtml/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsHtml](../../structs/oh-udshtml/document.md)\* pThis | Pointer to the [OH\_UdsHtml](../../structs/oh-udshtml/document.md) instance. |

#### \[h2\]OH\_UdsHtml\_GetType()

const char\* OH\_UdsHtml\_GetType(OH\_UdsHtml\* pThis)

**Description**

Obtains the type ID from an [OH\_UdsHtml](../../structs/oh-udshtml/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsHtml](../../structs/oh-udshtml/document.md)\* pThis | Pointer to the [OH\_UdsHtml](../../structs/oh-udshtml/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Returns a pointer to the type ID obtained if the operation is successful; returns **nullptr** otherwise. |

#### \[h2\]OH\_UdsHtml\_GetContent()

const char\* OH\_UdsHtml\_GetContent(OH\_UdsHtml\* pThis)

**Description**

Obtains the HTML content from an [OH\_UdsHtml](../../structs/oh-udshtml/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsHtml](../../structs/oh-udshtml/document.md)\* pThis | Pointer to the [OH\_UdsHtml](../../structs/oh-udshtml/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Returns a pointer to the HTML content obtained if the operation is successful; returns **nullptr** otherwise. |

#### \[h2\]OH\_UdsHtml\_GetPlainContent()

const char\* OH\_UdsHtml\_GetPlainContent(OH\_UdsHtml\* pThis)

**Description**

Obtains the plaintext content from an [OH\_UdsHtml](../../structs/oh-udshtml/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsHtml](../../structs/oh-udshtml/document.md)\* pThis | Pointer to the [OH\_UdsHtml](../../structs/oh-udshtml/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Returns a pointer to the plaintext obtained if the operation is successful; returns **nullptr** otherwise. |

#### \[h2\]OH\_UdsHtml\_SetContent()

int OH\_UdsHtml\_SetContent(OH\_UdsHtml\* pThis, const char\* content)

**Description**

Sets the HTML content for an [OH\_UdsHtml](../../structs/oh-udshtml/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsHtml](../../structs/oh-udshtml/document.md)\* pThis | Pointer to the [OH\_UdsHtml](../../structs/oh-udshtml/document.md) instance. |
| const char\* content | Pointer to the content in HTML format to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdsHtml\_SetPlainContent()

int OH\_UdsHtml\_SetPlainContent(OH\_UdsHtml\* pThis, const char\* plainContent)

**Description**

Sets the plaintext content for an [OH\_UdsHtml](../../structs/oh-udshtml/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsHtml](../../structs/oh-udshtml/document.md)\* pThis | Pointer to the [OH\_UdsHtml](../../structs/oh-udshtml/document.md) instance. |
| const char\* plainContent | Pointer to the plain text content to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdsAppItem\_Create()

OH\_UdsAppItem\* OH\_UdsAppItem\_Create()

**Description**

Creates an [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) instance and a pointer to it. If this pointer is no longer required, use [OH\_UdsAppItem\_Destroy](#oh_udsappitem_destroy) to destroy it. Otherwise, memory leaks may occur.

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md)\* | Returns a pointer to the [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) instance created if the operation is successful; returns **nullptr** otherwise. |

#### \[h2\]OH\_UdsAppItem\_Destroy()

void OH\_UdsAppItem\_Destroy(OH\_UdsAppItem\* pThis)

**Description**

Destroys an [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md)\* pThis | Pointer to the [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) instance. |

#### \[h2\]OH\_UdsAppItem\_GetType()

const char\* OH\_UdsAppItem\_GetType(OH\_UdsAppItem\* pThis)

**Description**

Obtains the type ID from an [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md)\* pThis | Pointer to the [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Returns a pointer to the type ID obtained if the operation is successful; returns **nullptr** otherwise. |

#### \[h2\]OH\_UdsAppItem\_GetId()

const char\* OH\_UdsAppItem\_GetId(OH\_UdsAppItem\* pThis)

**Description**

Obtains the application ID from an [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md)\* pThis | Pointer to the [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Returns a pointer to the application ID obtained if the operation is successful; returns **nullptr** otherwise. |

#### \[h2\]OH\_UdsAppItem\_GetName()

const char\* OH\_UdsAppItem\_GetName(OH\_UdsAppItem\* pThis)

**Description**

Obtains the application name from an [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md)\* pThis | Pointer to the [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Returns a pointer to the application name obtained if the operation is successful; returns **nullptr** otherwise. |

#### \[h2\]OH\_UdsAppItem\_GetIconId()

const char\* OH\_UdsAppItem\_GetIconId(OH\_UdsAppItem\* pThis)

**Description**

Obtains the image ID from an [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md)\* pThis | Pointer to the [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Returns a pointer to the application icon ID obtained if the operation is successful; returns **nullptr** otherwise. |

#### \[h2\]OH\_UdsAppItem\_GetLabelId()

const char\* OH\_UdsAppItem\_GetLabelId(OH\_UdsAppItem\* pThis)

**Description**

Obtains the label ID from an [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md)\* pThis | Pointer to the [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Returns a pointer to the application label ID obtained if the operation is successful; returns **nullptr** otherwise. |

#### \[h2\]OH\_UdsAppItem\_GetBundleName()

const char\* OH\_UdsAppItem\_GetBundleName(OH\_UdsAppItem\* pThis)

**Description**

Obtains the bundle name from an [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md)\* pThis | Pointer to the [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Returns a pointer to the bundle name obtained if the operation is successful; returns **nullptr** otherwise. |

#### \[h2\]OH\_UdsAppItem\_GetAbilityName()

const char\* OH\_UdsAppItem\_GetAbilityName(OH\_UdsAppItem\* pThis)

**Description**

Obtains the ability name from an [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md)\* pThis | Pointer to the [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Returns a pointer to the ability name obtained if the operation is successful; returns **nullptr** otherwise. |

#### \[h2\]OH\_UdsAppItem\_SetId()

int OH\_UdsAppItem\_SetId(OH\_UdsAppItem\* pThis, const char\* appId)

**Description**

Sets the application ID for an [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md)\* pThis | Pointer to the [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) instance. |
| const char\* appId | Pointer to the application ID to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdsAppItem\_SetName()

int OH\_UdsAppItem\_SetName(OH\_UdsAppItem\* pThis, const char\* appName)

**Description**

Sets the application name for an [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md)\* pThis | Pointer to the [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) instance. |
| const char\* appName | Pointer to the application name to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdsAppItem\_SetIconId()

int OH\_UdsAppItem\_SetIconId(OH\_UdsAppItem\* pThis, const char\* appIconId)

**Description**

Sets the icon ID for an [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md)\* pThis | Pointer to the [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) instance. |
| const char\* appIconId | Pointer to the application icon ID to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdsAppItem\_SetLabelId()

int OH\_UdsAppItem\_SetLabelId(OH\_UdsAppItem\* pThis, const char\* appLabelId)

**Description**

Sets the label ID for an [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md)\* pThis | Pointer to the [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) instance. |
| const char\* appLabelId | Pointer to the application label ID to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdsAppItem\_SetBundleName()

int OH\_UdsAppItem\_SetBundleName(OH\_UdsAppItem\* pThis, const char\* bundleName)

**Description**

Sets the bundle name for an [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md)\* pThis | Pointer to the [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) instance. |
| const char\* bundleName | Pointer to the bundle name to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdsAppItem\_SetAbilityName()

int OH\_UdsAppItem\_SetAbilityName(OH\_UdsAppItem\* pThis, const char\* abilityName)

**Description**

Sets the ability name for an [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md)\* pThis | Pointer to the [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) instance. |
| const char\* abilityName | Pointer to the ability name to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdsFileUri\_Create()

OH\_UdsFileUri\* OH\_UdsFileUri\_Create()

**Description**

Creates an [OH\_UdsFileUri](../../structs/oh-udsfileuri/document.md) instance and a pointer to it. If this pointer is no longer required, use [OH\_UdsFileUri\_Destroy](#oh_udsfileuri_destroy) to destroy it. Otherwise, memory leaks may occur.

**Since**: 13

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_UdsFileUri](../../structs/oh-udsfileuri/document.md)\* | Returns a pointer to the [OH\_UdsFileUri](../../structs/oh-udsfileuri/document.md) instance if the operation is successful; returns **nullptr** otherwise. |

#### \[h2\]OH\_UdsFileUri\_Destroy()

void OH\_UdsFileUri\_Destroy(OH\_UdsFileUri\* pThis)

**Description**

Destroys an [OH\_UdsFileUri](../../structs/oh-udsfileuri/document.md) instance.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsFileUri](../../structs/oh-udsfileuri/document.md)\* pThis | Pointer to the [OH\_UdsFileUri](../../structs/oh-udsfileuri/document.md) instance. |

#### \[h2\]OH\_UdsFileUri\_GetType()

const char\* OH\_UdsFileUri\_GetType(OH\_UdsFileUri\* pThis)

**Description**

Obtains the type ID from an [OH\_UdsFileUri](../../structs/oh-udsfileuri/document.md) instance.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsFileUri](../../structs/oh-udsfileuri/document.md)\* pThis | Pointer to the [OH\_UdsFileUri](../../structs/oh-udsfileuri/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Returns a pointer to the type ID obtained if the operation is successful; returns **nullptr** otherwise. |

#### \[h2\]OH\_UdsFileUri\_GetFileUri()

const char\* OH\_UdsFileUri\_GetFileUri(OH\_UdsFileUri\* pThis)

**Description**

Obtains the file URI from an [OH\_UdsFileUri](../../structs/oh-udsfileuri/document.md) instance.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsFileUri](../../structs/oh-udsfileuri/document.md)\* pThis | Pointer to the [OH\_UdsFileUri](../../structs/oh-udsfileuri/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Returns a pointer to the file URI obtained if the operation is successful; returns **nullptr** otherwise. |

#### \[h2\]OH\_UdsFileUri\_GetFileType()

const char\* OH\_UdsFileUri\_GetFileType(OH\_UdsFileUri\* pThis)

**Description**

Obtains the file type from an [OH\_UdsFileUri](../../structs/oh-udsfileuri/document.md) instance.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsFileUri](../../structs/oh-udsfileuri/document.md)\* pThis | Pointer to the [OH\_UdsFileUri](../../structs/oh-udsfileuri/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Returns a pointer to the file type obtained if the operation is successful; returns **nullptr** otherwise. |

#### \[h2\]OH\_UdsFileUri\_SetFileUri()

int OH\_UdsFileUri\_SetFileUri(OH\_UdsFileUri\* pThis, const char\* fileUri)

**Description**

Sets the URI information for an [OH\_UdsFileUri](../../structs/oh-udsfileuri/document.md) instance.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsFileUri](../../structs/oh-udsfileuri/document.md)\* pThis | Pointer to the [OH\_UdsFileUri](../../structs/oh-udsfileuri/document.md) instance. |
| const char\* fileUri | Pointer to the file URI to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdsFileUri\_SetFileType()

int OH\_UdsFileUri\_SetFileType(OH\_UdsFileUri\* pThis, const char\* fileType)

**Description**

Sets the file type for an [OH\_UdsFileUri](../../structs/oh-udsfileuri/document.md) instance.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsFileUri](../../structs/oh-udsfileuri/document.md)\* pThis | Pointer to the [OH\_UdsFileUri](../../structs/oh-udsfileuri/document.md) instance. |
| const char\* fileType | Pointer to the file type to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdsPixelMap\_Create()

OH\_UdsPixelMap\* OH\_UdsPixelMap\_Create()

**Description**

Creates an [OH\_UdsPixelMap](../../structs/oh-udspixelmap/document.md) instance and a pointer to it. If this pointer is no longer required, use [OH\_UdsPixelMap\_Destroy](#oh_udspixelmap_destroy) to destroy it. Otherwise, memory leaks may occur.

**Since**: 13

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_UdsPixelMap](../../structs/oh-udspixelmap/document.md)\* | Returns a pointer to the [OH\_UdsPixelMap](../../structs/oh-udspixelmap/document.md) instance if the operation is successful; returns **nullptr** otherwise. |

#### \[h2\]OH\_UdsPixelMap\_Destroy()

void OH\_UdsPixelMap\_Destroy(OH\_UdsPixelMap\* pThis)

**Description**

Destroys an [OH\_UdsPixelMap](../../structs/oh-udspixelmap/document.md) instance.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsPixelMap](../../structs/oh-udspixelmap/document.md)\* pThis | Pointer to the [OH\_UdsPixelMap](../../structs/oh-udspixelmap/document.md) instance. |

#### \[h2\]OH\_UdsPixelMap\_GetType()

const char\* OH\_UdsPixelMap\_GetType(OH\_UdsPixelMap\* pThis)

**Description**

Obtains the type ID from an [OH\_UdsPixelMap](../../structs/oh-udspixelmap/document.md) instance.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsPixelMap](../../structs/oh-udspixelmap/document.md)\* pThis | Pointer to the [OH\_UdsPixelMap](../../structs/oh-udspixelmap/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Returns a pointer to the type ID obtained if the operation is successful; returns **nullptr** otherwise. |

#### \[h2\]OH\_UdsPixelMap\_GetPixelMap()

void OH\_UdsPixelMap\_GetPixelMap(OH\_UdsPixelMap\* pThis, OH\_PixelmapNative\* pixelmapNative)

**Description**

Obtains the pointer to the [OH\_PixelmapNative](../../../../../media/image-kit/c-apis/header-files/pixelmap-native-h/document.md#oh_pixelmapnative_antialiasinglevel) instance from an [OH\_UdsPixelMap](../../structs/oh-udspixelmap/document.md) instance.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsPixelMap](../../structs/oh-udspixelmap/document.md)\* pThis | Pointer to the [OH\_UdsPixelMap](../../structs/oh-udspixelmap/document.md) instance. |
| OH\_PixelmapNative\* pixelmapNative | Pointer to the [OH\_PixelmapNative](../../../../../media/image-kit/c-apis/header-files/pixelmap-native-h/document.md#oh_pixelmapnative_antialiasinglevel) instance. |

#### \[h2\]OH\_UdsPixelMap\_SetPixelMap()

int OH\_UdsPixelMap\_SetPixelMap(OH\_UdsPixelMap\* pThis, OH\_PixelmapNative\* pixelmapNative)

**Description**

Sets the pixel image content for an [OH\_UdsPixelMap](../../structs/oh-udspixelmap/document.md) instance.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsPixelMap](../../structs/oh-udspixelmap/document.md)\* pThis | Pointer to the [OH\_UdsPixelMap](../../structs/oh-udspixelmap/document.md) instance. |
| OH\_PixelmapNative\* pixelmapNative | Pointer to the [OH\_PixelmapNative](../../../../../media/image-kit/c-apis/header-files/pixelmap-native-h/document.md#oh_pixelmapnative_antialiasinglevel) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdsArrayBuffer\_Create()

OH\_UdsArrayBuffer\* OH\_UdsArrayBuffer\_Create()

**Description**

Creates an [OH\_UdsArrayBuffer](../../structs/oh-udsarraybuffer/document.md) instance and a pointer to it. If this pointer is no longer required, use [OH\_UdsArrayBuffer\_Destroy](#oh_udsarraybuffer_destroy) to destroy it. Otherwise, memory leaks may occur.

**Since**: 13

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_UdsArrayBuffer](../../structs/oh-udsarraybuffer/document.md)\* | Returns a pointer to the [OH\_UdsArrayBuffer](../../structs/oh-udsarraybuffer/document.md) instance if the operation is successful; returns **nullptr** otherwise. |

#### \[h2\]OH\_UdsArrayBuffer\_Destroy()

int OH\_UdsArrayBuffer\_Destroy(OH\_UdsArrayBuffer\* buffer)

**Description**

Destroys an [OH\_UdsArrayBuffer](../../structs/oh-udsarraybuffer/document.md) instance.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsArrayBuffer](../../structs/oh-udsarraybuffer/document.md)\* buffer | Pointer to the [OH\_UdsArrayBuffer](../../structs/oh-udsarraybuffer/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [OH\_UdsArrayBuffer](../../structs/oh-udsarraybuffer/document.md).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdsArrayBuffer\_SetData()

int OH\_UdsArrayBuffer\_SetData(OH\_UdsArrayBuffer\* buffer, unsigned char\* data, unsigned int len)

**Description**

Sets the data content for an [OH\_UdsArrayBuffer](../../structs/oh-udsarraybuffer/document.md) instance.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsArrayBuffer](../../structs/oh-udsarraybuffer/document.md)\* buffer | Pointer to the [OH\_UdsArrayBuffer](../../structs/oh-udsarraybuffer/document.md) instance. |
| unsigned char\* data | Pointer to the ArrayBuffer data to set. |
| unsigned int len | Length of the ArrayBuffer data to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [OH\_UdsArrayBuffer](../../structs/oh-udsarraybuffer/document.md).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdsArrayBuffer\_GetData()

int OH\_UdsArrayBuffer\_GetData(OH\_UdsArrayBuffer\* buffer, unsigned char\*\* data, unsigned int\* len)

**Description**

Obtains the custom ArrayBuffer data from an [OH\_UdsArrayBuffer](../../structs/oh-udsarraybuffer/document.md) instance.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsArrayBuffer](../../structs/oh-udsarraybuffer/document.md)\* buffer | Pointer to the [OH\_UdsArrayBuffer](../../structs/oh-udsarraybuffer/document.md) instance. |
| unsigned char\*\* data | Double pointer to the ArrayBuffer data obtained. |
| unsigned int\* len | Pointer to the length of the ArrayBuffer data obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [OH\_UdsArrayBuffer](../../structs/oh-udsarraybuffer/document.md).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdsContentForm\_Create()

OH\_UdsContentForm\* OH\_UdsContentForm\_Create()

**Description**

Creates an [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md) instance and a pointer to it.

**Since**: 14

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md)\* | Returns a pointer to the [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md) instance if the operation is successful; returns **nullptr** otherwise. |

#### \[h2\]OH\_UdsContentForm\_Destroy()

void OH\_UdsContentForm\_Destroy(OH\_UdsContentForm\* pThis)

**Description**

Destroys an [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md) instance.

**Since**: 14

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md)\* pThis | Pointer to the [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md) instance. |

#### \[h2\]OH\_UdsContentForm\_GetType()

const char\* OH\_UdsContentForm\_GetType(OH\_UdsContentForm\* pThis)

**Description**

Obtains the type ID from an [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md) instance.

**Since**: 14

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md)\* pThis | Pointer to the [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Returns a pointer to the type ID obtained if the operation is successful; returns **nullptr** otherwise. |

#### \[h2\]OH\_UdsContentForm\_GetThumbData()

int OH\_UdsContentForm\_GetThumbData(OH\_UdsContentForm\* pThis, unsigned char\*\* thumbData, unsigned int\* len)

**Description**

Obtains the image data from an [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md) instance.

**Since**: 14

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md)\* pThis | Pointer to the [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md) instance. |
| unsigned char\*\* thumbData | Double pointer to the binary image data obtained. |
| unsigned int\* len | Pointer to the length of the binary image data obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

Returns **UDMF\_ERR** if an internal system error occurs.

 |

#### \[h2\]OH\_UdsContentForm\_GetDescription()

const char\* OH\_UdsContentForm\_GetDescription(OH\_UdsContentForm\* pThis)

**Description**

Obtains the description from an [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md) instance.

**Since**: 14

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md)\* pThis | Pointer to the [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Returns a pointer to the description string obtained if the operation is successful; returns **nullptr** otherwise. |

#### \[h2\]OH\_UdsContentForm\_GetTitle()

const char\* OH\_UdsContentForm\_GetTitle(OH\_UdsContentForm\* pThis)

**Description**

Obtains the title from an [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md) instance.

**Since**: 14

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md)\* pThis | Pointer to the [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Returns a pointer to the title string obtained if the operation is successful; returns **nullptr** otherwise. |

#### \[h2\]OH\_UdsContentForm\_GetAppIcon()

int OH\_UdsContentForm\_GetAppIcon(OH\_UdsContentForm\* pThis, unsigned char\*\* appIcon, unsigned int\* len)

**Description**

Obtains the application icon data from an [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md) instance.

**Since**: 14

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md)\* pThis | Pointer to the [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md) instance. |
| unsigned char\*\* appIcon | Double pointer to the binary application icon data obtained. |
| unsigned int\* len | Pointer to the length of the binary application icon data obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

Returns **UDMF\_ERR** if an internal system error occurs.

 |

#### \[h2\]OH\_UdsContentForm\_GetAppName()

const char\* OH\_UdsContentForm\_GetAppName(OH\_UdsContentForm\* pThis)

**Description**

Obtains the application name from an [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md) instance.

**Since**: 14

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md)\* pThis | Pointer to the [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Returns a pointer to the application name obtained if the operation is successful; returns **nullptr** otherwise. |

#### \[h2\]OH\_UdsContentForm\_GetLinkUri()

const char\* OH\_UdsContentForm\_GetLinkUri(OH\_UdsContentForm\* pThis)

**Description**

Obtains the hyperlink from an [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md) instance.

**Since**: 14

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md)\* pThis | Pointer to the [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Returns a pointer to the hyperlink obtained if the operation is successful; returns **nullptr** otherwise. |

#### \[h2\]OH\_UdsContentForm\_SetThumbData()

int OH\_UdsContentForm\_SetThumbData(OH\_UdsContentForm\* pThis, const unsigned char\* thumbData, unsigned int len)

**Description**

Sets the image data for an [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md) instance.

**Since**: 14

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md)\* pThis | Pointer to the [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md) instance. |
| const unsigned char\* thumbData | Pointer to the binary image data to set. |
| unsigned int len | Length of the binary image data to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdsContentForm\_SetDescription()

int OH\_UdsContentForm\_SetDescription(OH\_UdsContentForm\* pThis, const char\* description)

**Description**

Sets the description for an [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md) instance.

**Since**: 14

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md)\* pThis | Pointer to the [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md) instance. |
| const char\* description | Pointer to the description to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdsContentForm\_SetTitle()

int OH\_UdsContentForm\_SetTitle(OH\_UdsContentForm\* pThis, const char\* title)

**Description**

Sets the title for an [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md) instance.

**Since**: 14

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md)\* pThis | Pointer to the [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md) instance. |
| const char\* title | Pointer to the title to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdsContentForm\_SetAppIcon()

int OH\_UdsContentForm\_SetAppIcon(OH\_UdsContentForm\* pThis, const unsigned char\* appIcon, unsigned int len)

**Description**

Sets the application icon data for an [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md) instance.

**Since**: 14

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md)\* pThis | Pointer to the [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md) instance. |
| const unsigned char\* appIcon | Pointer to the binary application icon data to set. |
| unsigned int len | Length of the binary application icon data to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdsContentForm\_SetAppName()

int OH\_UdsContentForm\_SetAppName(OH\_UdsContentForm\* pThis, const char\* appName)

**Description**

Sets the application name for an [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md) instance.

**Since**: 14

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md)\* pThis | Pointer to the [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md) instance. |
| const char\* appName | Pointer to the application name to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdsContentForm\_SetLinkUri()

int OH\_UdsContentForm\_SetLinkUri(OH\_UdsContentForm\* pThis, const char\* linkUri)

**Description**

Sets the hyperlink for an [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md) instance.

**Since**: 14

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md)\* pThis | Pointer to the [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md) instance. |
| const char\* linkUri | Pointer to the hyperlink to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdsPlainText\_GetDetails()

int OH\_UdsPlainText\_GetDetails(OH\_UdsPlainText\* pThis, OH\_UdsDetails\* details)

**Description**

Obtains the pointer to the [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) instance from an [OH\_UdsPlainText](../../structs/oh-udsplaintext/document.md) instance.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsPlainText](../../structs/oh-udsplaintext/document.md)\* pThis | Pointer to the [OH\_UdsPlainText](../../structs/oh-udsplaintext/document.md) instance. |
| [OH\_UdsDetails](../../structs/oh-udsdetails/document.md)\* details | Pointer to the [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) instance, which cannot be null. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdsPlainText\_SetDetails()

int OH\_UdsPlainText\_SetDetails(OH\_UdsPlainText\* pThis, const OH\_UdsDetails\* details)

**Description**

Sets the [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) parameter for an [OH\_UdsPlainText](../../structs/oh-udsplaintext/document.md) instance.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsPlainText](../../structs/oh-udsplaintext/document.md)\* pThis | Pointer to the [OH\_UdsPlainText](../../structs/oh-udsplaintext/document.md) instance. |
| [const OH\_UdsDetails](../../structs/oh-udsdetails/document.md)\* details | Pointer to the [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) instance, which cannot be null. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdsHyperlink\_GetDetails()

int OH\_UdsHyperlink\_GetDetails(OH\_UdsHyperlink\* pThis, OH\_UdsDetails\* details)

**Description**

Obtains the pointer to the [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) instance from an [OH\_UdsHyperlink](../../structs/oh-udshyperlink/document.md) instance.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsHyperlink](../../structs/oh-udshyperlink/document.md)\* pThis | Pointer to the [OH\_UdsHyperlink](../../structs/oh-udshyperlink/document.md) instance. |
| [OH\_UdsDetails](../../structs/oh-udsdetails/document.md)\* details | Pointer to the [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) instance, which cannot be null. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdsHyperlink\_SetDetails()

int OH\_UdsHyperlink\_SetDetails(OH\_UdsHyperlink\* pThis, const OH\_UdsDetails\* details)

**Description**

Sets the [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) parameter for an [OH\_UdsHyperlink](../../structs/oh-udshyperlink/document.md) instance.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsHyperlink](../../structs/oh-udshyperlink/document.md)\* pThis | Pointer to the [OH\_UdsHyperlink](../../structs/oh-udshyperlink/document.md) instance. |
| [const OH\_UdsDetails](../../structs/oh-udsdetails/document.md)\* details | Pointer to the [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) instance, which cannot be null. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdsHtml\_GetDetails()

int OH\_UdsHtml\_GetDetails(OH\_UdsHtml\* pThis, OH\_UdsDetails\* details)

**Description**

Obtains the pointer to the [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) instance from an [OH\_UdsHtml](../../structs/oh-udshtml/document.md) instance.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsHtml](../../structs/oh-udshtml/document.md)\* pThis | Pointer to the [OH\_UdsHtml](../../structs/oh-udshtml/document.md) instance. |
| [OH\_UdsDetails](../../structs/oh-udsdetails/document.md)\* details | Pointer to the [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) instance, which cannot be null. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdsHtml\_SetDetails()

int OH\_UdsHtml\_SetDetails(OH\_UdsHtml\* pThis, const OH\_UdsDetails\* details)

**Description**

Sets the [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) parameter for an [OH\_UdsHtml](../../structs/oh-udshtml/document.md) instance.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsHtml](../../structs/oh-udshtml/document.md)\* pThis | Pointer to the [OH\_UdsHtml](../../structs/oh-udshtml/document.md) instance. |
| [const OH\_UdsDetails](../../structs/oh-udsdetails/document.md)\* details | Pointer to the [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) instance, which cannot be null. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdsAppItem\_GetDetails()

int OH\_UdsAppItem\_GetDetails(OH\_UdsAppItem\* pThis, OH\_UdsDetails\* details)

**Description**

Obtains the pointer to the [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) instance from an [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) object.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md)\* pThis | Pointer to the [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) instance. |
| [OH\_UdsDetails](../../structs/oh-udsdetails/document.md)\* details | Pointer to the [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) instance, which cannot be null. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdsAppItem\_SetDetails()

int OH\_UdsAppItem\_SetDetails(OH\_UdsAppItem\* pThis, const OH\_UdsDetails\* details)

**Description**

Sets the [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) parameter for an [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) instance.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md)\* pThis | Pointer to the [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) instance. |
| [const OH\_UdsDetails](../../structs/oh-udsdetails/document.md)\* details | Pointer to the [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) instance, which cannot be null. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdsFileUri\_GetDetails()

int OH\_UdsFileUri\_GetDetails(OH\_UdsFileUri\* pThis, OH\_UdsDetails\* details)

**Description**

Obtains the pointer to the [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) instance from an [OH\_UdsFileUri](../../structs/oh-udsfileuri/document.md) instance.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsFileUri](../../structs/oh-udsfileuri/document.md)\* pThis | Pointer to the [OH\_UdsFileUri](../../structs/oh-udsfileuri/document.md) instance. |
| [OH\_UdsDetails](../../structs/oh-udsdetails/document.md)\* details | Pointer to the [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) instance, which cannot be null. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdsFileUri\_SetDetails()

int OH\_UdsFileUri\_SetDetails(OH\_UdsFileUri\* pThis, const OH\_UdsDetails\* details)

**Description**

Sets the [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) parameter for an [OH\_UdsFileUri](../../structs/oh-udsfileuri/document.md) instance.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsFileUri](../../structs/oh-udsfileuri/document.md)\* pThis | Pointer to the [OH\_UdsFileUri](../../structs/oh-udsfileuri/document.md) instance. |
| [const OH\_UdsDetails](../../structs/oh-udsdetails/document.md)\* details | Pointer to the [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) instance, which cannot be null. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdsPixelMap\_GetDetails()

int OH\_UdsPixelMap\_GetDetails(OH\_UdsPixelMap\* pThis, OH\_UdsDetails\* details)

**Description**

Obtains the pointer to the [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) instance from an [OH\_UdsPixelMap](../../structs/oh-udspixelmap/document.md) instance.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsPixelMap](../../structs/oh-udspixelmap/document.md)\* pThis | Pointer to the [OH\_UdsPixelMap](../../structs/oh-udspixelmap/document.md) instance. |
| [OH\_UdsDetails](../../structs/oh-udsdetails/document.md)\* details | Pointer to the [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) instance, which cannot be null. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdsPixelMap\_SetDetails()

int OH\_UdsPixelMap\_SetDetails(OH\_UdsPixelMap\* pThis, const OH\_UdsDetails\* details)

**Description**

Sets the [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) parameter for an [OH\_UdsPixelMap](../../structs/oh-udspixelmap/document.md) instance.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsPixelMap](../../structs/oh-udspixelmap/document.md)\* pThis | Pointer to the [OH\_UdsPixelMap](../../structs/oh-udspixelmap/document.md) instance. |
| [const OH\_UdsDetails](../../structs/oh-udsdetails/document.md)\* details | Pointer to the [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) instance, which cannot be null. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdsDetails\_Create()

OH\_UdsDetails\* OH\_UdsDetails\_Create()

**Description**

Creates an [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) instance and a pointer to it.

If this pointer is no longer required, use [OH\_UdsDetails\_Destroy](#oh_udsdetails_destroy) to destroy it. Otherwise, memory leaks may occur.

**Since**: 22

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_UdsDetails\*](../../structs/oh-udsdetails/document.md) | Returns a pointer to the [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) instance if the operation is successful; returns **nullptr** otherwise. |

#### \[h2\]OH\_UdsDetails\_Destroy()

void OH\_UdsDetails\_Destroy(OH\_UdsDetails\* pThis)

**Description**

Destroys an [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) instance.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsDetails](../../structs/oh-udsdetails/document.md)\* pThis | Pointer to the [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) instance. |

#### \[h2\]OH\_UdsDetails\_HasKey()

bool OH\_UdsDetails\_HasKey(const OH\_UdsDetails\* pThis, const char\* key)

**Description**

Checks whether the [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) instance contains the specified key.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [const OH\_UdsDetails](../../structs/oh-udsdetails/document.md)\* pThis | Pointer to the [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) instance. |
| const char\* key | Key in a KV pair of the dictionary type. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Returns a check result. The value **false** indicates that the specified key does not exist, and **true** indicates the opposite. |

#### \[h2\]OH\_UdsDetails\_Remove()

int OH\_UdsDetails\_Remove(OH\_UdsDetails\* pThis, const char\* key)

**Description**

Deletes the specified KV pair from the [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) instance.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsDetails](../../structs/oh-udsdetails/document.md)\* pThis | Pointer to the [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) instance. |
| const char\* key | Key in a KV pair of the dictionary type. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdsDetails\_Clear()

int OH\_UdsDetails\_Clear(OH\_UdsDetails\* pThis)

**Description**

Clears all data from the [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) instance.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsDetails](../../structs/oh-udsdetails/document.md)\* pThis | Pointer to the [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdsDetails\_SetValue()

int OH\_UdsDetails\_SetValue(OH\_UdsDetails\* pThis, const char\* key, const char\* value)

**Description**

Adds a KV pair to an [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) instance.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsDetails](../../structs/oh-udsdetails/document.md)\* pThis | Pointer to the [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) instance. |
| const char\* key | Key in a KV pair of the dictionary type. |
| const char\* value | Value in a KV pair of the dictionary type. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdsDetails\_GetValue()

const char\* OH\_UdsDetails\_GetValue(const OH\_UdsDetails\* pThis, const char\* key)

**Description**

Obtains the value of a specified key from an [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) instance.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [const OH\_UdsDetails](../../structs/oh-udsdetails/document.md)\* pThis | Pointer to the [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) instance. |
| const char\* key | Key in a KV pair of the dictionary type. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Returns a pointer to the value of the dictionary type if the input parameters are valid; returns **nullptr** otherwise. |

#### \[h2\]OH\_UdsDetails\_GetAllKeys()

char\*\* OH\_UdsDetails\_GetAllKeys(OH\_UdsDetails\* pThis, unsigned int\* count)

**Description**

Obtains the result set of all keys from an [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) instance.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdsDetails](../../structs/oh-udsdetails/document.md)\* pThis | Pointer to the [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) instance. |
| unsigned int\* count | Pointer to the length of the result set. |

**Returns**

| Type | Description |
| :-- | :-- |
| char\*\* | 
Returns a double pointer to the result set if the operation is successful; returns **nullptr** otherwise.

When [OH\_UdsDetails\_Destroy](#oh_udsdetails_destroy) is used to destroy the [OH\_UdsDetails](../../structs/oh-udsdetails/document.md) instance, the return value is also released.

 |
