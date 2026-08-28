# Function Flow Runtime C APIs

#### Task Management

## ffrt\_deps\_t

**Declaration**

typedef enum {
    ffrt\_dependence\_data,
    ffrt\_dependence\_task,
} ffrt\_dependence\_type\_t;

typedef struct {
    ffrt\_dependence\_type\_t type;
    const void\* ptr;
} ffrt\_dependence\_t;

typedef struct {
    uint32\_t len;
    const ffrt\_dependence\_t\* items;
} ffrt\_deps\_t;

**Parameters**

-   len: number of data dependencies.
-   items: data dependency array. The data length is equal to len.
-   ptr: data address.
-   type: data type. It is different from task\_handle.

**Description**

The function of ffrt\_dependence\_t is the same as that of dependence in C++, and the function of ffrt\_deps\_t is the same as that of std::vector<dependence> in C++.

**Example**

// Create a data dependency.
int x = 0;
ffrt\_dependence\_t data\_dependence\[1\];
data\_dependence\[0\].type = ffrt\_dependence\_data;
data\_dependence\[0\].ptr = &x;
ffrt\_deps\_t data\_deps;
data\_deps.len = 1;
data\_deps.items = data\_dependence;

// Create a task dependency.
ffrt\_task\_handle\_t task = ffrt\_submit\_h\_base(user\_function\_header, NULL, NULL, &attr);
ffrt\_dependence\_t task\_dependence\[1\];
task\_dependence\[0\].type = ffrt\_dependence\_task;
task\_dependence\[0\].ptr = task;
ffrt\_deps\_t task\_deps;
task\_deps.len = 1;
task\_deps.items = task\_dependence;

## ffrt\_task\_attr\_t

**Declaration**

typedef struct {
    uint32\_t storage\[(ffrt\_task\_attr\_storage\_size + sizeof(uint32\_t) - 1) / sizeof(uint32\_t)\];
} ffrt\_task\_attr\_t;

**Description**

Describes the task attribute, which can be configured using ffrt\_task\_attr\_t when submitting a common task or queue task.

**Methods**

**ffrt\_task\_attr\_init**

FFRT\_C\_API int ffrt\_task\_attr\_init(ffrt\_task\_attr\_t\* attr);

Parameters

-   attr: pointer to the ffrt\_task\_attr\_t object.

Return Values

-   The value **0** indicates success, and the value **\-1** indicates failure.

Description

-   Initializes an ffrt\_task\_attr\_t object.

**ffrt\_task\_attr\_destroy**

FFRT\_C\_API void ffrt\_task\_attr\_destroy(ffrt\_task\_attr\_t\* attr);

Parameters

-   attr: pointer to the ffrt\_task\_attr\_t object.

Description

-   Destroys an ffrt\_task\_attr\_t object.

**ffrt\_task\_attr\_set\_name**

FFRT\_C\_API void ffrt\_task\_attr\_set\_name(ffrt\_task\_attr\_t\* attr, const char\* name);

Parameters

-   attr: pointer to the ffrt\_task\_attr\_t object.
-   name: task name.

Description

-   Sets the task name, which is valid for printing maintenance and test information.

**ffrt\_task\_attr\_get\_name**

FFRT\_C\_API const char\* ffrt\_task\_attr\_get\_name(const ffrt\_task\_attr\_t\* attr);

Parameters

-   attr: pointer to the ffrt\_task\_attr\_t object.

Return Values

-   Task name.

Description

-   Obtains the task name.

**ffrt\_task\_attr\_set\_qos**

FFRT\_C\_API void ffrt\_task\_attr\_set\_qos(ffrt\_task\_attr\_t\* attr, ffrt\_qos\_t qos);

Parameters

-   attr: pointer to the ffrt\_task\_attr\_t object.
-   qos: QoS.

Description

-   Sets the task QoS, which determines the system resource supply during task execution. If QoS is not set, the queue QoS is inherited by default. The default QoS of a common task is ffrt\_qos\_default.

**ffrt\_task\_attr\_get\_qos**

FFRT\_C\_API ffrt\_qos\_t ffrt\_task\_attr\_get\_qos(const ffrt\_task\_attr\_t\* attr);

Parameters

-   attr: pointer to the ffrt\_task\_attr\_t object.

Return Values

-   QoS.

Description

-   Obtains the configured QoS.

**ffrt\_task\_attr\_set\_delay**

FFRT\_C\_API void ffrt\_task\_attr\_set\_delay(ffrt\_task\_attr\_t\* attr, uint64\_t delay\_us);

Parameters

-   attr: pointer to the ffrt\_task\_attr\_t object.
-   delay\_us: scheduling delay. The unit is μs.

Description

-   Sets the scheduling delay of a task. The task will be scheduled and executed after the delay interval. If no delay is set, the default delay is 0.
-   After the scheduling delay is set, the input and output dependencies of the task will not take effect.

**ffrt\_task\_attr\_get\_delay**

FFRT\_C\_API uint64\_t ffrt\_task\_attr\_get\_delay(const ffrt\_task\_attr\_t\* attr);

Parameters

-   attr: pointer to the ffrt\_task\_attr\_t object.

Return Values

-   Scheduling delay.

Description

-   Obtains the scheduling delay.

**ffrt\_task\_attr\_set\_queue\_priority**

FFRT\_C\_API void ffrt\_task\_attr\_set\_queue\_priority(ffrt\_task\_attr\_t\* attr, ffrt\_queue\_priority\_t priority);

Parameters

-   attr: pointer to the ffrt\_task\_attr\_t object.
-   priority: task priority.

Description

-   Sets the task priority. Currently, only concurrent queue tasks support the priority function. Tasks in the same concurrent queue are scheduled based on their priorities. If the priority is not set, ffrt\_queue\_priority\_low is used by default.

**ffrt\_task\_attr\_get\_queue\_priority**

FFRT\_C\_API ffrt\_queue\_priority\_t ffrt\_task\_attr\_get\_queue\_priority(const ffrt\_task\_attr\_t\* attr);

Parameters

-   attr: pointer to the ffrt\_task\_attr\_t object.

Return Values

-   Task priority.

Description

-   Obtains the configured priority.

**ffrt\_task\_attr\_set\_stack\_size**

FFRT\_C\_API void ffrt\_task\_attr\_set\_stack\_size(ffrt\_task\_attr\_t\* attr, uint64\_t size);

Parameters

-   attr: pointer to the ffrt\_task\_attr\_t object.
-   size: size of the coroutine stack, in bytes.

Description

-   Sets the size of the coroutine stack, which affects the maximum space used by the call stack during task execution. If this parameter is not set, the default size of the coroutine stack is 1 MB.

**ffrt\_task\_attr\_get\_stack\_size**

FFRT\_C\_API uint64\_t ffrt\_task\_attr\_get\_stack\_size(const ffrt\_task\_attr\_t\* attr);

Parameters

-   attr: pointer to the ffrt\_task\_attr\_t object.

Return Values

-   Size of the coroutine stack.

Description

-   Obtains the size of the coroutine stack.

**Example**

// Submit a common task. The task name is "sample\_task", the QoS is background, the scheduling delay is 1 ms, and the coroutine stack size is 2 MB.
ffrt\_task\_attr\_t attr;
ffrt\_task\_attr\_init(&attr);
ffrt\_task\_attr\_set\_name(&attr, "sample\_task");
ffrt\_task\_attr\_set\_qos(&attr, ffrt\_qos\_background);
ffrt\_task\_attr\_set\_delay(&attr, 1000);
ffrt\_task\_attr\_set\_stack\_size(&attr, 2 \* 1024 \* 1024);
ffrt\_submit\_base(user\_function\_header, NULL, NULL, &attr);
ffrt\_task\_attr\_destroy(&attr);

## ffrt\_alloc\_auto\_managed\_function\_storage\_base

**Declaration**

typedef enum {
    ffrt\_function\_kind\_general,
    ffrt\_function\_kind\_queue,
} ffrt\_function\_kind\_t;

typedef void(\*ffrt\_function\_t)(void\*);
typedef struct {
    ffrt\_function\_t exec;
    ffrt\_function\_t destroy;
    uint64\_t reserve\[2\];
} ffrt\_function\_header\_t;

FFRT\_C\_API void \*ffrt\_alloc\_auto\_managed\_function\_storage\_base(ffrt\_function\_kind\_t kind);

**Parameters**

-   kind: ffrt\_function\_kind\_general for submitting a common task; ffrt\_function\_kind\_queue for submitting a queue task.
-   exec: function pointer invoked during task execution.
-   destroy: function pointer invoked after a task is complete. It can be used to destroy resources.
-   reserve: internal reserved space. It cannot be used by users.

**Return Values**

-   Pointer to the executor of the user task.

**Description**

Allocates memory space. The header of the memory space is in the ffrt\_function\_header\_t structure. The return pointer can be converted into the ffrt\_function\_header\_t\* pointer. A 64-byte space is reserved after the header for customizing the space for storing input parameters or return values.

**Example**

-   Example 1: Generate a task executor without parameters and return values.
    
    #include <stdio.h>
    #include "ffrt/task.h"
    
    void foo(void\* data)
    {
        printf("foo\\n");
    }
    
    void after\_foo(void\* data)
    {
        printf("after\_foo\\n");
    }
    
    int main()
    {
        ffrt\_function\_header\_t\* func = (ffrt\_function\_header\_t\*)ffrt\_alloc\_auto\_managed\_function\_storage\_base(ffrt\_function\_kind\_general);
    
        func->exec = foo;
        func->destroy = after\_foo;
    
        ffrt\_submit\_base(func, NULL, NULL, NULL);
        ffrt\_wait();
    
        return 0;
    }
    
