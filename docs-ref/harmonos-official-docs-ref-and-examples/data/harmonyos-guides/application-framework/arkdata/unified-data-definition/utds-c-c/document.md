# UTDs (C/C++)

#### When to Use

The Unified Data Management Framework (UDMF) provides standards for data interaction across applications and devices, defines a unified data language, and improves data interaction efficiency. With secure and unified data channels, UDMF supports data access permissions and lifecycle management policies at different levels, achieving efficient data sharing.

#### Basic Concepts

-   UTD
    
    A uniform type descriptor (UTD) defines data of the same type to eliminate data type ambiguity. It contains the data type ID and types to which the current data type belongs. UTDs are generally used to filter or identify the data type in file preview and file sharing.
    

#### Available APIs

For details about the APIs, see [utd.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-utd-h).

| API | Description |
| :-- | :-- |
| OH\_Utd\* OH\_Utd\_Create(const char\* typeId) | Creates a pointer to an **OH\_Utd** instance. |
| void OH\_Utd\_Destroy(OH\_Utd\* pThis) | Destroys the pointer to an **OH\_Utd** instance. |
| const char\*\* OH\_Utd\_GetTypesByFilenameExtension(const char\* extension, unsigned int\* count) | Obtains the uniform data types by file name extension. |
| const char\*\* OH\_Utd\_GetTypesByMimeType(const char\* mimeType, unsigned int\* count) | Obtains the uniform data types by MIME type. |
| bool OH\_Utd\_Equals(OH\_Utd\* utd1, OH\_Utd\* utd2) | Checks whether two UTDs are the same. |
| void OH\_Utd\_DestroyStringList(const char\*\* list, unsigned int count) | Destroys a UTD list. |
| bool OH\_Utd\_BelongsTo (const char \*srcTypeId, const char \*destTypeId) | Checks whether a UTD belongs to the target UTD. |
| bool OH\_Utd\_IsLower (const char\* srcTypeId, const char\* destTypeId ) | Checks whether a UTD is a lower-level type of the target UTD. For example, **TYPE\_SCRIPT** is a lower-level type of **SOURCE\_CODE**, and **TYPE\_SCRIPT** and **SOURCE\_CODE** are lower-level types of **PLAIN\_TEXT**. |
| bool OH\_Utd\_IsHigher (const char\* srcTypeId, const char\* destTypeId ) | Checks whether a UTD is a higher-level type of the target UTD. For example, **SOURCE\_CODE** is a higher-level type of **TYPE\_SCRIPT**, and **PLAIN\_TEXT** is a higher-level type of **SOURCE\_CODE** and **TYPE\_SCRIPT**. |

#### Adding Dynamic Link Libraries

Add the following libraries to **CMakeLists.txt**.

libudmf.so, libhilog\_ndk.z.so

#### Including Header Files

#include <cstdio>
#include <cstring>
#include <database/udmf/utd.h>
#include <database/udmf/uds.h>
#include <database/udmf/udmf.h>
#include <database/udmf/udmf\_meta.h>
#include <database/udmf/udmf\_err\_code.h>
#include <hilog/log.h>

#undef LOG\_TAG
#define LOG\_TAG "MY\_LOG"

#### Obtaining Different Types of Data and Comparing Their Relationships

The following walks you through on how to use the UTD to obtain plaintext data.

1.  Obtain **typeId** of the UTD based on the file name extension **.txt**.
2.  Obtain **typeId** of the UTD based on the MIME type **text/plain**.
3.  Use the **typeId**s obtained to create two UTD instances.
4.  Check whether the two UTD instances are the same.
5.  Check whether a **typeId** belongs to another **typeId**.
6.  Check whether **typeIds1\[0\]** is a lower-level type of **typeIds2\[0\]**.
7.  Check whether **typeIds1\[0\]** is a higher-level type of **typeIds2\[0\]**.
8.  Destroy the pointers created.

// 1. Obtain typeId of the UTD based on the file name extension .txt.
unsigned int typeIds1Count = 0;
const char \*\*typeIds1 = OH\_Utd\_GetTypesByFilenameExtension(".txt", &typeIds1Count);
OH\_LOG\_INFO(LOG\_APP, "the count of typeIds1 is %{public}u", typeIds1Count);
// 2. Obtain typeId based on the MIME type.
unsigned int typeIds2Count = 0;
const char \*\*typeIds2 = OH\_Utd\_GetTypesByMimeType("text/plain", &typeIds2Count);
OH\_LOG\_INFO(LOG\_APP, "the count of typeIds2 is %{public}u", typeIds2Count);
// 3. Use the typeIds obtained to create two UTD instances.
OH\_Utd \*utd1 = OH\_Utd\_Create(typeIds1\[0\]);
OH\_Utd \*utd2 = OH\_Utd\_Create(typeIds2\[0\]);
// 4. Check whether the two UTD instances are the same.
bool isEquals = OH\_Utd\_Equals(utd1, utd2);
if (isEquals) {
    OH\_LOG\_INFO(LOG\_APP, "utd1 == utd2");
} else {
    OH\_LOG\_INFO(LOG\_APP, "utd1 != utd2");
}
// 5. Check whether a typeId belongs to another typeId.
bool isBelongsTo = OH\_Utd\_BelongsTo(typeIds1\[0\], typeIds2\[0\]);
if (isBelongsTo) {
    OH\_LOG\_INFO(LOG\_APP, "typeIds1\[0\] belongs to typeIds2\[0\]");
} else {
    OH\_LOG\_INFO(LOG\_APP, "typeIds1\[0\] doesn't belong to typeIds2\[0\]");
}
// 6. Check whether typeIds1\[0\] is a lower-level type of typeIds2\[0\].
bool isLower = OH\_Utd\_IsLower(typeIds1\[0\], typeIds2\[0\]);
if (isLower) {
    OH\_LOG\_INFO(LOG\_APP, "typeIds1\[0\] is lower typeIds2\[0\]");
} else {
    OH\_LOG\_INFO(LOG\_APP, "typeIds1\[0\] is not lower typeIds2\[0\]");
}
// 7. Check whether typeIds1\[0\] is a higher-level type of typeIds2\[0\].
bool isHigher = OH\_Utd\_IsHigher(typeIds1\[0\], typeIds2\[0\]);
if (isHigher) {
    OH\_LOG\_INFO(LOG\_APP, "typeIds1\[0\] is higher typeIds2\[0\]");
} else {
    OH\_LOG\_INFO(LOG\_APP, "typeIds1\[0\] is not higher typeIds2\[0\]");
}
// 8. Destroy the pointers obtained by OH\_Utd\_GetTypesByFilenameExtension and OH\_Utd\_GetTypesByMimeType and the UTD pointers.
OH\_Utd\_DestroyStringList(typeIds1, typeIds1Count);
OH\_Utd\_DestroyStringList(typeIds2, typeIds2Count);
OH\_Utd\_Destroy(utd1);
OH\_Utd\_Destroy(utd2);
