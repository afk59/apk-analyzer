# Overview

ohpm-repo is a tool for setting up lightweight ohpm private repositories. It is compatible with the ohpm package manager and caches all dependencies on demand, accelerating installation in private networks.

#### Privacy

The published third-party libraries are private and can only be accessed based on the configuration.

#### Cache

ohpm-repo caches all dependencies as required to speed up the installation in private networks.

#### Deployment

ohpm-repo supports both single-node and multi-instance deployment.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/cOK1Esd8SiuZLdOb62k_7A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8298F6FF4F0EE2AB821153EF6D6A59CDA4A837DD6845728E341BB5E9F08FE935)

-   Single-node deployment: ohpm-repo is deployed on only one host.
-   Multi-instance deployment: ohpm-repo is deployed on multiple hosts with identical configurations and shared data storage space.
-   For details about how to migrate data from single-node deployment to multi-instance deployment, see [Data Migration Guide](../appendix/data-migration/document.md).
