# What should I do if the error message "Currently module for 'xxx.so' is not verified." is displayed when I use import { export } from 'xxx.so'; to import a .so file in a .ts file?

**Symptom**

When a .so file is imported to a .ts file through **import { export } from 'xxx.so';**, an error message is displayed as follows: "Currently module for 'xxx.so' is not verified. If you're importing napi, its verification will be enabled in later SDK version. Please make sure the corresponding .d.ts file is provided and the napis are correctly declared."

**Possible Causes**

When a .so file is imported through **import { export } from 'xxx.so';**, the compiler does not parse the variables, properties, or methods in the file. As a result, their types are assumed to be **any**, causing the error.

**Solution**

Solution 1: Assert the type for the variables, properties, and methods imported from the .so file.

Solution 2: If the .so file and .ts file exist in the same module, import the .so file using a relative path. For example, if both the .ts file and the index file of the .so file are in the same directory, you can use the import statement **import { export } from './index';**.
