# Common UI Application Freezing Issues

This document summarizes common ArkUI API misuse scenarios that may cause application freezes, and provides guidance to help you avoid similar issues during development.

#### Using syncLoad for Network Image Downloads

**Symptom**

The application becomes unresponsive, and the AppFreeze log shows a main thread call stack such as:

#00 pc 00000000001b5904 /system/lib/ld-musl-aarch64.so.1(\_\_timedwait\_cp+192)
#01 pc 00000000001b7908 /system/lib/ld-musl-aarch64.so.1(\_\_pthread\_cond\_timedwait+188)
#02 pc 00000000000c11c0 /system/lib64/libc++.so(std::\_\_h::condition\_variable::\_\_do\_timed\_wait(std::\_\_h::unique\_lock<std::\_\_h::mutex>&, std::\_\_h::chrono::time\_point<std::\_\_h::chrono::system\_clock, std::\_\_h::chrono::duration<long long, std::\_\_h::ratio<1l, 1000000000l>>>)+108)
#03 pc 0000000000019ed0 /system/lib64/platformsdk/libace\_network.z.so(std::\_\_h::cv\_status std::\_\_h::condition\_variable::wait\_for<long long, std::\_\_h::ratio<1l, 1000000000l>>(std::\_\_h::unique\_lock<std::\_\_h::mutex>&, std::\_\_h::chrono::duration<long long, std::\_\_h::ratio<1l, 1000000000l>> const&)+92)
#04 pc 0000000000019e5c /system/lib64/platformsdk/libace\_network.z.so
#05 pc 000000000001bc10 /system/lib64/platformsdk/libace\_network.z.so(OHOS::Ace::DownloadManagerImpl::HandleDownloadResult(bool, OHOS::Ace::DownloadCallback&&, std::\_\_h::shared\_ptr<OHOS::Ace::DownloadCondition> const&, int, std::\_\_h::basic\_string<char, std::\_\_h::char\_traits<char>, std::\_\_h::allocator<char>> const&)+248)
#06 pc 0000000000018564 /system/lib64/platformsdk/libace\_network.z.so(OHOS::Ace::DownloadManagerImpl::DownloadSync(OHOS::Ace::DownloadCallback&&, std::\_\_h::basic\_string<char, std::\_\_h::char\_traits<char>, std::\_\_h::allocator<char>> const&, int, int)+1096)
#07 pc 000000000096f4a8 /system/lib64/platformsdk/libace\_compatible.z.so(OHOS::Ace::NG::ImageLoadingContext::PerformDownload()+448)

**Possible Causes**

Enabling **syncLoad** for network image downloads forces synchronous loading, which blocks the main thread. Under poor network conditions, this can result in prolonged blocking and application freezes.

**Solution**

Do not set **syncLoad** to **true** when loading images from the network.

**Reference**

[syncLoad](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-image#syncload8)

#### Executing Time-Consuming Tasks on the Main UI Thread

**Symptom**

The application becomes unresponsive, and the AppFreeze log shows a non-main thread call stack such as:

#00 pc 00000000001b9a7c /system/lib/ld-musl-aarch64.so.1(\_\_timedwait\_cp+148)
#01 pc 00000000001bbacc /system/lib/ld-musl-aarch64.so.1(pthread\_cond\_timedwait+168)
#02 pc 00000000000c115c /system/lib64/libc++.so(std::\_\_h::condition\_variable::wait(std::\_\_h::unique\_lock<std::\_\_h::mutex>&)+20)
#03 pc 00000000000c1d1c /system/lib64/libc++.so(std::\_\_h::\_\_assoc\_sub\_state::\_\_sub\_wait(std::\_\_h::unique\_lock<std::\_\_h::mutex>&)+48)
#04 pc 0000000000baf2e4 /system/lib64/platformsdk/libace\_compatible.z.so(std::\_\_h::\_\_assoc\_state<int>::copy()+64)
#05 pc 0000000000baf0e0 /system/lib64/platformsdk/libace\_compatible.z.so(OHOS::Ace::CancelableCallback<void ()>::WaitUntilComplete(std::\_\_h::chrono::duration<long long, std::\_\_h::ratio<1l, 1000l>>)+120)
#06 pc 0000000000baed68 /system/lib64/platformsdk/libace\_compatible.z.so
#07 pc 0000000000bae640 /system/lib64/platformsdk/libace\_compatible.z.so(OHOS::Ace::TaskExecutor::PostSyncTask(std::\_\_h::function<void ()>&&, OHOS::Ace::TaskExecutor::TaskType, std::\_\_h::basic\_string<char, std::\_\_h::char\_traits<char>, std::\_\_h::allocator<char>> const&, OHOS::Ace::PriorityType) const+220)
#08 pc 000000000107d9d0 /system/lib64/platformsdk/libace\_compatible.z.so

**Possible Causes**

Synchronous tasks are dispatched to the main thread, which must complete them before continuing. This often occurs when the main thread executes coarse-grained tasks unrelated to the current stack, typically involving IPC interlocks across multiple processes.

**Solution**

This stack trace is part of an interlock chain that cannot be resolved directly. To address the issue, try the following: Analyze what the target thread is waiting for. Determine whether the task is time-consuming or involves synchronous waiting. Resolve the underlying cause from other points in the interlock chain.
