# What are the common component attributes for which auto can be set?

-   For the **Row**, **Column**, and **RelativeContainer** components, the **auto** option of **width** and **height** means to adapt to their child components.
-   For the **TextInput** component, the **auto** option of **width** means to adapt to the text width. Unlike the layout component, the auto width of the **TextInput** component is adjusted only based on the input text content and is not affected by child components.
-   For the **flexBasis** attribute, the **auto** option means that the base size of the component in the container along the main axis is the original size of the component.
