# How do I use ohpm to import third- and fourth-party libraries?

-   Method 1:
    1.  Open the **Terminal** window and run the following command to go to the **entry** directory:
        
        cd entry
        
    2.  Run the following command to install a third-party package, for example, **dayjs**:
        
        ohpm install dayjs
        
    3.  Add the following statement in the .js file to import the package:
        
        import dayjs from 'dayjs';
        
-   Method 2:
    1.  Enter the **entry** directory of the project and open the **oh-package.json5** file.
    2.  Write the third-party library to be installed (for example, **dayjs**) in the **oh-package.json5** file.
        
        "dependencies": {
          "dayjs": "^1.10.4",
        } ,
        
    3.  Open the **Terminal** window and run the following command to go to the **entry** directory:
        
        cd entry
        
    4.  Run the following command to install the third-party library:
        
        ohpm install
        
    5.  Add the following statement in the ArkTS file to import the package:
        
        import dayjs from 'dayjs';
