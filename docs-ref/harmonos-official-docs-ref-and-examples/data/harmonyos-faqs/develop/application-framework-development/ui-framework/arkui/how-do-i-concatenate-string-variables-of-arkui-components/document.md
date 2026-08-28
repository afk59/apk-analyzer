# How do I concatenate string variables of ArkUI components?

**Question**

How do I concatenate the following string variables of the **Text** component?

Text($r('app.string.EntryAbility\_desc', 'Hello'))

**Answer**

You can use **%d** and **%s** in the resource file for concatenation.

Perform the following steps:

1.  Modify the **src/main/resources/zh\_CN/element/string.json** file and add **%d** to the content to be concatenated.
    
    { 
      "string": \[ 
        { 
          "name": "module\_desc", 
          "value": "Module description%d"
        }, 
        { 
          "name": "EntryAbility\_desc", 
          "value": "description" 
        }, 
        { 
          "name": "EntryAbility\_label", 
          "value": "label" 
        } 
      \] 
    }
    
    Modify the **src/main/resources/en\_US/element/string.json** file and add **%d** to the content to be concatenated.
    
    { 
      "string": \[ 
        { 
          "name": "module\_desc", 
          "value": "module description%d" 
        }, 
        { 
          "name": "EntryAbility\_desc", 
          "value": "description%d" 
        }, 
        { 
          "name": "EntryAbility\_label", 
          "value": "label" 
        } 
      \] 
    }
    
2.  Use the **$r()** method to concatenate variables in the page component. The sample code is as follows:
    
    @Entry
    @Component
    struct Page1 {
      @State num1: number = 100;
    
      build() {
        Row() {
          Column() {
            Text($r('app.string.module\_desc', this.num1))
              .fontSize(50)
              .fontWeight(FontWeight.Bold)
          }
          .width('100%')
        }
        .height('100%')
      }
    }
    
3.  When you switch the language between Chinese and English, the corresponding variable information is automatically displayed.

**Reference**

[Resource Access](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/resource-categories-and-access#accessing-resources)
