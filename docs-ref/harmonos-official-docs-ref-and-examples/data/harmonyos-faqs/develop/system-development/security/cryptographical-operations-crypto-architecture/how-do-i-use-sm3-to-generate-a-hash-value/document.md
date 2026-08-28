# How do I use SM3 to generate a hash value?

Call [cryptoFramework.createMd](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-cryptoframework#cryptoframeworkcreatemd) with SM3 passed in.

Sample code:

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { util, buffer } from '@kit.ArkTS';

let base64 = new util.Base64Helper();

@Entry
@Component
struct SM3Encrypted {
  stringToUint8Array(str: string) {
    return new Uint8Array(buffer.from(str, 'utf-8').buffer);
  }

  // Complete the summary in Promise format
  doMdByPromise() {
    // Summary algorithm name.
    let mdAlgName = 'SM3';
    // The data to be summarized.
    let message = 'Hello,world';
    let md = cryptoFramework.createMd(mdAlgName);
    console.info('\[Promise\]: Md algName is: ' + md.algName);
    let promiseMdUpdate = md.update({ data: this.stringToUint8Array(message) });
    promiseMdUpdate.then(() => {
      // Call digest() to return the result.
      let PromiseMdDigest = md.digest();
      return PromiseMdDigest;
    }).then(digestOutput => {
      let mdOutput = digestOutput.data;
      //Uint8Array to base64
      let str2 = base64.encodeToStringSync(mdOutput);
      //Convert to hexadecimal
      let str = this.uint8ArrayToHexStr(mdOutput);
      console.info('\[Promise\]: MD result: ' + mdOutput);
      let mdLen = md.getMdLength();
      console.info('\[Promise\]: MD len: ' + mdLen);
    }).catch((error: BusinessError) => {
      console.error('\[Promise\]: error: ' + error.message);
    });
  }

  //The summary result is Uint8Array type, converted to hexadecimal string data
  uint8ArrayToHexStr(data: Uint8Array): string {
    let hexString = '';
    let i: number;
    for (i = 0; i < data.length; i++) {
      let char = ('00' + data\[i\].toString(16)).slice(-2);
      hexString += char;
    }
    return hexString;
  }

  build() {
    Column({ space: 10 }) {
      Button('Use SM3 for encryption')
        .onClick(() => {
          this.doMdByPromise();
        })
    }
    .alignItems(HorizontalAlign.Center)
    .height('100%')
    .width('100%')
  }
}
