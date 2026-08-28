# How do I write a temporary file to the user directory in native code?

**Question**

Which directories of an application can the user write temporary files to? Sample code for writing files in native code:

cpp

#include <stdio.h>

void writeTempFile(const char\* path, const char\* content) {

FILE\* file = fopen(path, "w");

if (file != NULL) {

fprintf(file, "%s", content);

fclose(file);

}

}

Directories where temporary files can be written include:

**Cache**: stores cache files.

**files**: stores application data files.

**Answer**

Currently, there is no native API you can use to write files. You can use the APIs of C++ base library to write files based on the sandbox path.

Sample code:

\# include "WriteFile.h" 
# include "napi/native\_api.h" 
# include <fstream> 
napi\_value WriteFile::WriteTemporaryFile(napi\_env env, napi\_callback\_info info) {
    std::ofstream file("data/storage/el2/base/temp/2.txt");
    if (file.is\_open()) {        // Determine if the file can be opened normally
        file << "Hello, World!"; // Write content to a file
        file.close();            // close file
    }
    return nullptr;
}

For details about the directories that can be accessed by users, see [Application Sandbox](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-sandbox-directory).
