# What should I do if using the Node-API generation feature results in the "Unsupported parameter type." or "Unsupported return type." error?

**Symptom**

An error occurs for generating glue code when you right-click a function and choose **Generate...** > **NAPI** from the shortcut menu.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/y5y0Nd08S9mrg4_mO9uaWw/en-us_image_0000002229604265.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062615Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EC9BE14CF7859EF4E80800E640FBCF17718B93CA48753E3428E435AB8EA1F4FA)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/1R7Mzi5FSPafKUMEecVjSQ/en-us_image_0000002194318496.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062615Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9BCD55853838203509F010EB0C45592D18B221E0E6C08218C093AC5C0E013A3A)

**Solution**

Modify the function parameter or return value type to a type that is supported.

Currently, the following types are supported, with JS types indicated before the colon (:) and their corresponding C++ types following after:

-   void: void
-   number: int, int32\_t, uint32\_t, int64\_t, uint64\_t, double (float is not supported by Node-API)
-   string: char\*, char16\_t\*, const char\*, const char16\_t\*, char, char const, const char, std::string
-   boolean: Boolean
-   User-defined structure type: C++ user-defined structure type class (excluding system library classes)
-   Array<>: std::vector<>, std::array<> (including nested parsing)

The following types are not supported:

-   Template functions
-   Template classes
-   Enumerations
-   Unions
-   System containers other than **std::vector<>** and **std::array<>**, such as **iterator**, **set**, **map**, **list**, and **stack**
-   System library classes other than user-defined classes
-   Other references and pointers
-   Function type conversion, for example, a function returning a callback function
-   auto
