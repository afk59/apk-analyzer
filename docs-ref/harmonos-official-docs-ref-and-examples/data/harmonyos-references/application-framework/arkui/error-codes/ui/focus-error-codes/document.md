# Focus Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/IJcmFa2KR1uLfT5qWs8mvg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062311Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A8EF0BB7D31421B3D3253AFD4AAB6F6F80657FE9ACC8544A6EBAB06B35AFE7AD)

This topic describes only module-specific error codes. For details about universal error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

#### 150001 Component Not Focusable

**Error Message**

the component cannot be focused.

**Description**

This error code is reported when the current component is not focusable.

**Possible Causes**

The component is not focusable by default or has been configured through attribute methods such as **focusable**.

**Solution**

Check whether the current component is focusable and whether **focusable** is set to **true**.

#### 150002 Ancestor Component Not Focusable

**Error Message**

This component has an unfocusable ancestor.

**Description**

This error code is reported when an ancestor of the current component is not focusable.

**Possible Causes**

The ancestor component is not focusable by default or has been configured through attribute methods such as **focusable**.

**Solution**

Check whether the ancestor component is focusable and whether **focusable** is set to **true**.

#### 150003 Component Does Not Exist

**Error Message**

the component is not on tree or does not exist.

**Description**

This error code is reported when the provided ID points to a non-existent, detached, or invisible component.

**Possible Causes**

-   The provided ID is incorrect, or the component has been destroyed.
    
-   Focus is requested for a component that is not focusable. For details about such components, see [Component Focusability](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-common-events-focus-event#component-focusability).
    

**Solution**

Use the correct ID or component.
