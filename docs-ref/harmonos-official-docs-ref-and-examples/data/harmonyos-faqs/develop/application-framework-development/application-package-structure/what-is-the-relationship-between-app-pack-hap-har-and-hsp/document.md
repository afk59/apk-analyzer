# What is the relationship between App Pack, HAP, HAR , and HSP?

-   App Pack: basic unit for releasing to AppGallery. It cannot be directly installed or run on a device.
-   Harmony Ability Package (HAP): basic unit for application installation and execution. It contains code, resource files, third-party libraries, and configuration files. HAPs are mainly categorized into entry and feature types.
-   Harmony Archive (HAR): static shared package that contains code, C++ libraries, resource files, and configuration files. HARs allow multiple modules or projects to share ArkUI components and related code.
-   Harmony Shared Package (HSP): dynamic shared package that contains code, C++ libraries, resource files, and configuration files. HSPs are used for code and resource sharing. Deployed with the App Pack of the host application, HSPs share the same process, bundle name, and lifecycle as the host application.
