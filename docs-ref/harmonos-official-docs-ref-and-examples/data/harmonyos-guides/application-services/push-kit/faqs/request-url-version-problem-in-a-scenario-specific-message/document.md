# Request URL Version Problem in a Scenario-specific Message

In the [request body](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-struct) of a scenario-specific message, if the API request URL version is V3 (https://push-api.cloud.huawei.com/v3/\[projectId\]/messages:send), the message can be pushed to HarmonyOS Next/5.x and later versions. If the API request URL version is V2 (https://push-api.cloud.huawei.com/v2/\[projectId\]/messages:send), the message can be pushed only to HarmonyOS 3.x/4.x.

Use the API request URL of the V3 version (**https://push-api.cloud.huawei.com/****v3****/_\[projectId\]_/messages:send**) to push messages.
