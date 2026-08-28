# What is the napi\_module struct?

The input parameter of the **napi\_module\_register(napi\_module\* mod)** method, **napi\_module**, has two key properties: **.nm\_register\_func** and **.nm\_modname**. **.nm\_register\_func** defines the module initialization function, and **.nm\_modname** defines the module name, that is, the name of the .so file imported by ArkTS. The napi\_module struct has the following properties:

static napi\_module demoModule = {
    .nm\_version = 1,             // nm Version number, default value is 1
    .nm\_flags = 0,               // nm Identifier
    .nm\_filename = nullptr,      // File name, don't pay attention to it for now, just use the default value
    .nm\_register\_func = Init,    // Specify the entrance function for nm
    .nm\_modname = "entry",       // Specify the module name to import from the ArkTS page
    .nm\_priv = ((void\*)0),       // Don't follow for now, just use the default settings
    .reserved = { 0 },           // Don't pay attention for now, just use the default value
};
