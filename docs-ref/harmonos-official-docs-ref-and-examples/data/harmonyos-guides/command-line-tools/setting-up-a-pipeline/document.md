# Setting Up a Pipeline

In addition to DevEco Studio, you can also invoke Hvigor tasks through the CLI to build your app/atomic service. This approach allows you to set up a continuous integration (CI) pipeline to automate scheduled operations such as HAP/App Pack building, signing, installation, and running.

You can run commands on Windows, Linux, or macOS to build your app/atomic service through the CLI. This section uses Linux as an example. The procedure for invoking commands is the same regardless of the operating system.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/5-rJqPTlTC6NBP4sL7i-kw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062200Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A35D98BD5D479095241BC65D1CE24F6A9CA7450EBB33B7EF1F5B285F3B0F8846)

-   If your computer is not connected to the Internet, follow the instructions in [Creating a CI Pipeline Offline](#section15767113454814).
-   Since the HarmonyOS SDK is embedded in DevEco Studio, there is no need for separate downloads or configurations.
-   Before running any commands, ensure that the current project is trustworthy for secure builds.

#### System Platform Requirements

-   Operating system: 64-bit Linux
    
-   glibc: 2.28 or later
    
-   Memory: 16 GB or larger recommended, 8 GB minimum
    
-   Hard disk: 100 GB or above
    

#### Prerequisites

## Configuring the JDK

1.  Download JDK 17.
2.  In **Terminal**, go to the JDK software package directory and run the following command, replacing **jdk-17.0.6\_linux-x64\_bin.tar.gz** with the actual package name, to decompress the package.
    
    tar -xvf jdk-17.0.6\_linux-x64\_bin.tar.gz
    
3.  Configure the JDK environment variables.
    
    #jdk
    export JAVA\_HOME=/opt/jdk-17.0.6\_linux-x64\_bin
    export PATH=$PATH:$JAVA\_HOME/bin
    
4.  Run the following command to check the JDK installation result:
    
    java -version
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/X73h-fZ3RbWlh3ggGXKRLw/en-us_image_0000002500910094.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062200Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=491760297B5CDF088EDD549DBD5B74E5B4A9431CC5A6DFA589A61EB96853F5E5)
    

## Obtaining Command Line Tools

1.  [Obtain the command line tools](../obtaining-command-line-tools/document.md#section21298572437) pertaining to your operating system. In this example, command line tools for Linux are downloaded.
2.  Run the following command to decompress the **commandline-tools-linux-xxx.zip** file (replace the file name with the actual package name in the command):
    
    unzip commandline-tools-linux-x64-5.0.3.XXX.zip
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/zLosR00tRoClFXhqeMqv2A/en-us_image_0000002532670011.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062200Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AB8EBB79497B022A38EEF546C644FB1325D513C7DE6506BBE939408C0611AF8B)
    
3.  Define the path where you decompress the tools as **COMMANDLINE\_TOOL\_DIR**, which will be used later when configuring the environment variables for Node.js, HDC, Hvigor, and ohpm.
    
    export COMMANDLINE\_TOOL\_DIR=/opt
    

## Setting the Node.js Environment Variables

The Command Line Tools package comes with a compatible version of Node.js. You can configure the environment variables by performing the following steps:

1.  Configure the Node.js environment variables.
    
    \# The following uses Linux as an example. The Node.js path varies with the operating system. Replace it with the actual path.
    export NODE\_HOME=${COMMANDLINE\_TOOL\_DIR}/command-line-tools/tool/node
    export PATH=$PATH:$NODE\_HOME/bin
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/AdTOGgNsQGm44OmI__fY0A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062200Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D1206D04D5A898A2F763F1659AD328387565585A317714EC4EB46436CB4C8EA9)
    
    The Node.js path varies depending on the OS. On Windows, the Node.js path is **tool/node**. On Linux and macOS, the Node.js path is **tool/node/bin**.
    
