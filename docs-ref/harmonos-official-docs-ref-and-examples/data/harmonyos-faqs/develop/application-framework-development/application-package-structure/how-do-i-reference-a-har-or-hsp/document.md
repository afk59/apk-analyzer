# How do I reference a HAR or HSP?

During HarmonyOS application development, referencing modules (HARs and HSPs) is a common scenario. Proper referencing ensures code modularity, reduces maintenance costs, and streamlines team collaborations. The following are recommended and non-recommended approaches for referencing modules.

-   Recommended approach:
    
    import { add } from "library";
    
-   Non-recommended approach:
    
    Avoid using relative or absolute paths for module references. This approach breaks module isolation, complicates team collaboration, and makes the codebase harder to maintain. The following is an incorrect usage:
    
    import { add } from "../../library/src/main/ets/page/Index";
    

To maintain code modularity, enhance maintainability, and simplify team collaboration, always use package names, instead of relative or absolute paths, for dependency references between modules. For more information, see [HAR](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/har-package).
