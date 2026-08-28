# How do I set a default page in the Navigation component?

**Symptom**

When the device is initially in landscape mode, **Navigation** is displayed in split-column mode. Since no pages are in the navigation stack, the right pane displays no content. How do I add a default page for the right pane?

**Solution**

You can use the [onNavigationModeChange](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-navigation#onnavigationmodechange11) method to listen to the mode of **Navigation** and manually control whether to load the default page:

-   If **Navigation** switches to split-screen mode and there are no pages in the stack, push the default placeholder page.
-   If it is switched to single-column mode and there is only a placeholder page in the stack, delete the placeholder page. If there is a page in the stack in split-screen mode, keep the existing page unchanged.

Since API version 20, you can set the [splitPlaceholder](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-navigation#splitplaceholder20) attribute of the **Navigation** component to set the default placeholder page.
