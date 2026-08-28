# Accessing Application Files (C/C++)

#### When to Use

The **FileIO** module provides some APIs for basic file operations. For details about other APIs, see [libc](https://developer.huawei.com/consumer/en/doc/harmonyos-references/musl) and [libc++](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cpp).

#### Constraints

Before performing file operations, ensure that the URI or path passed in is correct and valid.

#### Available APIs

For details about the APIs, see [FileIO](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-fileio-h).

| API | Description |
| :-- | :-- |
| FileManagement\_ErrCode OH\_FileIO\_GetFileLocation(char \*uri, int uriLength, FileIO\_FileLocation \*location) | Obtains the location of a file. |
| enum FileIO\_FileLocation FileIO\_FileLocation | Enumerates the file locations. |
| enum FileManagement\_ErrCode FileManagement\_ErrCode | Enumerates the error codes used in the **FileIO** module. |

#### How to Develop

**Adding the Dynamic Link Library**

Add the following library to **CMakeLists.txt**.

target\_link\_libraries(sample PUBLIC libohfileio.so)

**Adding the Header File**

#include <cstdio>
#include <cstring>
#include <filemanagement/fileio/oh\_fileio.h>

Call **OH\_FileIO\_GetFileLocation** to obtain the location of a file.

Example:

void GetFileLocationExample() {
    char \*uri = "file://com.example.demo/data/storage/el2/base/files/test.txt";
    FileIO\_FileLocation location;
    FileManagement\_ErrCode ret = OH\_FileIO\_GetFileLocation(uri, strlen(uri), &location);
    if (ret == 0) {
        if (location == FileIO\_FileLocation::LOCAL) {
            printf("This file is on local.");
        } else if (location == FileIO\_FileLocation::CLOUD) {
            printf("This file is on cloud.");
        } else if (location == FileIO\_FileLocation::LOCAL\_AND\_CLOUD) {
            printf("This file is both on local and cloud.");
        }
    } else {
        printf("GetFileLocation failed, error code is %d", ret);
    }
}
