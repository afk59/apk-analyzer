# Are the logs returned by the OH\_LOG\_SetCallback API of the HiLog module the same as HiLog logs flushed to disk by the system?

The **OH\_LOG\_SetCallback** API returns all logs in the application running process that are specified by the log output level. The returned logs are not controlled by the system threshold mechanism.

HiLog logs flushed to disk by the system are the logs of all system processes that specified by the log output level, including the logs of the application running process listened for by the **OH\_LOG\_SetCallback** API. The logs flushed to disk are controlled by the system threshold mechanism, and the logs that exceed the threshold cannot be exported or saved.

Therefore, the number of logs returned by **OH\_LOG\_SetCallback** must be greater than or equal to the number of application logs flushed to disk.
