# Sample Server Development

#### How to Develop

1.  Generate an SSL certificate.
    
    Generate the **serverKey.pem** and **serverCert.cer** files for SSL communication of the sample server.
    
    openssl req -newkey rsa:2048 -nodes -keyout serverKey.pem -x509 -days 365 -out serverCert.cer -subj "/C=CN/ST=GD/L=GZ/O=abc/OU=defg/CN=hijk/emailAddress=test.com"
    
2.  Modify the **bundle.json** file.
    
    Add **sub\_component** to the **build** field.
    
    "sub\_component": \[
        "//base/update/updateservice/server\_sample:testserver",
        ...
    \],
    
3.  Create a code directory.
    
    Go to the **update\_updateservice** directory and run the following commands to create a code directory:
    
    mkdir server\_sample                            // Create the server\_sample folder.
    touch server\_sample/BUILD.gn                   // Create the BUILD.gn file.
    mkdir server\_sample/include                    // Create the include folder to store the header file of the sample server.
    touch server\_process.h                         // Create the server\_process.h header file.
    mkdir server\_sample/src                        // Create the src folder to store the C/C++ files of the sample server.
    touch server\_sample/src/server\_process.c       // Create the server\_process.c file.
    touch server\_sample/src/main.cpp               // Create the main.cpp file.
    
4.  Write the **BUILD.gn** file.
    
    The **BUILD.gn** file contains two **ohos** components: **ohos\_shared\_library** file named **libserver\_process.z.so** and **ohos\_executable** file named **testserver**.
    
    import("//build/ohos.gni")
    
    ohos\_shared\_library("server\_process") {
        sources = \[
            "//base/update/updateservice/server\_sample/src/server\_process.c",
        \]
    
        include\_dirs = \[
            "//base/update/updateservice/server\_sample/include",
            "//third\_party/openssl/include",
        \]
    
        deps = \[
            "//base/update/updater/services/log:libupdaterlog",
            "//third\_party/bounds\_checking\_function:libsec\_static",
            "//third\_party/openssl:crypto\_source",
            "//third\_party/openssl:ssl\_source",
            "//utils/native/base:utils",
        \]
    
        part\_name = "update\_service"
    }
    
    ohos\_executable("testserver") {
        sources = \[
            "//base/update/updateservice/server\_sample/src/main.cpp",
        \]
    
        include\_dirs = \[
            "//base/update/updateservice/server\_sample/include",
        \]
    
        deps = \[
            "//base/update/updateservice/server\_sample:server\_process",
        \]
    
        part\_name = "update\_service"
    }
    
5.  Write the **server\_process.h** file.
    
    Declare the sample server APIs in the **server\_process.h** file.
    
    #ifndef \_\_SERVER\_PROCESS\_H\_\_
    #define \_\_SERVER\_PROCESS\_H\_\_
    
    /\*
    Init: creates a socket environment and presets certain attributes.
    \*/
    int Init();
    
    /\*
    SetParam: sets all plug-in parameters.
    \*/
    int SetParam(const char \*key, const char \*value);
    
    /\*
    GetParam: obtains all plug-in parameters.
    \*/
    int GetParam(const char \*key, char \*value);
    
    /\*
    ReverseSetParamCallback: callback.
    \*/
    int ReverseSetParamCallback(int(\*setParam)(const char \*key, const char \*value));
    
    /\*
    Open: starts the service.
    \*/
    int Open();
    
    /\*
    MainLoop: invoked every 100 ms.
    \*/
    int MainLoop();
    
    /\*
    Close: stops the service and releases related resources.
    \*/
    int Close();
    
    #endif //\_\_SERVER\_PROCESS\_H\_\_
    
6.  Write the **server\_process.c** and **main.cpp** files.
    
    In the **server\_process.c** file, mainly declare **respondContent**, the format of the response message returned by the server. Write the **main.cpp** file based on instructions for the common SSL protocol server. Be sure to include related header files and load the **serverKey.pem** and **serverCert.cer** files.
    
    #include "server\_process.h"
    
    #include <netinet/in.h>
    #include <sys/types.h>
    #include <sys/socket.h>
    #include <arpa/inet.h>
    #include <unistd.h>
    #include <stdlib.h>
    #include <string.h>
    #include <stdio.h>
    
    #include "openssl/err.h"
    #include "openssl/ssl.h"
    
    #define SERVER\_PEM "/data/sdcard/serverKey.pem"  // Use an absolute path.
    #define SERVER\_CER "/data/sdcard/serverCert.cer" // Use an absolute path.
    
    #define LOG\_PRINT(fmt, ...) printf("\[ServerProcess\]\[%s:%d\] " fmt "\\n", \_\_func\_\_, \_\_LINE\_\_, ##\_\_VA\_ARGS\_\_)
    #define DO\_CHECK(cond, log, ...) \\
        if (!(cond)) {\\
            LOG\_PRINT(log);\\
            \_\_VA\_ARGS\_\_;\\
            return -1;\\
        }
    
    // Implement the function by referring to the APIs in the server\_process.h file. Pay attention to the format of the response message from the server.
    respondContent = "{"
        "\\"searchStatus\\": 0,"
        "\\"errMsg\\": \\"success\\","
        "\\"checkResults\\": \[{"
            "\\"versionName\\": \\"sampleVersionName\\","
             "\\"versionCode\\": \\"sampleVersionCode\\","
            "\\"verifyInfo\\": \\"sampleVerifyInfoSha256Value\\","
            "\\"size\\": 1234567,"
            "\\"packageType\\": 1,"
            "\\"descriptPackageId\\": \\"abcdefg1234567ABCDEFG\\","
        "}\],"
        "\\"descriptInfo\\": \[{"
            "\\"descriptionType\\": 0,"
            "\\"content\\": \\"This package message is used for sampleContent\\""
        "}\]"
    "}";
    
7.  Start building.
    
    The **testserver** and **libserver\_process.z.so** files are added to the build output directory.
    
8.  Develop an update package.
    
    For details, see the [update\_packaging\_tools](https://gitcode.com/openharmony/update_packaging_tools) repository.
    
9.  Start the package search server.
    
    Create a directory that contains only English characters on the development board. Place the **testserver**, **libserver\_process.z.so**, **serverCert.cer**, and **serverKey.pem** files in the directory, go to the directory, and run the following command to start the package search server:
    
    ./testserver ./libserver\_process.z.so &
