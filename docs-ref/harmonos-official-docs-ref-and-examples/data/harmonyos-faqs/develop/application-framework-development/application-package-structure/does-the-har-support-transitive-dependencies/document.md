# Does the HAR support transitive dependencies?

**Question**

Assume that there are three HARs: A, B, and C. A depends on B, and B depends on C. Can A directly access or reference resources from C?

**Answer**

Transitive dependencies are not supported in HARs. Therefore, A cannot directly reference resources from C. To access or reference any of resources from C, A must explicitly declare a dependency on C.