2.  Run the following command to check the Node.js version to verify that the configuration is successful:
    
    node -v
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/ZkKMYz48Q927YfrgrbOSnA/en-us_image_0000002501069932.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062200Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=79FEE8A80F355495FCA77AA42BD6620F9407B238A9C073034A940B1AAF644AE4)
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/1Cxy7UorT4q6Z7KUNzaqfA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062200Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5F079DE7804D445E93A7FCE03DD0FAC760F5C5FA25FF6FCEBD71F8356B1C4321)

You are advised to use the Node.js tool included in the command-line tool suite. If you choose to use a separately installed Node.js version, v18 is recommended.

## Setting the hdc Environment Variable

The hdc command line tool is used as a debugging tool for HarmonyOS apps/atomic services. This tool is located in the **toolchains** directory of the SDK that comes with the Command Line Tools. To facilitate the use of hdc, add it to the environment variables.

1.  Complete [Obtaining Command Line Tools](#section88316312414).
2.  Run the following command to add hdc to the environment variables, where **${COMMANDLINE\_TOOL\_DIR}/command-line-tools/sdk/default/openharmony/toolchains** is used as an example of the hdc save path.
    
    export HDC\_HOME=${COMMANDLINE\_TOOL\_DIR}/command-line-tools/sdk/default/openharmony/toolchains
    export PATH=$PATH:$HDC\_HOME
    

## Setting the hvigor Environment Variable

1.  Complete [Obtaining Command Line Tools](#section88316312414).
2.  Run the following command to add hvigorw to the environment variable **PATH**:
    
    export PATH=${COMMANDLINE\_TOOL\_DIR}/command-line-tools/bin:$PATH
    
3.  Switch to the root directory of the project and run the following command to query the Hvigor version to verify that the installation is successful:
    
    hvigorw -v
    

## Configuring the npm Image Repository

If the dependencies configured the **hvigor/hvigor-config.json5** file contain any npm third-party libraries, you need to set the npm image repository address in the pipeline so that the libraries can be correctly downloaded during compilation.

npm config set registry https://repo.huaweicloud.com/repository/npm/
npm config set "@ohos:registry" https://repo.harmonyos.com/npm/

## Installing ohpm

1.  Complete [Obtaining Command Line Tools](#section88316312414).
2.  Run the following command to add ohpm to the environment variables:
    
    export PATH=${COMMANDLINE\_TOOL\_DIR}/command-line-tools/bin:$PATH
    
3.  Run the following command to check the ohpm version to verify that the installation is successful:
    
    ohpm -v
    
4.  Run the following commands to specify one or more repository addresses, separated by commas:
    
    ohpm config set registry https://ohpm.openharmony.cn/ohpm/
    ohpm config set strict\_ssl false
    

## Installing the libGL1 Library

To use [texture compression](../../building-an-app/configuration-files/project-level-build-profile-json5-file/document.md#section2095319147103) on Linux, you need to install the libGL1 library. The installation command varies by operating system. For example, install **libgl1-mesa-dev** on Ubuntu/Debian and **mesa-libGL-devel** on CentOS/RHEL.

The command below uses **libgl1-mesa-dev** as an example. For other operating systems, replace it with the actual package name.

apt install -y libgl1-mesa-dev

#### Building an App

## Installing Project and Module Dependencies

Before using the CLI to build a project, run the **ohpm install** command in the project and each module to install the third-party libraries on which the project and modules depend.

1.  Define the ohpm installation function. The following is an example:
    
    \# Switch to the specified directory $1 and run the ohpm install command.
    function ohpm\_install() {     
        cd $1              # $1: first parameter of the function, which must be a path.
        ohpm install --all # Install all dependencies.
    }
    
2.  Define the **PROJECT\_PATH** variable, which indicates the project path. The following is an example:
    
    PROJECT\_PATH=xxx/xxx/project\_name  # Project path.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/ME5kX8HmQq6RELCP0kS66g/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062200Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=82FCF90D369E92B188A9F153E96AFC8BFD3BD04007B09F99FBCEED97AFEE8AB1)
    
    Do not store the project directory in a hidden directory. That is, each level in the project path must not start with a period (.), for example, **xxx/.xxx/project** is not recommended. Otherwise, during the build process, the module's code and configuration files may be packaged into the product as resources without being obfuscated or encrypted.
    
3.  Install the third-party library dependencies of the project and modules. The following is an example:
    
    \# Install the third-party library dependencies based on service requirements.
    ohpm\_install "${PROJECT\_PATH}"
    ...
    

## Running Hvigor Build Commands

1.  Use the hvigorw command line tool to run the build command.
    
    \# Run a build command based on the service requirements. The following is an example:
    
    # Clean the project.
    hvigorw clean --no-daemon
    
    # Build a HAP. The generated file is ${PROJECT\_PATH}/{moduleName}/build/{productName}/outputs/{targetName}/xxx.hap.
    hvigorw assembleHap --mode module -p product=default -p buildMode=debug --no-daemon
    
    # Build an HSP. The generated files are ${PROJECT\_PATH}/{moduleName}/build/{productName}/outputs/{targetName}/(xxx.har | xxx.hsp).
    hvigorw assembleHsp --mode module -p module=library@default -p product=default --no-daemon
    
    # Build a HAR. The generated file is ${PROJECT\_PATH}/{moduleName}/build/{productName}/outputs/{targetName}/outputs/xxx.har.
    hvigorw assembleHar --mode module -p module=library1@default -p product=default --no-daemon
    
    # Build an App Pack. The generated file is ${PROJECT\_PATH}/build/outputs/{productName}/xxx.app.
    hvigorw assembleApp --mode project -p product=default -p buildMode=debug --no-daemon
    
    -   In non-daemon mode, you can modify the Node.js memory settings. To do so, uncomment line 15 in the **hvigor/bin/hvigorw** file and set the memory size to a value you prefer, such as 10240:
        
        NODE\_OPTS="--max-old-space-size=10240"
        
    -   If you are using daemon mode, see [Setting the Daemon Memory](../../building-an-app/improving-build-efficiency/using-the-daemon-process/document.md#section327617383145).
    -   When using Linux for your CI pipeline, be aware that Linux is case-sensitive. If your code has case mismatches in imports — for example, using **import funcA from './aaa'** when the actual file is named **AAA.ets** — the code might compile successfully on Windows or macOS due to their case-insensitive file systems. However, on Linux, this could lead to compilation failures. To maintain consistency in compilation results across Windows, macOS, and Linux, you can configure **caseSensitiveCheck** to **true** in the project-level **build-profile.json5** file. This configuration enforces case sensitivity during compilation, ensuring that any case mismatches are detected regardless of the operating system.
        
        // build-profile.json5 file
        {
            "name": "default",
            "compatibleSdkVersion": "6.0.2(22)",
            "runtimeOS": "HarmonyOS",
            "buildOption": {
              "strictMode": {
                "caseSensitiveCheck" : true
              }
            }
        }
        
    
2.  After a build command is executed, the HAP, HSP, HAR, or App Pack files are generated in the **build** directory of the project or corresponding module.

The tables below list the common command-line options for compilation and building. For details about more Hvigor command-line options, see [Common Commands](../using-hvigorw/document.md#section16300629103).

**Table 1** Common command-line options in building HarmonyOS apps
| 
Options

 | 

Description

 |
| :-- | :-- |
| 

\-p buildMode={debug | release}

 | 

Uses the debug or release mode for builds.

By default, the debug mode is used in building HAPs, HSPs, or HARs, and the release mode is used in building App Packs.

For details about build modes, see [Specifying a Build Mode](../../building-an-app/customizing-your-build/customizing-build-options/introduction/document.md#section192461528194916). For details about how to build a HAR, see [Building a HAR](../../building-an-app/configuring-your-build/building-a-har/document.md).

 |
| 

\-p product={ProductName}

 | 

Specifies the target product under which the module targets are built.

Default value: **default**

 |
| 

\-p module={ModuleName}@{TargetName}

 | 

Specifies the module and target for builds. You can specify multiple modules of the same type, separated with commas (,).

Note: This option must be used together with **\--mode module**.

By default, all modules in the project are built when the AssembleHap task is executed, and **default** is used for **TargetName**.

 |
| 

\-p ohos-test-coverage={true | false}

 | 

Executes the instrumentation compilation of the test framework code coverage.

 |

**Table 2** Options related to HarmonyOS app builds
| 
Options

 | 

Description

 |
| :-- | :-- |
| 

clean

 | 

Cleans build output.

 |
| 

assembleHap

 | 

Builds a HAP.

 |
| 

assembleApp

 | 

Builds an App Pack.

 |
| 

assembleHsp

 | 

Builds an HSP.

 |
| 

assembleHar

 | 

Builds a HAR.

 |

#### Running an App

If a signature file is configured for the build, respective signed (for example, **xxx-signed.hap**) and unsigned (for example, **xxx-unsigned.hap**) packages are generated. The signed package can be run directly on a real device without re-signing. To re-sign the package, use the signing tool on the unsigned one, as described below.

## Preparing Files to Apply for Signature

To apply for a signature, three files are required: keystore file (.p12 file), digital certificate (.cer file), and profile (.p7b file).

**Generating a Keystore File and CSR**

Use the Keytool in the JDK to generate a keystore file and certificate signing request (CSR).

1.  After configuring the environment variables by following steps in [Configuring the JDK](#section195447475220), open the CLI and run the following command to generate a keystore file. This example creates a keystore file named **demo.p12** and saves it to the **path** directory.
    
    keytool -genkeypair -alias "demo\_key" -keyalg EC -groupname secp256r1 -sigalg SHA256withECDSA -dname "C=CN,O=HUAWEI,OU=HUAWEI IDE,CN=demo\_key"  -keystore /path/demo.p12 -storetype pkcs12 -validity 9125 -storepass 123456Abc -keypass 123456Abc
    
    In the preceding command, modify settings of the following parameters and keep the other parameters as they are:
    
    -   **alias**: alias of the key, which is used to identify the key name.
    -   **dname**: basic certificate information.
        -   **C**: country/region code, such as **CN**.
        -   **O**: organization name, such as **HUAWEI**.
        -   **OU**: organization unit name, such as **HUAWEI IDE**.
        -   **CN**: your first name and last name. Set this parameter to be the same as **alias**.
    -   **keystore**: keystore file. Replace **/path/demo.p12** with the actual path to the file.
    -   **validity**: certificate validity period, for example, **9125** (25 years).
    -   **storepass**: key store password, which must contain at least 8 characters that include two types of the following: uppercase letters, lowercase letters, digits, and special characters. Make a note of the password. You will need it when configuring the signature.
    -   **keypass**: password of the key. The value must be the same as that of **storepass**.
    
2.  Run the following command. After the command is executed, enter the storepass to generate a .csr file.
    
    keytool -certreq -alias "demo\_key" -sigalg SHA256withECDSA -keystore /path/demo.p12 -storetype pkcs12 -file /path/demo.csr
    
    Parameters in the CSR:
    
    -   **alias**: alias. The value is the same as the alias set in the previous step.
    -   **keystore**: keystore file. The value is the same as the keystore set in the previous step.
    -   **file**: name of the generated CSR file, with a .csr extension. Replace **/path/demo.csr** with the actual path to the file.
    

**Requesting a Debug Digital Certificate and Profile File**

With the CSR, request and download a debug certificate and profile in AppGallery Connect. For details, see [Requesting a Debug Certificate](../../coding-and-debugging/configuring-a-debug-signature/document.md#section081822416419) and [Requesting a Profile File and Adding Permission Information](../../coding-and-debugging/configuring-a-debug-signature/document.md#section89479413571).

## Signing the Unsigned HAP or APP File

1.  Prepare the signing tool hap\_sign\_tool.jar, which is available in **${_COMMANDLINE\_TOOL\_DIR_}/command-line-tools/sdk/default/openharmony/toolchains/lib**.
2.  In the signing tool directory, run the following command to sign the HAP: For details about the signing tool, see [hapsigner](https://gitcode.com/openharmony/developtools_hapsigner).
    
    java -jar hap-sign-tool.jar sign-app -keyAlias "demo\_key" -signAlg "SHA256withECDSA" -mode "localSign" -appCertFile "/path/demo.cer" -profileFile "/path/demo.p7b" -inFile "/path/hap-unsigned.hap" -keystoreFile "/path/demo.p12" -outFile "/path/hap-signed.hap" -keyPwd "123456Abc" -keystorePwd "123456Abc"
    
    In the preceding command, modify settings of the following parameters and keep the other parameters as they are:
    
    -   **keyAlias**: key alias.
    -   **appCertFile**: debug certificate file in .cer format.
    -   **profileFile**: debug profile file in .p7b format.
    -   **inFile**: HAP to sign.
    -   **keystoreFile**: keystore file in .p12 format.
    -   **outFile**: HAP that carries the signature information, to be generated after the signing.
    -   **keyPwd**: key password.
    -   **keystorePwd**: keystore password.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/DsrTQl_XS2edN0JRaLt9Hw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062200Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F96AE9BEFF4110276F18ED1302C407EEBA21BF9BA5C4F10931970ADEE238F86D)
    
    To sign an APP Pack, modify the **inFile** and **outFile** parameters in the preceding command to point to the APP Pack.
    

## Running an App

Use [hdc](../../system/debugging-tools/performance-analysis-kit/command-line-tools/hdc/document.md) to push a signed HAP to a real device for installation. Note that if the pushed HAP is not signed, the installation will fail.

To push a HAP, run the following commands:

\# Push the HAP to the device.
hdc file send "{PROJECT\_PATH}/entry/build/default/outputs/default/entry-default-signed.hap" "data/local/tmp/entry-default-signed.hap"
# Install the HAP.
hdc shell bm install -p "data/local/tmp/entry-default-signed.hap"
# Delete the HAP.
hdc shell rm -rf "data/local/tmp/entry-default-signed.hap"

To run the HAP on the device, run the following command:

hdc shell aa start -a EntryAbility -b com.example.myapplication -m entry

#### Script Example

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/TVNj3HUJQgm-n7jFnWkqmA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062200Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4218C5A1BA404E1A315AC0BF8955856E16B3BB128A02046A8757D1DAFC0D3DF5)

The following example is not ready for direct use. Adapt it to meet your specific requirements.

#!/bin/bash
set -ex

JAVA\_HOME=xxx # Specify the installation directory of the JDK.
COMMANDLINE\_TOOL\_DIR=xxx # Specify the installation directory of the command line tool.

# Configure the hvigor and ohpm environment variables.
export PATH=${COMMANDLINE\_TOOL\_DIR}/command-line-tools/bin:$PATH

# Download and configure JDK.
function init\_JDK() {
  if \[ ! -d "${JAVA\_HOME}" \]; then 
     mkdir "${JAVA\_HOME}"
  fi
  cd ${JAVA\_HOME}
  wget --no-check-certificate -q "${jdk\_download\_path}" -O jdk-linux.tar.xz # Download JDK, specifying the actual download path.
  tar -vxf jdk-linux.tar.xz
  JDK\_DIR=xxx # Specify the directory in the compressed JDK package.
  cd ${JDK\_DIR}
  mv -f ./\* .\[^.\]\* ../
  cd ..
  rm -rf JDK\_DIR jdk-linux.tar.xz
  export JAVA\_HOME=${JAVA\_HOME}
  export PATH=$JAVA\_HOME/bin:$PATH
  java -version
}

# Configure the hdc environment variable.
function init\_hdc() {
  export HDC\_HOME=${COMMANDLINE\_TOOL\_DIR}/command-line-tools/sdk/default/openharmony/toolchains # Set the hdc environment variable. hdc is stored in toolchains.
  export PATH=$HDC\_HOME:$PATH
}

# Install ohpm. Skip this step if ohpm already exists in the image.
function init\_ohpm() {
    ohpm -v
    # Configure the address of the ohpm repository.
    ohpm config set registry https://ohpm.openharmony.cn/ohpm/
}

# Initialize related paths.
PROJECT\_PATH=xxx  # Project directory.
# Go to the package directory and install the dependency.
function ohpm\_install {
    cd $1
    ohpm install
}
# Environment adaptation
function buildHAP() {
# Install the third-party library dependencies based on service requirements.
    ohpm\_install "${PROJECT\_PATH}"
    ohpm\_install "${PROJECT\_PATH}/entry"
    ohpm\_install "${PROJECT\_PATH}/xxx"
    # Run commands based on your service requirements. For details, see the commands in the DevEco Studio build log.
    cd ${PROJECT\_PATH}
    hvigorw clean --no-daemon
    hvigorw assembleHap --mode module -p product=default -p debuggable=false --no-daemon # It is recommended that --no-daemon be added to the end of the command.
}
function install\_hap() {
    hdc file send "${PROJECT\_PATH}/entry/build/default/outputs/default/entry-default-signed.hap" "data/local/tmp/entry-default-signed.hap"
    hdc shell bm install -p "data/local/tmp/entry-default-signed.hap" 
    hdc shell rm -rf "data/local/tmp/entry-default-signed.hap"
    hdc shell aa start -a MainAbility -b com.example.myapplication -m entry
}

# Use ohpm to publish the HAR. function upload\_har {
  ohpm publish pkg.har
}

function main {
  local startTime=$(date '+%s')
  init\_JDK
  init\_hdc
  init\_ohpm
  buildHAP
  install\_hap
  upload\_har
  local endTime=$(date '+%s')
  local elapsedTime=$(expr $endTime - $startTime)
  echo "build success in ${elapsedTime}s..."
}
main

#### Creating a CI Pipeline Offline

If your computer is not connected to the Internet, you can build a pipeline environment by referring to the following steps.

## Installing the pnpm Plugin

1.  On the computer that has Internet access, create an empty folder and in it create the **package.json** file. Enter the following information in the file:
    
    {
      "dependencies": {
        "pnpm": "8.13.1"
      }
    }
    
2.  [Configure environment variables](../../coding-and-debugging/appendix/setting-up-the-proxy/document.md#en-us_topic_0000001056725590_li358362302311). Then open the [CLI](../obtaining-command-line-tools/document.md) and run the **ohpm install** command. The **node\_modules** folder is automatically generated.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/_5NVA6qtRFCmlK4R4mWYDA/en-us_image_0000002532749963.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062200Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=57A8BEC1A7306CC100F7658CCE90807DD56202C21FF28E66362AE8ECE6E9E5C5 "Click to enlarge")
    
3.  Copy the **node\_modules** folder and **package.json** file to the **C:\\Users\\_Username_\\.hvigor\\wrapper\\tools** directory on the computer without Internet access. If the directory does not exist, create one first.
4.  On the computer where Internet access is denied, run the following command to enable the npm offline mode:
    
    npm config set offline true
    

## Installing the npm Plugin

1.  On the computer that has Internet access, create an empty folder and in it create the **package.json** file. Enter the following information in the file:
    
    {
      "dependencies": {
        "ajv": "latest"
      }
    }
    
2.  Open the [CLI](../obtaining-command-line-tools/document.md) and run the **ohpm install** command. The **node\_modules** folder is automatically generated.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/korF-jY1RYqV7vHmtiFfSA/en-us_image_0000002532670009.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062200Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1CC9080ABDDFF72EAF44506D5691785FBB7C1FBAD2B50FF45A553DA8CC45C9DD)
    
3.  Copy the **node\_modules** folder to the project's root directory on the computer without Internet access.

## Installing the ohpm Plugin

For details, see [Installing a Third-Party Library](../../environment-setup/setting-up-the-development-environment-offline/document.md#section208435578175).

## Installing the libGL1 Library

To install the libGL1 library, which is required for using [texture compression](../../building-an-app/configuration-files/project-level-build-profile-json5-file/document.md#section2095319147103) on Linux:

Download the libGL1 library installation package on a computer with Internet access, for example, download **libgl1-mesa-dev** on Ubuntu/Debian and **mesa-libGL-devel** on CentOS/RHEL, then copy the downloaded package to the offline computer for installation.
