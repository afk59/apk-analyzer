# About This Kit

Media Library Kit provides the capabilities of managing albums and media files, including images and videos, to enable your application to quickly display images and play back videos.

#### Available Capabilities

With Media Library Kit, you can manage albums and media files, including creating and accessing albums and modifying media assets in albums.

The following capabilities are opened to all applications:

-   Selecting or saving media assets
    -   [Selecting Media Assets Using Picker](../selecting-media-assets-using-picker/document.md)
    -   [Saving Media Assets](../saving-media-assets/document.md)
-   Managing moving photos
    -   [Accessing and Managing Moving Photos](../moving-photos/accessing-and-managing-moving-photos/document.md)
    -   [Playing Moving Photos with MovingPhotoView](../moving-photos/playing-moving-photos-with-movingphotoview/document.md)
-   Using Picker Components
    -   [Accessing Images/Videos Using PhotoPickerComponent](../accessing-images-videos-using-photopickercomponent/document.md)
    -   [Accessing Albums Using AlbumPickerComponent](../accessing-albums-using-albumpickercomponent/document.md)
    -   [Obtaining the Latest Image/Video Using RecentPhotoComponent](../obtaining-the-latest-image-video-using-recentphotocomponent/document.md)
    -   [Using PickerController to Replace Original Images with Edited Images](../using-pickercontroller-to-replace-original-images-with-edited-images/document.md)

The following capabilities are restrictively open to third-party applications:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/iTO7J-woRkqNm3yrln9dCQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062044Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DD0D34598A258C436AB5A11DB4ED8C1C9498D203273149E0FDB3D426462FA402)

The restrictively open capabilities require [applying for permissions related to the album management module](../restricted-open-capabilities/before-you-start/document.md#requesting-permissions). These permissions are restrictively open. These permissions are restricted permissions, typically not granted to third-party applications. However, if you require these permissions in specific scenarios, submit relevant application materials and apply for permission certificates through AppGallery Connect (AGC).

-   [Managing media assets](../restricted-open-capabilities/managing-media-assets/document.md)
    -   Obtaining media assets
    -   Obtaining image and video thumbnails
    -   Renaming a media asset
-   [Managing user albums](../restricted-open-capabilities/managing-user-albums/document.md)
    -   Obtaining a user album
    -   Renaming a user album
    -   Adding images and videos to a user album.
    -   Obtaining images and videos from a user album
    -   Removing images and videos from a user album
-   [Managing system albums](../restricted-open-capabilities/managing-system-albums/document.md)
    -   Favorites
    -   Video album
-   [Monitoring media asset changes](../restricted-open-capabilities/observing-media-assets/document.md)
    -   Registering a listener for the specified URI
    -   Unregistering a listener for the specified URI

#### Features

-   Simple and efficient development thanks to object-based API design.
-   Integrated device-cloud access management.
-   Precise security control and automatic authorization with Pickers and security component **SaveButton**.
-   Intelligent format conversion completed at the framework layer in a unified manner.

#### Working Principles

The media library receives requests for obtaining or changing media assets from users, verifies the request validity and permissions, interacts with the database if the verification is successful, and returns the result.
