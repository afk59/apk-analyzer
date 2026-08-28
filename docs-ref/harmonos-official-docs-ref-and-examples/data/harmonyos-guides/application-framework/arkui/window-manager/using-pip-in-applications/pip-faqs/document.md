# PiP FAQs

#### How can I play multiple video streams in PiP?

To play multiple video streams in PiP, you can encapsulate each stream into a NodeController through a custom node. Then, when setting up PiP, configure the NodeController as a custom node controller ([customUIController](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-pipwindow#pipconfiguration)) to playback of multiple video streams.

#### How do I switch nodes in PiP?

You can use the typeNode approach for PiP, which allows you to update the PiP nodes using the [updateContentNode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-pipwindow#updatecontentnode18) API.

#### What should I do when audio keeps playing in the background after PiP is closed?

If the application requests a continuous task, deleting the PiP window by dragging it to the trash bin or tapping the close button will not stop the application process. To handle this, you should listen for the PiP lifecycle and proactively close the task or process upon receiving the STOPPED event.
