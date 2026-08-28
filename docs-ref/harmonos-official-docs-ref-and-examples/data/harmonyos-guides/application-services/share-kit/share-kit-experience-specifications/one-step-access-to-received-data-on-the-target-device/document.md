# One-Step Access to Received Data on the Target Device

To ensure better receiving experience on the Huawei Share target device and standardize the experience of direct access to the received shared data, the target device processes the received data according to the following rules.

| 
Receiving Capability

 | 

Data Type

 | 

Storage Location

 | 

Preview Mode

 |
| :-- | :-- | :-- | :-- |
| 

One-step access

 | 

Media (only image and video files)

 | 

PCs/2-in-1 devices: Huawei Share directory in the file manager

Other devices: Huawei Share album in the gallery

 | 

PCs/2-in-1 devices: The received files are highlighted in the file manager.

Other devices: The received files are in large image preview mode in the gallery.

 |
| 

Link

 | 

App Linking

 | 

N/A

 | 

Directly goes to a specified in-app page. If the app is not installed, the browser or AppGallery is started (depending on the App Linking configuration).

 |
| 

Deep link

 | 

N/A

 | 

Directly goes to a specified in-app page. If the app is not installed, a pop-up message is displayed to notify the user.

 |
| 

Common link (other HTTP/HTTPS links except the special links identified by the system)

 | 

N/A

 | 

Opens the corresponding link in the browser.

 |
| 

Text

 | 

Stored as a TXT file in the Huawei Share directory in the file manager

 | 

The file is opened in preview mode.

 |
| 

File

 | 

Huawei Share directory in the file manager

 | 

If there is only one file, the file is opened in preview mode. If there are multiple files, the files are highlighted.

 |
| 

Custom type (excluding the UTD types preconfigured in the system)

 | 

Huawei Share directory in the file manager

 | 

If a compatible app is available, it launches directly. If no such app is available, a message is displayed.

 |
| 

Receiving data in sandbox mode

 | 

Files (including preconfigured and custom file types)

 | 

Specified directory in the app sandbox

 | 

The app handles the preview.

 |

#### Direct Access to the Specified App

Starting from version 6.0.0(20) Beta3, Tap to Transfer supports the capability of starting a specified app.

In addition to the preceding default direct access modes, apps under the same developer account support the following startup rules:

-   Preferential direct access to the app with the same package name: If the receiver has installed the same app as the sender and can start the app (meeting [Matching Rules of Implicit Want](../../../../application-framework/ability-kit/stage-model-development/stage-model-application-components/want/matching-rules-of-explicit-want-and-implicit-want/document.md#matching-rules-of-implicit-want)), the app is started preferentially.
-   A specified app under the same developer account (**developerId**) can be preferentially started by configuring the [module.json5 configuration file](../../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md).

## Restrictions on Capabilities

-   Only apps under the same developer account (**developerId**) are supported.
-   Sharing of media files and compressed packages is not supported.
-   Only one file can be shared at a time.
-   Only Tap to Transfer is supported.

## Configuration Example

Configure [metadata](../../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md#metadata) in the configuration file **src/main/module.json5** to implement the feature.

-   **shareType**: used for group matching. The matching rule takes effect only when the host and target apps are configured with the same **shareType** value. Only one value can be configured. If multiple values are configured, only the first one takes effect.
-   **shareBundleName**: package name of the app to be started. Multiple values can be configured. When the **shareType** values are the same, the system will match the first installed and launchable app (meeting [Matching Rules of Implicit Want](../../../../application-framework/ability-kit/stage-model-development/stage-model-application-components/want/matching-rules-of-explicit-want-and-implicit-want/document.md#matching-rules-of-implicit-want)) according to the order of elements in the array, and prioritize launching that app.

{
  "module": {
    "abilities": \[
      {
        "name": "EntryAbility",
        "srcEntry": "./ets/entryability/EntryAbility.ets",
        "startWindowIcon": "$media:launcher",
        "startWindowBackground": "$color:start\_window\_background",
        "exported": true,
        "skills": \[
          {
            "entities": \[
              "entity.system.home",
            \],
            "actions": \[
              "ohos.want.action.viewData"
            \],
            "uris": \[
              {
                "scheme": "file",
                "linkFeature": "FileOpen",
                "type": "org.openxmlformats.wordprocessingml.document",
                "maxFileSupported": 1
              }
            \],
            "domainVerify": true
          }
        \]
      },
    \],
    "metadata": \[
      {
        "name": "shareType",
        "value": "sharekitModel",
      },
      {
        "name": "shareBundleName",
        "value": "com.example.sharekitPhone",
      },
      {
        "name": "shareBundleName",
        "value": "com.example.sharekitPc",
      }
    \]
  }
}
