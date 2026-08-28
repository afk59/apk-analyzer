# How do I verify file consistency?

You can check the file consistency by comparing hash values. The hash value is calculated using the MD5 algorithm. For details, see [Generating an MD Using MD5 (ArkTS)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-generate-message-digest-md5).

Sample code is as follows.

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { fileIo } from '@kit.CoreFileKit'
import { buffer } from '@kit.ArkTS';

async function calFileMd5(fileUrl: string) {
  let md = cryptoFramework.createMd('MD5');
  let file = fileIo.openSync(fileUrl, fileIo.OpenMode.READ\_ONLY);
  let arrayBuffer = new ArrayBuffer(2048);
  let len: number = 0;
  let position: number = 0;
  do {
    len = fileIo.readSync(file.fd, arrayBuffer, { offset: position });
    if (len > 0) {
      let uint8Array = new Uint8Array(arrayBuffer.slice(0, len));
      let updateMessageBlob: cryptoFramework.DataBlob = { data: uint8Array };
      await md.update(updateMessageBlob);
      position += len;
    }
  } while (len > 0);
  fileIo.closeSync(file);
  let mdOutput = await md.digest();
  console.info('...calFileMd5: ' + buffer.from(mdOutput.data).toString('hex'));
}

**Reference**

[@ohos.file.hash (File Hash Processing)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-hash)
