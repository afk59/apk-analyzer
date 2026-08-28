# Purgeable Memory Development

#### When to Use

HarmonyOS provides Purgeable Memory management, which enables you to use related APIs to create **PurgeableMemory** objects to manage purgeable memory.

You can use the native APIs to apply for and release purgeable memory.

The following scenarios are common for the development of purgeable memory management:

-   Apply for a **PurgeableMemory** object and write data to the object.
-   Release the **PurgeableMemory** object when it is no longer required.

#### Available APIs

| API | Description |
| :-- | :-- |
| OH\_PurgeableMemory \*OH\_PurgeableMemory\_Create(size\_t size, OH\_PurgeableMemory\_ModifyFunc func, void \*funcPara) | Creates a **PurgeableMemory** object. A new **PurgeableMemory** object is generated each time this API is called. |
| bool OH\_PurgeableMemory\_Destroy(OH\_PurgeableMemory \*purgObj) | Destroys a **PurgeableMemory** object. |
| bool OH\_PurgeableMemory\_BeginRead(OH\_PurgeableMemory \*purgObj) | Begins a read operation on a **PurgeableMemory** object. |
| void OH\_PurgeableMemory\_EndRead(OH\_PurgeableMemory \*purgObj) | Ends a read operation on a **PurgeableMemory** object and decreases the reference count of the object by 1. When the reference count reaches 0, the object can be reclaimed by the system. |
| bool OH\_PurgeableMemory\_BeginWrite(OH\_PurgeableMemory \*purgObj) | Begins a write operation on a **PurgeableMemory** object. |
| void OH\_PurgeableMemory\_EndWrite(OH\_PurgeableMemory \*purgObj) | Ends a write operation on a **PurgeableMemory** object and decreases the reference count of the object by 1. When the reference count reaches 0, the object can be reclaimed by the system. |
| void \*OH\_PurgeableMemory\_GetContent(OH\_PurgeableMemory \*purgObj) | Obtains the memory data of a **PurgeableMemory** object. |
| size\_t OH\_PurgeableMemory\_ContentSize(OH\_PurgeableMemory \*purgObj) | Obtains the memory data size of a **PurgeableMemory** object. |
| bool OH\_PurgeableMemory\_AppendModify(OH\_PurgeableMemory \*purgObj, OH\_PurgeableMemory\_ModifyFunc func, void \*funcPara) | Adds a function for modifying a **PurgeableMemory** object. |

#### How to Develop

The following walks you through on how to use the native purgeable memory APIs to apply for a **PurgeableMemory** object, write data to the object, and read data from the object.

1.  Declare the rules for creating a **PurgeableMemory** object.
    
    // Declare the parameters of the constructor.
    struct ParaData{
        int start;
        int end;
    };
    
    // Declare a function for modifying the object.
    bool FactorialFunc(void\* data, size\_t size, void\* param){
        bool ret = true;
        ParaData \*pdata = (ParaData\*) param;
        int\* oriData = (int\*)data;
        int i = pdata->start;
        while (i < pdata->end) {
            \*oriData \*= i;
            i++;
        }
        return ret;
    }
    
    // Declare the parameters of the extended function for modifying the object.
    struct AppendParaData{
        int newPara;
    };
    
    // Declare the extended function for modifying the object.
    bool AddFunc(void\* data, size\_t size, void\* param){
        bool ret = true;
        int \*oriDatap = (int\*) data;
        AppendParaData\* apData = (AppendParaData\*)param;
        \*oriDatap += apData->newPara;
        return ret;
    }
    
2.  Create a **PurgeableMemory** object.
    
    // Define the memory data size to 4 MB.
    #define DATASIZE (4 \* 1024 \* 1024)
    
    // Declare the parameters of the constructor.
    struct ParaData pdata = {1,2};
    
    // Create a PurgeableMemory object.
    OH\_PurgeableMemory\* pPurgmem = OH\_PurgeableMemory\_Create(DATASIZE, FactorialFunc, &pdata);
    
3.  Perform a read operation on the **PurgeableMemory** object.
    
    // Define an object type based on the service requirements.
    class ReqObj;
    
    // Begin a read operation on the object.
    if(OH\_PurgeableMemory\_BeginRead(pPurgmem)) {
        // Obtain the object size.
        size\_t size = OH\_PurgeableMemory\_ContentSize(pPurgmem);
    
        // Obtain the object content.
        ReqObj\* pReqObj = (ReqObj\*) OH\_PurgeableMemory\_GetContent(pPurgmem);
    
        // End the read operation on the object.
        OH\_PurgeableMemory\_EndRead(pPurgmem);
    }
    
4.  Perform a write operation on the **PurgeableMemory** object.
    
     // Define an object type based on the service requirements.
    class ReqObj;
    
    // Begin a write operation on the object.
    if(OH\_PurgeableMemory\_BeginWrite(pPurgmem)) {
        // Obtain the object data.
        ReqObj\* pReqObj = (ReqObj\*) OH\_PurgeableMemory\_GetContent(pPurgmem);
    
        // Declare the parameters of the extended constructor.
        struct AppendParaData apdata = {1};
    
        // Update the rules for recreating the object.
        OH\_PurgeableMemory\_AppendModify(pPurgmem, AddFunc, &apdata);
    
        // Stop writing data to the object.
        OH\_PurgeableMemory\_EndWrite(pPurgmem);
    }
    
5.  Destroy the **PurgeableMemory** object.
    
    // Destroy the object.
    OH\_PurgeableMemory\_Destroy(pPurgmem);
    // Set a null pointer to prevent UAF.
    pPurgmem = nullptr;