-   Example 2: Generate a task executor with parameters and return values.
    
    #include <stdio.h>
    #include "ffrt/task.h"
    
    int foo(int x, int y)
    {
        printf("foo: x = %d, y = %d\\n", x, y);
        return x + y;
    }
    
    void after\_foo(void\* data)
    {
        printf("after\_foo\\n");
    }
    
    // Custom task executor, which can carry parameters and return values.
    typedef struct {
        ffrt\_function\_header\_t header; // The header space is ffrt\_function\_header\_t.
        int arg1; // Argument 1
        int arg2; // Argument 2
        int ret; // Return value
    } user\_defined\_function;
    
    // Wrap foo into the exec function type of void(\*)(void\*).
    void exec\_func\_wrapper(void\* header)
    {
        user\_defined\_function\* func = (user\_defined\_function\*)header;
        func->ret = foo(func->arg1, func->arg2); // Expand the foo function, pass arguments, and obtain the return value.
    }
    
    int main()
    {
        user\_defined\_function\* func = (user\_defined\_function\*)ffrt\_alloc\_auto\_managed\_function\_storage\_base(ffrt\_function\_kind\_general);
    
        func->header.exec = exec\_func\_wrapper;
        func->header.destroy = after\_foo;
        func->arg1 = 1;
        func->arg2 = 2;
    
        ffrt\_submit\_base((ffrt\_function\_header\_t\*)func, NULL, NULL, NULL);
        ffrt\_wait();
    
        printf("ret = %d\\n", func->ret);
        return 0;
    }
    

## ffrt\_submit\_base

**Declaration**

FFRT\_C\_API void ffrt\_submit\_base(ffrt\_function\_header\_t\* f, const ffrt\_deps\_t\* in\_deps, const ffrt\_deps\_t\* out\_deps, const ffrt\_task\_attr\_t\* attr);

**Parameters**

-   f: task executor of a user. The value can be of the native ffrt\_function\_header\_t type or a custom extension type based on ffrt\_function\_header\_t.
-   in\_deps: input data dependency of a task. It is usually expressed as the actual data address. ffrt\_task\_handle\_t can also be used as a special input dependency.
-   out\_deps: output data dependency of a task. It is usually expressed as the actual data address. ffrt\_task\_handle\_t is not supported.
-   attr: task attribute.

**Description**

Submits a common task that supports attribute settings. After the input dependency is removed, the task can be scheduled and executed. After the task is executed, the output dependency is removed.

**Example**

-   Example 1: Submit a task with attributes.
    
    #include <stdio.h>
    #include "ffrt/task.h"
    
    void foo(void\* data)
    {
        printf("foo\\n");
    }
    
    void after\_foo(void\* data)
    {
        printf("after\_foo\\n");
    }
    
    int main()
    {
        // Submit a task.
        ffrt\_function\_header\_t\* func = (ffrt\_function\_header\_t\*)ffrt\_alloc\_auto\_managed\_function\_storage\_base(ffrt\_function\_kind\_general);
        func->exec = foo;
        func->destroy = after\_foo;
        ffrt\_submit\_base(func, NULL, NULL, NULL);
    
        // Submit a task with attributes.
        ffrt\_task\_attr\_t attr;
        ffrt\_task\_attr\_init(&attr);
        ffrt\_task\_attr\_set\_name(&attr, "sample\_task");
        ffrt\_task\_attr\_set\_qos(&attr, ffrt\_qos\_background);
        ffrt\_submit\_base(func, NULL, NULL, &attr);
    
        return 0;
    }
    
-   Example 2: Submit a task with data dependency.
    
    // Submit two tasks with data dependency. The Read-After-Write dependency exists between tasks.
    #include <math.h>
    #include <stdio.h>
    #include "ffrt/task.h"
    
    void cos\_func(float\* x, float\* y)
    {
        \*y = cos(\*x);
    }
    
    void tan\_func(float\* y, float\* z)
    {
        \*z = tan(\*y);
    }
    
    typedef struct {
        ffrt\_function\_header\_t header;
        float\* arg1; // Argument 1
        float\* arg2; // Argument 2
    } user\_defined\_function;
    
    void cos\_func\_wrapper(void\* header)
    {
        user\_defined\_function\* func = (user\_defined\_function\*)header;
        cos\_func(func->arg1, func->arg2);
    }
    
    void tan\_func\_wrapper(void\* header)
    {
        user\_defined\_function\* func = (user\_defined\_function\*)header;
        tan\_func(func->arg1, func->arg2);
    }
    
    void destroy(void\* header) {}
    
    int main()
    {
        float x = 0.5f, y, z;
    
        user\_defined\_function\* func1 = (user\_defined\_function\*)ffrt\_alloc\_auto\_managed\_function\_storage\_base(ffrt\_function\_kind\_general);
        func1->header.exec = cos\_func\_wrapper;
        func1->header.destroy = destroy;
        func1->arg1 = &x;
        func1->arg2 = &y;
    
        user\_defined\_function\* func2 = (user\_defined\_function\*)ffrt\_alloc\_auto\_managed\_function\_storage\_base(ffrt\_function\_kind\_general);
        func2->header.exec = tan\_func\_wrapper;
        func2->header.destroy = destroy;
        func2->arg1 = &y;
        func2->arg2 = &z;
    
        ffrt\_dependence\_t dependence\_x\[1\];
        dependence\_x\[0\].type = ffrt\_dependence\_data;
        dependence\_x\[0\].ptr = &x;
        ffrt\_deps\_t deps\_x;
        deps\_x.len = 1;
        deps\_x.items = dependence\_x;
        ffrt\_dependence\_t dependence\_y\[1\];
        dependence\_y\[0\].type = ffrt\_dependence\_data;
        dependence\_y\[0\].ptr = &y;
        ffrt\_deps\_t deps\_y;
        deps\_y.len = 1;
        deps\_y.items = dependence\_y;
        ffrt\_dependence\_t dependence\_z\[1\];
        dependence\_z\[0\].type = ffrt\_dependence\_data;
        dependence\_z\[0\].ptr = &z;
        ffrt\_deps\_t deps\_z;
        deps\_z.len = 1;
        deps\_z.items = dependence\_z;
    
        ffrt\_submit\_base((ffrt\_function\_header\_t\*)func1, &deps\_x, &deps\_y, NULL);
        ffrt\_submit\_base((ffrt\_function\_header\_t\*)func2, &deps\_y, &deps\_z, NULL);
    
        ffrt\_wait();
        printf("x = %f, y = %f, z = %f\\n", x, y, z);
        return 0;
    }
    

## ffrt\_submit\_f

**Declaration**

FFRT\_C\_API void ffrt\_submit\_f(ffrt\_function\_t func, void\* arg, const ffrt\_deps\_t\* in\_deps, const ffrt\_deps\_t\* out\_deps, const ffrt\_task\_attr\_t\* attr);

**Parameters**

-   func: specified task function.
-   arg: parameter passed to the task function.
-   in\_deps: input data dependency of a task. It is usually expressed as the actual data address. ffrt\_task\_handle\_t can also be used as a special input dependency.
-   out\_deps: output data dependency of a task. It is usually expressed as the actual data address. ffrt\_task\_handle\_t is not supported.
-   attr: task attribute.

**Description**

ffrt\_submit\_f is a simplified form of ffrt\_submit\_base. When the callback function does not need to be destroyed, the API packages the task function and its parameters into a common task structure. Then, ffrt\_submit\_base is called to submit the task.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/icrbbnm3SCGX7iTahK7NNA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062022Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C76E2670B8D3F4EA8D98E17303DD74532F096D4057443BC1950AE8B7AC645665)

This API is supported since API version 20.

**Example**

#include <stdio.h>
#include "ffrt/task.h"

// Function to be submitted for execution.
void OnePlusForTest(void\* arg)
{
    (\*static\_cast<int\*>(arg)) += 1;
}

int main()
{
    int a = 0;
    ffrt\_submit\_f(OnePlusForTest, &a, NULL, NULL, NULL);

    ffrt\_wait();

    printf("a = %d\\n", a);
    return 0;
}

## ffrt\_submit\_h\_base

**Declaration**

typedef void\* ffrt\_task\_handle\_t;

FFRT\_C\_API ffrt\_task\_handle\_t ffrt\_submit\_h\_base(ffrt\_function\_header\_t\* f, const ffrt\_deps\_t\* in\_deps, const ffrt\_deps\_t\* out\_deps, const ffrt\_task\_attr\_t\* attr);

**Parameters**

-   f: task executor of a user. The value can be of the native ffrt\_function\_header\_t type or a custom extension type based on ffrt\_function\_header\_t.
-   in\_deps: input data dependency of a task. It is usually expressed as the actual data address. ffrt\_task\_handle\_t can also be used as a special input dependency.
-   out\_deps: output data dependency of a task. It is usually expressed as the actual data address. ffrt\_task\_handle\_t is not supported.
-   attr: task attribute.

**Return Values**

-   ffrt\_task\_handle\_t task handle.

**Description**

Compared with the ffrt\_submit\_base API, the return value of the task handle is added.

**Example**

// Submit a task and obtain the task handle.
ffrt\_function\_header\_t\* func = (ffrt\_function\_header\_t\*)ffrt\_alloc\_auto\_managed\_function\_storage\_base(ffrt\_function\_kind\_general);
func->exec = foo;
func->destroy = after\_foo;
ffrt\_task\_handle\_t t = ffrt\_submit\_h\_base(func, NULL, NULL, NULL);
// Note that ffrt\_task\_handle\_t of the C API needs to be explicitly destroyed by calling ffrt\_task\_handle\_destroy.
ffrt\_task\_handle\_destroy(t);

## ffrt\_submit\_h\_f

**Declaration**

typedef void\* ffrt\_task\_handle\_t;

