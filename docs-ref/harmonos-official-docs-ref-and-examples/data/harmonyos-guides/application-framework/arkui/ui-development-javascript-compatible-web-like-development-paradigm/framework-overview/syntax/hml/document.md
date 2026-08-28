# HML

HML is an HTML-like language that allows you to build pages based on components and events. Pages built using HML have advanced capabilities such as data binding, event binding, loop rendering, conditional rendering, and logic control.

#### HML Page Structure

<!-- xxx.hml -->
<div class="item-container">
  <text class="item-title">Image Show</text>
  <div class="item-content">
    <image src="https://developer.huawei.com/common/xxx.png" class="image"></image>
  </div>
</div>

#### Data Binding

<!-- xxx.hml -->
<div class="container" onclick="changeText">
  <text> {{content\[1\]}} </text>
</div>

/\*xxx.css\*/
.container{
    margin: 200px;
}

// xxx.js
export default {
  data: {
    content: \['Hello World!', 'Welcome to my world!'\]
  },
  changeText: function() {
    this.content.splice(1, 1, this.content\[0\]);
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/QrDr5dKrQ2OVEr22bvKDBg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061942Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3E0BC182C1C7BDD71B66F9EA65356BAD3758868D8D9980FF27005F0115294DAB)

-   To make the array data modification take effect, use the **splice** method to change array items.
    
-   ECMAScript 6 (ES6) syntax is not supported in HML.
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/f5mdYU3ETmKQcgIg7FKirg/en-us_image_0000002537764896.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061942Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1D0DB3059B8BE622B1F40DCED6F4D0CC5B339427D56494047FB42A46CA59BB14)

#### Common Event Binding

Events are bound to components through **'on'** or **'@'**. When a component triggers an event, the corresponding event processing function in the **.js** file is executed.

Events can be written in the following formats:

-   **funcName**: name of the event callback, which is implemented by defining the corresponding function in the **.js** file.
    
-   **funcName(a,b)**: function parameters, such as **a** and **b**, which can be constants, or variables defined in **data** in the **.js** file. Do not add the prefix **this.** to variables.
    
-   Example
    
    <!-- xxx.hml -->
    <div class="container">
        <text class="title">{{count}}</text>
        <div class="box">
            <input type="button" class="btn" value="increase" onclick="increase" />
            <input type="button" class="btn" value="decrease" @click="decrease" />
            <!-- Pass additional parameters. -->
            <input type="button" class="btn" value="double" @click="multiply(2)" />
            <input type="button" class="btn" value="decuple" @click="multiply(10)" />
            <input type="button" class="btn" value="square" @click="multiply(count)" />
        </div>
    </div>
    
    // xxx.js
    export default {
      data: {
        count: 0
      },
      increase() {
        this.count++;
      },
      decrease() {
        this.count--;
      },
      multiply(multiplier) {
        this.count = multiplier \* this.count;
      }
    };
    
    /\* xxx.css \*/
    .container {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        left: 0px;
        top: 0px;
        width: 454px;
        height: 454px;
    }
    .title {
        font-size: 30px;
        text-align: center;
        width: 200px;
        height: 100px;
    }
    .box {
        width: 454px;
        height: 200px;
        justify-content: center;
        align-items: center;
        flex-wrap: wrap;
    }
    .btn {
        width: 200px;
        border-radius: 0;
        margin-top: 10px;
        margin-left: 10px;
    }
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/ynAHtrmXT56aKfKeV9WoCg/en-us_image_0000002537924836.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061942Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BE5BB75A858B3EB184CD6FA4B0548A086063485DFE73A9D65EB162246747C426)

#### Binding for Event Bubbling5+

Binding for event bubbling covers the following:

-   Bind an event callback for event bubbling: **on:{event}.bubble**. **on:{event}** is equivalent to **on:{event}.bubble**.
    
-   Bind an event callback, but stop the event from bubbling upwards: **grab:{event}.bubble**. **grab:{event}** is equivalent to **grab:{event}.bubble**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/ahsZQTzQTvSi1R36mMijZA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061942Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=299FE4E0C39E0228DCB12B7240AE2E637057BFA4CDCB132ADD1CFDB0BE32E227)
    
    Event bubbling occurs when the target element and its ancestors have registered a listener for the same event. When the event happens on the element, it first runs the event handler on it, then on its parent, and then all the way up on other ancestors. If an element triggers this event, it first triggers the callback on the element, then on its parent, and then all the way up on other ancestors.
    
    For details about event bubbling, see [Universal Events](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-components-common-events).
    
