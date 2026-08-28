# How do I concatenate string variables in ArkUI?

**Question**

How can string variable concatenation be implemented in ArkUI components, especially for enabling the string content to automatically adapt to language changes? How do I concatenate the following string variables of the **Text** component?

Text($r('app.string.EntryAbility\_desc', 'Hello'))

**Answer**

You can use **%d** and **%s** in the resource file for concatenation. The following is an example.

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
    
2.  Use **$r(_xx_)** and the variable in the page component.
    
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
    
3.  When the user switches between languages, the corresponding variable information is automatically displayed.

**Reference**

[Resource Categories and Access](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/resource-categories-and-access)
