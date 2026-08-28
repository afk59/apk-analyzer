# What should I do if uint8\_t in the .h file cannot be used?

**Solution**

1.  Modify the import header file in C++ as follows:
    
    #ifdef \_\_cplusplus
    extern "C" {
    #endif
    #include "MGDolphinTOTP.h"
    #include "MGDolphinTOTPsha1.h"
    #ifdef \_\_cplusplus}
    #endif
    
2.  Add the .c file to the **CMakeLists.txt** file for compilation.
    
    add\_library(entry SHARED hello.cpp NapiTest.cpp MGDolphinTOTP.c MGDolphinTOTPSha1.c)
