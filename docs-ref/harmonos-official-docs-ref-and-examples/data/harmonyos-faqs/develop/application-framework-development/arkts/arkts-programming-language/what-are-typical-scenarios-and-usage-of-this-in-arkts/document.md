# What are typical scenarios and usage of this in ArkTS?

In ArkTS, to access object properties and methods in a class, you can use **this** or call **UIContext.getHostContext** in the callback of a custom component.

-   For a class, **this** points to the object created from the class instantiation.
    
    class UserInfo {
      name: string = 'xxx';
    
      getName() {
        return this.name;
      }
    }
    
    const user: UserInfo = new UserInfo();
    
-   For a custom component, **this** is used in a callback event and points to the custom component itself. Therefore, **UIContext.getHostContext(this)** is used.
