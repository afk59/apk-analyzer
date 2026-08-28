# Why does playing a local video source immediately after adding it to the Video component fail?

There is a delay between loading the resource into the **Video** component and the video playing, as loading takes time. You are advised to write the logic to start playing into the **Video** component's **onPrepared** callback function, so that the video resource plays automatically once prepared.
