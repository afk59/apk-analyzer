# ohpm config

Sets user-level configuration items of ohpm.

Since ohpm 6.0.2.636, the **log\_level** and **debug** parameters can be appended to the command to obtain the log level and specify the log level for the current command execution.

#### Command Format

ohpm config set <key> <value>
ohpm config get <key>
ohpm config delete <key>
ohpm config list
ohpm config encrypt \[options\]

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/mwYBYDT_Sm-4iI88-tnaRQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1A5C53B96C8F1AD78F4850A7487C7AF70F65C583F9E83ACFDD31DA000E825F30)

Information in the configuration file is in the format of <key> = <value>.

#### Description

ohpm obtains its configuration settings from the command line and the .ohpmrc file. For more information about the .ohpmrc file and available configuration items, see [ohpmrc](../../ohpmrc/document.md).

**ohpm config** is used to configure only default fields, and only the .ohpmrc file in the user-level directory can be modified. For details about the default fields, see [ohpmrc](../../ohpmrc/document.md#en-us_topic_0000001792216397_%E9%BB%98%E8%AE%A4%E9%85%8D%E7%BD%AE%E9%A1%B9).

#### Subcommands

## set

ohpm config set <key> <value>

Writes data in the format of <key> = <value> to the .ohpmrc file in the user-level directory.

**Example**

1.  The following uses **log\_level** as an example to describe how to change the value to **debug** (options: **debug**, **info**, **warn**, and **error**).
    
    ohpm config set log\_level debug
    
2.  After the command is executed successfully, **log\_level=debug** is displayed in the **/.ohpm/.ohpmrc** file in the user directory.

## get

ohpm config get <key>

Outputs, in standard mode, values obtained from the command line, project-level .ohpmrc file, and user-level .ohpmrc file (in descending order of priority).

If no key value is provided, the execution result of this command is the same as that of the **ohpm config list** command.

**Example 1**

1.  Assume that **log\_level** is set to **info** in the project-level **.ohpmrc** file and set to **debug** in the user-level **.ohpmrc** file. Run the following command in any directory of the project:
    
    ohpm config get log\_level
    
2.  After the command is executed successfully, the value of **log\_level** is printed on the console.
    
    info
    

**Example 2**

1.  After completing steps in Example 1, delete the project-level **.ohpmrc** file and run the **get** command again.
    
    ohpm config get log\_level
    
2.  After the command is executed successfully, the value of **log\_level** is printed on the console.
    
    debug
    

**Example 3**

1.  Run the **ohpm config get** command without the **<key>** value.
    
    ohpm config get
    
2.  After the command is executed successfully, the .ohpmrc configurations are printed on the console.
    
    ; "user" config from C:\\Users\\username\\.ohpm\\.ohpmrc
    
    registry="http://localhost:8088/repos/ohpm"
    strict\_ssl = false
    log\_level = "debug"
    
    ; "user" config from C:\\Users\\username\\.ohpm\\.ohpmrc
    ; node bin location = C:\\Program Files\\nodejs\\node.exe
    ; node version = v18.19.1
    ; ohpm local prefix = C:\\Users\\username
    ; ohpm version = 5.1.2-rc.2
    ; cwd = C:\\Users\\username
    ; HOME = C:\\Users\\username
    

## list

ohpm config list
alias: ls

Shows the list of configuration items.

**Example**

1.  Run the **list** command.
    
    ohpm config list or ohpm config ls
    
2.  After the command is executed successfully, the .ohpmrc configurations are printed on the console.
    
    ; "user" config from C:\\Users\\username\\.ohpm\\.ohpmrc
    
    registry="http://localhost:8088/repos/ohpm"
    strict\_ssl = false
    log\_level = "debug"
    
    ; "user" config from C:\\Users\\username\\.ohpm\\.ohpmrc
    ; node bin location = C:\\Program Files\\nodejs\\node.exe
    ; node version = v18.19.1
    ; ohpm local prefix = C:\\Users\\username
    ; ohpm version = 5.1.2-rc.2
    ; cwd = C:\\Users\\username
    ; HOME = C:\\Users\\username
    

## delete

ohpm config delete <key>

Deletes the specified key from the **.ohpmrc** file in the user-level directory.

**Example**

1.  Obtain the original content in the user-level **.ohpmrc** file.
    
    registry=http://localhost:8088/repos/ohpm
    strict\_ssl=false
    log\_level=debug
    
2.  Run the **delete** command.
    
    ohpm config delete registry
    
3.  After the command is executed successfully, the **.ohpmrc** file contains the following content:
    
    strict\_ssl=false
    log\_level=debug
    

## encrypt

ohpm config encrypt \[options\]

Encrypts the data from the standard input using the encryption component and outputs the ciphertext to the standard output.

**First-time usage**

-   You must append [\--crypto\_path <string>](#section313318216424) to the end of the **config encrypt** command to generate an encryption component for data encryption.
    
    **Example**
    
    1.  Run the **encrypt --crypto\_path <string>** command, where the specified path is an empty directory.
        
        ohpm config encrypt --crypto\_path D:\\path\\to\\empty\_dir
        
    2.  After the command is executed successfully, an encryption component is generated in the specified path to encrypt user input, which is invisible during entry.
        
        ohpm INFO: Attempted to create an crypto component at the "D:\\path\\to\\empty\_dir" path...
        ohpm INFO: The crypto component has been created successfully.
        Please enter the password to be encrypted:
        ohpm INFO: encrypted result:
        security:01:61AE9D3219664B7B785XXXXX:201f713d625daddafcb12198ea9d5121xxxxxx
        
    3.  Configure the generated encryption component path in the **.ohpmrc** file so that the encryption component can be automatically read.
        
        crypto\_path=D:\\path\\to\\empty\_dir
        

**Non-first-time usage**

-   If [\--crypto\_path](#section313318216424) is not specified, the configuration is automatically read from the **.ohpmrc** file (priority: project-level **.ohpmrc** > user-level **.ohpmrc**). The configured path must exist and contain valid encryption components.
-   If an error message is displayed indicating that the encryption component is incorrect, run the **ohpm config encrypt --crypto\_path <string>** command again.
-   **Example**
    
    1.  Run the **encrypt** command.
        
        ohpm config encrypt
        
    2.  After successful execution, encrypt user input, which is invisible during entry.
        
        Please enter the password to be encrypted:
        ohpm INFO: encrypted result:
        security:01:61AE9D3219664B7B785XXXXX:201f713d625daddafcb12198ea9d5121xxxxxx
        

**Ciphertext usage**

The generated ciphertext can be configured in the project-level or user-level **.ohpmrc** file, which is used for [sensitive configuration items](../../ohpmrc/document.md#section18322038185010).

#### Options

## json

-   Default value: false
-   Value type: boolean
-   Alias: j

You can configure the **\-j** or **\--json** parameter at the end of the **config list** command to output all configuration items and default values in JSON format.

// Example
// 1. Run the list command and output the result in JSON format.
ohpm config list -j or ohpm config list --json
// 2. Check the command execution result.
{
  "registry": "http://localhost:8088/repos/ohpm", 
  "strict\_ssl": false,
  "log\_level": "info",
  ......
}

## crypto\_path

-   Default value: none
-   Value type: string

Specifies the path of the encryption component for data encryption. The following describes different situations of the specified path:

1.  If the specified path does not exist, the directory is automatically created and an encryption component is generated.
2.  If the specified path is an empty directory, the encryption component is automatically generated in the directory.
3.  If the specified path already has an encryption component, the existing encryption component will be used.

// Example 1
// 1. Run the encrypt --crypto\_path <string> command, where the specified path is an empty directory.
ohpm config encrypt --crypto\_path D:\\path\\to\\empty\_dir
// 2. After the command is executed successfully, an encryption component is generated in the specified path to encrypt user input, which is invisible during entry.
ohpm INFO: Attempted to create an crypto component at the "D:\\path\\to\\empty\_dir" path...
ohpm INFO: The crypto component has been created successfully.
Please enter the password to be encrypted:
ohpm INFO: encrypted result:
security:01:61AE9D3219664B7B785XXXXX:201f713d625daddafcb12198ea9d5121xxxxxx

// Example 2
// 1. Run encrypt --crypto\_path <string> with the specified path set to an encryption component.
ohpm config encrypt --crypto\_path D:\\path\\to\\crypto\_dir
// 2. After successful execution, encrypt user input, which is invisible during entry.
Please enter the password to be encrypted:
ohpm INFO: encrypted result:
security:01:61AE9D3219664B7B785XXXXX:201f713d625daddafcb12198ea9d5121xxxxxx

## log\_level

-   Default value: none
-   Value type: string

You can append the **\--log\_level <string>** parameter to the command to specify the log level (**info**, **debug**, **warn**, or **error**) for the execution of the current command. If this parameter is not specified, the **log\_level** setting in the .ohpmrc file is applied.

## debug

-   Default value: false
-   Value type: boolean

You can append the **\--debug** parameter to the command to set the log level to **debug** for the execution of the current command. This configuration takes effect only on the current command line and does not alter the log level configured in the .ohpmrc file. If this parameter is not specified, the **log\_level** setting in the .ohpmrc file is applied.
