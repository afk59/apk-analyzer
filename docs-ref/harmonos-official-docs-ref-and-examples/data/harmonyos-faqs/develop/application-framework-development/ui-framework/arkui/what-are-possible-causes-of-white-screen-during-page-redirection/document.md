# What are possible causes of white screen during page redirection?

**Possible Cause 1**

The inter-module redirection configuration is incorrect.

**Solution**

You can configure the routing table step by step according to the [System Routing Table](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-navigation-navigation#system-routing-table).

-   You need to configure the **@Builder** decorated entry function, and use the NavDestination component to display pages in the route table.
    
    // Jump Page Entry Function 
    @Builder
    export function pageOneBuilder() {
      NavigationJumpToPageWithWhiteScreen();
    }
    
    @Entry
    @Component
    struct NavigationJumpToPageWithWhiteScreen {
      pathStack: NavPathStack = new NavPathStack();
    
      build() {
        NavDestination() {
          // ...
        }
        .title('PageOne')
        .onReady((context: NavDestinationContext) => {
          this.pathStack = context.pathStack;
        })
      }
    }
    
-   HAR/HSP modules support redirection. You can check whether the type is **har** or **shared** via the **module.json5** file. If the type is **feature**, an error occurs.
    
    "module": {
      "name": "feature\_splash",
      "type": "feature",
      // The type needs to be either "har" or "shared"
    
    Even if the configuration is correct, a blank screen may still appear during redirection. You can clean the project to solve the problem.
    

**Possible Cause 2**

The **NavBar** is hidden.

**Solution**

Check whether the **NavBar** is hidden by using the [hideNavBar](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-navigation#hidenavbar9) attribute. If the attribute is set to **true**, the **NavBar** is hidden. In this case, if the page stack is empty, a white screen is displayed.

**Possible Cause 3**

The **Previewer** is used for debugging.

**Solution**

You are advised to use the Emulator or a real device to debug the redirection of complex pages. The **Previewer** does not support the redirection of the system routing table.

**Other Possible Causes**

If the **name** is empty or does not exist, a white screen is displayed.
