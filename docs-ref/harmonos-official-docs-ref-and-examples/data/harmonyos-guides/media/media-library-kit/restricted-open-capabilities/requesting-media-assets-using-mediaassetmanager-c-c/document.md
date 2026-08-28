# Requesting Media Assets Using MediaAssetManager (C/C++)

You can use **MediaAssetManager** to copy a media asset to a sandbox directory. This topic walks you through on how to use **MediaAssetManager** to copy an image to the specified sandbox directory.

The procedure is as follows: 1.

Create a MediaAssetManager instance. 2.

Set parameters for requesting an image and request the image.

3\. (Optional) Cancel the request.

#### How to Develop

Add the dynamic library in the CMake script.

target\_link\_libraries(sample PUBLIC libmedia\_asset\_manager.so)

Include the [media\_asset\_manager\_capi.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-media-asset-manager-capi-h) and [media\_asset\_base\_capi.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-media-asset-base-capi-h) header files to use the APIs of MediaAssetManager.

For details about the APIs, see [MediaAssetManager APIs](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-mediaassetmanager).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/Q44vY2_qTEqQb3jexZnn8A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062045Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=54A2616ECE14A03F4A5AAED82AD497C3FD6A93672F54D953F20136E3DB346EE6)

The application must have the ohos.permission.READ\_IMAGEVIDEO permission. For details, see [Before You Start](../before-you-start/document.md).

1.  Call **OH\_MediaAssetManager\_Create()** to create a MediaAssetManager instance.
2.  Set the URI of the image to request, destination URI, asset requesting policy, and callback used to return the result.
3.  Call **OH\_MediaAssetManager\_RequestImageForPath()** to copy the image to the target URI.
4.  (Optional) Call **OH\_MediaAssetManager\_CancelRequest()** to cancel the request.

#### Example

#include "multimedia/media\_library/media\_asset\_base\_capi.h"
#include "multimedia/media\_library/media\_asset\_manager\_capi.h"
#include <stdio.h>
#include <string.h>

const char ERROR\_REQUEST\_ID\[UUID\_STR\_MAX\_LENGTH\] = "00000000-0000-0000-0000-000000000000";

// Callback to be invoked when the request image is ready.
void OnDataPrepared(int32\_t result, MediaLibrary\_RequestId requestIdStruct)
{
    printf("OnDataPrepared requestId: %s result: %d\\n", requestIdStruct.requestId, result);
}

int main()
{
    // Create a MediaAssetManager instance.
    OH\_MediaAssetManager \*manager = OH\_MediaAssetManager\_Create();
    if (manager == nullptr) {
        // Exception handling.
        printf("Get MediaAssetManager failed.\\n");
    } else {
        // Set the callback.
        OH\_MediaLibrary\_OnDataPrepared callback = OnDataPrepared;
        
        // Set the delivery mode.
        MediaLibrary\_RequestOptions options;
        options.deliveryMode = MEDIA\_LIBRARY\_HIGH\_QUALITY\_MODE;

        // Preset the URI of the image with the default high quality. The URI used is an example only. You need to create or obtain the URI based on actual requirements.
        const char \*srcUri = "file://media/Photo/87/VID\_1712195295\_025/request\_image\_src.jpg";

        // URI of the destination directory. The URI used is an example. You need to create or obtain the URI based on actual requirements.
        const char \*destUri = "file://media/Photo/9/IMG\_1712195237\_008/request\_image\_dest.jpg";

        // Request the image and write it to the destination directory.
        MediaLibrary\_RequestId requestIdStruct = OH\_MediaAssetManager\_RequestImageForPath(manager, srcUri,
            options, destUri, callback);

        if (strcmp(requestIdStruct.requestId, ERROR\_REQUEST\_ID) == 0) {
            // Exception handling.
            printf("Request image failed requestId: %s\\n", requestIdStruct.requestId);
        } else {
            // Print the request ID if the request is successful.
            printf("Request image success, requestId: %s\\n", requestIdStruct.requestId);

            // Call CancelRequest() to cancel the request being processed.
            // Note that OH\_MediaAssetManager\_CancelRequest is optional.
            bool ret = OH\_MediaAssetManager\_CancelRequest(manager, requestIdStruct);
        }
    }
    return 0;
}
