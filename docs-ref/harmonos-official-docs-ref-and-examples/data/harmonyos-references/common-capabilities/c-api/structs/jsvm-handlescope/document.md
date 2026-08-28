# JSVM\_HandleScope\_\_\*

typedef struct JSVM\_HandleScope\_\_\* JSVM\_HandleScope

#### Overview

Defines the scope of the JavaScript value. It is used to control and modify the lifecycle of an object created in a specific scope. Typically, the JSVM-API value is created in the context of **JSVM\_HandleScope**. When the native method is called from JavaScript, the default **JSVM\_HandleScope** exists. If the user does not explicitly create a new **JSVM\_HandleScope**, the JSVM-API value is created in the default **JSVM\_HandleScope**. For any code call other than native method execution (for example, libuv callback), the module needs to create a scope before calling any function that may create a JavaScript value. **JSVM\_HandleScope** is created using **OH\_JSVM\_OpenHandleScope** and destroyed using **OH\_JSVM\_CloseHandleScope**. Closing the scope indicates to the GC that all **JSVM\_Values** created during the lifecycle of **JSVM\_HandleScope** will no longer be referenced from the stack frame of the current heap.

**Since**: 11

**Related module**: [JSVM](../../modules/jsvm/document.md)

**Header file**: [jsvm\_types.h](../../header-files/jsvm-types-h/document.md)
