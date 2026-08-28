# Live View Lifecycle

#### How to Automatically Close the Live View When an App Is Closed

When your app is closed, you can call the [liveViewManager.stopLiveView](https://developer.huawei.com/consumer/en/doc/harmonyos-references/liveview-liveviewmanager#section929145112243) method and set **keepTime** of the [PrimaryData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/liveview-liveviewmanager#section452772611408) instance to **0** to close the live view immediately.

#### How to Obtain the Live View Instance for Local Update and What Are the Restrictions After the Live View Deletion

1\. When a live view is updated locally, you can call the [liveViewManager.getActiveLiveView](https://developer.huawei.com/consumer/en/doc/harmonyos-references/liveview-liveviewmanager#section62361020561) function to obtain the [LiveView](https://developer.huawei.com/consumer/en/doc/harmonyos-references/liveview-liveviewmanager#section411410371767) instance.

2\. To end a live view, you are advised to use the [liveViewManager.stopLiveView](https://developer.huawei.com/consumer/en/doc/harmonyos-references/liveview-liveviewmanager#section929145112243) method. If a live view is deleted by **notificationManager.cancel** or **notificationManager.cancelAll**, the live view can no longer be updated or ended by Live View Kit or Push Kit through this ID.

3\. After the deletion, Live View Kit can use this ID to create another live view immediately, but Push Kit cannot use this ID to create another live view within 12 hours.
