# Subpass Shading

As game scenes become more complex, an increasing number of lighting effects are applied to games, leading to substantial lighting computation and bandwidth consumption. Currently, methods such as Tile-Based Deferred Rendering (TBDR) and Forward+ can address the problem of rendering time consumed by numerous lighting effects. However, the problem of excessive bandwidth usage remains unresolved. The Subpass Shading capability primarily reduces bandwidth consumption by minimizing read and write operations during the computation process.

The following figures show how Subpass Shading saves one read and write bandwidth from the device memory for Render Pass 1 and Compute Pass.

**Figure 1** Forward+ reading process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/WSckQxm0TSyaO4D8XoiLxQ/en-us_image_0000002498060740.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062054Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A2CE2E36BD49196F2B4AB132644A56E616443E8DAA3D30F8BB7402D7BA8F633E "Click to enlarge")

**Figure 2** Subpass Shading reading process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/u4EpTQjeRW-3LX6PakS3lA/en-us_image_0000002529808459.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062054Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1697C7924E30DD9358C957410E7E87585D7D826D7EC248C877310B26C8DBF498 "Click to enlarge")

#### Restrictions

Phones are supported. Additionally, tablets and PCs/2-in-1 devices are supported since version 5.0.2(14), and TVs are supported since version 5.1.0(18).

#### API Description

This kit provides the Subpass Shading API through the Vulkan extension API [VK\_HUAWEI\_subpass\_shading](https://registry.khronos.org/vulkan/specs/latest/man/html/VK_HUAWEI_subpass_shading.html). This extension supports the use of Compute Shaders within a Subpass and allows for direct data reading from the Tile buffer using SubpassLoad within the Compute Shader. It is designed to reduce DDR bandwidth and is suitable for TBDR and Forward+ pipelines.

For details about how to use the Subpass Shading capability, please refer to [Demo (XEngine Kit-Subpass Shading)](https://gitcode.com/harmonyos_samples/xengine-samplecode-subpass-shading-demo-cpp).