FFRT\_C\_API ffrt\_task\_handle\_t ffrt\_submit\_h\_f(ffrt\_function\_t func, void\* arg, const ffrt\_deps\_t\* in\_deps, const ffrt\_deps\_t\* out\_deps, const ffrt\_task\_attr\_t\* attr);

**Parameters**

-   func: specified task function.
-   arg: parameter passed to the task function.
-   in\_deps: input data dependency of a task. It is usually expressed as the actual data address. ffrt\_task\_handle\_t can also be used as a special input dependency.
-   out\_deps: output data dependency of a task. It is usually expressed as the actual data address. ffrt\_task\_handle\_t is not supported.
-   attr: task attribute.

**Return Values**

-   ffrt\_task\_handle\_t task handle.

**Description**

Adds the return value of the task handle compared with ffrt\_submit\_f.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/i6KBzsabQL6Shd46gFPeHA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062022Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7D7ADF84A3698A588389CD257900483567739F43C0B90CF3647658CCCFD4591C)

This API is supported since API version 20.

**Example**

#include <stdio.h>
#include <vector>
#include "ffrt/task.h"

// Function to be submitted for execution.
void OnePlusForTest(void\* arg)
{
    (\*static\_cast<int\*>(arg)) += 1;
}

int main()
{
    int a = 0;
    ffrt\_task\_handle\_t task = ffrt\_submit\_h\_f(OnePlusForTest, &a, NULL, NULL, NULL);

    const std::vector<ffrt\_dependence\_t> wait\_deps = {{ffrt\_dependence\_task, task}};
    ffrt\_deps\_t wait{static\_cast<uint32\_t>(wait\_deps.size()), wait\_deps.data()};
    ffrt\_wait\_deps(&wait);

    printf("a = %d\\n", a);
    return 0;
}

## ffrt\_task\_handle\_inc\_ref

**Declaration**

FFRT\_C\_API uint32\_t ffrt\_task\_handle\_inc\_ref(ffrt\_task\_handle\_t handle);

**Parameters**

-   handle: task handle.

**Return Values**

-   Reference count of a task.

**Description**

Increases the reference count of the task through the task handle by one each time the task handle is invoked. It is used to control the task lifecycle. When the reference count is not 0, the corresponding task resources are not released. Note that ffrt\_task\_handle\_t returned by ffrt\_submit\_h\_base has a reference count by default. By default, you can subtract a reference count when using ffrt\_task\_handle\_destroy to destroy ffrt\_task\_handle\_t.

## ffrt\_task\_handle\_dec\_ref

**Declaration**

FFRT\_C\_API uint32\_t ffrt\_task\_handle\_dec\_ref(ffrt\_task\_handle\_t handle);

**Parameters**

-   handle: task handle.

**Return Values**

-   Reference count of a task.

**Description**

Subtracts the reference count of the task through the task handle by one each time the task handle is invoked.

## ffrt\_task\_handle\_destroy

**Declaration**

FFRT\_C\_API void ffrt\_task\_handle\_destroy(ffrt\_task\_handle\_t handle);

**Parameters**

-   handle: task handle.

**Description**

Destroys a task handle and subtracts a task reference count by default.

## ffrt\_wait

**Declaration**

FFRT\_C\_API void ffrt\_wait(void);

**Description**

Waits until all tasks of the same level submitted earlier are complete.

**Example**

// Wait until three tasks are complete.
ffrt\_submit\_base(func1, NULL, NULL, NULL);
ffrt\_submit\_base(func2, NULL, NULL, NULL);
ffrt\_submit\_base(func3, NULL, NULL, NULL);
ffrt\_wait();

## ffrt\_wait\_deps

**Declaration**

FFRT\_C\_API void ffrt\_wait\_deps(const ffrt\_deps\_t\* deps);

**Parameters**

-   deps: data dependency to be synchronized.

**Description**

Waits until the data dependency is removed.

**Example**

// Build the data dependency of x.
int x = 0;
ffrt\_dependence\_t dependence\[1\];
dependence\[0\].type = ffrt\_dependence\_data;
dependence\[0\].ptr = &x;
ffrt\_deps\_t deps;
deps.len = 1;
deps.items = dependence;

// Submit a write task.
ffrt\_submit\_base(func, NULL, &deps, NULL);

// Wait until the data dependency of the write task is removed.
ffrt\_wait\_deps(&deps);

## ffrt\_this\_task\_update\_qos

**Declaration**

FFRT\_C\_API int ffrt\_this\_task\_update\_qos(ffrt\_qos\_t qos);

**Parameters**

-   qos: QoS.

**Return Values**

-   The value **0** indicates success, and the value **1** indicates failure.

**Description**

Updates the task QoS dynamically during task execution. Note that this API is used in the function closure of a task to update the QoS of the task that is being executed. If this API is invoked, the task is suspended and then resumed.

**Example**

// Dynamically update the QoS during the execution of a qos\_background task.
ffrt::submit(\[\]() {
    // ...
    int ret = ffrt\_this\_task\_update\_qos(ffrt\_qos\_user\_initiated);
    // ...
}, ffrt::task\_attr().qos(ffrt::qos\_background));

## ffrt\_this\_task\_get\_qos

**Declaration**

FFRT\_C\_API ffrt\_qos\_t ffrt\_this\_task\_get\_qos(void);

**Return Values**

-   QoS.

**Description**

Obtains the QoS of the task that is being executed.

**Example**

// Dynamically obtain the QoS during the execution of a task.
ffrt::submit(\[\]() {
    // ...
    // The obtained QoS is ffrt\_qos\_background.
    ffrt\_qos\_t qos = ffrt\_this\_task\_get\_qos();
    // ...
}, ffrt::task\_attr().qos(ffrt::qos\_background));

## ffrt\_this\_task\_get\_id

**Declaration**

FFRT\_C\_API uint64\_t ffrt\_this\_task\_get\_id(void);

**Return Values**

-   Task ID.

**Description**

Obtains the ID of the task that is being executed.

**Example**

// Dynamically obtain the task ID during task execution.
ffrt::submit(\[\]() {
    // ...
    // Obtain the unique task ID.
    uint64\_t task\_id = ffrt\_this\_task\_get\_id();
    // ...
}, ffrt::task\_attr().qos(ffrt::qos\_background));

#### Task Queue

## ffrt\_queue\_attr\_t

**Declaration**

typedef struct {
    uint32\_t storage\[(ffrt\_queue\_attr\_storage\_size + sizeof(uint32\_t) - 1) / sizeof(uint32\_t)\];
} ffrt\_queue\_attr\_t;

**Description**

Configures queue attributes, such as the QoS, timeout, callback function, and maximum concurrency.

**Methods**

**ffrt\_queue\_attr\_init**

int ffrt\_queue\_attr\_init(ffrt\_queue\_attr\_t\* attr);

Parameters

-   attr: pointer to the queue attribute.

Return Values

-   The value **0** indicates success while other values indicate failure.

Description

-   Initializes a queue attribute object.

**ffrt\_queue\_attr\_destroy**

void ffrt\_queue\_attr\_destroy(ffrt\_queue\_attr\_t\* attr);

Parameters

-   attr: pointer to the queue attribute.

Description

-   Destroys a queue attribute object.

**ffrt\_queue\_attr\_set\_qos**

void ffrt\_queue\_attr\_set\_qos(ffrt\_queue\_attr\_t\* attr, ffrt\_qos\_t qos);

Parameters

-   attr: pointer to the queue attribute.
-   qos: QoS.

Description

-   Sets the queue QoS.

**ffrt\_queue\_attr\_get\_qos**

ffrt\_qos\_t ffrt\_queue\_attr\_get\_qos(const ffrt\_queue\_attr\_t\* attr);

Parameters

-   attr: pointer to the queue attribute.

Return Values

-   Current QoS.

Description

-   Obtains the QoS set in the current attribute.

**ffrt\_queue\_attr\_set\_timeout**

void ffrt\_queue\_attr\_set\_timeout(ffrt\_queue\_attr\_t\* attr, uint64\_t timeout\_us);

Parameters

-   attr: pointer to the queue attribute.
-   timeout\_us: timeout (μs).

Description

-   Sets the queue timeout (unit: μs).

**ffrt\_queue\_attr\_get\_timeout**

uint64\_t ffrt\_queue\_attr\_get\_timeout(const ffrt\_queue\_attr\_t\* attr);

Parameters

-   attr: pointer to the queue attribute.

Return Values

-   Current timeout threshold (μs).

Description

-   Obtains the timeout set in the current attribute.

**ffrt\_queue\_attr\_set\_callback**

void ffrt\_queue\_attr\_set\_callback(ffrt\_queue\_attr\_t\* attr, ffrt\_function\_header\_t\* f);

Parameters

-   attr: pointer to the queue attribute.
-   f: pointer to the task executor, which describes how to execute and destroy the CPU task.

Description

-   Sets the callback function to be executed after a queue task times out.
-   You are not advised to call the exit function in f. Otherwise, undefined behavior may occur.

**ffrt\_queue\_attr\_get\_callback**

ffrt\_function\_header\_t\* ffrt\_queue\_attr\_get\_callback(const ffrt\_queue\_attr\_t\* attr);

Parameters

-   attr: pointer to the queue attribute.

Return Values

-   Pointer to the task executor, which describes how to execute and destroy the CPU task.

Description

-   Obtains the timeout callback function set in the current attribute.

**ffrt\_queue\_attr\_set\_max\_concurrency**

void ffrt\_queue\_attr\_set\_max\_concurrency(ffrt\_queue\_attr\_t\* attr, const int max\_concurrency);

Parameters

-   attr: pointer to the queue attribute.
-   max\_concurrency: maximum concurrency.

Description

-   Sets the maximum queue concurrency. (Only concurrent queues are supported.)

**ffrt\_queue\_attr\_get\_max\_concurrency**

