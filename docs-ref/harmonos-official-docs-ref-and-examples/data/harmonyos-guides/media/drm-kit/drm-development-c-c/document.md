# DRM Development (C/C++)

#### When to Use

DRM Kit provides C/C++ APIs for comprehensive digital rights management, covering certificate management, license management, content authorization, and content decryption.

Its implementation is built around two core classes: MediaKeySystem and MediaKeySession. MediaKeySystem handles system-level management of DRM certificates and licenses, as well as the lifecycle of MediaKeySession instances. MediaKeySession, in turn, is responsible for authorizing specific content and enabling its decryption through integration with AVCodec Kit for playback.

#### How to Develop

For details on the APIs, see [DRM API](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-drm).

1.  Import the DRM Kit module.
    
    #include "multimedia/drm\_framework/native\_drm\_common.h"
    #include "multimedia/drm\_framework/native\_drm\_err.h"
    #include "multimedia/drm\_framework/native\_mediakeysession.h"
    #include "multimedia/drm\_framework/native\_mediakeysystem.h"
    
2.  Link the dynamic libraries in the CMake script.
    
    target\_link\_libraries(PUBLIC libnative\_drm.so)
    
3.  Obtain the name and ID list of the DRM solutions supported by the device.
    
    uint32\_t count = 3; // count specifies the number of DRM plugins supported by the device. Pass in the actual number.
    DRM\_MediaKeySystemDescription descriptions\[3\];
    memset(descriptions, 0, sizeof(descriptions));
    Drm\_ErrCode ret = OH\_MediaKeySystem\_GetMediaKeySystems(descriptions, &count);
    if (ret != DRM\_ERR\_OK) {
        printf("OH\_MediaKeySystem\_GetMediaKeySystems failed.");
    }
    
4.  (Optional) Check whether the device supports a specific DRM solution based on the name, MIME type, and content protection level.
    
    bool isSupported = OH\_MediaKeySystem\_IsSupported3("com.wiseplay.drm", "video/mp4", CONTENT\_PROTECTION\_LEVEL\_SW\_CRYPTO);
    if (isSupported != true) {
        printf("The device does not support the content protection level.");
    }
    
5.  Create a MediaKeySystem instance.
    
    MediaKeySystem \*mediaKeySystem = nullptr;
    ret = OH\_MediaKeySystem\_Create("com.wiseplay.drm", &mediaKeySystem);
    if (ret != DRM\_ERR\_OK || mediaKeySystem == nullptr) {
        printf("OH\_MediaKeySystem\_Create failed.");
    }
    
6.  (Optional) Set the MediaKeySystem event listener callback.
    
    static Drm\_ErrCode SystemCallBackWithObj(MediaKeySystem \*mediaKeySystem, DRM\_EventType eventType,
        uint8\_t \*info, int32\_t infoLen, char \*extra)
    {
        printf("SystemCallBackWithObj enter");
        if (eventType == EVENT\_PROVISION\_REQUIRED) {
            // Request and process the DRM certificate.
        }
        return DRM\_ERR\_OK;
    }
    
    ret = OH\_MediaKeySystem\_SetCallback(mediaKeySystem, SystemCallBackWithObj);
    if (ret != DRM\_ERR\_OK) {
        printf("OH\_MediaKeySystem\_SetCallback failed.");
    }
    
7.  (Optional) Obtain the status of the DRM certificate.
    
    DRM\_CertificateStatus certStatus = CERT\_STATUS\_INVALID;
    // Check the DRM certificate status of the device.
    ret = OH\_MediaKeySystem\_GetCertificateStatus(mediaKeySystem, &certStatus);
    if (ret == DRM\_ERR\_OK && certStatus != CERT\_STATUS\_PROVISIONED) {
        // Request and process the DRM certificate.
    }
    