-   Example
    
    <!-- xxx.hml -->
    <div>
       <!-- Bind an event callback for event bubbling.5+ -->
        <div on:touchstart.bubble="touchstartfunc" style="background-color: red; width: 10%; height: 100%"></div>
        <div on:touchstart="touchstartfunc" style="background-color: orange; width: 10%; height: 100%"></div>
        <!-- Bind an event callback, but stop the event from bubbling upwards.5+ -->
        <div grab:touchstart.bubble="touchstartfunc" style="background-color: yellow; width: 10%; height: 100%"></div>
        <div grab:touchstart="touchstartfunc" style="background-color: greenyellow; width: 10%; height: 100%"></div>
        <!-- Bind an event callback for event bubbling.6+ -->
        <div on:click.bubble="clickfunc" style="background-color: lightskyblue; width: 10%; height: 100%"></div>
        <div on:click="clickfunc" style="background-color: cornflowerblue; width: 10%; height: 100%"></div>
        <!-- Bind an event callback, but stop the event from bubbling upwards.6+ -->
        <div grab:click.bubble="clickfunc" style="background-color: mediumslateblue; width: 10%; height: 100%"></div>
        <div grab:click="clickfunc" style="background-color: purple; width: 10%; height: 100%"></div>
    </div>
    
    // xxx.js
    export default {
        clickfunc: function(e) {
            console.info(e);
        },
        touchstartfunc: function(e) {
            console.info(e);
        },
    }
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/z7_RdDhlTti5pcRckuzVAQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061942Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8D16B4D89D68C130536179D6A27C5200C7FD28D3907370FE0ED0BA5C2463AD0B)

Events bound using a traditional statement (such as **onclick**) will bubble only when the API version in use is 6 or later.

#### Binding for Event Capturing5+

Touch events can be captured. In the capture phase, which precedes the bubbling phase, an event starts from the parent component to the child component.

Binding for event capturing covers the following:

-   Bind an event callback for event capturing: **on:{event}.capture**.
    
-   Bind an event callback, but stop the event from being captured during downward transfer: **grab:{event}.capture**.
    
-   Example
    
    <!-- xxx.hml -->
    <div>
        <!-- Bind an event callback for event capturing.5+ -->   
        <div on:touchstart.capture="touchstartfunc"></div>
        <!-- Bind an event callback, but stop the event from being captured during downward transfer.5+ -->
        <div grab:touchstart.capture="touchstartfunc"></div>
    </div>
    
    // xxx.js
    export default {
        touchstartfunc: function(e) {
            console.info(e);
        },
    }
    

#### Loop Rendering

<!-- xxx.hml -->
<div class="array-container" style="flex-direction: column;margin: 200px;">
  <!-- div loop rendering -->
  <!-- By default, $item indicates the element in the array, and $idx indicates the index of the element in the array. -->
  <div for="{{array}}" tid="id" onclick="changeText">
    <text>{{$idx}}.{{$item.name}}</text>
  </div>
  <!-- Define the name for an element variable. -->
  <div for="{{value in array}}" tid="id" onclick="changeText">    
    <text>{{$idx}}.{{value.name}}</text>
  </div>
  <!-- Define an element variable and its index name. -->
  <div for="{{(index, value) in array}}" tid="id" onclick="changeText">    
    <text>{{index}}.{{value.name}}</text>
  </div>
</div>

// xxx.js
export default {
  data: {
    array: \[
      {id: 1, name: 'jack', age: 18},
      {id: 2, name: 'tony', age: 18},
    \],
  },
  changeText: function() {
    if (this.array\[1\].name === "tony"){
      this.array.splice(1, 1, {id:2, name: 'Isabella', age: 18});
    } else {
      this.array.splice(2, 1, {id:3, name: 'Bary', age: 18});
    }
  },
}

The **tid** attribute accelerates the **for** loop and improves the re-rendering efficiency when data in a loop changes. It specifies the unique ID of each element in the array. If it is not specified, the index of each element in the array is used as the ID. For example, **tid="id"** indicates that the **id** attribute of each element is its unique ID. The **for** loop supports the following statements:

-   for="array": **array** is an array object, whose element variable is **$item** by default.
    
-   for="v in array": **v** is a custom element variable, whose index is **$idx** by default.
    
-   for="(i, v) in array": **i** indicates the element index, and **v** indicates the element variable. All elements of the array object will be looped through.
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/x4TmRi52QdmvKF4NbJZ4Qw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061942Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6E91027D25EBED4FCC2D695362E8C43F49A1D567DB2313505C541D2B84ECE082)

