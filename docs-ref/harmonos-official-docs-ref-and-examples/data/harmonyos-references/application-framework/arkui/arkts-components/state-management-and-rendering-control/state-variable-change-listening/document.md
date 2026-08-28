# State Variable Change Listening

The state variable listening module provides the capability to observe changes in state variables.

This document is solely for API reference. For details about the usage guidelines and constraints, see the development guide of each API.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/d1oQJ5wNSImj-vPY6m6jmQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CCFA0A006F5C6FC81F56736D47641579513E8835DA96A6EB947B5AEEA0A91F55)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Watch

Watch: (value: string) => PropertyDecorator

The @Watch decorator is used to listen for state variable changes in state management V1. For details about how to use @Watch, see [@Watch Decorator: Getting Notified of State Variable Changes](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-watch).

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | string | Yes | Name of the callback function used for listening. The value is specified by you. |

**Return value**

| Type | Description |
| :-- | :-- |
| PropertyDecorator | Property decorator. You do not need to concern yourself with this return value. |

**Example**

@Entry
@Component
struct Index {
  @State @Watch('onChange') num: number = 0; // The @Watch input parameter is the function name.

  onChange() {
    console.info(\`num change to ${this.num}\`);
  }

  build() {
    Column() {
      Text(\`num is: ${this.num}\`)
        .onClick(() => {
          this.num++; // This triggers the onChange callback.
        })
    }
  }
}

#### Monitor12+

Monitor: MonitorDecorator

The @Monitor decorator is used to listen for state variable changes in state management V2. For details about how to use @Monitor, see [@Monitor Decorator: Listening for Value Changes of the State Variables](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-new-monitor).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### MonitorDecorator12+

type MonitorDecorator = (value: string, ...args: string\[\]) => MethodDecorator

Represents the actual type of the @Monitor decorator.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | string | Yes | Variable path name used for listening, specified by you. When only one string is passed, this is the parameter type. |
| ...args | string\[\] | No | Array of variable path names used for listening, specified by you. When multiple strings are passed, this is the parameter type. |

**Return value**

| Type | Description |
| :-- | :-- |
| MethodDecorator | Method decorator. You do not need to concern yourself with this return value. |

**Example**

@ObservedV2
class Info {
  @Trace name: string = 'Tom';
  @Trace age: number = 25;
  @Trace height: number = 175;

  // Listen for one variable.
  @Monitor('name')
  onNameChange() {
    console.info(\`name change to ${this.name}\`);
  }

  // Listen for multiple variables.
  @Monitor('age','height')
  onRecordChange(monitor: IMonitor) {
    monitor.dirty.forEach((path: string) => {
      console.info(\`${path} change from ${monitor.value(path)?.before} to ${monitor.value(path)?.now}\`);
    })
  }
}

@Entry
@ComponentV2
struct Index {
  @Local info: Info = new Info();

  build() {
    Column() {
      Text(\`info.name: ${this.info.name}\`)
        .onClick(() => {
          this.info.name = 'Bob'; // Output log: name change to Bob
        })
      Text(\`info.age: ${this.info.age}, info.height: ${this.info.height}\`)
        .onClick(() => {
          this.info.age++; // Output log: age change from 25 to 26
          this.info.height++; // Output log: height change from 175 to 176
        })
    }
  }
}

#### IMonitor12+

When the monitored variable changes, the state management framework will call the registered function and pass the change information of the IMonitor type.

#### \[h2\]Properties

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| dirty12+ | Array<string> | No | No | Array of changed paths. |

#### \[h2\]value12+

value<T>(path?: string): IMonitorValue<T> | undefined

Obtains the change information for the specified path.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | No | Path name of the monitored variable. If it is not specified, the first path in the **dirty** array is used by default. |

**Return value**

| Type | Description |
| :-- | :-- |
| [IMonitorValue<T>](#imonitorvaluet12) | undefined | 
Path and change information for the monitored variable.

**T** is the type of the monitored variable.

If the monitored path does not exist, **undefined** is returned.

If no path is specified, the information corresponding to the first path in the **dirty** array is returned by default.

 |

**Example**

@ObservedV2
class Info {
  @Trace name: string = 'Tom';
  @Trace age: number = 25;
  @Trace height: number = 175;

  // Listen for one variable.
  @Monitor('name')
  onNameChange(monitor: IMonitor) {
    // If no path is specified for value, the first path in the dirty array is used by default.
    console.info(\`path: ${monitor.value()?.path} change from ${monitor.value()?.before} to ${monitor.value()?.now}\`);
  }

  // Listen for multiple variables.
  @Monitor('age','height')
  onRecordChange(monitor: IMonitor) {
    // If a path is specified for value, the change information for the specified path is returned.
    monitor.dirty.forEach((path: string) => {
      console.info(\`path: ${path} change from ${monitor.value(path)?.before} to ${monitor.value(path)?.now}\`);
    })
  }
}

@Entry
@ComponentV2
struct Index {
  @Local info: Info = new Info();

  build() {
    Column() {
      Text(\`info.name: ${this.info.name}\`)
        .onClick(() => {
          this.info.name = 'Bob'; // Output log: path: name change from Tom to Bob
        })
      Text(\`info.age: ${this.info.age}, info.height: ${this.info.height}\`)
        .onClick(() => {
          this.info.age++; // Output log: path: age change from 25 to 26
          this.info.height++; // Output log: path: height change from 175 to 176
        })
    }
  }
}

#### IMonitorValue<T>12+

Provides the specific change information for the monitored variable, obtained through the **value** API of **IMonitor**. **T** is the type of the variable.

#### \[h2\]Properties

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| before12+ | T | No | No | Variable value before change. |
| now12+ | T | No | No | Current variable value. |
| path12+ | string | No | No | Variable path. |

**Example**

@ObservedV2
class Info {
  @Trace name: string = 'Tom';
  @Monitor('name')
  onNameChange(monitor: IMonitor) {
    // The return value of value is of the IMonitorValue type, through which the variable change information can be obtained.
    console.info(\`path: ${monitor.value()?.path} change from ${monitor.value()?.before} to ${monitor.value()?.now}\`);
  }
}
@Entry
@ComponentV2
struct Index {
  @Local info: Info = new Info();
  build() {
    Column() {
      Text(\`info.name: ${this.info.name}\`)
        .onClick(() => {
          this.info.name = 'Bob'; // Output log: path: name change from Tom to Bob
        })
    }
  }
}
