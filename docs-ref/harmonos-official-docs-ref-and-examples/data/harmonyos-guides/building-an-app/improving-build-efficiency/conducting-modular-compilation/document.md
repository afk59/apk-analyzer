# Conducting Modular Compilation

Modular compilation is bundleless and uses native ES Module (ESM) rules to compile source code. Using modular compilation, enabled by default in projects developed on the stage model using API version 10 or later, can effectively shorten the incremental compilation time and reduce the package size after compilation.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/Dwf2swwPTm-Q2qMN9vQdww/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=676381DEC487EBFA0E83A56E6AB882E66B3C51B632B5E03C7B02351EF4736DBB)

Projects developed on the FA model are still built based on bundles.

Modular compilation solves the following problems caused by bundle-based compilation and packaging:

-   The same module is referenced for multiple times, leading to repeated packaging and loading. As a result, the running status cannot be shared and the singleton pattern cannot be implemented properly.
-   Modifying a single module file requires recompilation and repackaging of all module files, which is time-consuming.
-   Global variables are contaminated.

Advantages of modular compilation are as follows:

-   Modifying the code for a single module does not require recompilation and repacking of all modules, greatly shortening the time of incremental compilation.
-   Based on ESM rules, the utilization of module cache is high. Variable changes in a module can be quickly applied to the module and dynamically bound in real time.
-   The singleton pattern can be properly implemented.
-   The ROM size of the package is reduced.
-   Problems such as variable contamination are solved, and the module development efficiency is improved by using various APIs.

#### Specification Constraints

-   A HAP can reference the code of other HAPs in the same project, but this method is not recommended. It is recommended that HARs be used to organize and reference common code.
-   A HAP can reference the code of other HAPs in the same project through the **oh-package.json5** configuration file and ohpm, but this method is not recommended. It is recommended that HARs be used to organize and reference common code.
-   Code outside a project and code in any directory created in the project cannot be referenced. Otherwise, an error is reported during project compilation.
-   You are advised to use HAPs to reference common code in HAR (static library) mode.
-   You are advised to use HAPs to reference a shared library in HSP mode.
