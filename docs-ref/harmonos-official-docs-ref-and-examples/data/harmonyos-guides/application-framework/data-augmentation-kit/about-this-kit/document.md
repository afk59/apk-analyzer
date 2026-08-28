# About This Kit

Data Augmentation Kit provides the knowledge base, knowledge retrieval, retrieval-augmented generation (RAG), and on-device question & answer (Q&A) model capabilities to build a personalized intelligent data platform, delivering personalized intelligent experience.

#### Capabilities

Data Augmentation Kit provides the following capabilities:

-   [RAG](../rag/document.md): The kit provides a natural language processing technology that combines retrieval and generation techniques. It dynamically retrieves relevant information from external knowledge bases to assist in generating more accurate and reliable text content. Its core objective is to address the limitations of traditional generation models that rely on static knowledge, by integrating real-time knowledge retrieval with flexible content generation.
-   [Intelligent data retrieval](../intelligent-data-retrieval/document.md): The kit provides a knowledge retrieval framework based on multi-channel recall and re-ranking. In addition to traditional text retrieval based on inverted indexes, the kit also provides semantic retrieval based on vector indexes.
-   [On-device Q&A model](../on-device-q-a-model/document.md): The kit provides methods for accessing on-device models for Q&A, and uses HiAiMgr to connect to large language models (LLMs) to answer user questions within the device.

#### Highlights

## RAG

-   Real-time knowledge: The knowledge base can be dynamically updated without retraining the model, making it suitable for domains with frequent changes, such as news and policies.
-   Enhanced reliability: The generated content is based on retrieval results, reducing model hallucinations (fabricated information) and supporting answer traceability.
-   Flexible adaptation: A model can quickly switch between knowledge bases in different domains, reducing cross-scenario deployment costs.
-   Long-tail question coverage: External knowledge bases are used to supplement the knowledge of niche domains on which the model has not been trained.

## Intelligent Data Retrieval

-   Intelligent data construction: App data is processed and converted into knowledge, and the knowledge is stored in storage engines such as inverted index databases, vector databases, and graph databases.
-   Intelligent data retrieval: This kit supports complex data retrieval scenarios such as condition-based filtering and semantic understanding for integrated queries across various data types (such as images and text) or databases. Intelligent data retrieval is implemented in two phases: multi-channel recall and re-ranking.
-   RAG-based knowledge Q&A: This kit combines retrieval and generation techniques to dynamically retrieve information from external knowledge bases, improving the accuracy of LLMs in answering questions and reducing hallucinations (fabricated information).

## On-Device Q&A Model

-   An app can choose to use the on-device Q&A model, which ensures that data processing is performed on the device to protect user security and privacy.

#### Basic Concepts

-   LLM: an artificial intelligence (AI) model based on deep learning. It masters language rules through training on massive text data and can understand and generate human languages.
-   Chunk: a logical or structural unit formed by splitting text during knowledge processing. Currently, a single chunk contains a default of 3072 characters (where one character refers to either one Chinese character or one English letter).
-   Recall: a method of using a specific strategy or algorithm to quickly filter the candidate result set from massive data.

#### Restrictions

This kit is applicable to the following devices. Emulators are not supported currently.

| 
Capability

 | 

Supported Devices

 |
| :-- | :-- |
| 

RAG

 | 

PC/2-in-1 device

 |
| 

Knowledge processing

 | 

Phone, PC/2-in-1 device, and tablet

 |
| 

Intelligent data retrieval

 | 

Phone, PC/2-in-1 device, and tablet

 |
| 

On-device Q&A model

 | 

PC/2-in-1 device

 |

#### Supported Countries/Regions

Currently, this kit is available only in the Chinese mainland.
