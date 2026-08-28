# Overview

RAG combines intelligent retrieval and knowledge base technologies. It generates answers or content by retrieving information from knowledge bases, and features strong interpretability and customization capabilities. Apps can quickly implement services such as knowledge Q&A and smart assistant by integrating the [RAG](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataaugmentation-rag-api) capability provided by Data Augmentation Kit. The following uses the streaming knowledge Q&A scenario as an example to describe how to use RAG.

RAG requests the streamChat LLM to parse user questions. After retrieving relevant content from the knowledge base, RAG uses the LLM to integrate the retrieval results and generate human-like output.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/E6HuPBfqREOwTDiYOAzbwA/en-us_image_0000002342660670.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061952Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3A4194DA6B5BE6CB46E25EA0336072EF971C8A5001F25B46833EF70143951F64 "Click to enlarge")
