# Metadata Binding Development

#### Overview

Metadata binding allows the system to map the content browsed by the current user to the [App Linking link](../../../../application-services/app-linking-kit/about-this-kit/document.md) provided by a third-party application and save their mapping.

For details about the APIs, see the [MetadataBinding API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-awareness-metadatabinding).

#### When to Use

Third-party applications can use the metadata binding function to map the App Linking link to the desired content for easy access at a later time. For example, when a user is browsing a product in an e-commerce app and takes a screenshot of that product to save it, the system will record the mapping between the screenshot and the App Linking link provided by the e-commerce app. When the user views the screenshot again, the system will remind the user of whether to return to the e-commerce app to view the product details.

#### Demonstration Example

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/rMCsfplPQqqwPyFPPrq3zw/en-us_image_0000002537925048.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062024Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F3923D658C54DBD484293EFBC9CCA62477E9D04EEEDBA42C0372379BBE1E9DE9)

#### Available APIs

-   The initial APIs of this module are supported since API version 18. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   This module supports the metadata binding function.

| Name | Description |
| :-- | :-- |
| [submitMetadata](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-awareness-metadatabinding#metadatabindingsubmitmetadata)(metadata: string): void; | Passes the App Linking link mapped to the encoded metadata to Multimodal Awareness Kit, which then forwards the link to the system application that calls the encoding API at an appropriate time. |
| [on](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-awareness-metadatabinding#metadatabindingonoperationsubmitmetadata)(type: 'operationSubmitMetadata', bundleName: string, callback: Callback<number>): void; | Subscribes to system events that are used to obtain the encoded metadata. The application needs to register a callback to return the encoded metadata when the registered system event occurs. |
| [off](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-awareness-metadatabinding#metadatabindingoffoperationsubmitmetadata)(type: 'operationSubmitMetadata', bundleName: string, callback?: Callback<number>): void; | Unsubscribes from system events that are used to obtain the encoded metadata. The respective callback will be unregistered. |

#### Constraints

-   The maximum length of an App Linking link is 128 bytes.

#### How to Develop

1.  Import the related modules.
    
    import { metadataBinding } from '@kit.MultimodalAwarenessKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { Callback } from '@kit.BasicServicesKit';
    
2.  Define the callback used to return the encoded metadata and the bundle name.
    
    let callback : Callback<number> = (event: number) => {};
    let bundleName: string = '';
    
3.  Subscribe to system events that are used to obtain the encoded metadata.
    
    try {
       metadataBinding.on('operationSubmitMetadata', bundleName, callback);
       console.info("on succeeded");
    } catch (err) {
       let error = err as BusinessError;
       console.error("Register event error and err code is " + error.code);
    }
    
4.  Configure the App Linking link.
    
    // The application first enables the App Linking service, obtains the App Linking service, and then provides the service API for the link memory service
    let applink: string = "";
    try {
       metadataBinding.submitMetadata(applink);
    } catch (err) {
       let error = err as BusinessError;
       console.error("Submit metadata error and err code is " + error.code);
    }
    
5.  Unsubscribe from system events that are used to obtain the encoded metadata.
    
    try {
      metadataBinding.off('operationSubmitMetadata', bundleName, callback);
      console.info("off succeeded");
    } catch (err) {
      let error = err as BusinessError;
      console.error("Unregister event error and err code is " + error.code);
    }
