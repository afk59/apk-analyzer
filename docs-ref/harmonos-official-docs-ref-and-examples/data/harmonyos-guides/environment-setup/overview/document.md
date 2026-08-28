# Overview

#### IDE-based Development

## DevEco Studio: IDE for HarmonyOS App/Atomic Service Development

HUAWEI DevEco Studio (DevEco Studio for short; [download](https://developer.huawei.com/consumer/en/download/)) is a comprehensive one-stop integrated development environment (IDE) designed for HarmonyOS app/atomic service development across all scenarios. Powered by the IntelliJ IDEA Community Edition, it offers a robust suite of features to streamline the development process, including:

-   [Intelligent code editor](../../coding-and-debugging/writing-code/document.md): Draw on the intelligent code completion, code factoring, and other useful coding features to boost your ArkTS, JavaScript, and C/C++ development.
-   [Multi-device bidirectional real-time Previewer](../../coding-and-debugging/previewing-the-ui/document.md): See how your user interface (UI) and components look across different devices, right as you code, accelerating UI development.
-   [Hvigor](../../building-an-app/overview/document.md): Leverage this lightweight build tool for defining source code, resources, and build processes to flexibly create differentiated multi-target products, plus a powerful Build Analyzer that helps you analyze build performance and improve build efficiency.
-   [Cross-language debugger](../../coding-and-debugging/debugging-your-app/debugging-overview/document.md): Debug your code with advanced features, such as ArkTS and C++ cross-language debugging, assembly code debugging, LLDB-based debugging, reverse debugging, smart navigation, and data breakpoints.
-   [DevEco Profiler](../../performance-optimization/introduction-to-performance-optimization-tools/document.md): Profile your app performance for a diverse range of scenarios, including memory leakage, component time consumption, network requests, app startup, and UI freezing. See how your app is performing with visualized swimlanes.
-   [Emulator](../../coding-and-debugging/running-your-app-on-the-emulator/document.md): Use the Emulator to emulate devices such as phones (including foldable phones), tablets, PCs, and 2-in-1 devices to debug and test your app across various HarmonyOS devices, helping your app better adapt to different models and HarmonyOS versions.
-   Dependency management: Use ohpm, the default package management tool in DevEco Studio, to install, update, delete, and manage dependencies between Harmony Archives (HARs), Harmony Shared Packages (HSPs), or modules, streamlining code sharing, distribution, and dependency management. You can also use [ohpm-repo](../creating-a-project/managing-modules/ohpm-repo-private-repository-setup-tool/document.md) to set up a lightweight private repository for HarmonyOS third-party libraries. ohpm-repo is compatible with ohpm and enables you to store and manage your custom third-party libraries in a secure, private environment while facilitating easy sharing and reuse within your development team.

## Development Process

The figure below shows the process of developing an app/atomic service with DevEco Studio.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/11uOlUCTRAOgcqt781ALMw/en-us_image_0000002532670661.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062135Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AF1697C185DDFA647B1224D9381BD67C5907AAE90E18F2FB44387B02F1433FBE)

**1\. Get started.**

[Download](https://developer.huawei.com/consumer/en/download/) and install DevEco Studio.

The DevEco Studio development environment relies on an Internet connection to ensure that the tools function properly. [Proxy configuration](../../coding-and-debugging/appendix/setting-up-the-proxy/document.md) is necessary when you are on an enterprise network that has specific restrictions.

**2\. Develop your app/atomic service.**

[Kickstart your project](../creating-a-project/creating-a-project/document.md) by following the project wizard with ready-to-use, scenario-based templates for phones, tablets, 2-in-1 devices, and telematics devices.

Next, develop the UI and functionality for your app/atomic service. For details about the development process, see [Application Development Overview](../../getting-started/application-development-overview/document.md). For details about the available APIs, see [API References](https://developer.huawei.com/consumer/en/doc/harmonyos-references/development-intro-api).

During development, you can [preview how the UI of your app/atomic service looks](../../coding-and-debugging/previewing-the-ui/document.md) in real time and see the results of your code changes immediately.

**3\. Run, debug, and test your app/atomic service.**

You can [debug your app/atomic service on a real device](../../coding-and-debugging/debugging-your-app/debugging-overview/document.md), which requires a debug signature, using various debug modes, such as step-through and cross-language.

Before releasing your app/atomic service to AppGallery, [put it through tests, including the instrument test and local test](../../coding-and-debugging/conducting-self-test/test-framework/document.md), to ensure that it delivers a smooth, secure user experience.

**4\. Release your app/atomic service.**

When your app/atomic service is ready, [release it to AppGallery](../../app-release/release/document.md#section6406135115814) for users to download. Note that your app/atomic service must be signed with the release certificate before being released to AppGallery.

#### CLI-based Development

For those who prefer working with the command line interface (CLI) or need to integrate tools into a continuous integration/continuous deployment (CI/CD) pipeline, DevEco Studio offers the following [Command Line Tools](https://developer.huawei.com/consumer/en/download/command-line-tools-for-hmos) that make development more efficient and automated:

-   [codelinter](../../command-line-tools/using-codelinter/document.md): checks and fixes code quickly . You can integrate codelinter into gatekeeper (code gate) or CI environment.
-   [ohpm](../../command-line-tools/using-ohpm/document.md): centralizes the management of third-party libraries. It facilitates the publishing, installation, and dependency management for shared packages.
-   [hstack](../../command-line-tools/using-hstack/document.md): restores the crash stack of a release app to its corresponding stack in the source code.
-   [hvigorw](../../command-line-tools/using-hvigorw/document.md): serves as a wrapper for the Hvigor build tool, enabling automatic installation of Hvigor and its required plugin dependencies, and executing Hvigor build commands.

#### Constraints

Currently, the following features are available only in the Chinese mainland.

1.  Partner SDK
2.  Template Market
3.  Import Sample
4.  Device-cloud integrated development
5.  Upload Product
6.  Collect Logs and Diagnostic Data
7.  Operation Analyzer
8.  AppAnalyzer
9.  DevEco CodeGenie
10.  OHPM Index

#### General Statements

This document is applicable to the [latest version](https://developer.huawei.com/consumer/en/download/) of DevEco Studio. The GUI and operations may vary according to the DevEco Studio version.
