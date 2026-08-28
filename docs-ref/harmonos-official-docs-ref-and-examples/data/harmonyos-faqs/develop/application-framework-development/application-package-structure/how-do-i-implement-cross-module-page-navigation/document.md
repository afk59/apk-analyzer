# How do I implement cross-module page navigation?

In large or complex systems, services are often split into multiple modules, each as a HAR or HSP. To navigate between these modules, such as from the home page to a login page, there are three solutions:

-   Solution 1: Use **router.pushNamedRoute()** of the **router** module.
    
    Reference: [Page Routing (@ohos.router)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-routing)
    
-   Solution 2: Use the **Navigation** component.
    
    The following example describes how to navigate from the entry module's **NavigationPage** component to the **Login** module's **LoginPage** component:
    
    1.  In the **Login** module, develop the custom component **LoginPage** as the destination of the route redirection.
        
        @Component
        export struct LoginPage {
          @Consume('pathStack') pathStack: NavPathStack;
          @State message: string = 'Login Page';
        
          build() {
            NavDestination() {
              Column() {
                Text(this.message)
                  .fontSize(50)
                  .fontWeight(FontWeight.Bold)
              }
              .width('100%')
              .height('100%')
            }
            .onBackPressed(() => {
              this.pathStack.pop();
              return true;
            })
          }
        }
        
    2.  Export the custom component in the **Index.ets** file of the **Login** module. export { LoginPage } from './src/main/ets/pages/loginPage';
    3.  Add a dependency on the **Login** module in the **oh-package.json5** file of the entry module.
        
        {
          // ...
          "dependencies": {
            "@ohos/login": "file:../LoginModule"
          }
        }
        
    4.  Import the custom component of the **Login** module to the entry module and add it to the **Navigation** component's route table.
        
        // Import a custom component of the Login module
        import { LoginPage } from '@ohos/login';
        
        @Entry
        @Component
        struct NavigationPage {
          @Provide('pathStack') pathStack: NavPathStack = new NavPathStack();
        
          @Builder
          pageMap(name: string) {
            if (name === 'loginPage') {
              LoginPage()
            }
          }
        
          build() {
            Navigation(this.pathStack) {
              Button('jump to login page')
                .onClick(() => {
                  // The second parameter of NavPathInfo is a custom parameter that can be used for message transfer
                  let pathInfo: NavPathInfo = new NavPathInfo('loginPage', new Object());
                  this.pathStack.pushDestination(pathInfo, true);
                })
            }
            .navDestination(this.pageMap)
          }
        }
        
-   Solution 3: Use the custom routing framework based on the **Navigation** component.
    
    While solution 2 enables cross-module navigation, with increasing inter-module transitions, it can cause complex dependencies between modules and even potential circular dependencies among multiple HAR/HSP files. To address the strong coupling between modules and enhance page loading performance, [cross-package routing](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-navigation-navigation#cross-package-dynamic-routing) is recommended.
