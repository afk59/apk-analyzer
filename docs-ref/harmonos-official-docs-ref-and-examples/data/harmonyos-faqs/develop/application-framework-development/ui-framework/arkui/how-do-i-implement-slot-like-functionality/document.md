# How do I implement slot-like functionality?

-   ArkUI provides a lightweight mechanism for reusing UI elements: @Builder. The @Builder decorated function follows the build function syntax rules, allowing you to abstract frequently used UI elements into a method that can be called within the **build()** method.
-   ArkUI also offers the @BuilderParam decorator, which is used to decorate a custom component variable of type Reference to an @Builder method. When initializing a custom component, you can add a specific feature to it by assigning a value to the variable. This decorator can be used to declare an element of any UI description, similar to a slot placeholder. Refer to the code snippet below.
    
    @Component
    struct Child {
      @Builder funABuilder0() {}
      @BuilderParam aBuilder0: () => void = this.funABuilder0;
    
      build() {
        Column() {
          this.aBuilder0()
        }
      }
    }
    
    @Entry
    @Component
    struct Parent {
      @Builder componentBuilder() {
        Text(\`Parent builder \`)
      }
    
      build() {
        Column() {
          Child({ aBuilder0: this.componentBuilder })
        }
      }
    }
    

**Reference**

[@Builder Decorator: Custom Builder Function](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-builder)

[@BuilderParam Decorator: Referencing the @Builder Function](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-builderparam)