int ffrt\_queue\_attr\_get\_max\_concurrency(const ffrt\_queue\_attr\_t\* attr);

Parameters

-   attr: pointer to the queue attribute.

Return Values

-   Maximum concurrency.

Description

-   Obtains the maximum concurrency set in the current attribute. (Only concurrent queues are supported).

**ffrt\_queue\_attr\_set\_thread\_mode**

void ffrt\_queue\_attr\_set\_thread\_mode(ffrt\_queue\_attr\_t\* attr, bool mode);

Parameters

-   attr: pointer to the queue attribute.
-   mode: running mode of the queue task. The value true indicates the thread mode, and the value false indicates the coroutine mode.

Description

-   Sets the running mode of tasks in the queue. By default, the coroutine mode is used.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/z9nIiQMPRq-4RRE66dieug/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062022Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3FCDA6FB7AE2222002173828438A2CA0C04BDB6D31934C6FDE05F5F021B48267)

This API is supported since API version 20.

**ffrt\_queue\_attr\_get\_thread\_mode**

bool ffrt\_queue\_attr\_get\_thread\_mode(const ffrt\_queue\_attr\_t\* attr);

Parameters

-   attr: pointer to the queue attribute.

Return Values

-   The value true indicates the thread mode, and the value false indicates the coroutine mode.

Description

-   Obtains the running mode of tasks in the queue.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/C6ggCtlYQnSAUNWbswsNRA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062022Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0FEBB014930A8449E7BE646BCE0BDD8A079F7244E8EEF10CC3A4223ACA7B43CE)

This API is supported since API version 20.

**Example**

#include <functional>
#include "ffrt/queue.h"
#include "ffrt/cpp/task.h"

int main()
{
    ffrt\_queue\_attr\_t queue\_attr;
    // (Mandatory) Initialize the queue attribute.
    ffrt\_queue\_attr\_init(&queue\_attr);

    ffrt\_queue\_attr\_set\_qos(&queue\_attr, static\_cast<int>(ffrt\_qos\_utility));

    ffrt\_queue\_attr\_set\_timeout(&queue\_attr, 10000);

    int x = 0;
    std::function<void()>&& basicFunc = \[&x\]() { x += 1; };
    ffrt\_function\_header\_t\* func = ffrt\_queue\_attr\_get\_callback(&queue\_attr);

    ffrt\_queue\_attr\_set\_callback(&queue\_attr, ffrt::create\_function\_wrapper(basicFunc, ffrt\_function\_kind\_queue));
    // Destroy the queue attribute. This is mandatory.
    ffrt\_queue\_attr\_destroy(&queue\_attr);
    return 0;
}

## ffrt\_queue\_t

**Declaration**

typedef void\* ffrt\_queue\_t;

**Description**

Pointer to queues. It provides a series of C APIs for submitting, canceling, and waiting queue tasks and querying the number of queuing tasks.

**Methods**

**ffrt\_queue\_create**

ffrt\_queue\_t ffrt\_queue\_create(ffrt\_queue\_type\_t type, const char\* name, const ffrt\_queue\_attr\_t\* attr);

Parameters

-   type: queue type, for example, ffrt\_queue\_serial or ffrt\_queue\_concurrent.
-   name: queue name.
-   attr: pointer to the queue attribute.

Return Values

-   ffrt\_queue\_t: If the function is called successfully, a non-null queue handle is returned. Otherwise, a null pointer is returned.

Description

-   Creates a queue with a specified type and name.

**ffrt\_queue\_destroy**

void ffrt\_queue\_destroy(ffrt\_queue\_t queue);

Parameters

-   queue: queue handle.

Description

-   Destroys a queue.

**ffrt\_queue\_submit**

void ffrt\_queue\_submit(ffrt\_queue\_t queue, ffrt\_function\_header\_t\* f, const ffrt\_task\_attr\_t\* attr);

Parameters

-   queue: queue handle.
-   f: pointer to the task executor, which describes how to execute and destroy the CPU task.
-   attr: task attribute.

Description

-   Submits a task to a queue.

**ffrt\_queue\_submit\_f**

void ffrt\_queue\_submit\_f(ffrt\_queue\_t queue, ffrt\_function\_t func, void\* arg, const ffrt\_task\_attr\_t\* attr);

Parameters

-   queue: queue handle.
-   func: specified task function.
-   arg: parameter passed to the task function.
-   attr: task attribute.

Description

-   Submits a task to the queue when the callback function does not need to be destroyed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/326DOyYgQsCTpHkfoNOvLw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062022Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=900BAC8803D1DC637F21C7428CB2512DFFD89C4E2DE10EAFFD493981F58D909D)

This API is supported since API version 20.

**ffrt\_queue\_submit\_h**

ffrt\_task\_handle\_t ffrt\_queue\_submit\_h(ffrt\_queue\_t queue, ffrt\_function\_header\_t\* f, const ffrt\_task\_attr\_t\* attr);

Parameters

-   queue: queue handle.
-   f: pointer to the task executor, which describes how to execute and destroy the CPU task.
-   attr: task attribute.

Return Values

-   ffrt\_task\_handle\_t: If the function is called successfully, a non-null task handle is returned. Otherwise, a null pointer is returned.

Description

-   Submits a task to a queue and returns a task handle.

**ffrt\_queue\_submit\_h\_f**

ffrt\_task\_handle\_t ffrt\_queue\_submit\_h\_f(ffrt\_queue\_t queue, ffrt\_function\_t func, void\* arg, const ffrt\_task\_attr\_t\* attr);

Parameters

-   queue: queue handle.
-   func: specified task function.
-   arg: parameter passed to the task function.
-   attr: task attribute.

Return Values

-   ffrt\_task\_handle\_t: If the function is called successfully, a non-null task handle is returned. Otherwise, a null pointer is returned.

Description

-   Submits a task to the queue and returns the task handle when the callback function does not need to be destroyed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/XAf0NblQQlyRvfvv0hI8Sg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062022Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2F944659111BA76FA32F8E2A75BD9D701F1B426A3D67832EE9AAE9297B1E162C)

This API is supported since API version 20.

**ffrt\_queue\_wait**

void ffrt\_queue\_wait(ffrt\_task\_handle\_t handle);

Parameters

-   ffrt\_task\_handle\_t: task handle.

Description

-   Waits for a queue task to complete.

**ffrt\_queue\_cancel**

int ffrt\_queue\_cancel(ffrt\_task\_handle\_t handle);

Parameters

-   ffrt\_task\_handle\_t: task handle.

Return Values

-   The value **0** indicates success while other values indicate failure.

Description

-   Cancels a queue task.

**ffrt\_get\_main\_queue**

ffrt\_queue\_t ffrt\_get\_main\_queue();

Return Values

-   Main thread queue.

Description

-   Obtains the main thread queue for the FFRT thread to communicate with the main thread.

**ffrt\_get\_current\_queue**

ffrt\_queue\_t ffrt\_get\_current\_queue();

Return Values

-   ArkTS Worker thread queue.

Description

-   This API has been deprecated since API version 18. You are not advised to use it.
-   Obtains the ArkTS Worker thread queue for the FFRT thread to communicate with the ArkTS Worker thread.

**Example**

#include "ffrt/queue.h"
#include "ffrt/cpp/task.h"

int main()
{
    ffrt\_queue\_attr\_t queue\_attr;
    // 1. Initialize the queue attribute. This is mandatory.
    (void)ffrt\_queue\_attr\_init(&queue\_attr);

    // 2. Create a serial queue and return queue\_handle.
    ffrt\_queue\_t queue\_handle = ffrt\_queue\_create(ffrt\_queue\_serial, "test\_queue", &queue\_attr);

    int result = 0;
    std::function<void()>&& basicFunc = \[&result\]() { result += 1; };

    // 3. Submit a serial task.
    ffrt\_queue\_submit(queue\_handle, ffrt::create\_function\_wrapper(basicFunc, ffrt\_function\_kind\_queue), nullptr);

    // 4. Submit the serial task and return the task handle.
    ffrt\_task\_handle\_t t1 = ffrt\_queue\_submit\_h(queue\_handle, ffrt::create\_function\_wrapper(basicFunc, ffrt\_function\_kind\_queue), nullptr);
    // 5. Wait until the specified task is complete.
    ffrt\_queue\_wait(t1);

    ffrt\_task\_handle\_t t2 = ffrt\_queue\_submit\_h(queue\_handle, ffrt::create\_function\_wrapper(basicFunc, ffrt\_function\_kind\_queue), nullptr);
    // 6. Cancel the task with handle t2.
    ffrt\_queue\_cancel(t2);

    // 7. Destroy the handles t1 and t2 submitted to the serial queue task. This is mandatory.
    ffrt\_task\_handle\_destroy(t1);
    ffrt\_task\_handle\_destroy(t2);
    // 8. Destroy the queue attribute. This is mandatory.
    ffrt\_queue\_attr\_destroy(&queue\_attr);
    // 9. Destroy the queue handle. This is mandatory.
    ffrt\_queue\_destroy(queue\_handle);
    return 0;
}

#### Synchronization Primitive

## ffrt\_mutexattr\_t

**Declaration**

typedef enum {
    ffrt\_error = -1,
    ffrt\_success = 0,
    ffrt\_error\_nomem = ENOMEM,
    ffrt\_error\_timedout = ETIMEDOUT,
    ffrt\_error\_busy = EBUSY,
    ffrt\_error\_inval = EINVAL
} ffrt\_error\_t;

typedef enum {
    ffrt\_mutex\_normal = 0,
    ffrt\_mutex\_recursive = 2,
    ffrt\_mutex\_default = ffrt\_mutex\_normal
} ffrt\_mutex\_type;

struct ffrt\_mutexattr\_t;

