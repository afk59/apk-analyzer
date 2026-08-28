# What is the difference between fd and internal?

1.  **fd://<resource handle>**: identifier of a media file. It is generally used for playing resource files.
2.  **internal://cache**: path for storing files in an application's private directory. It is generally used for uploading and downloading files.
3.  **file://**: path for accessing files in the application sandbox directory and media library. It allows for operations such as opening, reading, and writing a file by using @ohos.file.fs APIs.