8.  (Optional) Generate a DRM certificate request and process its response.
    
    #define MAX\_DRM\_PROVISION\_BUF\_SIZE 24576 // 24576: (2 \* 12 \* 1024)
    unsigned char request\[MAX\_DRM\_PROVISION\_BUF\_SIZE\] = { 0x00 };  // MAX\_DRM\_PROVISION\_BUF\_SIZE specifies the maximum length of a DRM certificate request. Apply for memory based on the actual length.
    int32\_t requestLen = MAX\_DRM\_PROVISION\_BUF\_SIZE;
    // The maximum length of the DRM service URL is 2048.
    char defaultUrl\[2048\] = { 0x00 };
    int32\_t defaultUrlLen = 2048;
    ret = OH\_MediaKeySystem\_GenerateKeySystemRequest(mediaKeySystem, request, &requestLen, defaultUrl,
        defaultUrlLen);
    if (ret != DRM\_ERR\_OK) {
        printf("OH\_MediaKeySystem\_GenerateKeySystemRequest failed.");
    }
    /\*
      The application sends a DRM certificate request to the DRM service through a network request, obtains a response,
      and sets the response to the device. Pass in the actual data and length.
    \*/
    unsigned char keySystemResponse\[MAX\_DRM\_PROVISION\_BUF\_SIZE\] = {0x00};
    ret = OH\_MediaKeySystem\_ProcessKeySystemResponse(mediaKeySystem, keySystemResponse, sizeof(keySystemResponse));
    if (ret != DRM\_ERR\_OK) {
        printf("OH\_MediaKeySystem\_ProcessKeySystemResponse failed.");
    }
    
9.  (Optional) Obtain the maximum content protection level supported by the device.
    
    DRM\_ContentProtectionLevel maxContentProtectionLevel = CONTENT\_PROTECTION\_LEVEL\_UNKNOWN;
    ret = OH\_MediaKeySystem\_GetMaxContentProtectionLevel(mediaKeySystem, &maxContentProtectionLevel);
    if (ret != DRM\_ERR\_OK) {
        printf("OH\_MediaKeySystem\_GetMaxContentProtectionLevel failed.");
    }
    
10.  Create a MediaKeySession instance.
     
     MediaKeySession \*mediaKeySession = nullptr;
     DRM\_ContentProtectionLevel contentProtectionLevel = CONTENT\_PROTECTION\_LEVEL\_SW\_CRYPTO; // Set the content protection level supported by the device.
     ret = OH\_MediaKeySystem\_CreateMediaKeySession(mediaKeySystem, &contentProtectionLevel, &mediaKeySession);
     if (ret != DRM\_ERR\_OK || mediaKeySession == nullptr) {
         printf("OH\_MediaKeySystem\_CreateMediaKeySession failed.");
     }
     
11.  (Optional) Set the MediaKeySession event listener callback.
     
     static Drm\_ErrCode SessionEventCallBackWithObj(MediaKeySession \*mediaKeySession, DRM\_EventType eventType, uint8\_t \*info, int32\_t infoLen, char \*extra)
     {
         if (eventType == EVENT\_KEY\_REQUIRED) {
             // Request and process the media key.
         }
         return DRM\_ERR\_OK;
     }
     
     static Drm\_ErrCode SessionKeyChangeCallBackWithObj(MediaKeySession \*mediaKeySession, DRM\_KeysInfo \*keysInfo, bool hasNewGoodKeys)
     {
         return DRM\_ERR\_OK;
     }
     
     OH\_MediaKeySession\_Callback sessionCallback = { SessionEventCallBackWithObj, SessionKeyChangeCallBackWithObj };
     ret = OH\_MediaKeySession\_SetCallback(mediaKeySession, &sessionCallback);
     if (ret != DRM\_ERR\_OK) {
         printf("OH\_MediaKeySession\_SetCallback failed.");
     }
     
12.  (Optional) Check whether secure decoding is required.
     
     bool requireSecureDecoder;
     ret = OH\_MediaKeySession\_RequireSecureDecoderModule(mediaKeySession, "video/avc", &requireSecureDecoder);
     if (ret != DRM\_ERR\_OK) {
         printf("OH\_MediaKeySession\_RequireSecureDecoderModule failed.");
     }
     