int ffrt\_mutexattr\_init(ffrt\_mutexattr\_t\* attr);
int ffrt\_mutexattr\_settype(ffrt\_mutexattr\_t\* attr, int type);
int ffrt\_mutexattr\_gettype(ffrt\_mutexattr\_t\* attr, int\* type);
int ffrt\_mutexattr\_destroy(ffrt\_mutexattr\_t\* attr);

**Description**

-   Provides performance implementation similar to pthread mutex.

**Methods**

**ffrt\_mutexattr\_init**

FFRT\_C\_API int ffrt\_mutexattr\_init(ffrt\_mutexattr\_t\* attr);

Parameters

-   attr: FFRT mutex attribute.

Return Values

-   ffrt\_success is returned if attr is not empty. Otherwise, ffrt\_error\_inval is returned.

Description

-   Initializes mutexattr.

**ffrt\_mutexattr\_destroy**

FFRT\_C\_API int ffrt\_mutexattr\_destroy(ffrt\_mutexattr\_t\* attr);

Parameters

-   attr: FFRT mutex attribute.

Return Values

-   ffrt\_success is returned if attr is not empty. Otherwise, ffrt\_error\_inval is returned.

Description

-   Destroys mutexattr.

**ffrt\_mutexattr\_settype**

FFRT\_C\_API int ffrt\_mutexattr\_settype(ffrt\_mutexattr\_t\* attr, int type);

Parameters

-   attr: FFRT mutex attribute.
-   type: FFRT mutex type. Currently, only ffrt\_mutex\_normal and ffrt\_mutex\_recursive are supported.

Return Values

-   ffrt\_success is returned if attr is not empty and type is valid. Otherwise, ffrt\_error\_inval is returned.

Description

-   Sets the FFRT mutex attribute.

**ffrt\_mutexattr\_gettype**

FFRT\_C\_API int ffrt\_mutexattr\_gettype(ffrt\_mutexattr\_t\* attr, int\* type);

Parameters

-   attr: FFRT mutex attribute.
-   type: pointer to the FFRT mutex type.

Return Values

-   ffrt\_success is returned if neither attr nor type is empty. Otherwise, ffrt\_error\_inval is returned.

Description

-   Obtains the FFRT mutex attribute.

**Example**

ffrt\_mutexattr\_t attr;
// Initialize the mutex attribute.
ffrt\_mutexattr\_init(&attr);
// Set a mutex.
ffrt\_mutexattr\_settype(&attr, ffrt\_mutex\_normal);
// Set a recursive lock.
ffrt\_mutexattr\_settype(&attr, ffrt\_mutex\_recursive);
// Obtain the mutex type.
int type = ffrt\_mutex\_default;
ffrt\_mutexattr\_gettype(&attr, &type);
// Destroy the mutex attribute.
ffrt\_mutexattr\_destroy(&attr);

## ffrt\_mutex\_t

-   Implements pthread\_mutex\_t, but does not support initialization of PTHREAD\_MUTEX\_INITIALIZER.

**Declaration**

struct ffrt\_mutex\_t;
struct ffrt\_mutexattr\_t;

int ffrt\_mutex\_init(ffrt\_mutex\_t\* mutex, const ffrt\_mutexattr\_t\* attr);
int ffrt\_mutex\_lock(ffrt\_mutex\_t\* mutex);
int ffrt\_mutex\_unlock(ffrt\_mutex\_t\* mutex);
int ffrt\_mutex\_trylock(ffrt\_mutex\_t\* mutex);
int ffrt\_mutex\_destroy(ffrt\_mutex\_t\* mutex);

**Description**

-   This API can be called inside or outside an FFRT task.
-   The traditional function pthread\_mutex\_t may cause unexpected kernel mode trap when it fails to lock a mutex. **ffrt\_mutex\_t** solves this problem and therefore provides better performance if used properly.
-   ffrt\_mutexattr\_t in the C API needs to be explicitly created and destroyed by calling ffrt\_mutexattr\_init and ffrt\_mutexattr\_destroy. Otherwise, undefined behavior may occur.
-   ffrt\_mutex\_t in the C API needs to be explicitly created and destroyed by calling ffrt\_mutex\_init and ffrt\_mutex\_destroy. Otherwise, undefined behavior may occur.
-   You need to set the ffrt\_mutex\_t object in the C code to null or destroy the object. For the same ffrt\_mutex\_t object, ffrt\_mutex\_destroy can be called only once. Otherwise, undefined behavior may occur.
-   The same ffrt\_mutexattr\_t in the C API can call ffrt\_mutexattr\_init and ffrt\_mutexattr\_destroy only once. Repeated calling may cause undefined behavior.
-   You need to explicitly call ffrt\_mutexattr\_destroy after ffrt\_mutex\_init and before ffrt\_mutex\_destroy.
-   If ffrt\_mutex\_t is accessed after ffrt\_mutex\_destroy, undefined behavior may occur.

**Methods**

**ffrt\_mutex\_init**

FFRT\_C\_API int ffrt\_mutex\_init(ffrt\_mutex\_t\* mutex, const ffrt\_mutexattr\_t\* attr);

Parameters

-   mutex: pointer to the operated mutex.
-   attr: FFRT mutex attribute. Its valid value can be a null pointer, ffrt\_mutex\_normal, or ffrt\_mutex\_recursive.

Return Values

-   ffrt\_success is returned if mutex is not empty and attr is within the valid value range. Otherwise, ffrt\_error\_inval is returned.

Description

-   Initializes the FFRT mutex.

**ffrt\_mutex\_destroy**

FFRT\_C\_API int ffrt\_mutex\_destroy(ffrt\_mutex\_t\* mutex);

Parameters

-   mutex: pointer to the operated mutex.

Return Values

-   ffrt\_success is returned if mutex is not empty. Otherwise, ffrt\_error\_inval is returned.

Description

-   Destroys a specified mutex or recursive lock.

**ffrt\_mutex\_lock**

FFRT\_C\_API int ffrt\_mutex\_lock(ffrt\_mutex\_t\* mutex);

Parameters

-   mutex: pointer to the operated mutex.

Return Values

-   ffrt\_success is returned if mutex is not empty. Otherwise, ffrt\_error\_inval is returned.

Description

-   Locks a specified mutex or recursive lock. This method blocks the current task until the mutex is successfully obtained.

**ffrt\_mutex\_unlock**

FFRT\_C\_API int ffrt\_mutex\_unlock(ffrt\_mutex\_t\* mutex);

Parameters

-   mutex: pointer to the operated mutex.

Return Values

-   ffrt\_success is returned if mutex is not empty. Otherwise, ffrt\_error\_inval is returned.

Description

-   Unlocks a specified mutex or recursive lock.

**ffrt\_mutex\_trylock**

FFRT\_C\_API int ffrt\_mutex\_trylock(ffrt\_mutex\_t\* mutex);

Parameters

-   mutex: pointer to the operated mutex.

Return Values

-   **ffrt\_error\_inval** is returned if mutex is empty. ffrt\_success is returned if mutex is not empty and the mutex is successfully held. ffrt\_error\_busy is returned if mutex is not empty and the mutex fails to be held.

Description

-   Locks a specified mutex or recursive lock.

**Example**

#include "ffrt/mutex.h"
#include "ffrt/cpp/task.h"

int main()
{
    ffrt\_mutexattr\_t attr;
    ffrt\_mutex\_t lock;
    int sum = 0;
    int type = ffrt\_mutex\_default;
    ffrt\_mutexattr\_init(&attr);
    ffrt\_mutexattr\_settype(&attr, ffrt\_mutex\_recursive);
    ffrt\_mutexattr\_gettype(&attr, &type);
    ffrt\_mutex\_init(&lock, &attr);
    ffrt::submit(\[&\]() {
        ffrt\_mutex\_lock(&lock);
        ffrt\_mutex\_trylock(&lock);
        sum++;
        ffrt\_mutex\_lock(&lock);
        ffrt\_mutex\_trylock(&lock);
        sum++;
        ffrt\_mutex\_unlock(&lock);
        ffrt\_mutex\_unlock(&lock);
        ffrt\_mutex\_unlock(&lock);
        ffrt\_mutex\_unlock(&lock);
        }, {}, {});

    ffrt::wait();

    ffrt\_mutexattr\_destroy(&attr);
    ffrt\_mutex\_destroy(&lock);
    return 0;
}

## ffrt\_rwlock\_t

-   Implements pthread\_rwlock\_t.

**Declaration**

struct ffrt\_rwlock\_t;
struct ffrt\_rwlockattr\_t;

int ffrt\_rwlock\_init(ffrt\_rwlock\_t\* rwlock, const ffrt\_rwlockattr\_t\* attr);
int ffrt\_rwlock\_wrlock(ffrt\_rwlock\_t\* rwlock);
int ffrt\_rwlock\_rdlock(ffrt\_rwlock\_t\* rwlock);
int ffrt\_rwlock\_trywrlock(ffrt\_rwlock\_t\* rwlock);
int ffrt\_rwlock\_tryrdlock(ffrt\_rwlock\_t\* rwlock);
int ffrt\_rwlock\_unlock(ffrt\_rwlock\_t\* rwlock);
int ffrt\_rwlock\_destroy(ffrt\_rwlock\_t\* rwlock);

**Description**

-   This API can be called inside or outside an FFRT task.
-   This API can avoid the issue that pthread\_rwlock\_t sleeps without releasing threads. The performance is better when the API is properly used.
-   ffrt\_rwlock\_t in the C API needs to be explicitly created and destroyed by calling ffrt\_rwlock\_init and ffrt\_rwlock\_destroy. Otherwise, undefined behavior may occur.
-   When ffrt\_rwlockattr\_t is called, the input parameter of ffrt\_rwlockattr\_t must be a null pointer.
-   You need to set the ffrt\_rwlock\_t object in the C code to null or destroy the object. For the same ffrt\_rwlock\_t object, ffrt\_rwlock\_destroy can be called only once. Otherwise, undefined behavior may occur.
-   If ffrt\_rwlock\_t is accessed after ffrt\_rwlock\_destroy is called, undefined behavior may occur.