-   Each element in the array must have the data attribute specified by **tid**. Otherwise, an exception may occur.
    
-   The attribute specified by **tid** in the array must be unique. Otherwise, performance loss occurs. In the above example, only **id** and **name** can be used as **tid** because they are unique fields.
    
-   The **tid** attribute does not support expressions.
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/a_tLRxKXR_61i6VAUHVxSw/en-us_image_0000002568684613.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061942Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=64B701969517F139225D62DD0D097C216D56200E950A73CC302AF863304FCEE9)

#### Conditional Rendering

There are two ways to implement conditional rendering: **if-elif-else** or **show**. In **if-elif-else**, when the **if** statement evaluates to **false**, the component is not built in the VDOM and is not rendered. For **show**, when show is **false**, the component is not rendered but is built in the VDOM. In addition, the **if-elif-else** statements must be used in sibling nodes. Otherwise, the compilation fails. The following example uses both ways to implement conditional rendering:

<!-- xxx.hml -->
<div class="container">
  <button class="btn" type="capsule" value="toggleShow" onclick="toggleShow"></button>
  <button class="btn" type="capsule" value="toggleDisplay" onclick="toggleDisplay"></button>
  <text if="{{visible}}"> Hello-world1 </text>
  <text elif="{{display}}"> Hello-world2 </text>
  <text else> Hello-World </text>
</div>

/\* xxx.css \*/
.container{
  flex-direction: column;
  align-items: center;
}
.btn{
  width: 280px;
  font-size: 26px;
  margin: 10px 0;
}

// xxx.js
export default {
  data: {
    visible: false,
    display: true,
  },
  toggleShow: function() {
    this.visible = !this.visible;
  },
  toggleDisplay: function() {
    this.display = !this.display;
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/day8Tr_YQ2ak5gvETCBeDQ/en-us_image_0000002568764623.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061942Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D03E90AAA61BF8E7CAA3088F8E35B60F7020BFD9B80FCE62167A6D9A31EA135A)

In the optimized rendering (**show**), if **show** is **true**, the node is rendered properly; if it is **false**, the display style will be **none**.

<!-- xxx.hml -->
<div class="container">
  <button class="btn" type="capsule" value="toggle" onclick="toggle"></button>
  <text show="{{visible}}" > Hello World </text>
</div>

/\* xxx.css \*/
.container{
  flex-direction: column;
  align-items: center;
}
.btn{
  width: 280px;
  font-size: 26px;
  margin: 10px 0;
}

// xxx.js
export default {
  data: {
    visible: false,
  },
  toggle: function() {
    this.visible = !this.visible;
  },
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/Vp1R7NKlRt-YQyqhji4UzQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061942Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=013AF163A0488AA22C6E7378FCBCA3BC6446A681F9C1A8CF0A13202D1DFE6ED1)

Do not use **for** and **if** attributes at the same time in an element.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/ZPMLvtEUTjOOkCJgvSoKgA/en-us_image_0000002537764898.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061942Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5493663E60937DC8963EB4E09652BE0A035494BCC5C1A856269DDC8B9100EACC)

#### Logic Control Block

**<block>** makes loop rendering and conditional rendering more flexible. A **<block>** will not be compiled as a real component. Note that the **<block>** tag supports only the **for** and **if** attributes.

<!-- xxx.hml -->
<list>
  <block for="glasses">
    <list-item type="glasses">
      <text>{{$item.name}}</text>
    </list-item>
    <block for="$item.kinds">
      <list-item type="kind">
        <text>{{$item.color}}</text>
      </list-item>
    </block>
  </block>
</list>

// xxx.js
export default {
  data: {
    glasses: \[
      {name:'sunglasses', kinds:\[{name:'XXX',color:'XXX'},{name:'XXX',color:'XXX'}\]},
      {name:'nearsightedness mirror', kinds:\[{name:'XXX',color:'XXX'}\]},
    \],
  },
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/XxMaNynWQtmEMzYalhLvRA/en-us_image_0000002537924838.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061942Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EABEF8B3AAFEDD46BADB64C152523A34323A5F3751D8B726A23255A3D9CC91A6)

#### Template Reference

HML supports using **element** to reference template files. For details, see [Basic Usage of Custom Components](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-components-custom-basic-usage).

<!-- template.hml -->
<div class="item"> 
  <text>Name: {{name}}</text>
  <text>Age: {{age}}</text>
</div>

<!-- index.hml -->
<element name='comp' src='../../common/template.hml'></element>
<div>
  <comp name="Tony" age="18"></comp>
</div>
