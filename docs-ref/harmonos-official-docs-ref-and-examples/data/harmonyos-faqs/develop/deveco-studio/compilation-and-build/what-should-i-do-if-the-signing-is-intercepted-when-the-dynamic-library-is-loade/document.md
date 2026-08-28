# What should I do if the signing is intercepted when the dynamic library is loaded on macOS?

**Symptom**

On macOS, the following instrumentation configuration is added to the **build-profile.json** file for development in DevEco Studio, but the instrumentation function does not take effect.

"transformLib": "<Dynamic library path relative to the root path of the module, starting with ./>"

**Judgment and Verification**

1.  Go to the directory where es2abc is located in the **sdk** directory: \[DevEco Studio installation directory\]/Contents/sdk/default/openharmony/ets/build-tools/ets-loader/bin/ark/build-mac/bin
2.  Execute the following command:
    
    ./es2abc --merge-abc --transform-lib <Dynamic library path> <Test JS file path>
    
3.  If an error message similar to the following is displayed, the reason may be that es2abc and the dynamic library file do not belong to the same signature group.
    
    os::library\_loader::Load error: dlopen(..., 0x0001): 
    tried: '...' (code signature in <...> '...' not valid for use in process: mapped file has no cdhash, completely unsigned? Code has to be at least ad-hoc signed.)
    
4.  Run the following commands to view the signature group information of es2abc and the dynamic library file. If one file has signature information and the other does not, or if both have signature information but the **TeamIdentifier** property values in the signature information are different, the issue is caused by inconsistent signature groups.
    
    codesign -dv --verbose=1 <es2abc path>
    codesign -dv --verbose=1 <Dynamic library path>
    

**Solution**

Run the following command to replace the signature of the es2abc file with the same user signature as the dynamic library file.

codesign --remove-signature <es2abc path>
codesign -s - -v <es2abc path>