**Methods**

**ffrt\_rwlock\_init**

FFRT\_C\_API int ffrt\_rwlock\_init(ffrt\_rwlock\_t\* rwlock, const ffrt\_rwlockattr\_t\* attr);

Parameters

-   rwlock: pointer to the operated read-write lock.
-   attr: pointer to the attribute of the operated read-write lock. Only the default mode is supported. That is, attr must be set to a null pointer.

Return Values

-   ffrt\_success is returned if rwlock is not empty and attr is empty. Otherwise, ffrt\_error\_inval is returned.

Description

-   Initializes the read-write lock.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/pwz-J3CzQVmRGrrR1pEMuw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062022Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=88A5ACB3846D6F186ACBF3C9548A744FC856CB44B318A69ABD2E2EC3C38097E2)

This API is supported since API version 18.

**ffrt\_rwlock\_wrlock**

FFRT\_C\_API int ffrt\_rwlock\_wrlock(ffrt\_rwlock\_t\* rwlock);

Parameters

-   rwlock: pointer to the operated read-write lock.

Return Values

-   ffrt\_success is returned if rwlock is not empty. Otherwise, ffrt\_error\_inval is returned.

Description

-   Adds a write lock to the specified read-write lock.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/VLgY91XqQf6eeyDjbRTHHA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062022Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8292607A662A3F059E35586C350768E828567D8F666D6448032908753B0505B2)

This API is supported since API version 18.

**ffrt\_rwlock\_rdlock**

FFRT\_C\_API int ffrt\_rwlock\_rdlock(ffrt\_rwlock\_t\* rwlock);

Parameters

-   rwlock: pointer to the operated read-write lock.

Return Values

-   ffrt\_success is returned if rwlock is not empty. Otherwise, ffrt\_error\_inval is returned.

Description

-   Adds a read lock to the specified read-write lock.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/AEhTWSUlQzKMUAybgC5avg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062022Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=387FAC5C4BB3D62B2BBF321FE621C7BFCFDD769EC6B91F8DF1A1FCC38C0A7E6E)

This API is supported since API version 18.

**ffrt\_rwlock\_trywrlock**

FFRT\_C\_API int ffrt\_rwlock\_trywrlock(ffrt\_rwlock\_t\* rwlock);

Parameters

-   rwlock: pointer to the operated read-write lock.

Return Values

-   ffrt\_success is returned if rwlock is not empty and no other thread holds the read-write lock. Otherwise, ffrt\_error\_inval is returned.

Description

-   Adds a write lock to the specified read-write lock.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/WcnNeAu9Re229HBkJMFILQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062022Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4D1E4A6D298860D68FFCE2CAEE639FD3678585693920EE0D7D211651F77F1E44)

This API is supported since API version 18.

**ffrt\_rwlock\_tryrdlock**

FFRT\_C\_API int ffrt\_rwlock\_tryrdlock(ffrt\_rwlock\_t\* rwlock);

Parameters

-   rwlock: pointer to the operated read-write lock.

Return Values

-   ffrt\_success is returned if rwlock is not empty and no other thread holds the write lock. Otherwise, ffrt\_error\_inval is returned.

Description

-   Adds a read lock to the specified read-write lock.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/WR2QXyXaRt-bW7lBuo_iyw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062022Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=02F0830C675B121F8B9BBE8AA0EC3C92866588FA71EECD1F2105A5FD4EC04622)

This API is supported since API version 18.

**ffrt\_rwlock\_unlock**

FFRT\_C\_API int ffrt\_rwlock\_unlock(ffrt\_rwlock\_t\* rwlock);

Parameters

-   rwlock: pointer to the operated read-write lock.

Return Values

-   ffrt\_success is returned if rwlock is not empty. Otherwise, ffrt\_error\_inval is returned.

Description

-   Unlocks the specified read-write lock.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/FA9IcvllQga8xAjUTOE-qA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062022Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ECAC7B8FF29936D2CD343E63E49D76D8AAA5C8785F32AEB6F99A62E3447B24C0)

This API is supported since API version 18.

**ffrt\_rwlock\_destroy**

FFRT\_C\_API int ffrt\_rwlock\_destroy(ffrt\_rwlock\_t\* rwlock);

Parameters

-   rwlock: pointer to the operated read-write lock.

Return Values

-   ffrt\_success is returned if rwlock is not empty. Otherwise, ffrt\_error\_inval is returned.

Description

-   Destroys a specified read-write lock.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/nQ63P_T0TJiuzl5H9R91FA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062022Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4B9758F0E6986E5654AD27EAF3C2C38682BD9E51E643DA7827464667162301A3)

This API is supported since API version 18.

**Example**

#include "ffrt/shared\_mutex.h"
#include "ffrt/sleep.h"
#include "ffrt/cpp/task.h"

int main()
{
    ffrt\_rwlock\_t rwlock;
    int x = 0;
    ffrt\_rwlock\_init(&rwlock, nullptr);
    ffrt::submit(\[&\]() {
        ffrt\_rwlock\_wrlock(&rwlock);
        ffrt\_usleep(10);
        x++;
        ffrt\_rwlock\_unlock(&rwlock);
    },{},{});

    ffrt::submit(\[&\]() {
        ffrt\_usleep(2);
        ffrt\_rwlock\_rdlock(&rwlock);
        ffrt\_rwlock\_unlock(&rwlock);
    },{},{});

    ffrt::submit(\[&\]() {
        ffrt\_usleep(2);
        if(ffrt\_rwlock\_trywrlock(&rwlock)){
            x++;
            ffrt\_rwlock\_unlock(&rwlock);
        }
    },{},{});

    ffrt::submit(\[&\]() {
        ffrt\_usleep(2);
        if(ffrt\_rwlock\_tryrdlock(&rwlock)){
            ffrt\_rwlock\_unlock(&rwlock);
        }
    },{},{});

    ffrt::wait();

    ffrt\_rwlock\_destroy(&rwlock);
    return 0;
}

## ffrt\_cond\_t

-   Implements the pthread semaphore function, but does not support initialization of PTHREAD\_COND\_INITIALIZER.

**Declaration**

typedef enum {
    ffrt\_error = -1,
    ffrt\_success = 0,
    ffrt\_error\_nomem = ENOMEM,
    ffrt\_error\_timedout = ETIMEDOUT,
    ffrt\_error\_busy = EBUSY,
    ffrt\_error\_inval = EINVAL
} ffrt\_error\_t;

typedef struct {
    uint32\_t storage\[(ffrt\_cond\_storage\_size + sizeof(uint32\_t) - 1) / sizeof(uint32\_t)\];
} ffrt\_cond\_t;

int ffrt\_cond\_init(ffrt\_cond\_t\* cond, const ffrt\_condattr\_t\* attr);
int ffrt\_cond\_signal(ffrt\_cond\_t\* cond);
int ffrt\_cond\_broadcast(ffrt\_cond\_t\* cond);
int ffrt\_cond\_wait(ffrt\_cond\_t\*cond, ffrt\_mutex\_t\* mutex);
int ffrt\_cond\_timedwait(ffrt\_cond\_t\* cond, ffrt\_mutex\_t\* mutex, const struct timespec\* time\_point);
int ffrt\_cond\_destroy(ffrt\_cond\_t\* cond);

**Description**

-   This API can be called inside or outside an FFRT task.
-   The traditional function pthread\_cond\_t may cause unexpected kernel mode trap when the conditions are not met. **ffrt\_cond\_t** solves this problem and therefore provides better performance if being used properly.
-   Note that ffrt\_cond\_t in the C API needs to be explicitly created and destroyed by calling ffrt\_cond\_init and ffrt\_cond\_destroy. However, in the C++ API, the dependency construction and destruction are automatically completed.
-   You need to set the ffrt\_cond\_t object in the C code to null or destroy the object. For the same ffrt\_cond\_t object, ffrt\_cond\_destroy can be called only once. Otherwise, undefined behavior may occur.
-   If ffrt\_cond\_t is accessed after ffrt\_cond\_destroy is called, undefined behavior may occur.

**Methods**

**ffrt\_cond\_init**

FFRT\_C\_API int ffrt\_cond\_init(ffrt\_cond\_t\* cond, const ffrt\_condattr\_t\* attr);

Parameters

-   cond: pointer to the target semaphore.
-   attr: pointer to the attribute. A null pointer indicates that the default attribute is used.

Return Values

-   ffrt\_success is returned if cond is not empty. Otherwise, ffrt\_error\_inval is returned.

Description

-   Initializes the FFRT condition variable.

**ffrt\_cond\_destroy**

FFRT\_C\_API int ffrt\_cond\_destroy(ffrt\_cond\_t\* cond);

Parameters

-   cond: pointer to the target semaphore.

Return Values

-   ffrt\_success is returned if cond is not empty. Otherwise, ffrt\_error\_inval is returned.

Description

-   Destroys an FFRT condition variable.

**ffrt\_cond\_signal**

FFRT\_C\_API int ffrt\_cond\_signal(ffrt\_cond\_t\* cond);

Parameters

-   cond: pointer to the target semaphore.

Return Values

-   ffrt\_success is returned if cond is not empty. Otherwise, ffrt\_error\_inval is returned.

Description

-   Unblocks at least one of the threads that are blocked on a condition variable.

**ffrt\_cond\_broadcast**

FFRT\_C\_API int ffrt\_cond\_broadcast(ffrt\_cond\_t\* cond);

Parameters

