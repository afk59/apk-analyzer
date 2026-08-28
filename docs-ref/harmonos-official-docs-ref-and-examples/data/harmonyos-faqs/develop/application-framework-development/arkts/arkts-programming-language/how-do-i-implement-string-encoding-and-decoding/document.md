# How do I implement string encoding and decoding?

**TextEncoder** provides APIs to encode strings into byte arrays. It supports multiple formats, including UTF-8, UTF-16LE, and UTF-16BE.

**TextDecoder** provides APIs to decode byte arrays into strings. It supports multiple formats, including UTF-8, UTF-16LE, UTF-16BE, ISO-8859, and Windows-1251.

The following sample code shows how to use **TextEncoder** and **TextDecoder**:

import { util } from '@kit.ArkTS';
// Create Encoder
let textEncoder:util.TextEncoder = new util.TextEncoder('gbk');
let buffer:ArrayBuffer = new ArrayBuffer(20);
let encodeResult:Uint8Array = new Uint8Array(buffer);

// code
encodeResult = textEncoder.encodeInto('hello');
console.info('Encode result: ', encodeResult);

// Create decoder
let textDecoder = util.TextDecoder.create('gbk');

// decode
let decodeResult = textDecoder.decodeToString(encodeResult);
console.info('Decode result: ', decodeResult);

**Reference**

[TextEncoder](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-util#textencoder) and [TextDecoder](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-util#textdecoder)
