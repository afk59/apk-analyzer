# Can internal pages of the Navigation component be preloaded?

**Symptom**

Does the **Navigation** component support preloading, such as the content of the toolbar component? When entering the index page, even though the current page is Page 0, can the content of Page 3 and Page 4 be preloaded?

**Solution**

**Navigation** does not support preloading. However, you can create required components on the home page and manually control the visibility of the components using if-else to implement preloading.

The steps are as follows:

1.  Create all components that need to be preloaded during home page initialization.
2.  Use the @State variable to control component visibility.
3.  Manage the component lifecycle by conditional rendering (for example, **if/else**).
4.  Provide a code example to describe the memory management policy.
