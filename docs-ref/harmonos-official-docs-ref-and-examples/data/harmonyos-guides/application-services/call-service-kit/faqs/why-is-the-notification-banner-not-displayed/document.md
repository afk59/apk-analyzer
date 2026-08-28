# Why Is the Notification Banner Not Displayed?

**Problem**

The [voipCall.reportIncomingCall](https://developer.huawei.com/consumer/en/doc/harmonyos-references/call-voipcall#section13177019143216) API is called to report an incoming call, but the notification banner is not displayed.

**Solution**

1.  Check whether the app has been granted the [notification permission](../../../notification-kit/requesting-notification-authorization/document.md).
2.  Check whether **UIAbility** is inherited. If so, call [pushService.receiveMessage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-pushservice#section125883044911) to receive the incoming call notification message, and after this message is received, call the reporting API.
3.  Check whether **callId** obtained from the incoming call information is the same as that reported to Call Service Kit.
4.  Check whether parameters in **callInfo** are correctly set, for example, the value of **voipCallState** is set to **VOIP\_CALL\_STATE\_RINGING**.
5.  If the fault persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei technical support will get back to you as soon as possible.
