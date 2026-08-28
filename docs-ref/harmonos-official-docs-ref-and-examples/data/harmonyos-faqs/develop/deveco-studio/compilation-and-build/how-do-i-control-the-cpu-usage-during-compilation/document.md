# How do I control the CPU usage during compilation?

Add the following configuration to **buildOption.arguments** in the module-level **build-profile.json5** file to specify the CMake build arguments. The sample code is as follows:

{
  "buildOption": {
    "arguments": \[
      "-DCMAKE\_BUILD\_PARALLEL\_LEVEL=2",
      "-DCMAKE\_LINK\_PARALLEL\_LEVEL=2"
    \]
  }
}

This configuration specifies that two processors are used for build and linking, respectively.

"buildOption": {
  "externalNativeOptions": {
    "path": "../cpp/CMakeLists.txt",
    "arguments": "-DCMAKE\_JOB\_POOL\_COMPILE:STRING=compile -DCMAKE\_JOB\_POOL\_LINK:STRING=link -DCMAKE\_JOB\_POOLS:STRING=compile=2;link=2",
    "cppFlags": "",
    "abiFilters": \[
      "x86\_64",
      "arm64-v8a"
    \]
  }
},
