# What control capabilities are supported after casting?

After a successful casting, the following control capabilities are supported on the local device: play, pause, next, previous, fast-forward, rewind, progress control, and volume control.

The following control capabilities are supported on the remote device (large-screen device): play, pause, next, previous, fast-forward, rewind, and progress control.

The following capabilities are not supported: video resolution switching, audio track switching, speed adjustment, and bullet comments.

Supported API: [sendControlCommand](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-avsession-avsessioncontroller#sendcontrolcommand10)(command: AVCastControlCommand, callback: AsyncCallback<void>): void