13.  Generate a media key request and process its response to request a license for content authorization.
     
     #define MAX\_DRM\_MEDIA\_KEY\_RESPONSE\_BUF\_SIZE 24576 // 24576: (2 \* 12 \* 1024)
     DRM\_MediaKeyRequest mediaKeyRequest;
     DRM\_MediaKeyRequestInfo info;
     // initData corresponds to PSSH data in the stream. Pass in the actual data.
     unsigned char initData\[512\] = {0x00};
     memset(&info, 0, sizeof(DRM\_MediaKeyRequestInfo));
     info.initDataLen = sizeof(initData);
     info.type = MEDIA\_KEY\_TYPE\_ONLINE; // MEDIA\_KEY\_TYPE\_ONLINE: online media key request; MEDIA\_KEY\_TYPE\_OFFLINE: offline media key request.
     memcpy(info.mimeType, (char \*)"video/mp4", sizeof("video/mp4"));
     memcpy(info.initData, initData, sizeof(initData));
     memcpy(info.optionName\[0\], (char \*)"optionalDataName", sizeof("optionalDataName"));
     memcpy(info.optionData\[0\], (char \*)"optionalDataValue", sizeof("optionalDataValue"));
     info.optionsCount = 1;
     ret = OH\_MediaKeySession\_GenerateMediaKeyRequest(mediaKeySession, &info, &mediaKeyRequest);
     if (ret != DRM\_ERR\_OK) {
         printf("OH\_MediaKeySession\_GenerateMediaKeyRequest failed.");
     }
     /\*
       The application requests the DRM service through the network, obtains a media key response, and sends the response to OH\_MediaKeySession\_ProcessMediaKeyResponse.
       If the response is an offline media key response, the offline media key ID is returned. Set mediaKeyId based on the actual data and length.
     \*/
     unsigned char mediaKeyId\[128\] = {0x00};
     int32\_t mediaKeyIdLen = 128;
     // MAX\_DRM\_MEDIA\_KEY\_RESPONSE\_BUF\_SIZE specifies the maximum length of a media key response. Pass in the actual length.
     unsigned char mediaKeyResponse\[MAX\_DRM\_MEDIA\_KEY\_RESPONSE\_BUF\_SIZE\] = {0x00};
     int32\_t mediaKeyResponseLen = MAX\_DRM\_MEDIA\_KEY\_RESPONSE\_BUF\_SIZE;
     ret = OH\_MediaKeySession\_ProcessMediaKeyResponse(mediaKeySession, mediaKeyResponse,
         mediaKeyResponseLen, mediaKeyId, &mediaKeyIdLen);
     if (ret != DRM\_ERR\_OK) {
         printf("OH\_MediaKeySession\_ProcessMediaKeyResponse failed.");
     }
     
14.  (Optional) Restore offline media keys.
     
     // Load the media key with the specified media key ID to the current session.
     ret = OH\_MediaKeySession\_RestoreOfflineMediaKeys(mediaKeySession, mediaKeyId, mediaKeyIdLen);
     if (ret != DRM\_ERR\_OK) {
         printf("OH\_MediaKeySession\_RestoreOfflineMediaKeys failed.");
     }
     
15.  (Optional) Check the status of media keys.
     
     DRM\_MediaKeyStatus mediaKeyStatus;
     ret = OH\_MediaKeySession\_CheckMediaKeyStatus(mediaKeySession, &mediaKeyStatus);
     if (ret != DRM\_ERR\_OK) {
         printf("OH\_MediaKeySession\_CheckMediaKeyStatus failed.");
     }
     
16.  (Optional) Obtain the IDs of offline media keys, obtain their status, and clear them.
     
     DRM\_OfflineMediakeyIdArray offlineMediaKeyIds;
     ret = OH\_MediaKeySystem\_GetOfflineMediaKeyIds(mediaKeySystem, &offlineMediaKeyIds);
     if (ret != DRM\_ERR\_OK) {
         printf("OH\_MediaKeySystem\_GetOfflineMediaKeyIds failed.");
     }
     DRM\_OfflineMediaKeyStatus OfflineMediaKeyStatus = OFFLINE\_MEDIA\_KEY\_STATUS\_UNKNOWN;
     ret = OH\_MediaKeySystem\_GetOfflineMediaKeyStatus(mediaKeySystem, offlineMediaKeyIds.ids\[0\], offlineMediaKeyIds.idsLen\[0\], &OfflineMediaKeyStatus);
     if (ret != DRM\_ERR\_OK) {
         printf("OH\_MediaKeySystem\_GetOfflineMediaKeyStatus failed.");
     }
     ret = OH\_MediaKeySystem\_ClearOfflineMediaKeys(mediaKeySystem, offlineMediaKeyIds.ids\[0\], offlineMediaKeyIds.idsLen\[0\]);
     if (ret != DRM\_ERR\_OK) {
         printf("OH\_MediaKeySystem\_ClearOfflineMediaKeys failed.");
     }
     
17.  Destroy the MediaKeySession instance.
     
     ret = OH\_MediaKeySession\_Destroy(mediaKeySession);
     if (ret != DRM\_ERR\_OK) {
         printf("OH\_MediaKeySession\_Destroy failed.");
     }
     
18.  Destroy the MediaKeySystem instance.
     
     ret = OH\_MediaKeySystem\_Destroy(mediaKeySystem);
     if (ret != DRM\_ERR\_OK) {
         printf("OH\_MediaKeySystem\_Destroy failed.");
     }
