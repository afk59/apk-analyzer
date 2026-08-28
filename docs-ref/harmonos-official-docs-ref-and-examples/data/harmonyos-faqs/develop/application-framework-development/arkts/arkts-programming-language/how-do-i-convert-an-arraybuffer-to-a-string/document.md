# How do I convert an ArrayBuffer to a string?

You can use **util.TextDecoder.create()** to create a utility class, and then call [decodeToString()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-util#decodetostring12) for conversion.

let decoder = util.TextDecoder.create('utf-8');
let str = decoder.decodeToString(new Uint8Array(arrayBuffer));

You can convert **arrayBufferVal** of the ArrayBuffer type returned by **proArrayBuffer** to a string.

import { util, buffer } from '@kit.ArkTS';

let blobValue: buffer.Blob = new buffer.Blob(\['name', 'age', 'sex'\]);
let proArrayBuffer = blobValue.arrayBuffer();

proArrayBuffer.then((arrayBufferVal: ArrayBuffer) => {
  let decoder = util.TextDecoder.create('utf-8');
  let stringData = decoder.decodeToString(new Uint8Array(arrayBufferVal));
  console.log('stringData:', stringData);
});
