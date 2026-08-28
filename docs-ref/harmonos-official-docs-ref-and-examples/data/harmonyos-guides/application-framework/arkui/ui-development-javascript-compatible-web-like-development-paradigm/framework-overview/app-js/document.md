# app.js

#### Application Lifecycle

You can customize the [lifecycle](../lifecycle/document.md) implementation logic on an application-by-application basis in app.js. The following example only prints the corresponding logs in the lifecycle function:

// app.js
export default {
    onCreate() {
        console.info('Application onCreate');
    },

    onDestroy() {
        console.info('Application onDestroy');
    },
}

#### Application Object6+

| Property | Type | Description |
| :-- | :-- | :-- |
| getApp | Function | Obtains the object exposed in the **app.js** file from the custom **.js** file. |

The following is a sample code snippet:

// app.js
export default {
    data: {
        test: "by getApp"
    },
    onCreate() {
        console.info('AceApplication onCreate');
    },
    onDestroy() {
        console.info('AceApplication onDestroy');
    },
}

// test.js custom logic code.
export var appData = getApp().data;
