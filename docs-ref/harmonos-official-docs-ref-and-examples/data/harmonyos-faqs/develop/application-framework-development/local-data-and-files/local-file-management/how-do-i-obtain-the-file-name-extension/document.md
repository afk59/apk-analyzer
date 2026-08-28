# How do I obtain the file name extension?

You can use [fs.listFile](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-fs#fslistfile) to obtain a list of files in a folder. The return value is an array of file names. You can obtain the file name extensions by processing the file name string. For example, you can use the **lastIndexOf()** method of the string to locate the position of the last dot (.) and use **substring()** to obtain the file name extension.
