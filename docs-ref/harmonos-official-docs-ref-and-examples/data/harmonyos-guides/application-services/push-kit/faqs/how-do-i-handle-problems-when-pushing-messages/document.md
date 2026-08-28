# How Do I Handle Problems When Pushing Messages?

When you use REST APIs to push messages, you may encounter some problems. In case of any problem, locate the fault following this process:

1.  Check whether the [message push API](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-struct) URL (https://push-api.cloud.huawei.com/**v3**/**\[projectId\]**/messages:send) is correct.
    -   Use the message push API URL of the V3 version but not the V1 or V2 version. For details, please refer to [Request URL Version Problem in a Scenario-specific Message](../request-url-version-problem-in-a-scenario-specific-message/document.md).
    -   Check whether the **projectId** in the push API URL is the same as that of the project to which the current app belongs. If not, update **projectId** in the push API URL, [regenerate a JWT](../../device-cloud-debugging/generating-a-jwt-based-on-a-service-account/document.md), complete operations in [Obtaining a Push Token](../../preparations/obtaining-a-push-token/document.md) again, and send the message again.
2.  If the message push API returns an error code, rectify the fault based on [Service Response Codes](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-response#section204526160327).
3.  If the message push API is successfully called but the message is not displayed on the target device, rectify the fault by referring to [Why Does the Target Device Fail to Receive a Push Message After the Push API Is Successfully Called on the Cloud?](../why-does-the-target-device-fail-to-receive-a-push-message-after-the-push-api-is-/document.md).
