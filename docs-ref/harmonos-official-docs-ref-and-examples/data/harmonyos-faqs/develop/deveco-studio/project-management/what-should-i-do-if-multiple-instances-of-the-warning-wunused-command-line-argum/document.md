# What should I do if multiple instances of the warning "-Wunused-command-line-argument" in the project, which affect the viewing of valid logs?

**Symptom**

clang: warning: argument unused during compilation: '–gcc-toolchain=C:/Users/username/AppData/Local/Huawei/Sdk/openharmony/9/native/llvm' \[-Wunused-command-line-argument\];

The clang compiler in API version 9 reports a warning for each file compiled. Though the warnings can be suppressed with the **\-Wno-unused-command-line-argument** option, manually adding the option can be troublesome if there are many files in the project.

**Solution**

The warnings are triggered by the **\-Werror** and **\-Wunused-command-line-argument** options in clang. They are likely caused by unsupported variable syntax in the code. To disable this specific type of warning, add the **\-Wno-unused-command-line-argument** option to your configuration, or upgrade the SDK to API version 11.
