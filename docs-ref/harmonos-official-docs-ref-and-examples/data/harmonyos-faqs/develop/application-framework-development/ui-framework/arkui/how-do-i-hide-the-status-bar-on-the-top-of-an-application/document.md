# How do I hide the status bar on the top of an application?

Use **setWindowSystemBarEnable** in the **onWindowStageCreate** lifecycle callback of UIAbility.

onWindowStageCreate(windowStage: window.WindowStage): void {
  windowStage.getMainWindowSync().setWindowSystemBarEnable(\[\])
  // ...
}

**Reference**

[Experiencing the Immersive Window Feature](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/application-window-stage#experiencing-the-immersive-window-feature)
