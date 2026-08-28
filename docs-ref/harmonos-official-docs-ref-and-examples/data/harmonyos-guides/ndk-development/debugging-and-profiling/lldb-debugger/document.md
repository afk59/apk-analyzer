# LLDB Debugger

#### Overview

Low Level Debugger (LLDB) is a next-generation, high-performance debugger. It supports breakpoint setting, variable viewing and modification, memory operations, thread control, expression calculation, and stack backtracking, featuring cross-platform support and plugin extension.

Developed on [llvm15.0.4](https://github.com/llvm/llvm-project/releases/tag/llvmorg-15.0.4), LLDB is the default debugger in HUAWEI DevEco Studio for debugging C and C++ applications.

For details, see the [LLDB documentation](https://lldb.llvm.org/).

#### Features

LLDB has the following features:

-   **Powerful debugging capabilities**: include breakpoint setting, variable viewing and modification, memory operations, thread control, expression calculation, and stack backtracking.
-   **Cross-platform support**: applicable to Windows, Linux x86\_64, OHOS, and macOS.
-   **Plugin extension**: allows for plugin customization to fit specific needs.

#### How to Obtain

-   Install HUAWEI DevEco Studio, and obtain LLDB from its SDK components.
-   The following shows the path of LLDB in Huawei DevEco Studio (on Windows).
    
    DevEco\_Studio\_Home/
    └── sdk/
        ├── default/
        │   ├── openharmony/
        │   │   └── native/
        │   │       └── llvm/
        │   │           ├── bin/
        │   │           │   └── lldb.exe                 # Main program on the Windows client
        │   │           └── lib/
        │   │               └── clang/
        │   │                   └── current/
        │   │                       └── bin/
        │   │                           ├── aarch64-linux-ohos/
        │   │                           │   └── lldb      # Independent ARM64 debugger
        │   │                           └── arm-linux-ohos/
        │   │                               └── lldb      # Independent ARM32 debugger
        │   └── hms/
        │       └── native/
        │           └── lldb/
        │               ├── aarch64-linux-ohos/
        │               │   └── lldb-server              # ARM64 debugging server
        │               ├── arm-linux-ohos/
        │               │   └── lldb-server              # ARM32 debugging server
        │               └── x86\_64-linux-ohos/
        │                   └── lldb-server              # x86\_64 emulator debugging server
    
-   Path of the execution file of the LLDB client (on Windows):
    
    <DevEco\_Studio\_Home>\\sdk\\default\\openharmony\\native\\llvm\\bin\\lldb.exe
    
-   Static lldb
    
    **Table 1** Directories
    | 
    Path
    
     | 
    
    Description
    
     |
    | :-: | :-: |
    | 
    
    \\DevEco Studio\\sdk\\default\\openharmony\\native\\llvm\\lib\\clang\\current\\bin\\aarch64-linux-ohos\\lldb
    
     | 
    
    Static lldb for the aarch64-linux-ohos architecture
    
     |
    | 
    
    \\DevEco Studio\\sdk\\default\\openharmony\\native\\llvm\\lib\\clang\\current\\bin\\arm-linux-ohos\\lldb
    
     | 
    
    Static lldb for the arm-linux-ohos architecture
    
     |
    
-   lldb-server
    
    **Table 2** Directories
    | 
    Path
    
     | 
    
    Description
    
     |
    | :-: | :-: |
    | 
    
    \\DevEco Studio\\sdk\\default\\hms\\native\\lldb\\aarch64-linux-ohos\\lldb-server
    
     | 
    
    lldb-server for the aarch64-linux-ohos architecture
    
     |
    | 
    
    \\DevEco Studio\\sdk\\default\\hms\\native\\lldb\\arm-linux-ohos\\lldb-server
    
     | 
    
    lldb-server for the arm-linux-ohos architecture
    
     |
    | 
    
    \\DevEco Studio\\sdk\\default\\hms\\native\\lldb\\x86\_64-linux-ohos\\lldb-server
    
     | 
    
    lldb-server for the x86\_64-linux-ohos architecture
    
     |
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/-dEfwzH9TZKPGANJcWWYKQ/notice_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062135Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=69C35E3DFA0883DBC1D5B7ECCCD5ACC43D47D28824194F2A6F625224839A3BBD)

Signature verification mechanism:

At runtime, lldb-server verifies its digital signature. Only lldb-servers signed by Huawei can be used to debug applications.

lldb-server in [Table 2](#table15380916136) are signed in closed-source mode.

This design is used to protect HarmonyOS debugging permissions and prevent unauthorized debugging.

#### Functionalities

The following lists some LLDB functionalities. For more functionalities and related commands, see [LLDB Usage Guide](https://gitee.com/openharmony/third_party_llvm-project/blob/master/lldb/README.md) and [LLDB official manual](https://lldb.llvm.org/use/map.html#). LLDB may vary by platform, such as Windows, Linux x86\_64, and macOS.

-   Logging
    
    \# Log the complete debugging session to a file.
    (lldb) log enable -F -T -p -f d:\\lldb.log lldb all
    (lldb) log enable -F -T -p -f d:\\lldbgdbremote.log gdb-remote all
    # Example: Log only breakpoint events.
    (lldb) log enable -f /tmp/breakpoints.log lldb break
    # View the current log configuration.
    (lldb) log list
    
-   Breakpoint management
    
    \# Set a function breakpoint (fuzzy match is supported).
    (lldb) breakpoint -f main.cpp -l 266
    # Set a conditional breakpoint (triggered when x is greater than 100).
    (lldb) breakpoint set -f main.cpp -l 20 -c '(x > 100)'
    # List all breakpoints.
    (lldb) breakpoint list
    # Temporarily disable a breakpoint.
    (lldb) breakpoint disable 1
    
-   Watchpoint management
    
    \# Watch for variable changes.
    (lldb) watchpoint set variable global\_var
    # Watch for memory address changes.
    (lldb) watchpoint set expression -w write -- 0x7ffeefbff5d8
    # Obtain the watchpoint list.
    (lldb) watchpoint list
    
-   Expression processing
    
    \# Create variables.
    (lldb) print int $value1 = 7
    (lldb) expression int $value2 = 7
    # Print variable values.
    (lldb) print $value1
    (lldb) expression $value2
    # Calculate a variable.
    (lldb) expression $value1 \* 3
    # Print the value in hexadecimal.
    (lldb) p/x 12345
    
-   Viewing variables
    
    \# View initialized local variables of the current frame.
    (lldb) frame variable
    # View global variables and static variables.
    (lldb) frame variable -g
    # View registers.
    (lldb) register read
    
-   Process/Thread management
    
    \# Display the backtraces of all threads.
    (lldb) thread backtrace all
    # Step over.
    (lldb) thread step-over (or next)
    # Step out of the selected frame.
    (lldb) thread step-out (or finish)
    
-   Assembly processing
    
    \# View registers.
    (lldb) register read
    # Modify the PC register.
    (lldb) register write pc \`$pc+8\`
    # View the assembly instruction of the current stack frame.
    (lldb) disassemble --frame (or dis -f)
    # View the assembly instruction of the main function.
    (lldb) disassemble -name main
    # Execute instructions at the assembly level and step over the function body.
    (lldb) nexti
    # Execute instructions at the assembly level and step into the function body.
    (lldb) stepi
    
-   Signal processing
    
    \# Print the backtrace when capturing a signal.
    (lldb) process handle SIGSEGV -s true
    # View the current signal processing configuration.
    (lldb) process handle
    
-   Attaching to a process
    
    \# Attach to a PID (debugging permission required).
    (lldb) process attach -p 1234
    

#### Environment Setup

-   Local debugging (**limited mode**)
    
    -   Obtain the root permissions for the HarmonyOS device.
    -   Debug directly on the device. There is no need to use DevEco Studio.
    
    -   Select the path of static lldb based on the CPU architecture (refer to [Table 1](#table187851036494)) and use hdc to transfer the path to the device.
        
        hdc file send \\DevEco Studio\\sdk\\default\\openharmony\\native\\llvm\\lib\\clang\\current\\bin\\aarch64-linux-ohos\\lldb /data/local/tmp/debugserver
        
    -   Select the path of lldb-server based on the CPU architecture (refer to [Table 2](#table15380916136)) and use hdc to transfer the path to the device.
        
        hdc file send \\DevEco Studio\\sdk\\default\\hms\\native\\lldb\\aarch64-linux-ohos\\lldb-server /data/local/tmp/debugserver
        

-   Remote debugging (**primary mode**)
    
    -   One-click debugging:
        -   Install HUAWEI DevEco Studio and perform debugging by referring to [Debugging in DevEco Studio](../overview/document.md).
        -   You can connect a Windows or macOS computer to a HarmonyOS device or Emulator to debug native C++ applications.
        -   Debug directly on DevEco Studio without pushing lldb or lldb-server.
    -   Manual debugging:
        -   To manually perform remote debugging (without using DevEco Studio), for example, to debug binary files, ensure that the device has LLDB server and the PC has LLDB.
        -   Push lldb-server to the device. You are advised to use DevEco Studio to push lldb-server. For manual push, select the path of lldb-server based on the CPU architecture (refer to [Table 2](#table15380916136)) and use hdc to transfer the path to the device.
            
            hdc file send \\DevEco Studio\\sdk\\default\\hms\\native\\lldb\\aarch64-linux-ohos\\lldb-server /data/local/tmp/debugserver
            
        -   Install LLDB on the PC (use the **lldb.exe** file on Windows). Then, establish a remote connection between the LLDB and the LLDB server on the OHOS device for debugging.
            
            ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/lecq1dUzTNapBUhGiJ0Xkg/en-us_image_0000002531158756.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062135Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F1E8FFB355F2B390E491DAA2B0A6925B9FF52ED2CBA485D6AB3D79CA7BFEA4AC)
            
    
    -   The following table describes the device status and supported debugging.
        
        | 
        Device Status
        
         | 
        
        Supported Debugging
        
         | 
        
        lldb-server Path
        
         |
        | :-- | :-- | :-- |
        | 
        
        root image + SELinux disabled
        
         | 
        
        All types of C/C++ applications and binary files
        
         | 
        
        Any executable directory
        
         |
        | 
        
        root image + SELinux enabled
        
         | 
        
        All types of C/C++ applications and binary files
        
         | 
        
        /data/local/tmp/debugserver
        
         |
        | 
        
        user image + SELinux enabled
        
         | 
        
        HAP files compiled and signed in debug mode in DevEco Studio
        
         | 
        
        Automatic
        
         |
        

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/KOJg08n9Qay8MyFQ1_yQcg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062135Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=27F22D31DBA8FAFFDC4B017681E398A24EADFCE14358587588ED3CE0B8CED418)

root image: Run the **hdc shell id** command and **uid=0(root)** is displayed. Alternatively, run the **hdc shell** command to enter the interactive command environment and the prompt is **#**.

user image: Run the **hdc shell id** command and **uid=2000(shell)** is displayed. Alternatively, run the **hdc shell** command to enter the interactive command environment and the prompt is **$**.

SELinux enabled: Run the **hdc shell getenforce** command and **Enforcing** is displayed.

SELinux disabled: Run the **hdc shell getenforce** command and **Permissive** is displayed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/hHHwtfbMReG61v6pLGeqQQ/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062135Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6411F4C20AAC0A8D3C7540ACCE883D15E6085F0BCD6D47647D51030D54FD5691)

You are advised to create a native project in DevEco Studio and click the **Debug** button to automatically push the lldb-server. This avoids version compatibility and permission issues.

#### Local Debugging

## Using LLDB to Start and Debug Applications

The following walks you through on how to debug an executable file named **a.out** in HarmonyOS. The file contains debugging information and is generated by the Clang compiler, which is of the same version as LLDB.

Source file: **hello.cpp**

#include <iostream>
using namespace std;
int main() {
    cout << "hello world!" <<endl;
    return 0;
}

Compilation:

<clang distribution>/bin/clang++ --target=aarch64-linux-ohos --sysroot=<sysroot distribution> -g hello.cpp -o a.out

1.  Obtain the executable file **a.out**.
2.  Run the **hdc shell** command to enter the interactive command environment of the mobile phone and access the lldb path.
3.  Run LLDB and specify the file to debug as **a.out**.
    
    ./lldb a.out
    
4.  Set breakpoints at the **main** function in the code.
    
    (lldb) b main
    
5.  Run the application, and it stops at the first breakpoint.
    
    (lldb) run
    
6.  Continue to run the application.
    
    (lldb) continue
    
7.  List all the breakpoints.
    
    (lldb) breakpoint list
    
8.  Show the arguments and local variables of the current frame.
    
    (lldb) frame variable
    
9.  Run debugging commands as required to continue debugging.
10.  Exit debugging.
     
     (lldb) quit
     

## Using LLDB to Debug Running Applications

The following walks you through on how to debug an executable file named **a.out** in the mobile phone. The file contains user input and debugging information and is generated by the Clang compiler.

Source file: **hello.cpp**

#include <iostream>
using namespace std;

int main() {
    int i = 0, j = 5, sum = 0;
    cout << "Please input a number of type int" <<endl;
    cin >> i;
    cout << i;
    sum = i + j;
    cout << sum <<endl;
    return 0;
}

Compilation:

<clang distribution>/bin/clang++ --target=aarch64-linux-ohos --sysroot=<sysroot distribution> -g hello.cpp -o a.out

1.  Run the **hdc shell** command to enter the interactive command environment of the mobile phone and access the lldb path.
2.  Start the application on CLI 1. (The message "Please input a number of type int" is displayed.)
    
    ./a.out
    
3.  Run LLDB on CLI 2.
    
    ./lldb
    
4.  Attach to the application.
    
    (lldb) process attach --name a.out
    
5.  Set a breakpoint in line 10 of **hello.cpp**.
    
    (lldb) breakpoint set --file hello.cpp --line 10
    
6.  Enter an integer on CLI 1.
    
    88
    
7.  Continue to run the application on CLI 2. The application stops at the breakpoint.
    
    (lldb) continue
    
8.  Run debugging commands as required to continue debugging.
9.  Detach from the application.
    
    (lldb) detach
    
10.  Exit debugging.
     
     (lldb) quit
     

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/6ecl1k97ReqR6TWw7Woi5g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062135Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6FEC3DF5F94669B3FF9FC7C6DC04C4BB2909929DC4E6DA96564534B4D85A3EFD)

You can either [attach to the application](#li185118185491) first and then [set a breakpoint](#li15852111874920), or do it the other way around.

#### Remote Debugging

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/jMLFdn8zQLe35wT-5xPKsA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062135Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3F2AB4F47745F85653C81BE561BAC3B792585C9E4780A8EA89F811EBB29FA05F)

-   Remote debugging refers to cross-device debugging using LLDB. The following describes how to debug applications on HarmonyOS devices across devices.
-   For details about remote debugging based on HUAWEI DevEco Studio, see [Starting Debugging](https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/ide-debug-native-enable-V5).
-   During remote debugging, LLDB server and LLDB must be used together.
-   The remote debugging procedures for Windows, Linux x86\_64, and macOS are the same.

## Remote Debugging on Root Image

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/9QQjeHQ-Qj-zxlM-yq4pyg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062135Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5CBA4A2B0ED825E58C2DD7455E779DBF4CA29212AD7232534A5D4E621D73CA83)

-   The application or binary file to be debugged must be a native C++ project of the aarch64-linux-ohos architecture.
-   You are advised to disable SELinux during debugging.

Source file: **hello.cpp**

#include <iostream>
using namespace std;
int main() {
    cout << "hello world!" <<endl;
    return 0;
}

Compilation:

<clang distribution>/bin/clang++ --target=aarch64-linux-ohos --sysroot=<sysroot distribution> -g hello.cpp -o a.out

1.  Open CLI 1 and disable SELinux.
    
    hdc shell setenforce 0
    
2.  Open CLI 1 and push lldb-server and **a.out** to the device.
    
    hdc file send lldb-server hdc file send a.out /data/local/tmp/debugserver/debugserver
    hdc shell chmod 755 
    /data/local/tmp/debugserver/lldb-server /data/local/tmp/debugserver/a.out
    
3.  Run LLDB server. (**8080** is a valid port number that is not in use. You can customize it.)
    
    hdc shell /data/local/tmp/debugserver/lldb-server p --server --listen "\*:8080"
    
4.  Open CLI 2 and run the binary file **lldb**.
    
    lldb
    
5.  Select and connect to the remote device on the LLDB CLI.
    
    (lldb) platform select remote-ohos
    (lldb) platform connect connect://localhost:8080 
    
6.  Specify the binary file **a.out** on the device to be debugged.
    
    (lldb) target create /data/local/tmp/debugserver/a.out
    
7.  Set breakpoints at the **main** function in the code.
    
    (lldb) b main
    
8.  Start the application.
    
    (lldb) run
    
9.  Display source code for the current target process.
    
    (lldb) source list
    
10.  Run debugging commands as required to continue debugging.
11.  Exit debugging.
     
     (lldb) quit
     

## Remote Debugging on User Image

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/qJHr-vxJSr-gELV8MrSf0A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062135Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=029DC1ABC9BBFC060679A159E61E440D76A9AB4498386A2D774300ACA70F4848)

-   SELinux is enabled by default for the user image and cannot be disabled.
-   You are advised to use HUAWEI DevEco Studio to debug the HAP file of the HarmonyOS device running a user image.
-   lldb-server must be pushed to the specified directory **/data/local/tmp/debugserver**, for example, **/data/local/tmp/debugserver/lldb-server** or **/data/local/tmp/debugserver/com.example.myapplication/lldb-server**.
-   lldb-server is obtained from the aarch64-linux-ohos architecture directory. For details, see [Table 2 Directories](#table15380916136).
-   In this example, the HAP file is compiled from the native C++ default project created based on HUAWEI DevEco Studio, which contains the debug information.
-   During debugging, ensure that the device is unlocked. The debugger cannot start when the screen is locked.

1.  Open CLI window 1 and push lldb-server and the HAP file to the device.
    
    hdc shell mkdir data/local/tmp/debugserver/com.example.myapplication
    hdc file send lldb-server data/local/tmp/debugserver/com.example.myapplication
    hdc shell chmod 755 data/local/tmp/debugserver/com.example.myapplication/lldb-server
    hdc shell mkdir data/local/tmp/d333e74fe3ab488aad622a7055fbf396
    hdc file send C:\\Users\\xxx\\DevEcoStudioProjects\\MyApplication\\entry\\build\\default\\outputs\\default\\entry-default-signed.hap data/local/tmp/d333e74fe3ab488aad622a7055fbf396
    
2.  Install and run the HAP file, and disable appfreeze.
    
    hdc shell bm install -p data/local/tmp/d333e74fe3ab488aad622a7055fbf396
    hdc shell aa start -a EntryAbility -b com.example.myapplication
    hdc shell aa attach -b com.example.myapplication
    
3.  Run LLDB server.
    
    hdc shell aa process -a EntryAbility -b com.example.myapplication -D "/data/local/tmp/debugserver/com.example.myapplication/lldb-server platform --listen unix-abstract:///lldb-server/platform.sock"
    
4.  Open CLI 2 and run the binary file **lldb**.
    
    lldb
    
5.  Select and connect to the remote device on the LLDB CLI.
    
    (lldb) platform select remote-ohos 
    (lldb) platform connect unix-abstract-connect:///lldb-server/platform.sock
    
6.  Add the search path of the target executable file.
    
    (lldb) settings append target.exec-search-paths "C:\\Users\\xxx\\DevEcoStudioProjects\\MyApplication \\entry\\build\\default\\intermediates\\cmake\\default\\obj\\arm64-v8a"
    
7.  Set a breakpoint at line 6 in the source code.
    
    (lldb) breakpoint set --file "C:/Users/xxx/DevEcoStudioProjects/MyApplication/entry/src/main/cpp/napi\_init.cpp" --line 6
    
8.  Specify the PID of the application corresponding to the HAP file on the device to be debugged.
    
    (lldb) attach <pid>
    
9.  Tap the device application to continue the response. The application stops at the breakpoint.
10.  Continue the debugging.
     
     (lldb) continue
     
11.  Show the stack backtrace for the current thread.
     
     (lldb) bt
     
12.  Run debugging commands as required to continue debugging.
13.  Exit debugging.
     
     (lldb) quit
     

#### FAQ

-   When the **run** command is executed in the LLDB debugging environment, the console returns "error: 'A' packet returned an error: 8" or a similar error code indicating that the debugger cannot create a debugging process. What should I do?
    
    This problem is usually caused by insufficient permissions. You are advised to perform the following steps to locate the fault:
    
    (1) Check whether **Developer options** is enabled on the target device.
    
    If not, enable it and then debug the device.
    
    (2) Check whether the current user has the debugging permission on the target process.
    
    The user can debug applications, but not executable files.
    

-   What should I do if the error message "Permission denied" is displayed when I run the LLDB server?
    
    Typically, this problem occurs because lldb-server lacks executable permissions; you must grant them.
