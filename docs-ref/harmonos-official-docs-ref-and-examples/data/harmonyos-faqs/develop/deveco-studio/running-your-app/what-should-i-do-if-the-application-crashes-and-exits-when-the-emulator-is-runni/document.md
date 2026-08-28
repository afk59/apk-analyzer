# What should I do if the application crashes and exits when the Emulator is running?

**Symptom**

The application exits abnormally during debugging or running.

**Solution**

1.  The Emulator is different from the real device. Ensure that you are using the specifications and capabilities supported by the Emulator. If the application crashes when running in the Emulator, the possible cause is that the capability used in the current code is not supported. If the function implemented by the problematic code segment is not the target of debugging, you can take the following measures to avoid the issue:
    -   Use the **try-catch** statement to capture exceptions.
    -   Check whether the device is an emulator. For details, see [How do I distinguish real devices from emulators in applications?](../how-do-i-distinguish-real-devices-from-emulators-in-applications/document.md) For emulator debugging scenarios, use the **if** statement to skip abnormal code segments.
2.  If a third-party shared library (.so) is used in the application, the x86 or Arm version corresponding to the emulator is required.
