# How do I use OH\_JSVM\_GetValueStringUtf8 to obtain a string?

**Question**

1.  The size of the buffer passed in **OH\_JSVM\_GetValueStringUtf8** is uncertain.
2.  Using OH\_JSVM\_GetValueStringUtf8 to obtain an overlong string may cause a crash.

**Solution**

The third parameter of **OH\_JSVM\_GetValueStringUtf8** is the memory address to which the string is written. If a null pointer is passed in, the interface returns the length of the string (excluding the terminator) through the last parameter result.

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetValueStringUtf8(JSVM\_Env env,
                                                   JSVM\_Value value,
                                                   char\* buf,
                                                   size\_t bufsize,
                                                   size\_t\* result);

To obtain a string, perform the following steps:

1.  Call **OH\_JSVM\_GetValueStringUtf8** to obtain the length of the string.
2.  Request memory for the buffer.
3.  Call **OH\_JSVM\_GetValueStringUtf8** to obtain the string.
    
    std::string GetValueString(JSVM\_Env env, JSVM\_Value value) {
        constexpr size\_t PREALLOC\_SIZE = 256;
        char preallocMemory\[PREALLOC\_SIZE\];
    
    
        char \*buff = preallocMemory;
        
        // Obtain length
        size\_t totalLen = 0;
        OH\_JSVM\_GetValueStringUtf8(env, value, nullptr, 0, &totalLen);
        size\_t needed = totalLen + 1;
    
    
        if (needed > PREALLOC\_SIZE) {
            // Allocate space, size must include termination character
            buff = new char\[needed\];
        }
        // get string
        OH\_JSVM\_GetValueStringUtf8(env, value, buff, needed, nullptr);
    
    
        std::string ret(buff, totalLen);
    
    
        if (needed > PREALLOC\_SIZE) {
            delete\[\] buff;
        }
        return ret;
    }
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/NAb0MY08SwGiZyVx7wrGJw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062547Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=770F39FEF0D0D2BFF0820A4A09BC018493954920345D7415BDC4D0C68A6875B4)

1.  The allocated buffer size must be greater than the string length because the string length does not contain the last termination character. If the buffer size is equal to the string length, the last character of the string will be overwritten by the termination character.
2.  You are advised not to allocate space using **char buff\[totalLen + 1\]** on the stack. If the string is too long, stack overflow may occur, causing application breakdown.
