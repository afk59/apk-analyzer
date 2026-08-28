# Can child component events be passed to parent components?

Currently, ArkUI does not support event propagation chains. To achieve similar functionality, use @Link or @Provide and @Consume for state synchronization between parent and child components; combined with @Watch, changes to state variables can be passed between components.

**Reference**

[@Link Decorator: Implementing Two-Way Synchronization Between Parent and Child Components](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-link)

[@Provide and @Consume Decorators: Two-Way Synchronization with Descendant Components](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-provide-and-consume)

[@Watch Decorator: Getting Notified of State Variable Changes](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-watch)
