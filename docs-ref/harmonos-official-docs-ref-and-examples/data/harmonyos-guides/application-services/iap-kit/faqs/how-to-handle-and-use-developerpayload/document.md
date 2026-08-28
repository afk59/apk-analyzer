# How to Handle and Use developerPayload?

You can set the **developerPayload** field via [PurchaseParameter](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section1340120344598) when creating a purchase or subscription order. This field is typically used to identify which app account initiated the paid transaction, ensuring that the corresponding entitlements are correctly granted to that account.

**developerPayload handling in subscription purchase scenarios**:

-   Initial purchase
    
    If a **developerPayload** is provided during the initial subscription purchase, it will be bound to that subscription and remain unchanged throughout its entire lifecycle.
    

-   Subscription resumption
    
    If a new **developerPayload** is provided during subscription resumption, it will overwrite the original value and be used in all subsequent event notifications. If no new value is provided, the original **developerPayload** remains unchanged.
    

-   Subscription switching
    
    Switching a subscription involves canceling the existing subscription and creating a new one. The new subscription will use the **developerPayload** provided at the time of the switching as its initial value. If no new **developerPayload** is provided, the new subscription will inherit the value from the previous subscription. Subsequent handling of the **developerPayload** follows the same rules as in the initial purchase scenario.
    

-   Operations on the subscription management screen
    
    When users manage their subscriptions through the subscription management screen, such as pausing, canceling, or resuming, the original **developerPayload** remains unchanged. If the user switches to a new subscription on this page, the new subscription will inherit the **developerPayload** from the previous one.
    

**Recommended usage of developerPayload:**

1.  You are advised to use app account–related information as the basis for **developerPayload**.
    
    To align with the principle of data minimization, it is recommended to generate an identifier by applying one-way hashing or encryption to obfuscate the account information, and take the identifier as **developerPayload**. This identifier should be consistently associated with the app account and remain valid throughout its lifecycle.
    
2.  Because **developerPayload** of subscriptions can be updated and subscriptions may have long lifecycles, you are strongly advised not to use the self-generated order ID as **developerPayload** to determine subscription ownership. If the transaction becomes invalid or is lost, it may be impossible to reliably identify the associated subscription.
