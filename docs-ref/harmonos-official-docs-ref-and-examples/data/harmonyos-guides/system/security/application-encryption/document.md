# Application Encryption

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/wGmZFzXBRI21xAzHV2Ewlw/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061959Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9365122EDCA731E094801F3CC519FFA9BE7A4B4ABA991F1024D968F1DE35DEB2)

The application encryption feature can effectively increase the difficulty in reverse engineering of application code. However, defending against reverse engineering is a continuous attack-defense confrontation process. Other security hardening measures need to be taken for higher levels of code protection.

#### Introduction

To protect application code security and your core assets, HarmonyOS provides an end-to-end mechanism to protect the kernel-level application code throughout its lifecycle based on system security.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/9EeXBPbIRyi3aIypVIBaJw/en-us_image_0000001945728710.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061959Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E1C27A028A6363925153BD7FAEC853422953C9739646739DD7E181868BA2DFCE "Click to enlarge")

You can submit an application release request to AppGallery Connect (AGC) and [choose to encrypt](https://developer.huawei.com/consumer/en/doc/app/agc-help-release-app-choose-pkg-0000002278981434) the uploaded application package.

Then the application code will be encrypted by AGC after the release request is approved. When the application is installed on a device, the installation file is still protected after being stored on the device, which effectively guards the application. When the application is started, it is decrypted as required.

The system-level application encryption stands out with the following features:

-   Kernel-level security protection and end-to-end encryption enable applications to be decrypted and executed as required.
-   System-level decryption optimization has less impact on performance than traditional packing.

#### Encryption Impact

1.  The encrypted application may slightly increase performance overheads during startup and running.
2.  The encrypted application is larger in size than the unencrypted one and may slightly increase the download and installation time.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/18BFV4z5T-m75Wpl4qfoCQ/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061959Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E5A4A927C037CA06887F33A54C2AD371FA1D70FD2302E8F62477BBDEB693CC19)

The impact of application encryption has been optimized at the system level. In certain enhanced versions, the performance and package size of the application stay nearly the same with or without encryption.

#### Protection Effect

The application encryption feature protects core assets (for example, .abc files) in the application package. Unencrypted code files can be decompiled. After encryption, the security of the code files is greatly enhanced, increasing the difficulty in reverse engineering.

#### How to Use

The application encryption feature allows applications to be encrypted in the release process and decrypted on demand at runtime. It enhances application security while minimizing your adaptation work, ensuring a seamless and secure user experience.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/nVd0zlWLTciuL71lB72umQ/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061959Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1A2A346AFD204F574426CDA5B181D237087F80ABBD739643A09DDCC27729A6CC)

Currently, the **widgets.abc** file of the ArkTS widget service does not support encryption.

The following outlines how the application encryption feature is utilized throughout the application lifecycle:

-   Development: No special operation is required.
-   Release: You can determine whether to encrypt the software package to be released.
    
    For details, see [Selecting a Package to Be Released](https://developer.huawei.com/consumer/en/doc/app/agc-help-release-app-choose-pkg-0000002278981434).
    
-   Distribution: The application is encrypted and distributed in AGC to prevent reverse engineering.
-   Installation: The application code is protected in the installation phase.
-   Running: The application code is decrypted as required during the runtime.

#### FAQs

-   **Q1: Are additional code protection measures necessary for the applications safeguarded by the official code encryption feature?**
    
    A1: The application encryption feature can effectively increase the difficulty in reverse engineering of application code. However, defending against reverse engineering is a continuous attack-defense confrontation process. Further security hardening measures, such as code obfuscation and third-party security hardening features, are still necessary for higher levels of code protection.
    

-   **Q2: What other measures can be used to protect application code if code encryption is not used?**
    
    A2: You can use code obfuscation and third-party security hardening measures. For details, see [Protecting Application Code](https://developer.huawei.com/consumer/en/doc/best-practices-V5/bpta-app-asset-protection-design-V5#section24320461547).
    
-   **Q3: What is the impact of code encryption on application packages?**
    
    A3: An encrypted application may slightly increase performance overheads during startup and runtime. Compared with an unencrypted application, an encrypted application is larger in size, and may slightly increase the download and installation time.
