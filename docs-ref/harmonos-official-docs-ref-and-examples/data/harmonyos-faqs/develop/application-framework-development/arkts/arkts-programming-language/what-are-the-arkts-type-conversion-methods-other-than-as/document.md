# What are the ArkTS type conversion methods other than as?

**Symptom**

When an **any** object is converted into a specific class using **as**, the class may be incorrect. If the pointer is directly invoked, the system crashes. Is there a safer type conversion method?

**Solution**

1.  Use **instanceof** to check the type.
    
    Before conversion, you can use the **instanceof** operator to check whether the object is an instance of the target type. This prevents crashes caused by unsafe type conversion.
    
    if (anyObject instanceof TargetClass) {
      // Safely use anyObject as an instance of TargetClass
      const targetObject = anyObject as TargetClass;
      // Now it is safe to call the methods of TargetClass
    } else {
      // Handling cases where the object is not a targetClass instance
    }
    
2.  Use a type guard function.
    
    You can define a type guard function to check whether an object is an instance of a particular type and to perform validation logic.
    
    function isTargetClass(obj: object): boolean {
      return obj instanceof TargetClass && obj.someProperty === 'expectedValue';
    }
    
    if (isTargetClass(anyObject)) {
      // Now it is safe to use anyObject as an instance of TargetClass
    } else {
      // Dealing with objects that do not conform to the TargetClass
    }
    
3.  Use the **try-catch** block to handle possible errors.
    
    In some cases, you can also use the **try-catch** block to catch possible errors, although **instanceof** and **typeguard** functions are usually safe enough.
    
    function testFn2(anyObject: object): void {
      try {
        const targetObject = anyObject as TargetClass;
        // Attempt to call a method that is only available for the targetClass
        targetObject.someMethod();
      } catch (error) {
        // Dealing with situations where type conversion fails or method calls are incorrect
      }
    }
    
4.  Use type assertion function.
    
    You can create a type assertion function, which internally performs type checking and conversions, although it is not a standard ArkTS function.
    
    function assertIsTargetClass(obj: object): void {
      if (!(obj instanceof TargetClass)) {
        throw new Error('Object is not an instance of TargetClass');
      }
    }
    
    try {
      assertIsTargetClass(anyObject);
      // Now it is safe to use anyObject as an instance of TargetClass
    } catch (error) {
      // Failure to handle type assertion
    }
