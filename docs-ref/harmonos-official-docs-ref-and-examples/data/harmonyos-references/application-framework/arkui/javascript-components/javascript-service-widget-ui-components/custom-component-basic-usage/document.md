# Custom Component Basic Usage

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/60U3eER9QUWDkscivXRj5w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062301Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6C3C98C5244A66B7967B8203B29F1D8833D6260954652CF76BA760CB929A64A6)

The APIs of this module are supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.

Custom components are existing components encapsulated based on service requirements. A custom component can be invoked multiple times in a project to improve the code readability. You can introduce a custom component to the host page through **element** as shown in the following code snippet:

<element name='comp' src='../../common/component/comp.hml'></element>
<div>
  <comp prop1='xxxx' @child1="bindParentVmMethod"></comp>
</div>

-   The **name** attribute indicates the custom component name (optional), which is case-insensitive and is in lowercase by default. The **src** attribute indicates the **.hml** file path (mandatory) of the custom component. If **name** is not set, the **.hml** file name is used as the component name by default.
    
-   Event binding: Use **(on|@)child1** in the custom component to bind a child component event. In the child component, use **{action:"proxy", method: "eventName"}** to trigger the bound event and pass the parameter value. In the parent component, call **bindParentVmMethod** and receive the parameter passed from the child component.
    

#### Labels of Custom Component Configuration File

| Name | Type | Description |
| :-- | :-- | :-- |
| data | Object | Data model of the page. The name cannot start with a dollar sign ($) or underscore (\_). Do not use reserved words (**for**, **if**, **show**, and **tid**). |
| props | Array/Object | Used for communication between components. This attribute can be transferred to components via **<tag xxxx='value'>**. A **props** name must be in lowercase and cannot start with a dollar sign ($) or underscore (\_). Do not use reserved words (**for**, **if**, **show**, and **tid**). Currently, **props** does not support functions. |

#### Adding a Custom Event

Custom components support custom events, whose **action** is **proxy** and name is specified by **method**. A service widget page that uses a custom component can register an event callback corresponding to the custom event name. When the custom event in the custom component is triggered, the registered callback will be invoked.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/3KSb_GgtS-WZhl6ZajRIfA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062301Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4F13A409FBBA5FB3B4E1326051EE98534F46768D2144E4161168AECC64A3074D)

The event name cannot contain uppercase letters.

Example of a custom child component:

<!-- comp.hml -->
<div class="container">
    <div class="row-3" if="true">
        <button onclick="buttonClicked" value="click"></button>
    </div>
</div>

/\* comp.css \*/
.container {
    flex-direction:column;
    background-color: green;
    width: 100%;
    height: 100%;
}

.row-3 {
    width: 100%;
    height: 50px;
    background-color: orange;
    font-size:15px;
}

{
    "data": {
    },
    "actions": {
        "buttonClicked": {
            "action": "proxy",
            "method":"event\_1"
        }
    }
}

Example of a parent component:

<!-- xxx.hml --> 
<element name='comp' src='../../common/customComponent/customComponent.hml'></element>

<div class="container">
    <comp @event\_1="click"></comp>
    <button value="parentClick" @click="buttonClick"></button>
</div>

/\* xxx.css \*/
.container {
  background-color: red;
  height: 500px;
  width: 500px;
}

{
  "data": {
  },
  "actions": {
    "click": {
      "action": "message",
      "params": {
        "message": "click event"
      }
    },
    "buttonClick": {
      "action": "message",
      "params": {
        "message": "click event 2"
      }
    }
  }
}

#### props

You can use **props** to declare custom attributes of a custom component. The attributes can be used by a parent component to pass parameters to a child component.

#### \[h2\]Default Value

You can set the default value for a child component attribute via **default**. The default value is used if the parent component does not have **default** set. In this case, the **props** attribute must be in object format instead of an array.

<!-- comp.hml -->
<div class="container">
    <div class="row-1">
        <div class="box-1">
            <text>xiaoziti</text>
        </div>
        <div class="box-2">
            <text>{{text}}</text>
        </div>
        <div class="box-3">
            <text>{{textdata\[0\]}}</text>
        </div>
    </div>
    <div class="row-2" if="true">
        <button value="{{progress}}"></button>
    </div>
    <div class="row-3" if="true">
        <button onclick="buttonClicked" value="click"></button>
    </div>
</div>

{
  "data": {
    "progress": {
      "default": "80"
    }
  },
  "props": {
    "textdata": {
      "default": \["a","b"\]
    },
    "progress": {
      "default": 60
    },
    "text": {
      "default": "ha"
    }
  },
  "actions": {
    "buttonClicked": {
      "action": "proxy",
      "method": "event\_1"
    }
  }
}

Example of the parent component that references the **comp** child component:

<!-- xxx.hml -->
<element name='comp' src='../../common/customComponent/customComponent.hml'></element>

<div class="container">
    <comp progress="{{clicknow}}" textdata="{{texts}}" if="false" @event\_1="click"></comp>
</div>

#### \[h2\]Unidirectional Value Transfer

Data can be transferred only from the parent component to child components. You are not allowed to change the value passed to the child component. However, you can receive the value passed by **props** as a default value in **data**, and then change the **data** value.

For details, see [props](../../javascript-compatible-web-like-development-paradigm-arkui-full/custom-components/data-transfer-and-processing/document.md).
