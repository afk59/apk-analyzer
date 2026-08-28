# Audio Workgroup Management

The audio workgroup is a set of APIs that help the system identify key audio threads within an application through tagging. By providing key audio threads and workgroup runtime information, the system can ensure healthier operation of audio threads.

#### How to Use

For audio playback applications, you need to create an audio workgroup first and then periodically inform the system of the workgroup's runtime information. After the work is completed, it is necessary to clean up the audio workgroup.

## Obtaining an AudioResourceManager Instance

Before calling any API of OH\_AudioWorkgroup, you must use [OH\_AudioManager\_GetAudioResourceManager](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audio-resource-manager-h#oh_audiomanager_getaudioresourcemanager) to obtain an OH\_AudioResourceManager instance.

#include <ohaudio/native\_audio\_resource\_manager.h>

OH\_AudioResourceManager \*resMgr;
OH\_AudioManager\_GetAudioResourceManager(&resMgr);

## Creating an Audio Workgroup and Adding Key Threads

Call [OH\_AudioResourceManager\_CreateWorkgroup](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audio-resource-manager-h#oh_audioresourcemanager_createworkgroup) to create an audio workgroup, and then call [OH\_AudioWorkgroup\_AddCurrentThread](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audio-resource-manager-h#oh_audioworkgroup_addcurrentthread) to add key threads to the workgroup.

#include <chrono>

int32\_t tokenId;
OH\_AudioWorkgroup \*grp = nullptr;

OH\_AudioResourceManager\_CreateWorkgroup(resMgr, "workgroup", &grp);
OH\_AudioWorkgroup\_AddCurrentThread(grp, &tokenId);

## Notifying the System of Workgroup Start and End

When an audio workgroup begins a cycle of work, you can notify the system of the task's start time and expected end time. When the workgroup finishes its work for the current cycle, notify the system that the task has ended.

constexpr static uint64\_t intervalMs = 20;
bool threadShouldRun = true;

while (threadShouldRun) {
  auto now = std::chrono::system\_clock::now().time\_since\_epoch();
  auto startTimeMs = std::chrono::duration\_cast<std::chrono::milliseconds>(now).count();

  OH\_AudioWorkgroup\_Start(grp, startTimeMs, startTimeMs + intervalMs);
  
  // Process audio data.

  OH\_AudioWorkgroup\_Stop(grp);
}

## Cleanup After Workgroup Task Completion

// Remove the thread from the workgroup when it is no longer required.
OH\_AudioWorkgroup\_RemoveThread(grp, tokenId);

OH\_AudioResourceManager\_ReleaseWorkgroup(resMgr, grp);
grp = nullptr;
