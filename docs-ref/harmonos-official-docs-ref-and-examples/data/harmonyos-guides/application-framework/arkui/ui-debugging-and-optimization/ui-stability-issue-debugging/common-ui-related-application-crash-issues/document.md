# Common UI-Related Application Crash Issues

This topic outlines frequent misuse patterns of ArkUI APIs that may lead to application crashes. It is intended to help you recognize and avoid common pitfalls during development.

#### Premature Release of the OH\_NativeXComponent Callback Object

**Symptom**

The application crashes with a cppcrash stack trace resembling the following:

Reason:Signal:SIGSEGV(SEGV\_ACCERR)@0x0000005c5f09a280

#00 pc 0000000000ac9280 \[anon:native\_heap:jemalloc\]
#01 pc 0000000002615120 /system/lib64/platformsdk/libace\_compatible.z.so(OHOS::Ace::NG::XComponentPattern::OnSurfaceDestroyed()+468)
#02 pc 0000000002614b18 /system/lib64/platformsdk/libace\_compatible.z.so(OHOS::Ace::NG::XComponentPattern::OnDetachFromFrameNode(OHOS::Ace::NG::FrameNode\*)+88)
#03 pc 0000000000875294 /system/lib64/platformsdk/libace\_compatible.z.so(OHOS::Ace::NG::FrameNode::~FrameNode()+264)

The final call frame of **libace\_compatible.z.so** typically belongs to one of the **XComponentPattern** APIs: **OnSurfaceCreated**, **OnSurfaceChanged**, **OnSurfaceDestroyed**, or **DispatchTouchEvent**. Frame **#00** often points to an invalid address, with **pc** matching the last few digits of the address following **Reason** in the signal line. This indicates a corrupted function pointer.

**Possible Causes**

The application registers a callback object of type [OH\_NativeXComponent\_Callback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ent-native-xcomponent-oh-nativexcomponent-callback) using [OH\_NativeXComponent\_RegisterCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-interface-xcomponent-h#oh_nativexcomponent_registercallback). Internally, this callback is stored as a raw pointer within the **XComponentPattern**. The callbacks is controlled by the application. If the application destroys the **OH\_NativeXComponent\_Callback** object prematurely, the pointer becomes invalid, leading to a use-after-free error.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/jdT8Am54TDa8I4IcE-PFag/en-us_image_0000002568684687.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061944Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C2012A6E8F0AFF711486F28DB924CBCEEA0FAF3DFD74A46F93C4A3285FBCAD41)

**Solution**

The **onSurfaceDestroy** callback is the final callback invoked during the destruction of the **XComponentPattern**; its execution signifies that the component has been destroyed. Therefore, the application must ensure that these callback objects remain valid until after the **onSurfaceDestroy** callback has been executed.

**Reference**

[OH\_NativeXComponent Native XComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-nativexcomponent-native-xcomponent)

#### Premature Release of the OH\_NativeXComponent Object

**Symptom**

The application crashes with a cppcrash stack trace resembling the following:

#00 pc 00000000000c8b3c /system/lib64/libc++.so(std::\_\_h::basic\_string<char, std::\_\_h::char\_traits<char>, std::\_\_h::allocator<char>>::basic\_string(std::\_\_h::basic\_string<char, std::\_\_h::char\_traits<char>, std::\_\_h::allocator<char>> const&)+16)
#01 pc 0000000000034f64 /system/lib64/libace\_ndk.z.so(OH\_NativeXComponent::GetXComponentId(char\*, unsigned long\*)+76)
#02 pc 00000000000867c0 /data/storage/el1/bundle/libs/arm64/librenderer.so

The top of the stack shows frames related to **libace\_ndk.z.so(OH\_NativeXComponent::XXX...)**, and the subsequent frame is within the application's own shared object (.so).

**Possible Causes**

The application holds a raw pointer to an **OH\_NativeXComponent** object. If this object is destroyed but the pointer is still used to invoke methods, a use-after-free crash occurs.

**Solution**

Do not access any **OH\_NativeXComponent** APIs after the **onSurfaceDestroy** callback has completed. This callback signals the end of the component's lifecycle.

**Reference**

[OH\_NativeXComponent Native XComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-nativexcomponent-native-xcomponent)

#### Missing Matching @Provide for @Consume

**Symptom**

The application crashes with a JS crash stack trace during initialization.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/qmoUYQYdQfSYNob6CW7szA/en-us_image_0000002568764697.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061944Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=733542CB12502D5313F0884AB81E33F722EA2AE6B527A75B99C627041D62896F)

