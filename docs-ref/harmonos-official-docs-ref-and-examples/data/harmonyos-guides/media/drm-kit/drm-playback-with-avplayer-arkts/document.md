# DRM Playback with AVPlayer (ArkTS)

To play DRM-protected content using AVPlayer, you can use the ArkTS APIs provided by DRM Kit and Media Kit.

#### How to Develop

1.  Import the DRM Kit and Media Kit modules.
    
    import { drm } from '@kit.DrmKit'
    import { media } from '@kit.MediaKit'
    
2.  Import the BusinessError module to handle error codes from DRM Kit APIs.
    
    import { BusinessError } from '@kit.BasicServicesKit'
    
3.  Call [createAVPlayer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-f#mediacreateavplayer9) to create an AVPlayer instance and set a DRM information listener.
    
    let playerHandle: media.AVPlayer;
    async function initPlayer() {
    playerHandle = await media.createAVPlayer();
    playerHandle.on('mediaKeySystemInfoUpdate', async (mediaKeySystemInfo: drm.MediaKeySystemInfo\[\]) => {
    console.info('player has received drmInfo signal: ' + JSON.stringify(mediaKeySystemInfo))
    // Process DRM information.
    // Set a decryption session.
    })
    }
    
4.  Call [createMediaKeySystem](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-drm-f#drmcreatemediakeysystem) and [createMediaKeySession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-drm-mediakeysystem#createmediakeysession) to create MediaKeySystem and MediaKeySession instances based on the UUID in the DRM information.
    
    let mediaKeySystem: drm.MediaKeySystem
    let mediaKeySession: drm.MediaKeySession
    let drmInfoArr: drm.MediaKeySystemInfo\[\] = mediaKeySystemInfo
    for (let i = 0; i < drmInfoArr.length; i++) {
      console.info('drmInfoArr - uuid: ' + drmInfoArr\[i\].uuid)
      console.info('drmInfoArr - pssh: ' + drmInfoArr\[i\].pssh)
      let description: drm.MediaKeySystemDescription\[\] = drm.getMediaKeySystems();
      let solutionName: string = "com.wiseplay.drm"
      for (let item of description) {
        if (drmInfoArr\[i\].uuid == item.uuid) {
          solutionName = item.name
          }
        }
        let isSupported: boolean = drm.isMediaKeySystemSupported(solutionName, "video/mp4");
        if (isSupported) {
          mediaKeySystem = drm.createMediaKeySystem(solutionName);
          mediaKeySession = mediaKeySystem.createMediaKeySession();
      }
      // Request and process the media key.
    }
    
5.  Call [generateMediaKeyRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-drm-mediakeysession#generatemediakeyrequest) to generate a media key request, and call [processMediaKeyResponse](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-drm-mediakeysession#processmediakeyresponse) to process its response.
    
    let initData: Uint8Array = new Uint8Array(drmInfoArr\[i\].pssh);
    const optionsData: drm.OptionsData\[\] = \[{
      name: "optionalDataName",
      value: "optionalDataValue"
    }\]
    mediaKeySession.generateMediaKeyRequest("video/mp4", initData, drm.MediaKeyType.MEDIA\_KEY\_TYPE\_ONLINE, optionsData).then(async (licenseRequest) => {
      console.info("generateMediaKeyRequest success", licenseRequest.mediaKeyRequestType, licenseRequest.data, licenseRequest.defaultURL);
      // Send licenseRequest.data returned by the media key request to the DRM service through a network request and process the response.
      let licenseResponse = new Uint8Array(\[0x00, 0x00, 0x00, 0x00\]);
      mediaKeySession.processMediaKeyResponse(licenseResponse).then((mediaKeyId: Uint8Array) => {
        console.info("processMediaKeyResponse success");
      }).catch((err:BusinessError) =>{
        console.error("processMediaKeyResponse err end", err.code);
      });
    }).catch((err:BusinessError) =>{
      console.error("generateMediaKeyRequest err end", err.code);
    });
    
6.  Call [requireSecureDecoderModule](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-drm-mediakeysession#requiresecuredecodermodule) and [setDecryptionConfig](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-avplayer#setdecryptionconfig11) to set the decryption session after the media key response is successfully processed.
    
    let svp: boolean = mediaKeySession.requireSecureDecoderModule('video/avc');
    playerHandle.setDecryptionConfig(mediaKeySession, svp)
    
7.  Destroy the AVPlayer instance and destroy the MediaKeySession and MediaKeySystem instances based on the released event.
    
    playerHandle.on('stateChange', async (state: string, reason: media.StateChangeReason) => {
       if (state == 'released') {
          mediaKeySession.destroy();
          mediaKeySystem.destroy();
       } else if (state == 'releasing') {
          await playerHandle.release();
       }
    })
