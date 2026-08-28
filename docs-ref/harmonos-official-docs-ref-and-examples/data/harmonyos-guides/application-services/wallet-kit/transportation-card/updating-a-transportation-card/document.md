# Updating a Transportation Card

Transportation card data such as the validity period can be updated. The update involves three steps: card display, update order generation, and update initiation. For details about the relevant APIs, please refer to [walletTransitCard (Transportation Card Capability)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-wallettransitcard).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/K7HlETo9Re6vva7sUXA9kQ/en-us_image_0000002218521721.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062123Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CD92EBAAE61DD2DF76AC023A067FDC632EF1F135ADD00886309C2D4F47EEB326 "Click to enlarge")

-   After your app is started, it calls the [getCardMetadataInDevice](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-wallettransitcard#section3931434195115) API to obtain the information about transportation cards that can be accessed by the app on a specified device. The result is returned in an array. If the returned array is empty, your app does not have any accessible transportation cards on this device and does not need to display the card activation entry. If the returned array is not empty, your app displays a proper page based on the actual transportation card information. If the transportation card information includes the card number and balance, the card has been activated, and your app can directly display the transportation card information. Otherwise, your app can display the card activation entry.
-   When a user requests to update a transportation card, your app sends an update order generation request to your server.
-   Your app calls the [updateTransitCard](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-wallettransitcard#section8973172765418) API to update the transportation card. If the update fails due to an exception, your app will receive an error code. For details, please refer to [ArkTS API Error Codes](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-error-code).

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
    
2.  Update the transportation card.
    
    import { common } from '@kit.AbilityKit';
    import { walletTransitCard } from '@kit.WalletKit'
    import { BusinessError } from '@kit.BasicServicesKit';
    
    transitCardClient: walletTransitCard.TransitCardClient = new walletTransitCard.TransitCardClient(this.getUIContext().getHostContext() as common.UIAbilityContext, 'callerId');
    
    async updateTransitCard() {
      // Number of the activated transportation card, returned by the [getCardMetadataInDevice](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-wallettransitcard#section3931434195115) API in step 1.
      const logicalCardNumber = 'logicalCardNumber';
      // The value of **specifiedDeviceId** is returned by [getCardMetadataInDevice](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-wallettransitcard#section3931434195115).
      const specifiedDeviceId = 'specifiedDeviceId';
      // Order ID generated in your app after payment, which is implemented by you.
      const serverOrderId = 'serverOrderId';
      this.transitCardClient.updateTransitCard(logicalCardNumber, specifiedDeviceId, serverOrderId).then(() => {
        console.info(\`Succeeded in updating TransitCard\`);
      }).catch((err: BusinessError) => {
        console.error(\`Failed to update TransitCard, code:${err.code}, message:${err.message}\`);
      })
    }