**Possible Causes**

The @Consume decorator requires a matching @Provide variable with the same key. If no such @Provide variable exists, initialization fails.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/byu_8gUzRReYLIGvJUNf8g/en-us_image_0000002537764972.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061944Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0FFCBB65A37B30FDF805E10AD7A6231200F7BB87A0E041B0996CB9A44EE2C4E0)

**Solution**

When examining the component tree, ensure that variables decorated with @Provide are defined in ancestor components. These variables are considered state variables provided to descendants. Variables decorated with @Consume are used in descendant components to bind to the variables provided by ancestor components. If the key bound by @Consume is not defined in any ancestor component, it will cause this error. Investigate from the usage perspective.

**Reference**

[@Provider and @Consumer Decorators: Synchronizing Across Component Levels in a Two-Way Manner](../../../ui-development-arkts-based-declarative-development-paradigm/ui-paradigm-state-management/state-management-v2/component-state-management/provider-and-consumer-decorators-synchronizing-across-component-levels-in-a-two-/document.md)

#### Incorrect Data Source Type for @Link

**Symptom**

The application crashes with a JS crash stack trace during initialization.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/nG4WNKiQRY6UW6eZ6mfNfA/en-us_image_0000002537924912.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061944Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3955A82756775CCB419118FE0BFC31DCFDDCC4C327B3DB84DE0A5DDA58757098)

**Possible Causes**

During initialization, @Link registers itself with the parent component and calls the parent component's **addSubscriber** API. If the type of the data source does not exactly match the type of the @Link variable, or if a constant is used to initialize @Link, this API cannot be called, resulting in an "is not callable" error.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/ahUDY40JTlanUsd0kFdGQQ/en-us_image_0000002568684689.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061944Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CD2A5903FEF4522137706C634FF8F5D715C2DBBF7863D2C61F6429DE966A0840)

**Solution**

Verify that the data source bound to @Link is a state variable and that its type matches the @Link declaration.

**Reference**

[@Link Decorator: Implementing Two-Way Synchronization Between Parent and Child Components](../../../ui-development-arkts-based-declarative-development-paradigm/ui-paradigm-state-management/state-management-v1/component-state-management/link-decorator-two-way-synchronization-between-parent-and-child-components/document.md)

#### Missing allowOverride in @Provide Declaration

**Symptom**

The application crashes with a JS crash stack trace during initialization.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/IsTdRUqkQVeR-kvuYhFm9g/en-us_image_0000002568764699.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061944Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C6B61B48C860528D9220F9D62410A93E43F5AFE3C65440F279806729AE9CD47E)

**Possible Causes**

Overriding an @Provide variable requires the declaration of **allowOverride**. After declaration, both the alias and the property name can be overridden. If **allowOverride** is not declared and a duplicate alias or property name exists, it will cause an error (duplicate @Provide property with name xxxxx).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/eh36bSXeToeI1aZhA-g7rA/en-us_image_0000002537764974.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061944Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=38E5D02468F0B6B84C49E8BCE4EBEC820991E8C2F14322E5F7775144729EE203)

**Solution**

Use **allowOverride** when declaring @Provide variables that may be overridden. This enables child components using @Consume to bind to the nearest matching @Provide in the hierarchy based on the alias or property name.

**Reference**

[@Provider and @Consumer Decorators: Synchronizing Across Component Levels in a Two-Way Manner](../../../ui-development-arkts-based-declarative-development-paradigm/ui-paradigm-state-management/state-management-v2/component-state-management/provider-and-consumer-decorators-synchronizing-across-component-levels-in-a-two-/document.md)