-   cond: pointer to the target semaphore.

Return Values

-   ffrt\_success is returned if cond is not empty. Otherwise, ffrt\_error\_inval is returned.

Description

-   Unblocks all threads currently blocked on a condition variable.

**ffrt\_cond\_wait**

FFRT\_C\_API int ffrt\_cond\_wait(ffrt\_cond\_t\* cond, ffrt\_mutex\_t\* mutex);

Parameters

-   cond: pointer to the target semaphore.
-   mutex: pointer to the target mutex.

Return Values

-   ffrt\_success is returned if neither cond nor mutex is empty. Otherwise, ffrt\_error\_inval is returned.

Description

-   Blocks a task on a condition variable. When using this method, a task releases the input mutex and enters the waiting state. The task obtains the mutex again and continues to execute until another task notifies the condition variable.
-   This method is usually used together with ffrt\_mutex\_lock or ffrt\_mutex\_trylock to ensure that the mutex is held before entering the wait state.

**ffrt\_cond\_timedwait**

FFRT\_C\_API int ffrt\_cond\_timedwait(ffrt\_cond\_t\* cond, ffrt\_mutex\_t\* mutex, const struct timespec\* time\_point);

Parameters

-   cond: pointer to the target semaphore.
-   mutex: pointer to the target mutex.
-   time\_point: pointer to the maximum duration during which the thread is blocked.

Return Values

-   ffrt\_success is returned if cond, mutex, and time\_point are not empty. Otherwise, ffrt\_error\_inval is returned.

Description

-   Blocks a task on a condition variable until the specified timeout is reached.
-   Unlike ffrt\_cond\_wait, the ffrt\_cond\_timedwait method allows a task to wait for a period of time on a condition variable. If no notification is received within the specified period of time, the task is woken up and the function returns.

**Example**

#include <iostream>
#include "ffrt/condition\_variable.h"
#include "ffrt/mutex.h"
#include "ffrt/sleep.h"
#include "ffrt/cpp/task.h"

struct timespec timeoutms\_to\_tm(int timeout\_ms) {
    struct timespec ts;
    clock\_gettime(CLOCK\_REALTIME, &ts);
    ts.tv\_sec += timeout\_ms / 1000;
    ts.tv\_nsec += (timeout\_ms % 1000) \* 1000000;
    if (ts.tv\_nsec >= 1000000000) {
        ts.tv\_sec += 1;
        ts.tv\_nsec -= 1000000000;
    }
    return ts;
}

int main()
{
    int a = 0;
    ffrt\_cond\_t cond;
    ffrt\_mutex\_t lock\_;
    ffrt\_cond\_init(&cond, nullptr);
    ffrt\_mutex\_init(&lock\_, nullptr);

    for (int i = 0; i < 3; i++) {
        ffrt::submit(\[&\]() {
            int timeout = 2000;
            struct timespec tm = timeoutms\_to\_tm(timeout);
            ffrt\_mutex\_lock(&lock\_);
            auto start = std::chrono::high\_resolution\_clock::now();
            ffrt\_cond\_timedwait(&cond, &lock\_, &tm);
            auto end = std::chrono::high\_resolution\_clock::now();
            a = 123;
            ffrt\_mutex\_unlock(&lock\_);
            std::chrono::duration<double, std::milli> elapsed = end - start;
            double t = elapsed.count();
            std::cout << "ffrt\_cond\_timedwait " << t << " ms" << std::endl;
            }, {}, {});
    }

    ffrt::submit(\[&\]() {
        ffrt\_usleep(1000 \* 1000);
        ffrt\_mutex\_lock(&lock\_);
        a = 5;
        ffrt\_cond\_broadcast(&cond);
        ffrt\_mutex\_unlock(&lock\_);
        }, {}, {});
    ffrt::wait();
    ffrt\_cond\_destroy(&cond);
    ffrt\_mutex\_destroy(&lock\_);
    return 0;
}

#### Blocking Primitive

## ffrt\_usleep

**Declaration**

FFRT\_C\_API int ffrt\_usleep(uint64\_t usec);

**Parameters**

-   usec: sleep duration, in μs.

**Description**

-   This API can be called inside or outside an FFRT task.
-   Provides performance implementation similar to C11 sleep and Linux usleep.
-   The sleep precision of this API is μs.
-   The traditional function sleep may cause unexpected kernel mode trap. **ffrt\_usleep** solves this problem and therefore provides better performance if used properly.

**Example**

#include "ffrt/sleep.h"
#include "ffrt/cpp/task.h"

int main()
{
    ffrt::submit(\[=\]() { ffrt\_usleep(10); }, {}, {});
    ffrt::wait();
    return 0;
}

#### Cooperative Primitive

## ffrt\_yield

**Declaration**

FFRT\_C\_API void ffrt\_yield();

**Description**

-   This API can be called inside or outside an FFRT task.
-   Yields CPU execution resources for other executable tasks. If there is no other executable task, yield is invalid.
-   The exact behavior of this API depends on the implementation, especially the mechanism and system state of the FFRT scheduler in use.

**Example**

#include <iostream>
#include "ffrt/sleep.h"
#include "ffrt/cpp/task.h"

int main()
{
    int count = 12;
    for (int i = 0; i < count; i++) {
        ffrt::submit(\[&\]() {
            ffrt\_usleep(100);
            std::cout << "test" << std::endl;
            ffrt\_yield();
        }, {}, {});
    }
    ffrt::wait();
    return 0;
}

#### Timer

## ffrt\_timer\_t

**Declaration**

typedef int ffrt\_timer\_t;
typedef void (\*ffrt\_timer\_cb)(void\* data);

**Description**

Provides timer-related functions.

**Methods**

**ffrt\_timer\_start**

Declaration

FFRT\_C\_API ffrt\_timer\_t ffrt\_timer\_start(ffrt\_qos\_t qos, uint64\_t timeout, void\* data, ffrt\_timer\_cb cb, bool repeat);

Parameters

-   qos: QoS.
-   timeout: timer timeout, in ms.
-   cb: callback function after expiration.
-   data: input parameter of the callback function.
-   repeat: whether the timer is triggered repeatedly.

Return Values

-   ffrt\_timer\_t, which indicates the timer handle.

Description

-   Starts a timer. If the timer expires and is not stopped, the callback function is executed. If repeat is set to repeat, the timer is set again after it expires.
-   You are not advised to call the exit function in cb. Otherwise, undefined behavior may occur.

**ffrt\_timer\_stop**

Declaration

FFRT\_C\_API int ffrt\_timer\_stop(ffrt\_qos\_t qos, ffrt\_timer\_t handle);

Parameters

-   qos: QoS.
-   handle: timer handle.

Return Values

-   The value **0** indicates success, and the value **\-1** indicates failure.

Description

-   Stops a timer. It is used with ffrt\_timer\_start.
-   This is a blocking API and should be avoided in the callback to prevent deadlock or synchronization problems. If the callback corresponding to the input handle is being executed, this function will wait until the callback is complete.

**Example**

-   Example 1: Use a one-shot timer.
    
    #include <stdio.h>
    #include <unistd.h>
    #include "ffrt/timer.h"
    
    static void test\_fun(void \*data)
    {
        \*(int \*)data += 1;
    }
    
    void (\*cb)(void \*) = test\_fun;
    
    int main()
    {
        static int x = 0;
        void \*data = &x;
        uint64\_t timeout = 200;
        // Start a timer and execute the callback function after 200 ms.
        int handle = ffrt\_timer\_start(ffrt\_qos\_default, timeout, data, cb, false);
        usleep(300000);
        // The timer has been executed and cannot be stopped.
        ffrt\_timer\_stop(ffrt\_qos\_default, handle);
        printf("data: %d\\n", x); // Set the value of x to 1.
        return 0;
    }
    
-   Example 2: Use a repeating timer.
    
    #include <stdio.h>
    #include <unistd.h>
    #include "ffrt/timer.h"
    
    static void test\_fun(void \*data)
    {
        \*(int \*)data += 1;
    }
    
    void (\*cb)(void \*) = test\_fun;
    
    int main()
    {
        static int x = 0;
        void \*data = &x;
        uint64\_t timeout = 200;
        // Start a repeating timer and execute the callback function every 200 ms.
        int handle = ffrt\_timer\_start(ffrt\_qos\_default, timeout, data, cb, true);
        usleep(500000);
        // Stops the repeating timer.
        ffrt\_timer\_stop(ffrt\_qos\_default, handle);
        printf("data: %d\\n", x); // Set the value of x to 2.
        return 0;
    }
    

#### Loop

## ffrt\_loop\_t

**Declaration**

typedef void\* ffrt\_loop\_t;

**Description**

Provides loop-related functions.

**Methods**

**ffrt\_loop\_create**

Declaration

FFRT\_C\_API ffrt\_loop\_t ffrt\_loop\_create(ffrt\_queue\_t queue);

Parameters

-   queue: a concurrent queue that needs to be bound with a loop.

Return Values

-   ffrt\_loop\_t object.

Description

-   Creates a loop and bind a concurrent queue for storing tasks. You can submit a task to the queue so that the task can be executed in the loop.

**ffrt\_loop\_destroy**

Declaration

FFRT\_C\_API int ffrt\_loop\_destroy(ffrt\_loop\_t loop);

Parameters

-   loop: loop object.

Return Values

-   The value **0** indicates success, and the value **\-1** indicates failure.

Description

-   Destroys a loop and unbinds it from the queue.

**ffrt\_loop\_run**

Declaration

FFRT\_C\_API int ffrt\_loop\_run(ffrt\_loop\_t loop);

Parameters

-   loop: loop object.

Return Values

-   The value **0** indicates success, and the value **\-1** indicates failure.

Description

-   Runs a loop. The thread that invokes this method executes the loop at the same time, executes queue tasks, and listens for the poller and timer.

