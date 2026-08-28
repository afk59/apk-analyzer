# How do I create an ArkTS object on the native side?

1.  Use **napi\_create\_object** to create an object.
    
    // Create object arg\_order in the native layer
    napi\_value arg\_object;
    napi\_create\_object(env, &arg\_object);
    
2.  Use **napi\_set\_named\_property** to assign values to this object.
    
    napi\_value testNum, testString;
    // Set the property testNum and assign a value of 123 to the arg\_order object created above
    napi\_create\_int32(env, 123, &testNum);
    napi\_set\_named\_property(env, arg\_object, "testNum", testNum);
    // Set the property testString and assign 'Pure' to the arg\_order object created above
    napi\_create\_string\_utf8(env, "Pure", NAPI\_AUTO\_LENGTH, &testString);
    napi\_set\_named\_property(env, arg\_object, "testString", testString);
