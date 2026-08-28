# What should I do if an include <stddef.h> error is reported during compilation?

**Symptom**

An error is reported during compilation when the C code contains **<stddef.h>**:

lib/clang/15.0.4/include/stddef. h:74:24: error: typedef redefinition with different types ('unsigned short" vs 'unsigned int")typedef_WCHAR\_TYPE_ \_ wchar\_t;… 10/native/sysroot/us/include/aarch64-linux-ohos/bits/alltypes.h:15:18: note: previous definition is here typedef unsigned wchar\_t.

**Solution**

Delete the **\-fshort-wchar** parameter from **TARGET\_COMPILE\_OPTIONS** in the **CMakeLists.txt** file.
