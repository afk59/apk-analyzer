# How do I convert a HAR into an HSP?

To convert a [HAR](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/har-package) into an [HSP](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/in-app-hsp), perform the following steps:

1.  Create an HSP, copy the HAR to the **lib** directory, and configure the HAR under **dependencies** in the **oh-package.json5** file of the HSP.
    
    "dependencies": {
      "myhar": "file:./lib/myHar.har" // MyHar.Har path: oh-package.json5 file in the same directory as the lib folder
    },
    
2.  Export the HAR content from the **Index.ets** file of the HSP.
    
    export \* as myhar from 'myhar';
    
3.  Compile the HSP.
