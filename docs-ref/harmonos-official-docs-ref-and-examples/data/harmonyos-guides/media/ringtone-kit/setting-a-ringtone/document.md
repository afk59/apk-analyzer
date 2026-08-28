# Setting a Ringtone

1.  Import the **ringtone** module and related common modules.
    
    import { common } from '@kit.AbilityKit';
    import { ringtone } from '@kit.RingtoneKit'
    import { uniformTypeDescriptor } from '@kit.ArkData';
    import { JSON } from '@kit.ArkTS';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    const APP\_TAG = "Msc\_Demo"
    const DOMAIN = 0x0001
    
2.  Call the [ringtone.getSupportedRingtoneTypes](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ringtone-ringtone#section81796536265) API to query the supported ringtone types.
    
    let ringtoneTypeList: Array<ringtone.RingtoneType> = ringtone.getSupportedRingtoneTypes();
    hilog.info(DOMAIN, APP\_TAG,'getSupportedRingtoneTypes : ' + JSON.stringify(ringtoneTypeList));
    
3.  Call the [ringtone.getSupportedDataTypes](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ringtone-ringtone#section1858041418291) API to query the supported data types. Currently supported formats are MP3, OGG, FLAC, AAC, MP2, and M4A.
    
    // **ringtone.RingtoneType.NOTIFICATION** indicates the ringtone for a notification.
    let dataTypeList: Array<uniformTypeDescriptor.UniformDataType> = ringtone.getSupportedDataTypes(ringtone.RingtoneType.NOTIFICATION);
    hilog.info(DOMAIN, APP\_TAG,'getSupportedDataTypes: ' + JSON.stringify(dataTypeList));
    
4.  Call the [ringtone.startRingtoneSetting](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ringtone-ringtone#section5949453189) API to display the setting pop-up window for the user to set the ringtone and return the ringtone type.
    
    The result is returned asynchronously through a promise:
    
    // For details about the code, see the API reference.
    let prefixUri: string = '';
    let audioPath: string = prefixUri + '/' + this.buttonText;
    let fileName: string = audioPath.substring(audioPath.lastIndexOf('/') + 1, audioPath.lastIndexOf('.'));
    await ringtone.startRingtoneSetting(this.context, audioPath, fileName).then(res => {
      hilog.info(DOMAIN, APP\_TAG,'setFlag :' + res);
    });
    
    The result is returned asynchronously through a callback:
    
    // For details about the code, see the API reference.
    let prefixUri: string = '';
    let audioPath: string = prefixUri + '/' + this.buttonText;
    let fileName: string = audioPath.substring(audioPath.lastIndexOf('/') + 1, audioPath.lastIndexOf('.'));
    ringtone.startRingtoneSetting(this.context, audioPath, fileName, (err, data) => {
      hilog.info(DOMAIN, APP\_TAG,'setFlag :' + data);
    }); 
    
5.  Call the [ringtone.getSupportedMaxDuration](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ringtone-ringtone#section759192934316) API to obtain the maximum duration supported by the current ringtone.
    
    // **ringtone.RingtoneType.MESSAGE** indicates the ringtone for an SMS message.
    let maxDuration: number =
      ringtone.getSupportedMaxDuration(ringtone.RingtoneType.MESSAGE, uniformTypeDescriptor.UniformDataType.MP3)
    hilog.info(DOMAIN, APP\_TAG,'getSupportedMaxDuration: ' + maxDuration);