**ffrt\_loop\_stop**

Declaration

FFRT\_C\_API void ffrt\_loop\_stop(ffrt\_loop\_t loop);

Parameters

-   loop: loop object.

Description

-   Stops a loop. This method is invoked to enable the thread that executes the loop to exit the loop.

**ffrt\_loop\_epoll\_ctl**

Declaration

int ffrt\_loop\_epoll\_ctl(ffrt\_loop\_t loop, int op, int fd, uint32\_t events, void \*data, ffrt\_poller\_cb cb)

Parameters

-   loop: loop object.
-   op: FD operator. For details, see the operation type of **epoll\_ctl**.
-   fd: event descriptor.
-   events: event. For details, see the event type of **epoll\_ctl**.
-   data: input parameter of the callback function.
-   cb: callback function.

Return Values

-   The value **0** indicates success, and the value **\-1** indicates failure.

Description

-   Manages FD listening on the loop. Event listening and callback are processed on the loop thread.
-   You are not advised to call the exit function in cb. Otherwise, undefined behavior may occur.

**ffrt\_loop\_timer\_start**

Declaration

FFRT\_C\_API ffrt\_timer\_t ffrt\_loop\_timer\_start(ffrt\_loop\_t loop, uint64\_t timeout, void\* data, ffrt\_timer\_cb cb, bool repeat);

Parameters

-   loop: loop object.
-   timeout: timer timeout, in ms.
-   cb: callback function after expiration.
-   data: input parameter of the callback function.
-   repeat: whether the timer is triggered repeatedly.

Return Values

-   ffrt\_timer\_t, which indicates the timer handle.

Description

-   Starts a timer on the loop. The usage is the same as that of ffrt\_timer\_start. The only difference is that the listening and callback execution of the timer are processed on the loop thread.
-   You are not advised to call the exit function in cb. Otherwise, undefined behavior may occur.

**ffrt\_loop\_timer\_stop**

Declaration

FFRT\_C\_API int ffrt\_loop\_timer\_stop(ffrt\_loop\_t loop, ffrt\_timer\_t handle);

Parameters

-   loop: loop object.
-   handle: timer handle.

Return Values

-   The value **0** indicates success, and the value **\-1** indicates failure.

Description

-   Stops a timer. The usage is the same as that of ffrt\_timer\_stop.

**Example**

-   Example 1: loop and concurrent queue.
    
    #include <pthread.h>
    #include <stdio.h>
    #include "ffrt/loop.h"
    
    void\* ThreadFunc(void\* p)
    {
        int ret = ffrt\_loop\_run(p);
        if (ret == 0) {
            printf("loop normal operation.");
        }
        return NULL;
    }
    
    int main()
    {
        // Create a concurrent queue.
        ffrt\_queue\_attr\_t queue\_attr;
        (void)ffrt\_queue\_attr\_init(&queue\_attr);
        ffrt\_queue\_t queue\_handle = ffrt\_queue\_create(ffrt\_queue\_concurrent, "test\_queue", &queue\_attr);
    
        // Create a loop.
        ffrt\_loop\_t loop = ffrt\_loop\_create(queue\_handle);
    
        // Create a separate thread to perform the loop.
        pthread\_t thread;
        int ret = pthread\_create(&thread, 0, ThreadFunc, loop);
        if (ret != 0) {
            printf("pthread\_create failed!");
            ffrt\_loop\_destroy(loop);
            ffrt\_queue\_attr\_destroy(&queue\_attr);
            ffrt\_queue\_destroy(queue\_handle);
            return 0;
        }
    
        // Stop and destroy the loop.
        ffrt\_loop\_stop(loop);
        ffrt\_loop\_destroy(loop);
    
        // Destroy the concurrent queue.
        ffrt\_queue\_attr\_destroy(&queue\_attr);
        ffrt\_queue\_destroy(queue\_handle);
        return 0;
    }
    
-   Example 2: loop, concurrent queue, and timer.
    
    #include <pthread.h>
    #include <unistd.h>
    #include <stdio.h>
    #include <functional>
    #include <sys/epoll.h>
    #include <sys/eventfd.h>
    #include "ffrt/loop.h"
    #include "ffrt/cpp/task.h"
    
    void\* ThreadFunc(void\* p)
    {
        ffrt\_loop\_run(p);
        return nullptr;
    }
    
    static void test\_fun(void\* data)
    {
        \*(int\*)data += 1;
    }
    
    static void (\*cb)(void\*) = test\_fun;
    
    void testCallBack(void \*data, unsigned int events) {}
    
    struct TestData {
        int fd;
        uint64\_t expected;
    };
    
    int main()
    {
        // Create a concurrent queue.
        ffrt\_queue\_attr\_t queue\_attr;
        (void)ffrt\_queue\_attr\_init(&queue\_attr);
        ffrt\_queue\_t queue\_handle = ffrt\_queue\_create(ffrt\_queue\_concurrent, "test\_queue", &queue\_attr);
    
        // Create a loop.
        auto loop = ffrt\_loop\_create(queue\_handle);
        int result1 = 0;
    
        // Submit a task to the loop queue.
        std::function<void()> &&basicFunc1 = \[&result1\]() { result1 += 10; };
        ffrt\_task\_handle\_t task = ffrt\_queue\_submit\_h(queue\_handle, ffrt::create\_function\_wrapper(basicFunc1, ffrt\_function\_kind\_queue), nullptr);
    
        // Create a separate thread to perform the loop.
        pthread\_t thread;
        int ret = pthread\_create(&thread, 0, ThreadFunc, loop);
        if (ret != 0) {
            printf("pthread\_create failed!");
            ffrt\_loop\_destroy(loop);
            ffrt\_queue\_attr\_destroy(&queue\_attr);
            ffrt\_queue\_destroy(queue\_handle);
            return 0;
        }
    
        static int x = 0;
        int\* xf = &x;
        void\* data = xf;
        uint64\_t timeout1 = 20;
        uint64\_t timeout2 = 10;
        uint64\_t expected = 0xabacadae;
    
        int testFd = eventfd(0, EFD\_NONBLOCK | EFD\_CLOEXEC);
        struct TestData testData {.fd = testFd, .expected = expected};
    
        // Register a timer with the loop.
        ffrt\_timer\_t timeHandle = ffrt\_loop\_timer\_start(loop, timeout1, data, cb, false);
    
        // Register an FD listener with the loop.
        int ret = ffrt\_loop\_epoll\_ctl(loop, EPOLL\_CTL\_ADD, testFd, EPOLLIN, (void\*)(&testData), testCallBack);
        if (ret == 0) {
            printf("ffrt\_loop\_epoll\_ctl executed successfully.\\n");
        }
        ssize\_t n = write(testFd, &expected, sizeof(uint64\_t));
        usleep(25000);
        // Delete the FD listener.
        ffrt\_loop\_epoll\_ctl(loop, EPOLL\_CTL\_DEL, testFd, 0, nullptr, nullptr);
    
        // Stop the loop.
        ffrt\_loop\_stop(loop);
        pthread\_join(thread, nullptr);
    
        // Delete the timer.
        ffrt\_loop\_timer\_stop(loop, timeHandle);
    
        // Destroy the loop.
        ret = ffrt\_loop\_destroy(loop);
    
        // Destroy the concurrent queue.
        ffrt\_queue\_attr\_destroy(&queue\_attr);
        ffrt\_queue\_destroy(queue\_handle);
        return 0;
    }
    

#### Fiber

## ffrt\_fiber\_t

**Declaration**

struct ffrt\_fiber\_t;

**Description**

-   A fiber is a lightweight user mode thread that enables efficient task scheduling and context switching within the user space.
-   ffrt\_fiber\_t is used to save and restore the execution context of the fiber.

**Methods**

**ffrt\_fiber\_init**

Declaration

FFRT\_C\_API int ffrt\_fiber\_init(ffrt\_fiber\_t\* fiber, void(\*func)(void\*), void\* arg, void\* stack, size\_t stack\_size);

Parameters

-   fiber: pointer to the fiber.
-   func: pointer to the function when the fiber is started.
-   arg: pointer to the argument when the fiber is started.
-   stack: pointer to the start address of the stack space used by the fiber during execution.
-   stack\_size: size of the fiber stack, in bytes.

Return Values

-   If the initialization is successful, ffrt\_success is returned. Otherwise, ffrt\_error is returned.
-   The common reason of the error is that stack\_size does not meet the minimum stack space limit that varies by platform. It is recommended that the stack space size be set to 4 KB or larger.

Description

-   Initializes a fiber. The pointer and arguments for starting the fiber process, and the stack space used at runtime need to be transferred. The fiber does not manage any memory; the lifecycle of the stack is managed by the caller.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/mFbKMrQSTcKUa3LQcGTu9A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062022Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6300D2256EC349E02C0374C69983C66F792FC7937E102FCAA34BA96D1ACAFDD5)

This API is supported since API version 20.

**ffrt\_fiber\_switch**

Declaration

FFRT\_C\_API void ffrt\_fiber\_switch(ffrt\_fiber\_t\* from, ffrt\_fiber\_t\* to);

Parameters

-   from: pointer to the saved fiber context. The thread that calls this function suspends the current task.
-   to: pointer to the restored fiber context. The thread that calls this function executes the task specified by to.

Description

-   When the fiber context is switched, the thread that calls this function suspends the current task, saves the context to the from fiber, restores the context of the to fiber, and executes the task specified by to.
-   Note that from and to are not verified. The caller must ensure the validity of these addresses to prevent process crashes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/_ok2pm4-RNC-kF9JsMMAqA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062022Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9FFFC48116F11D989A8F34B18271E2694FFF4AB911FBC41675DE2A53BDDD6E30)

This API is supported since API version 20.
