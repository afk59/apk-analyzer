# Generating an MD Using SHA-256 (ArkTS)

For details about the algorithm specifications, see [Supported Algorithms and Specifications](../../md-overview-and-algorithm-specifications/document.md#supported-algorithms-and-specifications).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/f5J1Hb7QTaG5yYWzAVInLw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062004Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8D0998FAE2A8899A56180278E94DFA375962A5AB8944AD9172D7624A1C12A0D3)

Since API version 12, wearable devices support MD operations.

#### How to Develop

During the MD operation, you can [pass in all the data at a time](#generating-an-md-by-passing-in-full-data) or [pass in data by segment](#generating-an-md-by-passing-in-data-by-segment). For the same piece of data, the result will be the same no matter how the data is passed. Use the appropriate method based on the data size.

The following provides examples of MD operations with different data passing methods.

## Generating an MD by Passing In Full Data

1.  Call [cryptoFramework.createMd](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-cryptoframework#cryptoframeworkcreatemd) with the MD algorithm **SHA256** to create a message digest (**Md**) instance.
    
2.  Call [Md.update](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-cryptoframework#update-6) to pass in the full data. The data to be passed in by a single **update()** operation is not size bound.
    
3.  Call [Md.digest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-cryptoframework#digest) to generate an MD.
    
4.  Call [Md.getMdLength](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-cryptoframework#getmdlength) to obtain the MD length, in bytes.
    

-   Example: Pass in the full data to generate an MD using **await**.
    
    import { cryptoFramework } from '@kit.CryptoArchitectureKit';
    import { buffer } from '@kit.ArkTS';
    
    async function doSha256() {
      let mdAlgName = "SHA256"; // Algorithm to use.
      let message = 'mdTestMessage'; // Message to be digested.
      let md = cryptoFramework.createMd(mdAlgName);
      // If there is a small amount of data to be processed, call update() to pass in all the data at a time. The amount of data to be passed in by a single update() call is not limited.
      await md.update({ data: new Uint8Array(buffer.from(message, 'utf-8').buffer) });
      let mdResult = await md.digest();
      console.info('Md result:' + mdResult.data);
      let mdLen = md.getMdLength();
      console.info("md len: " + mdLen);
    }
    
-   Example: Pass in the full data to generate an MD using a synchronous API.
    
    import { cryptoFramework } from '@kit.CryptoArchitectureKit';
    import { buffer } from '@kit.ArkTS';
    
    function doSha256BySync() {
      let mdAlgName = "SHA256"; // Algorithm to use.
      let message = 'mdTestMessage'; // Message to be digested.
      let md = cryptoFramework.createMd(mdAlgName);
      // If there is a small amount of data to be processed, call update() to pass in all the data at a time. The amount of data to be passed in by a single update() call is not limited.
      md.updateSync({ data: new Uint8Array(buffer.from(message, 'utf-8').buffer) });
      let mdResult = md.digestSync();
      console.info('\[Sync\]:Md result:' + mdResult.data);
      let mdLen = md.getMdLength();
      console.info("md len: " + mdLen);
    }
    

## Generating an MD by Passing In Data by Segment

1.  Call [cryptoFramework.createMd](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-cryptoframework#cryptoframeworkcreatemd) with the MD algorithm **SHA256** to create a message digest (**Md**) instance.
    
2.  Call [Md.update](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-cryptoframework#update-7) multiple times to pass in 20 bytes each time.
    
3.  Call [Md.digest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-cryptoframework#digest-1) to generate an MD.
    
4.  Call [Md.getMdLength](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-cryptoframework#getmdlength) to obtain the MD length, in bytes.
    

-   Example: Pass in data by segment to generate an MD using **await**.
    
    import { cryptoFramework } from '@kit.CryptoArchitectureKit';
    import { buffer } from '@kit.ArkTS';
    
    async function doLoopSha256() {
      let mdAlgName = "SHA256"; // Algorithm to use.
      let md = cryptoFramework.createMd(mdAlgName);
      // In this example, the message is of 43 bytes. After decoded in UTF-8 format, the message is also of 43 bytes.
      let messageText = "aaaaa.....bbbbb.....ccccc.....ddddd.....eee";
      let messageData = new Uint8Array(buffer.from(messageText, 'utf-8').buffer);
      let updateLength = 20; // Pass in 20 bytes each time. You can set this parameter as required.
      for (let i = 0; i < messageData.length; i += updateLength) {
        let updateMessage = messageData.subarray(i, i + updateLength);
        let updateMessageBlob: cryptoFramework.DataBlob = { data: updateMessage };
        await md.update(updateMessageBlob);
      }
      let mdOutput = await md.digest();
      console.info("md result: " + mdOutput.data);
      let mdLen = md.getMdLength();
      console.info("md len: " + mdLen);
    }
    
-   Example: Pass in data by segment to generate an MD using a synchronous API.
    
    import { cryptoFramework } from '@kit.CryptoArchitectureKit';
    import { buffer } from '@kit.ArkTS';
    
    function doLoopSha256BySync() {
      let mdAlgName = "SHA256"; // Algorithm to use.
      let md = cryptoFramework.createMd(mdAlgName);
      // In this example, the message is of 43 bytes. After decoded in UTF-8 format, the message is also of 43 bytes.
      let messageText = "aaaaa.....bbbbb.....ccccc.....ddddd.....eee";
      let messageData = new Uint8Array(buffer.from(messageText, 'utf-8').buffer);
      let updateLength = 20; // Pass in 20 bytes each time. You can set this parameter as required.
      for (let i = 0; i < messageData.length; i += updateLength) {
        let updateMessage = messageData.subarray(i, i + updateLength);
        let updateMessageBlob: cryptoFramework.DataBlob = { data: updateMessage };
        md.updateSync(updateMessageBlob);
      }
      let mdOutput = md.digestSync();
      console.info("\[Sync\]:md result: " + mdOutput.data);
      let mdLen = md.getMdLength();
      console.info("md len: " + mdLen);
    }
