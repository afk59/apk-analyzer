# Node-API FAQs

#### Stability

1.  [How do I troubleshoot the issue that an application often crashes during running?](../faqs-about-stability/document.md#how-do-i-troubleshoot-the-issue-that-an-application-often-crashes-during-running)
2.  [How to handle thread safety issues when the ArkTS method is concurrently called in the thread pool?](../faqs-about-stability/document.md#how-to-handle-thread-safety-issues-when-the-arkts-method-is-concurrently-called-in-the-thread-pool)
3.  [What should I do if the content of napi\_value changes?](../faqs-about-stability/document.md#what-should-i-do-if-the-content-of-napi_value-changes)
4.  [Is there a method to obtain the latest napi\_env?](../faqs-about-stability/document.md#is-there-a-method-to-obtain-the-latest-napi_env)
5.  [What should I do if napi\_add\_env\_cleanup\_hook is called incorrectly?](../faqs-about-stability/document.md#what-should-i-do-if-napi_add_env_cleanup_hook-is-called-incorrectly)

#### Memory Leak

1.  [Is there any mechanism to check whether napi\_ref leaks?](../faqs-about-memory-leaks/document.md#is-there-any-mechanism-to-check-whether-napi_ref-leaks)
2.  [How do I locate and resolve memory leaks during Node-API development?](../faqs-about-memory-leaks/document.md#how-do-i-locate-and-resolve-memory-leaks-during-node-api-development)
3.  [For details about parameter leaks, see napi\_open\_handle\_scope and napi\_close\_handle\_scope](../../node-api-guides/performing-lifecycle-management-using-node-api/document.md).
4.  [What should I do if memory leaks when napi\_threadsafe\_function is used?](../faqs-about-memory-leaks/document.md#what-should-i-do-if-memory-leaks-when-napi_threadsafe_function-is-used)

#### Basic Functionalities

1.  [What should I do if the module fails to be loaded and the error message "Error message: is not callable" is displayed?](../faqs-about-basic-functionalities/document.md)
2.  [How to ensure the order of asynchronous tasks in scenarios where a large number of ArkTS methods need to be called for communication?](../faqs-about-basic-functionalities/document.md#how-to-ensure-the-order-of-asynchronous-tasks-in-scenarios-where-a-large-number-of-arkts-methods-need-to-be-called-for-communication)
3.  [Is there a convenient way to call back ArkTS?](../faqs-about-basic-functionalities/document.md#is-there-a-convenient-way-to-call-back-arkts)
4.  [How do I invoke a function transferred from ArkTS in a C++ subthread?](https://developer.huawei.com/consumer/en/doc/harmonyos-faqs/faqs-ndk-26)
5.  [How to ensure the correct mapping of data types and the security of memory management?](../faqs-about-basic-functionalities/document.md#how-to-ensure-the-correct-mapping-of-data-types-and-the-security-of-memory-management)
6.  [Integrating a Third-Party Dynamic Link Library](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-dynamic-link-library)
7.  [What are the error codes of the napi\_get\_uv\_event\_loop API?](../faqs-about-basic-functionalities/document.md#what-are-the-error-codes-of-the-napi_get_uv_event_loop-api)
8.  [Must a function be passed to the native layer when the native layer calls the object method of the ArkTS layer?](../faqs-about-basic-functionalities/document.md#must-a-function-be-passed-to-the-native-layer-when-the-native-layer-calls-the-object-method-of-the-arkts-layer)
9.  [Can I call an ArkTS method and obtain the result?](../faqs-about-basic-functionalities/document.md#can-i-call-an-arkts-method-and-obtain-the-result)
10.  [Whether there is a napi\_get\_value\_string\_utf8 API or capability that does not need the copy operation?](../faqs-about-basic-functionalities/document.md#whether-there-is-a-napi_get_value_string_utf8-api-or-capability-that-does-not-need-the-copy-operation)
11.  [What are the precautions for using napi\_env in multi-thread mode?](../faqs-about-basic-functionalities/document.md#what-are-the-precautions-for-using-napi_env-in-multi-thread-mode)
12.  [What should I do if the napi\_call\_threadsafe\_function execution sequence does not meet the expectation?](../faqs-about-basic-functionalities/document.md#what-should-i-do-if-the-napi_call_threadsafe_function-execution-sequence-does-not-meet-the-expectation)
13.  [What should I do if an error message "undefined" is displayed on the ArkTS side?](../faqs-about-basic-functionalities/document.md#what-should-i-do-if-an-error-message-undefined-is-displayed-on-the-arkts-side)
14.  [What should I do if the API execution result is unexpected?](../faqs-about-basic-functionalities/document.md#what-should-i-do-if-the-api-execution-result-is-unexpected)
15.  [What are the differences between the lifecycle of napi\_value and napi\_ref?](../faqs-about-basic-functionalities/document.md#what-are-the-differences-between-the-lifecycle-of-napi_value-and-napi_ref)
16.  [How do I locate the fault if the return value of a Node-API is not "napi\_ok"?](../faqs-about-basic-functionalities/document.md#how-do-i-locate-the-fault-if-the-return-value-of-a-node-api-is-not-napi_ok)
17.  [How do I ensure that objects wrapped by napi\_wrap are destructed in the expected order?](../faqs-about-basic-functionalities/document.md#how-do-i-ensure-that-objects-wrapped-by-napi_wrap-are-destructed-in-the-expected-order)
18.  [What should I do if the napi\_call\_threadsafe\_function callback task is not executed?](../faqs-about-basic-functionalities/document.md#what-should-i-do-if-the-napi_call_threadsafe_function-callback-task-is-not-executed)
