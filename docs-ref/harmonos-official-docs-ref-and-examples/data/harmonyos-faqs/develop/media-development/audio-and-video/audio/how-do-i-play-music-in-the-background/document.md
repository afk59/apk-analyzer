# How do I play music in the background?

AVSession controls media playback. When a third-party application switches to the background or encounters a screen lock event, media playback is forcibly paused and the application is unaware of the pause. To enable the application to continue the playback in the background, request a continuous task and access the AVSession capability, which allows the control panel of the Media Controller to control the playback behavior of third-party applications.

**Reference**

[backgroundTaskManager.startBackgroundRunning](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager#backgroundtaskmanagerstartbackgroundrunning12)

[AVSession Provider](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/using-avsession-developer)
