# Preparations for Development

This document is intended for novices at developing HarmonyOS applications. By building a simple application with page navigation (as shown below), you will better understand the project directory and the typical HarmonyOS application development process.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/zqbbqK8aTdK3nLPG3RmBhw/en-us_image_0000002529580171.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061911Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=242AB679574B7395C0E9F87BA37575EFC4C026BB54610A5125DB481F0573327D)

Before you begin, there are two basic concepts that will help you better understand HarmonyOS: UI framework and application model.

#### Basic Concepts

## UI Framework

HarmonyOS provides a UI development framework, known as ArkUI. ArkUI provides a full array of capabilities you may need for application UI development, ranging from components to layout calculation, animation, UI interaction, and rendering capabilities.

ArkUI comes with two development paradigms: ArkTS-based declarative development paradigm (declarative development paradigm for short) and JavaScript-compatible web-like development paradigm (web-like development paradigm for short). You can choose whichever development paradigm that aligns with your practice.

| 
**Development Paradigm**

 | 

**Programming Language**

 | 

**UI Update Mode**

 | 

**Applicable Scenario**

 | 

**Intended Audience**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

Declarative development paradigm

 | 

ArkTS

 | 

Data-driven

 | 

Applications involving technological sophistication and teamwork

 | 

Mobile application and system application developers

 |
| 

Web-like development paradigm

 | 

JavaScript

 | 

Data-driven

 | 

Applications with simple UIs and service widgets

 | 

Frontend web developers

 |

For details about the UI development and guidelines, see [Introduction to ArkUI](../../../application-framework/arkui/about-this-kit/document.md).

## Application Model

An application model abstracts the capabilities required by an application and provides components and mechanisms required for running the application. By adhering to a unified model, you can streamline application development, making it more efficient and straightforward.

With the evolution of the system, HarmonyOS has provided two application models:

-   **Feature Ability (FA) model**: This model is supported since HarmonyOS API version 7 and is no longer recommended. For details about development based on the FA model, see [FA Model Development Overview](../../../application-framework/ability-kit/fa-model-development/fa-model-development-overview/document.md). This document does not provide development examples for this model.
-   **Stage model**: This model is supported since HarmonyOS API version 9. It is the mainstream model with a long evolution plan. In this model, classes such as **AbilityStage** and **WindowStage** are provided as the stage of application components and windows. That's why it is named stage model. For details about development based on the stage model, see [Stage Model Development Overview](../../../application-framework/ability-kit/stage-model-development/stage-model-development-overview/document.md). **The examples in this document are all based on the stage model.**
    

For details about the differences between the FA model and the stage model, see [Application Models](../../../application-framework/ability-kit/application-models/document.md).

To help you better understand the preceding basic concepts and application development process, **Quick Start** walks you through an example of building your first ArkTS application with two pages in the stage model.

#### Tool Preparation

Download and install [DevEco Studio of the latest version](https://developer.huawei.com/consumer/en/download/) by referring to [Downloading and Installing DevEco Studio](../../../environment-setup/downloading-and-installing-deveco-studio/document.md). For details about usage, see [Overview](../../../environment-setup/overview/document.md).

After completing the preceding operations and understanding basic concepts, proceed to [Building Your First HarmonyOS Application (ArkTS)](../building-your-first-harmonyos-application-arkts/document.md) for a hands-on tutorial.
