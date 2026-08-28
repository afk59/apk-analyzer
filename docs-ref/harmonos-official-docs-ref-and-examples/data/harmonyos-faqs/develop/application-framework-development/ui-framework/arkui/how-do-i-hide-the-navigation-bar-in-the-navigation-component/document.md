# How do I hide the navigation bar in the Navigation component?

**Symptom**

The **Navigation** component is set to be hidden, but a blank navigation bar still appears, and the navigation bar reappears after the user switches to a new page.

**Solution**

You must set the **hideTitleBar** attribute of both the **Navigation** component and its **NavDestination** child component to **true** to completely hide the navigation bar.

**Reference**

[Navigation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-navigation#navigation10)
