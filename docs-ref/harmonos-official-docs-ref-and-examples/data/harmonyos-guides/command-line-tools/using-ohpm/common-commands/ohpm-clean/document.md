# ohpm clean

Cleans directories and files generated during ohpm installation for all modules in the project.

Since ohpm 6.0.2.636, the **log\_level** and **debug** parameters can be appended to the command to obtain the log level and specify the log level for the current command execution.

#### Command Format

ohpm clean|cls 

#### Description

This command cleans the **oh\_modules** directory, the **oh-package-lock.json5** file, and the **oh-package-targetName-lock.json5** file (generated during installation with the **\--target\_path** option) of all modules in the project. Upon completion, it prints the elapsed time to the console.

#### Options

## keep-lockfile

-   Default value: **false**
-   Value type: boolean
-   Alias: kl

You can append the **\--kl** or **\--keep-lockfile** parameter to the **ohpm clean** command. This ensures that the **oh-package-lock.json5** and **oh-package-targetName-lock.json5** files (generated during installation with the **\--target\_path** option) are retained during the cleanup.

## log\_level

-   Default value: none
-   Value type: string

You can append the **\--log\_level <string>** parameter to the **ohpm clean** command to specify the log level (**info**, **debug**, **warn**, or **error**) for the execution of the current command. If this parameter is not specified, the **log\_level** setting in the .ohpmrc file is applied.

## debug

-   Default value: false
-   Value type: boolean

You can append the **\--debug** parameter to the command to set the log level to **debug** for the execution of the current command. This configuration takes effect only on the current command line and does not alter the log level configured in the .ohpmrc file. If this parameter is not specified, the **log\_level** setting in the .ohpmrc file is applied.

#### Notes

-   The **ohpm clean** command clears only the root directory of the project and the modules configured under **modules** in the **build-profile.json5** file.
-   If the **build-profile.json5** file does not exist, the directory where the **oh-package.json5** file is located is the root directory of the project.

#### Example

The current project is **test**, and the submodule is **testModule1**. The project structure is as follows:

test 
|————testModule1   
     |————libs   
     |————oh-package.json5 
|————build-profile.json5 
|————oh-package.json5  

Run the following command in any subdirectory (**libs**, for example) of the current project:

ohpm clean 

Below is an output example:

D:\\test\\testModule1\\libs>ohpm clean 
ohpm DEBUG: startClean. 
ohpm DEBUG: clean all modules under: D:\\test 
ohpm DEBUG: begin to clean module: D:\\test\\testModule1 
ohpm DEBUG: begin to clean module: D:\\test 
ohpm DEBUG: clean module: D:\\test\\testModule1 succeed. 
ohpm DEBUG: clean module: D:\\test succeed. 
clean completed in 0s 67ms
