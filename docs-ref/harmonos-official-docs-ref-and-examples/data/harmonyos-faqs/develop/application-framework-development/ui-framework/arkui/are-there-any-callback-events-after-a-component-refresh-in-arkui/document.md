# Are there any callback events after a component refresh in ArkUI?

In ArkUI, there are callback events after a component refresh.

1\. If it is an attribute refresh of the component, the attribute can be stored in a state variable, and changes in the state variable can be listened for with @Watch.

2\. If it is a change in the size of the component, the change in the component area can be listened for through **onSizeChange()**.

**Reference**

[State Variable Change Listening](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-state-management-watch-monitor)
