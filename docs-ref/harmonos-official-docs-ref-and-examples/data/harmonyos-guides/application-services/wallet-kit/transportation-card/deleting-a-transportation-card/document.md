# Deleting a Transportation Card

The transportation card deletion process consists of three steps: card display, deletion order generation, and deletion initiation. For details about the relevant APIs, please refer to [walletTransitCard (Transportation Card Capability)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-wallettransitcard).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/08FXSrFZTmGn821rmCPsRA/en-us_image_0000002182921502.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062123Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=689E1B4A5D400541BDDE45FC628B61E578844B6A98209EF7A18875F4D47072DD "Click to enlarge")

-   After your app is started, it calls the [getCardMetadataInDevice](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-wallettransitcard#section3931434195115) API to obtain the information about transportation cards that can be accessed by the app on a specified device. The result is returned in an array. If the returned array is empty, your app does not have any accessible transportation cards on this device and does not need to display the card activation entry. If the returned array is not empty, your app displays a proper page based on the actual transportation card information.
-   If the transportation card information includes the card number and balance, the card has been activated, and your app can directly display the transportation card information. Otherwise, your app can display the card activation entry.
-   When a user requests to delete a transportation card, your app sends a deletion order generation request to your server.
-   Your app calls the [deleteTransitCard](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-wallettransitcard#section12742829145411) API to delete the transportation card. If the deletion fails due to an exception, your app will receive an error code. For details, please refer to [ArkTS API Error Codes](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-error-code).

#### Development Procedure

1.  Obtain the list of activated transportation cards on a device.
    
    During **TransitCardClient** initialization, the second input parameter **callerId** of the construction method is the ID of the API caller. You can contact the Wallet Kit operations personnel to obtain the caller ID when applying for the transportation card service.
    
    import { common } from '@kit.AbilityKit';
    import { walletTransitCard } from '@kit.WalletKit'
    import { BusinessError } from '@kit.BasicServicesKit';
    
    transitCardClient: walletTransitCard.TransitCardClient = new walletTransitCard.TransitCardClient(this.getUIContext().getHostContext() as common.UIAbilityContext, 'callerId');
    
    async getCardMetadataInDevice() {
      this.transitCardClient.getCardMetadataInDevice(walletTransitCard.DeviceType.DEVICE\_PHONE).then((result) => {
        console.info(\`Succeeded in getting cardMetadataInDevice\`);
        // Display the transportation card list.
      }).catch((err: BusinessError) => {
        console.error(\`Failed to get CardMetadataInDevice, code:${err.code}, message:${err.message}\`);
      })
    }
    
2.  Delete the transportation card.
    
    import { common } from '@kit.AbilityKit';
    import { walletTransitCard } from '@kit.WalletKit'
    import { BusinessError } from '@kit.BasicServicesKit';
    
    transitCardClient: walletTransitCard.TransitCardClient = new walletTransitCard.TransitCardClient(this.getUIContext().getHostContext() as common.UIAbilityContext, 'callerId');
    
    async deleteTransitCard() {
      // Number of the activated transportation card, returned by the [getCardMetadataInDevice](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-wallettransitcard#section3931434195115) API in step 1.
      const logicalCardNumber = 'logicalCardNumber';
      // The value of **specifiedDeviceId** is returned by [getCardMetadataInDevice](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-wallettransitcard#section3931434195115).
      const specifiedDeviceId = 'specifiedDeviceId';
      // Order ID generated in your app after payment, which is implemented by you.
      const serverOrderId = 'serverOrderId';
      this.transitCardClient.deleteTransitCard(logicalCardNumber, specifiedDeviceId, serverOrderId).then(() => {
        console.info(\`Succeeded in deleting TransitCard\`);
      }).catch((err: BusinessError) => {
        console.error(\`Failed to delete TransitCard, code:${err.code}, message:${err.message}\`);
      })
    }
