# How do I use the .so file built from another module in a module?

**Question**

To integrate the.so file compiled in module b into module a on the native side, perform the following steps:

1\. Ensure that the .so file in module b has been successfully compiled and the path is correct.

2\. Add the reference to the.so file in module b to the **CMakeLists.txt** of module a.

For example, add the following content to the **CMakeLists.txt** file:

cmake

add\_library(b SHARED IMPORTED)

set\_target\_properties(b PROPERTIES IMPORTED\_LOCATION ${CMAKE\_SOURCE\_DIR}/path/to/b/libb.so)

target\_link\_libraries(a b)

3\. Ensure that the build script of module a can correctly find and link the .so file of module b.

After the preceding steps are performed, module a can successfully integrate the .so file compiled in module b on the native side.

**Answer**

1.  Use the NDK to build the pure CPP code into a .so or .a file and store in the HAR or HSP.
2.  Use the link and header files to share the pure cpp across modules. During linking, write the name of the library file. For the module called by Node-API, wite the Node-API code separately. In this case, the capabilities encapsulated by the Node-API can be used by other modules through module dependency.

**Procedure**

1.  In the **build-profile.json5** file of the HAR or HSP module, set the API file path to **buildOption/nativeLib/headerPath**.
    
    buildOption: { nativeLib: { headerPath: "src/main/cpp/include" } }
    
2.  Define the dependencies.
    
    // oh-package.json dependencies: { curl: "1.0.0" }
    
3.  In the CMake file, set the target link library in the format of **packageName::soName**.
    
    target\_link\_libraries(entry PUBLIC curl::curl)
