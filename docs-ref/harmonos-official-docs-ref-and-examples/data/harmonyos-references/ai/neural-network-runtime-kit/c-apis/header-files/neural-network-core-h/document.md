# neural\_network\_core.h

#### Overview

Defines APIs for the Neural Network Core module. The AI inference framework uses the native APIs provided by Neural Network Core to compile models and perform inference and computing on acceleration hardware.

Some API definitions have been moved from **neural\_network\_runtime.h** to this file for unified presentation. These APIs are supported since API version 11 and can be used in all later versions.

Currently, the APIs of Neural Network Core do not support multi-thread calling.

**File to include**: <neural\_network\_runtime/neural\_network\_core.h>

**Library**: libneural\_network\_core.so

**System capability**: SystemCapability.Ai.NeuralNetworkRuntime

**Since**: 11

**Related module**: [NeuralNetworkRuntime](../../modules/neuralnetworkruntime/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_NNCompilation \*OH\_NNCompilation\_Construct(const OH\_NNModel \*model)](#oh_nncompilation_construct) | 
Creates an [OH\_NNCompilation](../../structs/oh-nncompilation/document.md) instance.

After an [OH\_NNModel](../../structs/oh-nnmodel/document.md) instance is created, the OH\_NNCompilation module passes the model instance to the underlying device for compilation.

 |
| [OH\_NNCompilation \*OH\_NNCompilation\_ConstructWithOfflineModelFile(const char \*modelPath)](#oh_nncompilation_constructwithofflinemodelfile) | 

Creates a model compilation instance based on an offline model file.

This API conflicts with the one that utilizes an online model or offline model buffer. You can select only one of the three compilation APIs.

An offline model is one that is offline-compiled by the model converter provided by hardware vendors. As such, it can only be used on designated devices. However, the compilation time of an offline model is generally much shorter than that of the graph construction instance [OH\_NNModel](../../structs/oh-nnmodel/document.md).

During development, offline compilation needs to be performed and offline models need to be deployed in application packages.

 |
| [OH\_NNCompilation \*OH\_NNCompilation\_ConstructWithOfflineModelBuffer(const void \*modelBuffer, size\_t modelSize)](#oh_nncompilation_constructwithofflinemodelbuffer) | 

Creates a model compilation instance based on the offline model buffer.

This API conflicts with the one that utilizes an online model or offline model file. You can select only one of the three compilation APIs.

The returned [OH\_NNCompilation](../../structs/oh-nncompilation/document.md) instance only saves the **modelBuffer** pointer, but does not copy its data. The **modelBuffer** instance should not be released before the [OH\_NNCompilation](../../structs/oh-nncompilation/document.md) instance is destroyed.

 |
| [OH\_NNCompilation \*OH\_NNCompilation\_ConstructForCache()](#oh_nncompilation_constructforcache) | 

Creates an empty model compilation instance for later recovery from the model cache.

For details about the model cache, see [OH\_NNCompilation\_SetCache](#oh_nncompilation_setcache).

The time required for model recovery from the model cache is less than the time required for compilation using [OH\_NNModel](../../structs/oh-nnmodel/document.md).

Call [OH\_NNCompilation\_SetCache](#oh_nncompilation_setcache) or [OH\_NNCompilation\_ImportCacheFromBuffer](#oh_nncompilation_importcachefrombuffer) and then [OH\_NNCompilation\_Build](#oh_nncompilation_build) to complete model recovery.

 |
| [OH\_NN\_ReturnCode OH\_NNCompilation\_ExportCacheToBuffer(OH\_NNCompilation \*compilation,const void \*buffer,size\_t length,size\_t \*modelSize)](#oh_nncompilation_exportcachetobuffer) | 

Writes the model cache to the specified buffer.

For details about the model cache, see [OH\_NNCompilation\_SetCache](#oh_nncompilation_setcache).

The model cache stores the result of [OH\_NNCompilation\_Build](#oh_nncompilation_build). Therefore, this API must be called after [OH\_NNCompilation\_Build](#oh_nncompilation_build) is complete.

 |
| [OH\_NN\_ReturnCode OH\_NNCompilation\_ImportCacheFromBuffer(OH\_NNCompilation \*compilation,const void \*buffer,size\_t modelSize)](#oh_nncompilation_importcachefrombuffer) | 

Reads the model cache from the specified buffer.

For details about the model cache, see [OH\_NNCompilation\_SetCache](#oh_nncompilation_setcache).

After calling [OH\_NNCompilation\_ImportCacheFromBuffer](#oh_nncompilation_importcachefrombuffer), call [OH\_NNCompilation\_Build](#oh_nncompilation_build) to complete model recovery.

The **compilation** instance only stores the **buffer** pointer, but does not copy its data. You cannot release the **buffer** before the **compilation** instance is destroyed.

 |
| [OH\_NN\_ReturnCode OH\_NNCompilation\_AddExtensionConfig(OH\_NNCompilation \*compilation,const char \*configName,const void \*configValue,const size\_t configValueSize)](#oh_nncompilation_addextensionconfig) | 

Adds extended configurations for custom device attributes.

Some devices have their own attributes, which have not been enabled in NNRt. This API helps you to set custom attributes for these devices.

You need to obtain their names and values from the device vendor's documentation and add them to the model compilation instance. These attributes are passed directly to the device driver. If the device driver cannot parse the attributes, an error is returned.

After [OH\_NNCompilation\_Build](#oh_nncompilation_build) is called, **configName** and **configValue** can be released.

 |
| [OH\_NN\_ReturnCode OH\_NNCompilation\_SetDevice(OH\_NNCompilation \*compilation, size\_t deviceID)](#oh_nncompilation_setdevice) | 

Sets the device for model compilation and computing.

In the compilation phase, you need to specify the device for model compilation and computing. Call [OH\_NNDevice\_GetAllDevicesID](#oh_nndevice_getalldevicesid) to obtain available device IDs. Then, call [OH\_NNDevice\_GetType](#oh_nndevice_gettype) and [OH\_NNDevice\_GetType](#oh_nndevice_gettype) to obtain device information and pass target device IDs to this API.

 |
| [OH\_NN\_ReturnCode OH\_NNCompilation\_SetCache(OH\_NNCompilation \*compilation, const char \*cachePath, uint32\_t version)](#oh_nncompilation_setcache) | Sets the cache directory and version for model compilation. |
| [OH\_NN\_ReturnCode OH\_NNCompilation\_SetPerformanceMode(OH\_NNCompilation \*compilation,OH\_NN\_PerformanceMode performanceMode)](#oh_nncompilation_setperformancemode) | 

Sets the performance mode for model computing.

NNRt allows you to set the performance mode for model computing to meet the requirements of low power consumption and ultimate performance. If this API is not called to set the performance mode in the compilation phase, the model compilation instance assigns the [OH\_NN\_PERFORMANCE\_NONE](../neural-network-runtime-type-h/document.md#oh_nn_performancemode) mode for the model by default. In this case, the device performs computing in the default performance mode. If this API is called on a device that does not support setting of the performance mode, the error code [OH\_NN\_UNAVAILABLE\_DEVICE](../neural-network-runtime-type-h/document.md#oh_nn_returncode) is returned.

 |
| [OH\_NN\_ReturnCode OH\_NNCompilation\_SetPriority(OH\_NNCompilation \*compilation, OH\_NN\_Priority priority)](#oh_nncompilation_setpriority) | 

Sets the priority for model computing.

NNRt allows you to set computing priorities for models. The priorities apply only to models created by the process with the same UID. The settings will not affect models created by processes with different UIDs on different devices. If this API is called on a device that does not support priority setting, the error code [OH\_NN\_UNAVAILABLE\_DEVICE](../neural-network-runtime-type-h/document.md#oh_nn_returncode) is returned.

 |
| [OH\_NN\_ReturnCode OH\_NNCompilation\_EnableFloat16(OH\_NNCompilation \*compilation, bool enableFloat16)](#oh_nncompilation_enablefloat16) | 

Enables float16 for computing.

By default, the floating-point model uses float32 for computing. If this API is called on a device that supports float16, floating-point model that supports float32 will use float16 for computing, so to reduce memory usage and execution time. This option is invalid for fixed-point models, for example, fixed-point models of the int8 type.

If this API is called on a device that does not support float16, the error code [OH\_NN\_UNAVAILABLE\_DEVICE](../neural-network-runtime-type-h/document.md#oh_nn_returncode) is returned.

 |
| [OH\_NN\_ReturnCode OH\_NNCompilation\_Build(OH\_NNCompilation \*compilation)](#oh_nncompilation_build) | 

Performs model compilation.

After the compilation configuration is complete, call this API to start model compilation. The model compilation instance pushes the model and compilation options to the device for compilation.

After this API is called, additional compilation operations cannot be performed. If [OH\_NNCompilation\_SetDevice](#oh_nncompilation_setdevice), [OH\_NNCompilation\_SetCache](#oh_nncompilation_setcache), [OH\_NNCompilation\_SetPerformanceMode](#oh_nncompilation_setperformancemode), [OH\_NNCompilation\_SetPriority](#oh_nncompilation_setpriority), or [OH\_NNCompilation\_EnableFloat16](#oh_nncompilation_enablefloat16) is called, [OH\_NN\_OPERATION\_FORBIDDEN](../neural-network-runtime-type-h/document.md#oh_nn_returncode) is returned.

 |
| [void OH\_NNCompilation\_Destroy(OH\_NNCompilation \*\*compilation)](#oh_nncompilation_destroy) | 

Destroys an [OH\_NNCompilation](../../structs/oh-nncompilation/document.md) instance.

This API needs to be used to destroy the model compilation instances created by calling [OH\_NNCompilation\_Construct](#oh_nncompilation_construct), [OH\_NNCompilation\_ConstructWithOfflineModelFile](#oh_nncompilation_constructwithofflinemodelfile), [OH\_NNCompilation\_ConstructWithOfflineModelBuffer](#oh_nncompilation_constructwithofflinemodelbuffer) or [OH\_NNCompilation\_ConstructForCache](#oh_nncompilation_constructforcache). If **compilation** or **\*compilation** is a null pointer, this API only prints warning logs but does not perform the destruction operation.

 |
| [NN\_TensorDesc \*OH\_NNTensorDesc\_Create()](#oh_nntensordesc_create) | 

Creates an [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance.

[NN\_TensorDesc](../../structs/nn-tensordesc/document.md) describes various tensor attributes, such as the name, data type, shape, and format.

You can create an [NN\_Tensor](../../structs/nn-tensor/document.md) instance based on the input [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance by calling the following APIs:

[OH\_NNTensor\_Create](#oh_nntensor_create)

[OH\_NNTensor\_CreateWithSize](#oh_nntensor_createwithsize)

[OH\_NNTensor\_CreateWithFd](#oh_nntensor_createwithfd)

This API copies the [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance to [NN\_Tensor](../../structs/nn-tensor/document.md). This way, you can create multiple [NN\_Tensor](../../structs/nn-tensor/document.md) instances with the same [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance. If the [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance is no longer needed, call [OH\_NNTensorDesc\_Destroy](#oh_nntensordesc_destroy) to destroy it.

 |
| [OH\_NN\_ReturnCode OH\_NNTensorDesc\_Destroy(NN\_TensorDesc \*\*tensorDesc)](#oh_nntensordesc_destroy) | 

Destroys an [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance.

If the [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance is no longer needed, call this API to destroy it. Otherwise, a memory leak occurs.

If **tensorDesc** or **\*tensorDesc** is a null pointer, an error is returned but the object will not be destroyed.

 |
| [OH\_NN\_ReturnCode OH\_NNTensorDesc\_SetName(NN\_TensorDesc \*tensorDesc, const char \*name)](#oh_nntensordesc_setname) | 

Sets the name of an [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance.

After an [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance is created, call this API to set the tensor name. The value of \*name is a C-style string ending with \\0.

If **tensorDesc** or **name** is a null pointer, an error is returned.

 |
| [OH\_NN\_ReturnCode OH\_NNTensorDesc\_GetName(const NN\_TensorDesc \*tensorDesc, const char \*\*name)](#oh_nntensordesc_getname) | 

Obtains the name of an [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance.

You can use this API to obtain the name of the specified [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance. The value of **\*name** is a C-style string ending with **\\0**.

If **tensorDesc** or **name** is a null pointer, an error is returned. As an output parameter, **\*name** must be a null pointer. Otherwise, an error is returned.

For example, you should define **char\* tensorName = NULL** and pass **&tensorName** as a parameter of **name**.

You do not need to release the memory of **name**. When **tensorDesc** is destroyed, it is automatically released.

 |
| [OH\_NN\_ReturnCode OH\_NNTensorDesc\_SetDataType(NN\_TensorDesc \*tensorDesc, OH\_NN\_DataType dataType)](#oh_nntensordesc_setdatatype) | 

Sets the data type of an [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance.

After an [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance is created, call this API to set the tensor data type.

If **tensorDesc** is a null pointer, an error is returned.

 |
| [OH\_NN\_ReturnCode OH\_NNTensorDesc\_GetDataType(const NN\_TensorDesc \*tensorDesc, OH\_NN\_DataType \*dataType)](#oh_nntensordesc_getdatatype) | 

Obtains the data type of an [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance.

You can use this API to obtain the data type of the specified [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance.

If **tensorDesc** or **dataType** is a null pointer, an error is returned.

 |
| [OH\_NN\_ReturnCode OH\_NNTensorDesc\_SetShape(NN\_TensorDesc \*tensorDesc, const int32\_t \*shape, size\_t shapeLength)](#oh_nntensordesc_setshape) | 

Sets the data shape of an [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance.

After an [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance is created, call this API to set the tensor shape.

If **tensorDesc** or **shape** is a null pointer, or **shapeLength** is 0, an error is returned.

 |
| [OH\_NN\_ReturnCode OH\_NNTensorDesc\_GetShape(const NN\_TensorDesc \*tensorDesc, int32\_t \*\*shape, size\_t \*shapeLength)](#oh_nntensordesc_getshape) | 

Obtains the shape of an [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance.

You can use this API to obtain the shape of the specified [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance.

If **tensorDesc**, **shape**, or **shapeLength** is a null pointer, an error is returned. As an output parameter, **\*shape** must be a null pointer. Otherwise, an error is returned.

For example, you should define **int32\_t\* tensorShape = NULL** and pass **&tensorShape** as a parameter of **shape**.

You do not need to release the memory of **shape**. When **tensorDesc** is destroyed, it is automatically released.

 |
| [OH\_NN\_ReturnCode OH\_NNTensorDesc\_SetFormat(NN\_TensorDesc \*tensorDesc, OH\_NN\_Format format)](#oh_nntensordesc_setformat) | 

Sets the data format of an [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance.

After an [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance is created, call this API to set [OH\_NN\_Format](../neural-network-runtime-type-h/document.md#oh_nn_format) of the tensor.

If **tensorDesc** is a null pointer, an error is returned.

 |
| [OH\_NN\_ReturnCode OH\_NNTensorDesc\_GetFormat(const NN\_TensorDesc \*tensorDesc, OH\_NN\_Format \*format)](#oh_nntensordesc_getformat) | 

Obtains the data format of an [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance.

You can use this API to obtain [OH\_NN\_Format](../neural-network-runtime-type-h/document.md#oh_nn_format) of the specified [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance.

If **tensorDesc** or **format** is a null pointer, an error is returned.

 |
| [OH\_NN\_ReturnCode OH\_NNTensorDesc\_GetElementCount(const NN\_TensorDesc \*tensorDesc, size\_t \*elementCount)](#oh_nntensordesc_getelementcount) | 

Obtains the number of elements in an [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance.

You can use this API to obtain the number of elements in the specified [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance. To obtain the size of tensor data, call [OH\_NNTensorDesc\_GetByteSize](#oh_nntensordesc_getbytesize).

If the tensor shape is dynamically variable, this API returns an error code and **elementCount** is **0**.

If **tensorDesc** or **elementCount** is a null pointer, an error is returned.

 |
| [OH\_NN\_ReturnCode OH\_NNTensorDesc\_GetByteSize(const NN\_TensorDesc \*tensorDesc, size\_t \*byteSize)](#oh_nntensordesc_getbytesize) | 

Obtains the number of bytes occupied by the tensor data obtained through calculation based on the shape and data type of an [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance.

You can use this API to obtain the number of bytes occupied by the tensor data obtained through calculation based on the shape and data type of the specified [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance.

If the tensor shape is dynamically variable, this API returns an error code and **byteSize** is **0**.

To obtain the number of elements in the tensor data, call [OH\_NNTensorDesc\_GetElementCount](#oh_nntensordesc_getelementcount).

If **tensorDesc** or **byteSize** is a null pointer, an error is returned.

 |
| [NN\_Tensor \*OH\_NNTensor\_Create(size\_t deviceID, NN\_TensorDesc \*tensorDesc)](#oh_nntensor_create) | 

Creates an [NN\_Tensor](../../structs/nn-tensor/document.md) instance from [NN\_TensorDesc](../../structs/nn-tensordesc/document.md).

This API uses [OH\_NNTensorDesc\_GetByteSize](#oh_nntensordesc_getbytesize) to calculate the number of bytes of tensor data and allocate device memory for it. The device driver directly obtains tensor data in zero-copy mode.

This API copies **tensorDesc** to [NN\_Tensor](../../structs/nn-tensor/document.md). Therefore, if **tensorDesc** is no longer needed, destroy it by calling [OH\_NNTensorDesc\_Destroy](#oh_nntensordesc_destroy).

If the tensor shape is dynamic, an error is returned.

**deviceID** indicates the selected device. If the value is **0**, the first device in the current device list is used by default.

**tensorDesc is mandatory**. If it is a null pointer, an error is returned.

If the [NN\_Tensor](../../structs/nn-tensor/document.md) instance is no longer needed, destroy it by calling [OH\_NNTensor\_Destroy](#oh_nntensor_destroy).

 |
| [NN\_Tensor \*OH\_NNTensor\_CreateWithSize(size\_t deviceID, NN\_TensorDesc \*tensorDesc, size\_t size)](#oh_nntensor_createwithsize) | 

Creates an [NN\_Tensor](../../structs/nn-tensor/document.md) instance based on the specified memory size and [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance.

This API uses **size** as the number of bytes of tensor data and allocates device memory to it. The device driver directly obtains tensor data in zero-copy mode.

Note that this API copies **tensorDesc** to [NN\_Tensor](../../structs/nn-tensor/document.md). Therefore, if **tensorDesc** is no longer needed, destroy it by calling [OH\_NNTensorDesc\_Destroy](#oh_nntensordesc_destroy).

**deviceID** indicates the ID of the selected device. If the value is **0**, the first device is used.

**tensorDesc** is mandatory. If it is a null pointer, an error is returned.

The value of **size** must be greater than or equal to the number of bytes occupied by **tensorDesc**, which can be obtained by calling [OH\_NNTensorDesc\_GetByteSize](#oh_nntensordesc_getbytesize). Otherwise, an error is returned. If the tensor shape is dynamic, **size** is not checked.

If the [NN\_Tensor](../../structs/nn-tensor/document.md) instance is no longer needed, destroy it by calling [OH\_NNTensor\_Destroy](#oh_nntensor_destroy).

 |
| [NN\_Tensor \*OH\_NNTensor\_CreateWithFd(size\_t deviceID,NN\_TensorDesc \*tensorDesc,int fd,size\_t size,size\_t offset)](#oh_nntensor_createwithfd) | 

Creates an [NN\_Tensor](../../structs/nn-tensor/document.md) instance based on the specified file descriptor of the shared memory and [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance.

This API reuses the shared memory corresponding to **fd**, which may source from another [NN\_Tensor](../../structs/nn-tensor/document.md) instance. When the tensor created by calling [OH\_NNTensor\_Destroy](#oh_nntensor_destroy) is destroyed, the memory storing the tensor data is not released.

Note that this API copies **tensorDesc** to [NN\_Tensor](../../structs/nn-tensor/document.md). Therefore, if **tensorDesc** is no longer needed, destroy it by calling [OH\_NNTensorDesc\_Destroy](#oh_nntensordesc_destroy).

**deviceID** indicates the selected device. If the value is **0**, the first device in the current device list is used by default.

**tensorDesc** is mandatory. If the pointer is null, an error is returned.

If the [NN\_Tensor](../../structs/nn-tensor/document.md) instance is no longer needed, destroy it by calling [OH\_NNTensor\_Destroy](#oh_nntensor_destroy).

 |
| [OH\_NN\_ReturnCode OH\_NNTensor\_Destroy(NN\_Tensor \*\*tensor)](#oh_nntensor_destroy) | 

Destroys an [NN\_Tensor](../../structs/nn-tensor/document.md) instance.

If the [NN\_Tensor](../../structs/nn-tensor/document.md) instance is no longer needed, call this API to destroy it. Otherwise, a memory leak occurs.

If **tensor** or **\*tensor** is a null pointer, an error is returned but the object will not be destroyed.

 |
| [NN\_TensorDesc \*OH\_NNTensor\_GetTensorDesc(const NN\_Tensor \*tensor)](#oh_nntensor_gettensordesc) | 

Obtains an [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance of [NN\_Tensor](../../structs/nn-tensor/document.md).

You can use this API to obtain the pointer to the [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance of the specified [NN\_Tensor](../../structs/nn-tensor/document.md) instance.

You can obtain tensor attributes of various types from the returned [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance, such as the name, data format, data type, and shape.

You should not destroy the returned [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance because it points to an internal instance of [NN\_Tensor](../../structs/nn-tensor/document.md). Otherwise, once [OH\_NNTensor\_Destroy](#oh_nntensor_destroy) is called, a crash may occur due to double memory release.

If **Tensor** is a null pointer, a null pointer is returned.

 |
| [void \*OH\_NNTensor\_GetDataBuffer(const NN\_Tensor \*tensor)](#oh_nntensor_getdatabuffer) | 

Obtains the memory address of [NN\_Tensor](../../structs/nn-tensor/document.md) data.

You can read/write data from/to tensor data memory. The data memory is mapped from the shared memory on the device. Therefore, the device driver can directly obtain tensor data in zero-copy mode.

Only tensor data in the \[offset, size) segment in the corresponding shared memory can be used. **offset** indicates the offset in the shared memory and can be obtained by calling [OH\_NNTensor\_GetOffset](#oh_nntensor_getoffset). **size** indicates the total size of the shared memory, which can be obtained by calling [OH\_NNTensor\_GetSize](#oh_nntensor_getsize).

If **Tensor** is a null pointer, a null pointer is returned.

 |
| [OH\_NN\_ReturnCode OH\_NNTensor\_GetFd(const NN\_Tensor \*tensor, int \*fd)](#oh_nntensor_getfd) | 

Obtains the file descriptor (**fd**) of the shared memory where [NN\_Tensor](../../structs/nn-tensor/document.md) data is stored.

**fd** corresponds to a device shared memory and can be used by another [NN\_Tensor](../../structs/nn-tensor/document.md) through [OH\_NNTensor\_CreateWithFd](#oh_nntensor_createwithfd).

If **tensor** or **fd** is a null pointer, an error is returned.

 |
| [OH\_NN\_ReturnCode OH\_NNTensor\_GetSize(const NN\_Tensor \*tensor, size\_t \*size)](#oh_nntensor_getsize) | 

Obtains the size of the shared memory where the [NN\_Tensor](../../structs/nn-tensor/document.md) data is stored.

The value of **size** is the same as that of [OH\_NNTensor\_CreateWithSize](#oh_nntensor_createwithsize) and [OH\_NNTensor\_CreateWithFd](#oh_nntensor_createwithfd). However, for a tensor created by using [OH\_NNTensor\_Create](#oh_nntensor_create), the value of **size** is equal to the number of bytes actually occupied by the tensor data, which can be obtained by calling [OH\_NNTensorDesc\_GetByteSize](#oh_nntensordesc_getbytesize).

Only tensor data in the \[offset, size) segment in the shared memory corresponding to the **fd** can be used. **offset** indicates the offset in the shared memory and can be obtained by calling [OH\_NNTensor\_GetOffset](#oh_nntensor_getoffset). **size** indicates the total size of the shared memory, which can be obtained by calling [OH\_NNTensor\_GetSize](#oh_nntensor_getsize).

If **tensor** or **size** is a null pointer, an error is returned.

 |
| [OH\_NN\_ReturnCode OH\_NNTensor\_GetOffset(const NN\_Tensor \*tensor, size\_t \*offset)](#oh_nntensor_getoffset) | 

Obtains the offset of [NN\_Tensor](../../structs/nn-tensor/document.md) data in the shared memory.

**offset** indicates the offset of tensor data in the corresponding shared memory. It can be used by another [NN\_Tensor](../../structs/nn-tensor/document.md) together with **fd** and **size** of the shared memory through [OH\_NNTensor\_CreateWithFd](#oh_nntensor_createwithfd).

Only tensor data in the \[offset, size) segment in the shared memory corresponding to the **fd** can be used. **offset** indicates the offset in the shared memory and can be obtained by calling [OH\_NNTensor\_GetOffset](#oh_nntensor_getoffset). **size** indicates the total size of the shared memory, which can be obtained by calling [OH\_NNTensor\_GetSize](#oh_nntensor_getsize).

If **tensor** or **offset** is a null pointer, an error is returned.

 |
| [OH\_NNExecutor \*OH\_NNExecutor\_Construct(OH\_NNCompilation \*compilation)](#oh_nnexecutor_construct) | 

Creates an [OH\_NNExecutor](../../structs/oh-nnexecutor/document.md) executor instance.

This API constructs a model inference executor for a device based on the specified [OH\_NNCompilation](../../structs/oh-nncompilation/document.md) instance. Use [OH\_NNExecutor\_SetInput](../neural-network-runtime-h/document.md#oh_nnexecutor_setinput) to set the model input data. After the input data is set, call [OH\_NNExecutor\_Run](../neural-network-runtime-h/document.md#oh_nnexecutor_run) to perform inference and then call [OH\_NNExecutor\_SetOutput](../neural-network-runtime-h/document.md#oh_nnexecutor_setoutput) to obtain the computing result. After an [OH\_NNExecutor](../../structs/oh-nnexecutor/document.md) instance is created through the [OH\_NNCompilation](../../structs/oh-nncompilation/document.md) instance, destroy the [OH\_NNCompilation](../../structs/oh-nncompilation/document.md) instance if it is no longer needed.

 |
| [OH\_NN\_ReturnCode OH\_NNExecutor\_GetOutputShape(OH\_NNExecutor \*executor,uint32\_t outputIndex,int32\_t \*\*shape,uint32\_t \*shapeLength)](#oh_nnexecutor_getoutputshape) | Obtains the dimension information about the output tensor. |
| [void OH\_NNExecutor\_Destroy(OH\_NNExecutor \*\*executor)](#oh_nnexecutor_destroy) | 

Destroys an executor instance to release the memory occupied by it.

This API needs to be called to release the executor instance created by calling [OH\_NNExecutor\_Construct](#oh_nnexecutor_construct). Otherwise, a memory leak occurs. If **executor** or **\*executor** is a null pointer, this API only prints the warning log and does not execute the release logic.

 |
| [OH\_NN\_ReturnCode OH\_NNExecutor\_GetInputCount(const OH\_NNExecutor \*executor, size\_t \*inputCount)](#oh_nnexecutor_getinputcount) | 

Obtains the number of input tensors.

You can obtain the number of input tensors from **executor**, and then use [OH\_NNExecutor\_CreateInputTensorDesc](#oh_nnexecutor_createinputtensordesc) to create a tensor description based on the specified tensor index.

 |
| [OH\_NN\_ReturnCode OH\_NNExecutor\_GetOutputCount(const OH\_NNExecutor \*executor, size\_t \*outputCount)](#oh_nnexecutor_getoutputcount) | 

Obtains the number of output tensors.

You can obtain the number of output tensors from **executor**, and then use [OH\_NNExecutor\_CreateOutputTensorDesc](#oh_nnexecutor_createoutputtensordesc) to create a tensor description based on the specified tensor index.

 |
| [NN\_TensorDesc \*OH\_NNExecutor\_CreateInputTensorDesc(const OH\_NNExecutor \*executor, size\_t index)](#oh_nnexecutor_createinputtensordesc) | 

Creates the description of an input tensor based on the specified index value.

The description contains all types of attribute values of the tensor. If the value of **index** reaches or exceeds the number of input tensors, an error is returned. You can obtain the number of input tensors by calling [OH\_NNExecutor\_GetInputCount](#oh_nnexecutor_getinputcount).

 |
| [NN\_TensorDesc \*OH\_NNExecutor\_CreateOutputTensorDesc(const OH\_NNExecutor \*executor, size\_t index)](#oh_nnexecutor_createoutputtensordesc) | 

Creates the description of an output tensor based on the specified index value.

The description contains all types of attribute values of the tensor. If the value of **index** reaches or exceeds the number of output tensors, an error is returned. You can obtain the number of output tensors by calling [OH\_NNExecutor\_GetOutputCount](#oh_nnexecutor_getoutputcount).

 |
| [OH\_NN\_ReturnCode OH\_NNExecutor\_GetInputDimRange(const OH\_NNExecutor \*executor,size\_t index,size\_t \*\*minInputDims,size\_t \*\*maxInputDims,size\_t \*shapeLength)](#oh_nnexecutor_getinputdimrange) | 

Obtains the dimension range of all input tensors.

If the input tensor has a dynamic shape, the dimension range supported by the tensor may vary according to device. You can call this API to obtain the dimension range supported by the current device. **\*minInputDims** saves the minimum dimension of the specified input tensor (the number of dimensions matches the shape), while **\*maxInputDims** saves the maximum dimension.

 |
| [OH\_NN\_ReturnCode OH\_NNExecutor\_SetOnRunDone(OH\_NNExecutor \*executor, NN\_OnRunDone onRunDone)](#oh_nnexecutor_setonrundone) | 

Sets the callback processing function invoked when the asynchronous inference ends.

For details about the callback function, see [NN\_OnRunDone](../neural-network-runtime-type-h/document.md#nn_onrundone).

 |
| [OH\_NN\_ReturnCode OH\_NNExecutor\_SetOnServiceDied(OH\_NNExecutor \*executor, NN\_OnServiceDied onServiceDied)](#oh_nnexecutor_setonservicedied) | 

Sets the callback processing function invoked when the device driver service terminates unexpectedly during asynchronous inference.

For details about the callback function, see [NN\_OnServiceDied](../neural-network-runtime-type-h/document.md#nn_onservicedied).

 |
| [OH\_NN\_ReturnCode OH\_NNExecutor\_RunSync(OH\_NNExecutor \*executor,NN\_Tensor \*inputTensor\[\],size\_t inputCount,NN\_Tensor \*outputTensor\[\],size\_t outputCount)](#oh_nnexecutor_runsync) | 

Performs synchronous inference.

You need to create input and output tensors by calling [OH\_NNTensor\_Create](#oh_nntensor_create), [OH\_NNTensor\_CreateWithSize](#oh_nntensor_createwithsize), or [OH\_NNTensor\_CreateWithFd](#oh_nntensor_createwithfd). Then, use [OH\_NNTensor\_GetDataBuffer](#oh_nntensor_getdatabuffer) to obtain the pointer to tensor data and copy the input data to it. The executor performs model inference, generates the inference result, and writes the result to the output tensor.

If the output tensor has a dynamic shape, you can obtain the actual shape of the output tensor by calling [OH\_NNExecutor\_GetOutputShape](#oh_nnexecutor_getoutputshape). Alternatively, obtain the tensor description from the input tensor by calling [OH\_NNTensor\_GetTensorDesc](#oh_nntensor_gettensordesc), and then obtain the actual shape by calling [OH\_NNTensorDesc\_GetShape](#oh_nntensordesc_getshape).

 |
| [OH\_NN\_ReturnCode OH\_NNExecutor\_RunAsync(OH\_NNExecutor \*executor,NN\_Tensor \*inputTensor\[\],size\_t inputCount,NN\_Tensor \*outputTensor\[\],size\_t outputCount,int32\_t timeout,void \*userData)](#oh_nnexecutor_runasync) | 

Performs asynchronous inference.

You need to create input and output tensors by calling [OH\_NNTensor\_Create](#oh_nntensor_create), [OH\_NNTensor\_CreateWithSize](#oh_nntensor_createwithsize), or [OH\_NNTensor\_CreateWithFd](#oh_nntensor_createwithfd). Then, use [OH\_NNTensor\_GetDataBuffer](#oh_nntensor_getdatabuffer) to obtain the pointer to tensor data and copy the input data to it. The executor performs model inference, generates the inference result, and writes the result to the output tensor.

If the output tensor has a dynamic shape, you can obtain the actual shape of the output tensor by calling [OH\_NNExecutor\_GetOutputShape](#oh_nnexecutor_getoutputshape). Alternatively, obtain the tensor description from the input tensor by calling [OH\_NNTensor\_GetTensorDesc](#oh_nntensor_gettensordesc), and then obtain the actual shape by calling [OH\_NNTensorDesc\_GetShape](#oh_nntensordesc_getshape).

This API works in non-blocking mode and returns the result immediately after being called. You can obtain the inference result and execution return status through the [NN\_OnRunDone](../neural-network-runtime-type-h/document.md#nn_onrundone) callback. If the device driver service stops abnormally during execution, you can use the [NN\_OnServiceDied](../neural-network-runtime-type-h/document.md#nn_onservicedied) callback for exception processing.

You can set the NN\_OnRunDone\](capi-neural-network-runtime-type-h.md#nn\_onrundone) and [NN\_OnServiceDied](../neural-network-runtime-type-h/document.md#nn_onservicedied) callbacks by calling [OH\_NNExecutor\_SetOnRunDone](#oh_nnexecutor_setonrundone) and [OH\_NNExecutor\_SetOnServiceDied](#oh_nnexecutor_setonservicedied).

If the inference times out, it is terminated immediately and the error code [OH\_NN\_TIMEOUT](../neural-network-runtime-type-h/document.md#oh_nn_returncode) is returned through the [NN\_OnRunDone](../neural-network-runtime-type-h/document.md#nn_onrundone) callback.

**userData** is the identifier used to distinguish different asynchronous inferences and is returned as the first parameter in the callback. You can use any data that can distinguish different inferences as the identifier.

 |
| [OH\_NN\_ReturnCode OH\_NNDevice\_GetAllDevicesID(const size\_t \*\*allDevicesID, uint32\_t \*deviceCount)](#oh_nndevice_getalldevicesid) | 

Obtains the ID of the device connected to NNRt.

Each device has a unique and fixed ID, which is returned through a uint32\_t array.

When device IDs are returned through the size\_t array, each element of the array is the ID of a single device. Internal management is used for array memory. The data pointer remains valid before this API is called next time.

 |
| [OH\_NN\_ReturnCode OH\_NNDevice\_GetName(size\_t deviceID, const char \*\*name)](#oh_nndevice_getname) | 

Obtains the name of the specified device.

**deviceID** specifies the device ID used to obtain the device name. The device ID needs to be obtained by calling [OH\_NNDevice\_GetAllDevicesID](#oh_nndevice_getalldevicesid). If the value of **deviceID** is **0**, the first device in the device list is used by default. **\*name** is a C-style string ended with **\\0**.

**\*name** must be a null pointer. Otherwise, the error code [OH\_NN\_INVALID\_PARAMETER](../neural-network-runtime-type-h/document.md#oh_nn_returncode) is returned. For example, you should define **char\* deviceName = NULL**, and then pass **&deviceName** as an input parameter.

 |
| [OH\_NN\_ReturnCode OH\_NNDevice\_GetType(size\_t deviceID, OH\_NN\_DeviceType \*deviceType)](#oh_nndevice_gettype) | 

Obtains the type of the specified device.

**deviceID** specifies the device ID used to obtain the device type. If the value of **deviceID** is **0**, the first device in the device list is used by default. Currently, the following device types are supported:

\- **OH\_NN\_CPU**: CPU device.

\- **OH\_NN\_GPU**: GPU device.

\- **OH\_NN\_ACCELERATOR**: machine learning dedicated accelerator.

\- **OH\_NN\_OTHERS**: other device types.

 |

#### Function Description

#### \[h2\]OH\_NNCompilation\_Construct()

OH\_NNCompilation \*OH\_NNCompilation\_Construct(const OH\_NNModel \*model)

**Description**

Creates an [OH\_NNCompilation](../../structs/oh-nncompilation/document.md) instance.

After an [OH\_NNModel](../../structs/oh-nnmodel/document.md) instance is created, the OH\_NNCompilation module passes the model instance to the underlying device for compilation.

This API creates an [OH\_NNCompilation](../../structs/oh-nncompilation/document.md) instance based on the passed [OH\_NNModel](../../structs/oh-nnmodel/document.md) instance. The [OH\_NNCompilation\_SetDevice](#oh_nncompilation_setdevice) API is called to specify the device for model compilation, and the [OH\_NNCompilation\_Build](#oh_nncompilation_build) API is then called to complete model compilation.

In addition to computing device selection, the OH\_NNCompilation module supports features such as model cache, performance preference, priority setting, and float16 computing, which can be implemented by the following APIs:

[OH\_NNCompilation\_SetCache](#oh_nncompilation_setcache)

[OH\_NNCompilation\_SetPerformanceMode](#oh_nncompilation_setperformancemode)

[OH\_NNCompilation\_SetPriority](#oh_nncompilation_setpriority)

[OH\_NNCompilation\_EnableFloat16](#oh_nncompilation_enablefloat16)

After this API is called to create an [OH\_NNCompilation](../../structs/oh-nncompilation/document.md) instance, the [OH\_NNModel](../../structs/oh-nnmodel/document.md) instance can be released.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [const OH\_NNModel](../../structs/oh-nnmodel/document.md) \*model | Pointer to the [OH\_NNModel](../../structs/oh-nnmodel/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NNCompilation](../../structs/oh-nncompilation/document.md) \* | Pointer to the [OH\_NNCompilation](../../structs/oh-nncompilation/document.md) instance. If the operation fails, **NULL** is returned. |

#### \[h2\]OH\_NNCompilation\_ConstructWithOfflineModelFile()

OH\_NNCompilation \*OH\_NNCompilation\_ConstructWithOfflineModelFile(const char \*modelPath)

**Description**

Creates a model compilation instance based on an offline model file.

This API conflicts with the one that utilizes an online model or offline model buffer. You can select only one of the three compilation APIs.

An offline model is one that is offline-compiled by the model converter provided by hardware vendors. As such, it can only be used on designated devices. However, the compilation time of an offline model is generally much shorter than that of the graph construction instance [OH\_NNModel](../../structs/oh-nnmodel/document.md).

During development, offline compilation needs to be performed and offline models need to be deployed in application packages.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*modelPath | Path of the offline model file. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NNCompilation](../../structs/oh-nncompilation/document.md) \* | Pointer to the [OH\_NNCompilation](../../structs/oh-nncompilation/document.md) instance. If the operation fails, **NULL** is returned. |

#### \[h2\]OH\_NNCompilation\_ConstructWithOfflineModelBuffer()

OH\_NNCompilation \*OH\_NNCompilation\_ConstructWithOfflineModelBuffer(const void \*modelBuffer, size\_t modelSize)

**Description**

Creates a model compilation instance based on the offline model buffer.

This API conflicts with the one that utilizes an online model or offline model file. You can select only one of the three compilation APIs.

The returned [OH\_NNCompilation](../../structs/oh-nncompilation/document.md) instance only saves the **modelBuffer** pointer, but does not copy its data. The **modelBuffer** instance should not be released before the [OH\_NNCompilation](../../structs/oh-nncompilation/document.md) instance is destroyed.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| const void \*modelBuffer | Memory for storing offline model files. |
| size\_t modelSize | Memory size of the offline model. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NNCompilation](../../structs/oh-nncompilation/document.md) \* | Pointer to the [OH\_NNCompilation](../../structs/oh-nncompilation/document.md) instance. If the operation fails, **NULL** is returned. |

#### \[h2\]OH\_NNCompilation\_ConstructForCache()

OH\_NNCompilation \*OH\_NNCompilation\_ConstructForCache()

**Description**

Creates an empty model compilation instance for later recovery from the model cache.

For details about the model cache, see [OH\_NNCompilation\_SetCache](#oh_nncompilation_setcache).

The time required for model recovery from the model cache is less than the time required for compilation using [OH\_NNModel](../../structs/oh-nnmodel/document.md).

Call [OH\_NNCompilation\_SetCache](#oh_nncompilation_setcache) or [OH\_NNCompilation\_ImportCacheFromBuffer](#oh_nncompilation_importcachefrombuffer) and then [OH\_NNCompilation\_Build](#oh_nncompilation_build) to complete model recovery.

**Since**: 11

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NNCompilation](../../structs/oh-nncompilation/document.md) \* | Pointer to the [OH\_NNCompilation](../../structs/oh-nncompilation/document.md) instance. If the operation fails, **NULL** is returned. |

#### \[h2\]OH\_NNCompilation\_ExportCacheToBuffer()

OH\_NN\_ReturnCode OH\_NNCompilation\_ExportCacheToBuffer(OH\_NNCompilation \*compilation,const void \*buffer,size\_t length,size\_t \*modelSize)

**Description**

Writes the model cache to the specified buffer.

For details about the model cache, see [OH\_NNCompilation\_SetCache](#oh_nncompilation_setcache).

The model cache stores the result of [OH\_NNCompilation\_Build](#oh_nncompilation_build). Therefore, this API must be called after [OH\_NNCompilation\_Build](#oh_nncompilation_build) is complete.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NNCompilation](../../structs/oh-nncompilation/document.md) \*compilation | Pointer to the [OH\_NNCompilation](../../structs/oh-nncompilation/document.md) instance. |
| const void \*buffer | Pointer to the given memory. |
| size\_t length | Memory length. |
| size\_t \*modelSize | Size of the model cache, in bytes. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode) | Execution result of the function. If the operation is successful, **OH\_NN\_SUCCESS** is returned. If the operation fails, an error is returned. For details about the error codes, see [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode). |

#### \[h2\]OH\_NNCompilation\_ImportCacheFromBuffer()

OH\_NN\_ReturnCode OH\_NNCompilation\_ImportCacheFromBuffer(OH\_NNCompilation \*compilation,const void \*buffer,size\_t modelSize)

**Description**

Reads the model cache from the specified buffer.

For details about the model cache, see [OH\_NNCompilation\_SetCache](#oh_nncompilation_setcache).

After calling [OH\_NNCompilation\_ImportCacheFromBuffer](#oh_nncompilation_importcachefrombuffer), call [OH\_NNCompilation\_Build](#oh_nncompilation_build) to complete model recovery.

The **compilation** instance only stores the **buffer** pointer, but does not copy its data. You cannot release the **buffer** before the **compilation** instance is destroyed.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NNCompilation](../../structs/oh-nncompilation/document.md) \*compilation | Pointer to the [OH\_NNCompilation](../../structs/oh-nncompilation/document.md) instance. |
| const void \*buffer | Pointer to the given memory. |
| size\_t modelSize | Size of the model cache, in bytes. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode) | Execution result of the function. If the operation is successful, **OH\_NN\_SUCCESS** is returned. If the operation fails, an error is returned. For details about the error codes, see [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode). |

#### \[h2\]OH\_NNCompilation\_AddExtensionConfig()

OH\_NN\_ReturnCode OH\_NNCompilation\_AddExtensionConfig(OH\_NNCompilation \*compilation,const char \*configName,const void \*configValue,const size\_t configValueSize)

**Description**

Adds extended configurations for custom device attributes.

Some devices have their own attributes, which have not been enabled in NNRt. This API helps you to set custom attributes for these devices.

You need to obtain their names and values from the device vendor's documentation and add them to the model compilation instance. These attributes are passed directly to the device driver. If the device driver cannot parse the attributes, an error is returned.

After [OH\_NNCompilation\_Build](#oh_nncompilation_build) is called, **configName** and **configValue** can be released.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NNCompilation](../../structs/oh-nncompilation/document.md) \*compilation | Pointer to the [OH\_NNCompilation](../../structs/oh-nncompilation/document.md) instance. |
| const char \*configName | Configuration name. |
| const void \*configValue | Configured value. |
| const size\_t configValueSize | Size of the configured value, in bytes. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode) | Execution result of the function. If the operation is successful, **OH\_NN\_SUCCESS** is returned. If the operation fails, an error is returned. For details about the error codes, see [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode). |

#### \[h2\]OH\_NNCompilation\_SetDevice()

OH\_NN\_ReturnCode OH\_NNCompilation\_SetDevice(OH\_NNCompilation \*compilation, size\_t deviceID)

**Description**

Sets the device for model compilation and computing.

In the compilation phase, you need to specify the device for model compilation and computing. Call [OH\_NNDevice\_GetAllDevicesID](#oh_nndevice_getalldevicesid) to obtain available device IDs. Then, call [OH\_NNDevice\_GetType](#oh_nndevice_gettype) and [OH\_NNDevice\_GetType](#oh_nndevice_gettype) to obtain device information and pass target device IDs to this API.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NNCompilation](../../structs/oh-nncompilation/document.md) \*compilation | Pointer to the [OH\_NNCompilation](../../structs/oh-nncompilation/document.md) instance. |
| size\_t deviceID | Device ID. If the value is **0**, the first device in the current device list is used by default. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode) | Execution result of the function. If the operation is successful, **OH\_NN\_SUCCESS** is returned. If the operation fails, an error is returned. For details about the error codes, see [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode). |

#### \[h2\]OH\_NNCompilation\_SetCache()

OH\_NN\_ReturnCode OH\_NNCompilation\_SetCache(OH\_NNCompilation \*compilation, const char \*cachePath, uint32\_t version)

**Description**

Sets the cache directory and version for model compilation.

On the device that supports model caching, a model can be saved as a cache file after a successful compilation at the device driver layer. The model can be directly read from the cache file, saving the compilation time.

This API performs different operations based on the model cache directory and version:

-   If no file exists in the specified model cache directory, cache the built model to the directory and set the cache version to the value of **version**.
-   If a complete cached file exists in the specified model cache directory, and its version number is equal to **version**, read the cached file in the directory and pass it to the underlying device to convert it into an executable model instance.
-   If a complete cached file exists in the specified model cache directory, but its version is earlier than **version**, update the cached file. After the model is built on the underlying device, the cached file in the cache directory is overwritten and the version is updated to **version**.
-   If a complete cached file exists in the specified model cache directory, but its version is later than **version**, the cached file is not read and the error code [OH\_NN\_INVALID\_PARAMETER](../neural-network-runtime-type-h/document.md#oh_nn_returncode) is returned.
-   If the cached file in the specified model cache directory is incomplete or you do not have the file access permission, the error code [OH\_NN\_INVALID\_FILE](../neural-network-runtime-type-h/document.md#oh_nn_returncode) is returned.
-   If the model cache directory does not exist or you do not have the file access permission, the error code [OH\_NN\_INVALID\_PATH](../neural-network-runtime-type-h/document.md#oh_nn_returncode) is returned.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NNCompilation](../../structs/oh-nncompilation/document.md) \*compilation | Pointer to the [OH\_NNCompilation](../../structs/oh-nncompilation/document.md) instance. |
| const char \*cachePath | Directory for storing model cache files. This API creates model cache directories for different devices in the cachePath directory. You are advised to use a separate cache directory for each model. |
| uint32\_t version | Cached model version. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode) | Execution result of the function. If the operation is successful, **OH\_NN\_SUCCESS** is returned. If the operation fails, an error is returned. For details about the error codes, see [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode). |

#### \[h2\]OH\_NNCompilation\_SetPerformanceMode()

OH\_NN\_ReturnCode OH\_NNCompilation\_SetPerformanceMode(OH\_NNCompilation \*compilation,OH\_NN\_PerformanceMode performanceMode)

**Description**

Sets the performance mode for model computing.

NNRt allows you to set the performance mode for model computing to meet the requirements of low power consumption and ultimate performance. If this API is not called to set the performance mode in the compilation phase, the model compilation instance assigns the [OH\_NN\_PERFORMANCE\_NONE](../neural-network-runtime-type-h/document.md#oh_nn_performancemode) mode for the model by default. In this case, the device performs computing in the default performance mode. If this API is called on a device that does not support setting of the performance mode, the error code [OH\_NN\_UNAVAILABLE\_DEVICE](../neural-network-runtime-type-h/document.md#oh_nn_returncode) is returned.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NNCompilation](../../structs/oh-nncompilation/document.md) \*compilation | Pointer to the [OH\_NNCompilation](../../structs/oh-nncompilation/document.md) instance. |
| [OH\_NN\_PerformanceMode](../neural-network-runtime-type-h/document.md#oh_nn_performancemode) performanceMode | Performance mode for model computing. For details, see [OH\_NN\_PerformanceMode](../neural-network-runtime-type-h/document.md#oh_nn_performancemode). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode) | Execution result of the function. If the operation is successful, **OH\_NN\_SUCCESS** is returned. If the operation fails, an error is returned. For details about the error codes, see [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode). |

#### \[h2\]OH\_NNCompilation\_SetPriority()

OH\_NN\_ReturnCode OH\_NNCompilation\_SetPriority(OH\_NNCompilation \*compilation, OH\_NN\_Priority priority)

**Description**

Sets the priority for model computing.

NNRt allows you to set computing priorities for models. The priorities apply only to models created by the process with the same UID. The settings will not affect models created by processes with different UIDs on different devices. If this API is called on a device that does not support priority setting, the error code [OH\_NN\_UNAVAILABLE\_DEVICE](../neural-network-runtime-type-h/document.md#oh_nn_returncode) is returned.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NNCompilation](../../structs/oh-nncompilation/document.md) \*compilation | Pointer to the [OH\_NNCompilation](../../structs/oh-nncompilation/document.md) instance. |
| [OH\_NN\_Priority](../neural-network-runtime-type-h/document.md#oh_nn_priority) priority | Sets the priority. For details about the available priorities, see [OH\_NN\_Priority](../neural-network-runtime-type-h/document.md#oh_nn_priority). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode) | Execution result of the function. If the operation is successful, **OH\_NN\_SUCCESS** is returned. If the operation fails, an error is returned. For details about the error codes, see [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode). |

#### \[h2\]OH\_NNCompilation\_EnableFloat16()

OH\_NN\_ReturnCode OH\_NNCompilation\_EnableFloat16(OH\_NNCompilation \*compilation, bool enableFloat16)

**Description**

Enables float16 for computing.

By default, the floating-point model uses float32 for computing. If this API is called on a device that supports float16, floating-point model that supports float32 will use float16 for computing, so to reduce memory usage and execution time. This option is invalid for fixed-point models, for example, fixed-point models of the int8 type.

If this API is called on a device that does not support float16, the error code [OH\_NN\_UNAVAILABLE\_DEVICE](../neural-network-runtime-type-h/document.md#oh_nn_returncode) is returned.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NNCompilation](../../structs/oh-nncompilation/document.md) \*compilation | Pointer to the [OH\_NNCompilation](../../structs/oh-nncompilation/document.md) instance. |
| bool enableFloat16 | Whether to enable float16. If this parameter is set to **true**, float16 inference is performed. If this parameter is set to **false**, float32 inference is performed. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode) | Execution result of the function. If the operation is successful, **OH\_NN\_SUCCESS** is returned. If the operation fails, an error is returned. For details about the error codes, see [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode). |

#### \[h2\]OH\_NNCompilation\_Build()

OH\_NN\_ReturnCode OH\_NNCompilation\_Build(OH\_NNCompilation \*compilation)

**Description**

Performs model compilation.

After the compilation configuration is complete, call this API to start model compilation. The model compilation instance pushes the model and compilation options to the device for compilation.

After this API is called, additional compilation operations cannot be performed. If [OH\_NNCompilation\_SetDevice](#oh_nncompilation_setdevice), [OH\_NNCompilation\_SetCache](#oh_nncompilation_setcache), [OH\_NNCompilation\_SetPerformanceMode](#oh_nncompilation_setperformancemode), [OH\_NNCompilation\_SetPriority](#oh_nncompilation_setpriority), or [OH\_NNCompilation\_EnableFloat16](#oh_nncompilation_enablefloat16) is called, [OH\_NN\_OPERATION\_FORBIDDEN](../neural-network-runtime-type-h/document.md#oh_nn_returncode) is returned.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NNCompilation](../../structs/oh-nncompilation/document.md) \*compilation | Pointer to the [OH\_NNCompilation](../../structs/oh-nncompilation/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode) | Execution result of the function. If the operation is successful, **OH\_NN\_SUCCESS** is returned. If the operation fails, an error is returned. For details about the error codes, see [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode). |

#### \[h2\]OH\_NNCompilation\_Destroy()

void OH\_NNCompilation\_Destroy(OH\_NNCompilation \*\*compilation)

**Description**

Destroys an [OH\_NNCompilation](../../structs/oh-nncompilation/document.md) instance.

This API needs to be used to destroy the model compilation instances created by calling [OH\_NNCompilation\_Construct](#oh_nncompilation_construct), [OH\_NNCompilation\_ConstructWithOfflineModelFile](#oh_nncompilation_constructwithofflinemodelfile), [OH\_NNCompilation\_ConstructWithOfflineModelBuffer](#oh_nncompilation_constructwithofflinemodelbuffer) or [OH\_NNCompilation\_ConstructForCache](#oh_nncompilation_constructforcache). If **compilation** or **\*compilation** is a null pointer, this API only prints warning logs but does not perform the destruction operation.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NNCompilation](../../structs/oh-nncompilation/document.md) \*\*compilation | Level-2 pointer to the [OH\_NNCompilation](../../structs/oh-nncompilation/document.md) instance. After the model building instance is destroyed, this API sets **\*compilation** to a null pointer. |

#### \[h2\]OH\_NNTensorDesc\_Create()

NN\_TensorDesc \*OH\_NNTensorDesc\_Create()

**Description**

Creates an [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance.

[NN\_TensorDesc](../../structs/nn-tensordesc/document.md) describes various tensor attributes, such as the name, data type, shape, and format.

You can create an [NN\_Tensor](../../structs/nn-tensor/document.md) instance based on the input [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance by calling the following APIs:

[OH\_NNTensor\_Create](#oh_nntensor_create)

[OH\_NNTensor\_CreateWithSize](#oh_nntensor_createwithsize)

[OH\_NNTensor\_CreateWithFd](#oh_nntensor_createwithfd)

This API copies the [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance to [NN\_Tensor](../../structs/nn-tensor/document.md). This way, you can create multiple [NN\_Tensor](../../structs/nn-tensor/document.md) instances with the same [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance. If the [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance is no longer needed, call [OH\_NNTensorDesc\_Destroy](#oh_nntensordesc_destroy) to destroy it.

**Since**: 11

**Returns**

| Type | Description |
| :-- | :-- |
| [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) \* | Pointer to the [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance. If the operation fails, **NULL** is returned. |

#### \[h2\]OH\_NNTensorDesc\_Destroy()

OH\_NN\_ReturnCode OH\_NNTensorDesc\_Destroy(NN\_TensorDesc \*\*tensorDesc)

**Description**

Destroys an [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance.

If the [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance is no longer needed, call this API to destroy it. Otherwise, a memory leak occurs.

If **tensorDesc** or **\*tensorDesc** is a null pointer, an error is returned but the object will not be destroyed.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) \*\*tensorDesc | Level-2 pointer to the [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode) | Execution result of the function. If the operation is successful, **OH\_NN\_SUCCESS** is returned. If the operation fails, an error is returned. For details about the error codes, see [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode). |

#### \[h2\]OH\_NNTensorDesc\_SetName()

OH\_NN\_ReturnCode OH\_NNTensorDesc\_SetName(NN\_TensorDesc \*tensorDesc, const char \*name)

**Description**

Sets the name of an [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance.

After an [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance is created, call this API to set the tensor name. The value of \*name is a C-style string ending with \\0.

If **tensorDesc** or **name** is a null pointer, an error is returned.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) \*tensorDesc | Pointer to the [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance. |
| const char \*name | Name of the tensor to be set. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode) | Execution result of the function. If the operation is successful, **OH\_NN\_SUCCESS** is returned. If the operation fails, an error is returned. For details about the error codes, see [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode). |

#### \[h2\]OH\_NNTensorDesc\_GetName()

OH\_NN\_ReturnCode OH\_NNTensorDesc\_GetName(const NN\_TensorDesc \*tensorDesc, const char \*\*name)

**Description**

Obtains the name of an [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance.

You can use this API to obtain the name of the specified [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance. The value of **\*name** is a C-style string ending with **\\0**.

If **tensorDesc** or **name** is a null pointer, an error is returned. As an output parameter, **\*name** must be a null pointer. Otherwise, an error is returned.

For example, you should define **char\* tensorName = NULL** and pass **&tensorName** as a parameter of **name**.

You do not need to release the memory of **name**. When **tensorDesc** is destroyed, it is automatically released.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [const NN\_TensorDesc](../../structs/nn-tensordesc/document.md) \*tensorDesc | Pointer to the [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance. |
| const char \*\*name | Tensor name. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode) | Execution result of the function. If the operation is successful, **OH\_NN\_SUCCESS** is returned. If the operation fails, an error is returned. For details about the error codes, see [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode). |

#### \[h2\]OH\_NNTensorDesc\_SetDataType()

OH\_NN\_ReturnCode OH\_NNTensorDesc\_SetDataType(NN\_TensorDesc \*tensorDesc, OH\_NN\_DataType dataType)

**Description**

Sets the data type of an [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance.

After an [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance is created, call this API to set the tensor data type.

If **tensorDesc** is a null pointer, an error is returned.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) \*tensorDesc | Pointer to the [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance. |
| [OH\_NN\_DataType](../neural-network-runtime-type-h/document.md#oh_nn_datatype) dataType | Tensor data type to be set. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode) | Execution result of the function. If the operation is successful, **OH\_NN\_SUCCESS** is returned. If the operation fails, an error is returned. For details about the error codes, see [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode). |

#### \[h2\]OH\_NNTensorDesc\_GetDataType()

OH\_NN\_ReturnCode OH\_NNTensorDesc\_GetDataType(const NN\_TensorDesc \*tensorDesc, OH\_NN\_DataType \*dataType)

**Description**

Obtains the data type of an [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance.

You can use this API to obtain the data type of the specified [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance.

If **tensorDesc** or **dataType** is a null pointer, an error is returned.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [const NN\_TensorDesc](../../structs/nn-tensordesc/document.md) \*tensorDesc | Pointer to the [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance. |
| [OH\_NN\_DataType](../neural-network-runtime-type-h/document.md#oh_nn_datatype) \*dataType | Pointer to the returned tensor data type, which is used as the output parameter. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode) | Execution result of the function. If the operation is successful, **OH\_NN\_SUCCESS** is returned. If the operation fails, an error is returned. For details about the error codes, see [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode). |

#### \[h2\]OH\_NNTensorDesc\_SetShape()

OH\_NN\_ReturnCode OH\_NNTensorDesc\_SetShape(NN\_TensorDesc \*tensorDesc, const int32\_t \*shape, size\_t shapeLength)

**Description**

Sets the data shape of an [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance.

After an [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance is created, call this API to set the tensor shape.

If **tensorDesc** or **shape** is a null pointer, or **shapeLength** is 0, an error is returned.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) \*tensorDesc | Pointer to the [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance. |
| const int32\_t \*shape | List of tensor shapes to be set. |
| size\_t shapeLength | Length of the list of tensor shapes. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode) | Execution result of the function. If the operation is successful, **OH\_NN\_SUCCESS** is returned. If the operation fails, an error is returned. For details about the error codes, see [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode). |

#### \[h2\]OH\_NNTensorDesc\_GetShape()

OH\_NN\_ReturnCode OH\_NNTensorDesc\_GetShape(const NN\_TensorDesc \*tensorDesc, int32\_t \*\*shape, size\_t \*shapeLength)

**Description**

Obtains the shape of an [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance.

You can use this API to obtain the shape of the specified [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance.

If **tensorDesc**, **shape**, or **shapeLength** is a null pointer, an error is returned. As an output parameter, **\*shape** must be a null pointer. Otherwise, an error is returned.

For example, you should define **int32\_t\* tensorShape = NULL** and pass **&tensorShape** as a parameter of **shape**.

You do not need to release the memory of **shape**. When **tensorDesc** is destroyed, it is automatically released.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [const NN\_TensorDesc](../../structs/nn-tensordesc/document.md) \*tensorDesc | Pointer to the [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance. |
| int32\_t \*\*shape | List of tensor shapes. |
| size\_t \*shapeLength | Length of the list of tensor shapes. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode) | Execution result of the function. If the operation is successful, **OH\_NN\_SUCCESS** is returned. If the operation fails, an error is returned. For details about the error codes, see [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode). |

#### \[h2\]OH\_NNTensorDesc\_SetFormat()

OH\_NN\_ReturnCode OH\_NNTensorDesc\_SetFormat(NN\_TensorDesc \*tensorDesc, OH\_NN\_Format format)

**Description**

Sets the data format of an [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance.

After an [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance is created, call this API to set [OH\_NN\_Format](../neural-network-runtime-type-h/document.md#oh_nn_format) of the tensor.

If **tensorDesc** is a null pointer, an error is returned.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) \*tensorDesc | Pointer to the [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance. |
| [OH\_NN\_Format](../neural-network-runtime-type-h/document.md#oh_nn_format) format | Tensor data format to be set. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode) | Execution result of the function. If the operation is successful, **OH\_NN\_SUCCESS** is returned. If the operation fails, an error is returned. For details about the error codes, see [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode). |

#### \[h2\]OH\_NNTensorDesc\_GetFormat()

OH\_NN\_ReturnCode OH\_NNTensorDesc\_GetFormat(const NN\_TensorDesc \*tensorDesc, OH\_NN\_Format \*format)

**Description**

Obtains the data format of an [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance.

You can use this API to obtain [OH\_NN\_Format](../neural-network-runtime-type-h/document.md#oh_nn_format) of the specified [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance.

If **tensorDesc** or **format** is a null pointer, an error is returned.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [const NN\_TensorDesc](../../structs/nn-tensordesc/document.md) \*tensorDesc | Pointer to the [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance. |
| [OH\_NN\_Format](../neural-network-runtime-type-h/document.md#oh_nn_format) \*format | Tensor data format. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode) | Execution result of the function. If the operation is successful, **OH\_NN\_SUCCESS** is returned. If the operation fails, an error is returned. For details about the error codes, see [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode). |

#### \[h2\]OH\_NNTensorDesc\_GetElementCount()

OH\_NN\_ReturnCode OH\_NNTensorDesc\_GetElementCount(const NN\_TensorDesc \*tensorDesc, size\_t \*elementCount)

**Description**

Obtains the number of elements in an [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance.

You can use this API to obtain the number of elements in the specified [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance. To obtain the size of tensor data, call [OH\_NNTensorDesc\_GetByteSize](#oh_nntensordesc_getbytesize).

If the tensor shape is dynamically variable, this API returns an error code and **elementCount** is **0**.

If **tensorDesc** or **elementCount** is a null pointer, an error is returned.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [const NN\_TensorDesc](../../structs/nn-tensordesc/document.md) \*tensorDesc | Pointer to the [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance. |
| size\_t \*elementCount | Number of elements. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode) | Execution result of the function. If the operation is successful, **OH\_NN\_SUCCESS** is returned. If the operation fails, an error is returned. For details about the error codes, see [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode). |

#### \[h2\]OH\_NNTensorDesc\_GetByteSize()

OH\_NN\_ReturnCode OH\_NNTensorDesc\_GetByteSize(const NN\_TensorDesc \*tensorDesc, size\_t \*byteSize)

**Description**

Obtains the number of bytes occupied by the tensor data obtained through calculation based on the shape and data type of an [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance.

You can use this API to obtain the number of bytes occupied by the tensor data obtained through calculation based on the shape and data type of the specified [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance.

If the tensor shape is dynamically variable, this API returns an error code and **byteSize** is **0**.

To obtain the number of elements in the tensor data, call [OH\_NNTensorDesc\_GetElementCount](#oh_nntensordesc_getelementcount).

If **tensorDesc** or **byteSize** is a null pointer, an error is returned.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [const NN\_TensorDesc](../../structs/nn-tensordesc/document.md) \*tensorDesc | Pointer to the [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance. |
| size\_t \*byteSize | Size of the returned data, in bytes. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode) | Execution result of the function. If the operation is successful, **OH\_NN\_SUCCESS** is returned. If the operation fails, an error is returned. For details about the error codes, see [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode). |

#### \[h2\]OH\_NNTensor\_Create()

NN\_Tensor \*OH\_NNTensor\_Create(size\_t deviceID, NN\_TensorDesc \*tensorDesc)

**Description**

Creates an [NN\_Tensor](../../structs/nn-tensor/document.md) instance from [NN\_TensorDesc](../../structs/nn-tensordesc/document.md).

This API uses [OH\_NNTensorDesc\_GetByteSize](#oh_nntensordesc_getbytesize) to calculate the number of bytes of tensor data and allocate device memory for it. The device driver directly obtains tensor data in zero-copy mode.

This API copies **tensorDesc** to [NN\_Tensor](../../structs/nn-tensor/document.md). Therefore, if **tensorDesc** is no longer needed, destroy it by calling [OH\_NNTensorDesc\_Destroy](#oh_nntensordesc_destroy).

If the tensor shape is dynamic, an error is returned.

**deviceID** indicates the selected device. If the value is **0**, the first device in the current device list is used by default.

**tensorDesc is mandatory**. If it is a null pointer, an error is returned.

If the [NN\_Tensor](../../structs/nn-tensor/document.md) instance is no longer needed, destroy it by calling [OH\_NNTensor\_Destroy](#oh_nntensor_destroy).

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| size\_t deviceID | Device ID. If the value is **0**, the first device in the current device list is used by default. |
| [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) \*tensorDesc | Pointer to the [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [NN\_Tensor](../../structs/nn-tensor/document.md) \* | Pointer to the [NN\_Tensor](../../structs/nn-tensor/document.md) instance. If the operation fails, **NULL** is returned. |

#### \[h2\]OH\_NNTensor\_CreateWithSize()

NN\_Tensor \*OH\_NNTensor\_CreateWithSize(size\_t deviceID, NN\_TensorDesc \*tensorDesc, size\_t size)

**Description**

Creates an [NN\_Tensor](../../structs/nn-tensor/document.md) instance based on the specified memory size and [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance.

This API uses **size** as the number of bytes of tensor data and allocates device memory to it. The device driver directly obtains tensor data in zero-copy mode.

Note that this API copies **tensorDesc** to [NN\_Tensor](../../structs/nn-tensor/document.md). Therefore, if **tensorDesc** is no longer needed, destroy it by calling [OH\_NNTensorDesc\_Destroy](#oh_nntensordesc_destroy).

**deviceID** indicates the ID of the selected device. If the value is **0**, the first device is used.

**tensorDesc** is mandatory. If it is a null pointer, an error is returned.

The value of **size** must be greater than or equal to the number of bytes occupied by **tensorDesc**, which can be obtained by calling [OH\_NNTensorDesc\_GetByteSize](#oh_nntensordesc_getbytesize). Otherwise, an error is returned. If the tensor shape is dynamic, **size** is not checked.

If the [NN\_Tensor](../../structs/nn-tensor/document.md) instance is no longer needed, destroy it by calling [OH\_NNTensor\_Destroy](#oh_nntensor_destroy).

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| size\_t deviceID | Device ID. If the value is **0**, the first device in the current device list is used by default. |
| [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) \*tensorDesc | Pointer to the [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance. |
| size\_t size | Size of the tensor data to be allocated. |

**Returns**

| Type | Description |
| :-- | :-- |
| [NN\_Tensor](../../structs/nn-tensor/document.md) \* | Pointer to the [NN\_Tensor](../../structs/nn-tensor/document.md) instance. If the operation fails, **NULL** is returned. |

#### \[h2\]OH\_NNTensor\_CreateWithFd()

NN\_Tensor \*OH\_NNTensor\_CreateWithFd(size\_t deviceID,NN\_TensorDesc \*tensorDesc,int fd,size\_t size,size\_t offset)

**Description**

Creates an [NN\_Tensor](../../structs/nn-tensor/document.md) instance based on the specified file descriptor of the shared memory and [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance.

This API reuses the shared memory corresponding to **fd**, which may source from another [NN\_Tensor](../../structs/nn-tensor/document.md) instance. When the tensor created by calling [OH\_NNTensor\_Destroy](#oh_nntensor_destroy) is destroyed, the memory storing the tensor data is not released.

Note that this API copies **tensorDesc** to [NN\_Tensor](../../structs/nn-tensor/document.md). Therefore, if **tensorDesc** is no longer needed, destroy it by calling [OH\_NNTensorDesc\_Destroy](#oh_nntensordesc_destroy).

**deviceID** indicates the selected device. If the value is **0**, the first device in the current device list is used by default.

**tensorDesc** is mandatory. If the pointer is null, an error is returned.

If the [NN\_Tensor](../../structs/nn-tensor/document.md) instance is no longer needed, destroy it by calling [OH\_NNTensor\_Destroy](#oh_nntensor_destroy).

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| size\_t deviceID | Device ID. If the value is **0**, the first device in the current device list is used by default. |
| [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) \*tensorDesc | Pointer to the [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance. |
| int fd | **fd** of the shared memory to be used. |
| size\_t size | Size of the shared memory to be used. |
| size\_t offset | Offset of the shared memory to be used. |

**Returns**

| Type | Description |
| :-- | :-- |
| [NN\_Tensor](../../structs/nn-tensor/document.md) \* | Pointer to the [NN\_Tensor](../../structs/nn-tensor/document.md) instance. If the operation fails, **NULL** is returned. |

#### \[h2\]OH\_NNTensor\_Destroy()

OH\_NN\_ReturnCode OH\_NNTensor\_Destroy(NN\_Tensor \*\*tensor)

**Description**

Destroys an [NN\_Tensor](../../structs/nn-tensor/document.md) instance.

If the [NN\_Tensor](../../structs/nn-tensor/document.md) instance is no longer needed, call this API to destroy it. Otherwise, a memory leak occurs.

If **tensor** or **\*tensor** is a null pointer, an error is returned but the object will not be destroyed.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [NN\_Tensor](../../structs/nn-tensor/document.md) \*\*tensor | Level-2 pointer to the [NN\_Tensor](../../structs/nn-tensor/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode) | Execution result of the function. If the operation is successful, **OH\_NN\_SUCCESS** is returned. If the operation fails, an error is returned. For details about the error codes, see [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode). |

#### \[h2\]OH\_NNTensor\_GetTensorDesc()

NN\_TensorDesc \*OH\_NNTensor\_GetTensorDesc(const NN\_Tensor \*tensor)

**Description**

Obtains an [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance of [NN\_Tensor](../../structs/nn-tensor/document.md).

You can use this API to obtain the pointer to the [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance of the specified [NN\_Tensor](../../structs/nn-tensor/document.md) instance.

You can obtain tensor attributes of various types from the returned [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance, such as the name, data format, data type, and shape.

You should not destroy the returned [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance because it points to an internal instance of [NN\_Tensor](../../structs/nn-tensor/document.md). Otherwise, once [OH\_NNTensor\_Destroy](#oh_nntensor_destroy) is called, a crash may occur due to double memory release.

If **Tensor** is a null pointer, a null pointer is returned.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [const NN\_Tensor](../../structs/nn-tensor/document.md) \*tensor | Pointer to the [NN\_Tensor](../../structs/nn-tensor/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) \* | Pointer to the [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance. If the operation fails, **NULL** is returned. |

#### \[h2\]OH\_NNTensor\_GetDataBuffer()

void \*OH\_NNTensor\_GetDataBuffer(const NN\_Tensor \*tensor)

**Description**

Obtains the memory address of [NN\_Tensor](../../structs/nn-tensor/document.md) data.

You can read/write data from/to tensor data memory. The data memory is mapped from the shared memory on the device. Therefore, the device driver can directly obtain tensor data in zero-copy mode.

Only tensor data in the \[offset, size) segment in the corresponding shared memory can be used. **offset** indicates the offset in the shared memory and can be obtained by calling [OH\_NNTensor\_GetOffset](#oh_nntensor_getoffset). **size** indicates the total size of the shared memory, which can be obtained by calling [OH\_NNTensor\_GetSize](#oh_nntensor_getsize).

If **Tensor** is a null pointer, a null pointer is returned.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [const NN\_Tensor](../../structs/nn-tensor/document.md) \*tensor | Pointer to the [NN\_Tensor](../../structs/nn-tensor/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| void \* | Pointer to the tensor data memory. If the operation fails, a null pointer is returned. |

#### \[h2\]OH\_NNTensor\_GetFd()

OH\_NN\_ReturnCode OH\_NNTensor\_GetFd(const NN\_Tensor \*tensor, int \*fd)

**Description**

Obtains the file descriptor (**fd**) of the shared memory where [NN\_Tensor](../../structs/nn-tensor/document.md) data is stored.

**fd** corresponds to a device shared memory and can be used by another [NN\_Tensor](../../structs/nn-tensor/document.md) through [OH\_NNTensor\_CreateWithFd](#oh_nntensor_createwithfd).

If **tensor** or **fd** is a null pointer, an error is returned.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [const NN\_Tensor](../../structs/nn-tensor/document.md) \*tensor | Pointer to the [NN\_Tensor](../../structs/nn-tensor/document.md) instance. |
| int \*fd | **fd** of the shared memory. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode) | Execution result of the function. If the operation is successful, **OH\_NN\_SUCCESS** is returned. If the operation fails, an error is returned. For details about the error codes, see [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode). |

#### \[h2\]OH\_NNTensor\_GetSize()

OH\_NN\_ReturnCode OH\_NNTensor\_GetSize(const NN\_Tensor \*tensor, size\_t \*size)

**Description**

Obtains the size of the shared memory where the [NN\_Tensor](../../structs/nn-tensor/document.md) data is stored.

The value of **size** is the same as that of [OH\_NNTensor\_CreateWithSize](#oh_nntensor_createwithsize) and [OH\_NNTensor\_CreateWithFd](#oh_nntensor_createwithfd). However, for a tensor created by using [OH\_NNTensor\_Create](#oh_nntensor_create), the value of **size** is equal to the number of bytes actually occupied by the tensor data, which can be obtained by calling [OH\_NNTensorDesc\_GetByteSize](#oh_nntensordesc_getbytesize).

Only tensor data in the \[offset, size) segment in the shared memory corresponding to the **fd** can be used. **offset** indicates the offset in the shared memory and can be obtained by calling [OH\_NNTensor\_GetOffset](#oh_nntensor_getoffset). **size** indicates the total size of the shared memory, which can be obtained by calling [OH\_NNTensor\_GetSize](#oh_nntensor_getsize).

If **tensor** or **size** is a null pointer, an error is returned.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [const NN\_Tensor](../../structs/nn-tensor/document.md) \*tensor | Pointer to the [NN\_Tensor](../../structs/nn-tensor/document.md) instance. |
| size\_t \*size | Size of the shared memory where the returned data is located. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode) | Execution result of the function. If the operation is successful, **OH\_NN\_SUCCESS** is returned. If the operation fails, an error is returned. For details about the error codes, see [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode). |

#### \[h2\]OH\_NNTensor\_GetOffset()

OH\_NN\_ReturnCode OH\_NNTensor\_GetOffset(const NN\_Tensor \*tensor, size\_t \*offset)

**Description**

Obtains the offset of [NN\_Tensor](../../structs/nn-tensor/document.md) data in the shared memory.

**offset** indicates the offset of tensor data in the corresponding shared memory. It can be used by another [NN\_Tensor](../../structs/nn-tensor/document.md) together with **fd** and **size** of the shared memory through [OH\_NNTensor\_CreateWithFd](#oh_nntensor_createwithfd).

Only tensor data in the \[offset, size) segment in the shared memory corresponding to the **fd** can be used. **offset** indicates the offset in the shared memory and can be obtained by calling [OH\_NNTensor\_GetOffset](#oh_nntensor_getoffset). **size** indicates the total size of the shared memory, which can be obtained by calling [OH\_NNTensor\_GetSize](#oh_nntensor_getsize).

If **tensor** or **offset** is a null pointer, an error is returned.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [const NN\_Tensor](../../structs/nn-tensor/document.md) \*tensor | Pointer to the [NN\_Tensor](../../structs/nn-tensor/document.md) instance. |
| size\_t \*offset | Offset for the fd of the tensor. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode) | Execution result of the function. If the operation is successful, **OH\_NN\_SUCCESS** is returned. If the operation fails, an error is returned. For details about the error codes, see [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode). |

#### \[h2\]OH\_NNExecutor\_Construct()

OH\_NNExecutor \*OH\_NNExecutor\_Construct(OH\_NNCompilation \*compilation)

**Description**

Creates an [OH\_NNExecutor](../../structs/oh-nnexecutor/document.md) executor instance.

This API constructs a model inference executor for a device based on the specified [OH\_NNCompilation](../../structs/oh-nncompilation/document.md) instance. Use [OH\_NNExecutor\_SetInput](../neural-network-runtime-h/document.md#oh_nnexecutor_setinput) to set the model input data. After the input data is set, call [OH\_NNExecutor\_Run](../neural-network-runtime-h/document.md#oh_nnexecutor_run) to perform inference and then call [OH\_NNExecutor\_SetOutput](../neural-network-runtime-h/document.md#oh_nnexecutor_setoutput) to obtain the computing result. After an [OH\_NNExecutor](../../structs/oh-nnexecutor/document.md) instance is created through the [OH\_NNCompilation](../../structs/oh-nncompilation/document.md) instance, destroy the [OH\_NNCompilation](../../structs/oh-nncompilation/document.md) instance if it is no longer needed.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NNCompilation](../../structs/oh-nncompilation/document.md) \*compilation | Pointer to the [OH\_NNCompilation](../../structs/oh-nncompilation/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NNExecutor](../../structs/oh-nnexecutor/document.md) \* | Pointer to the [OH\_NNExecutor](../../structs/oh-nnexecutor/document.md) instance. If the operation fails, NULL is returned. |

#### \[h2\]OH\_NNExecutor\_GetOutputShape()

OH\_NN\_ReturnCode OH\_NNExecutor\_GetOutputShape(OH\_NNExecutor \*executor,uint32\_t outputIndex,int32\_t \*\*shape,uint32\_t \*shapeLength)

**Description**

Obtains the dimension information about the output tensor.

You can use this API to obtain information about the specified output dimension and number of dimensions after a single inference is performed by calling [OH\_NNExecutor\_Run](../neural-network-runtime-h/document.md#oh_nnexecutor_run). It is commonly used in dynamic shape input and output scenarios.

If the value of **outputIndex** reaches or exceeds the number of output tensors, an error is returned. You can obtain the number of output tensors by calling [OH\_NNExecutor\_GetOutputCount](#oh_nnexecutor_getoutputcount).

As an output parameter, **\*shape** cannot be a null pointer. Otherwise, an error is returned. For example, you should define **int32\_t\* tensorShape = NULL** and pass **&tensorShape** as an input parameter.

You do not need to release the memory of **shape**. It is released with **executor**.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NNExecutor](../../structs/oh-nnexecutor/document.md) \*executor | Pointer to the [OH\_NNExecutor](../../structs/oh-nnexecutor/document.md) instance. |
| uint32\_t outputIndex | Output index value, which is the same as the sequence of the output data when [OH\_NNModel\_SpecifyInputsAndOutputs](../neural-network-runtime-h/document.md#oh_nnmodel_specifyinputsandoutputs) is called. Assume that **outputIndices** is {4, 6, 8} when [OH\_NNModel\_SpecifyInputsAndOutputs](../neural-network-runtime-h/document.md#oh_nnmodel_specifyinputsandoutputs) is called. When you obtain information about the output dimension, set the value of this parameter to {0, 1, 2}. |
| int32\_t \*\*shape | Pointer to the int32\_t array. The value of each element in the array is the length of the output tensor in each dimension. |
| uint32\_t \*shapeLength | Pointer to the uint32\_t type. The number of output dimensions is returned. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode) | Execution result of the function. If the operation is successful, **OH\_NN\_SUCCESS** is returned. If the operation fails, an error is returned. For details about the error codes, see [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode). |

#### \[h2\]OH\_NNExecutor\_Destroy()

void OH\_NNExecutor\_Destroy(OH\_NNExecutor \*\*executor)

**Description**

Destroys an executor instance to release the memory occupied by it.

This API needs to be called to release the executor instance created by calling [OH\_NNExecutor\_Construct](#oh_nnexecutor_construct). Otherwise, a memory leak occurs. If **executor** or **\*executor** is a null pointer, this API only prints the warning log and does not execute the release logic.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NNExecutor](../../structs/oh-nnexecutor/document.md) \*\*executor | Level-2 pointer to the [OH\_NNExecutor](../../structs/oh-nnexecutor/document.md) instance. |

#### \[h2\]OH\_NNExecutor\_GetInputCount()

OH\_NN\_ReturnCode OH\_NNExecutor\_GetInputCount(const OH\_NNExecutor \*executor, size\_t \*inputCount)

**Description**

Obtains the number of input tensors.

You can obtain the number of input tensors from **executor**, and then use [OH\_NNExecutor\_CreateInputTensorDesc](#oh_nnexecutor_createinputtensordesc) to create a tensor description based on the specified tensor index.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [const OH\_NNExecutor](../../structs/oh-nnexecutor/document.md) \*executor | Pointer to the [OH\_NNExecutor](../../structs/oh-nnexecutor/document.md) instance. |
| size\_t \*inputCount | Number of returned input tensors. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode) | Execution result of the function. If the operation is successful, **OH\_NN\_SUCCESS** is returned. If the operation fails, an error is returned. For details about the error codes, see [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode). |

#### \[h2\]OH\_NNExecutor\_GetOutputCount()

OH\_NN\_ReturnCode OH\_NNExecutor\_GetOutputCount(const OH\_NNExecutor \*executor, size\_t \*outputCount)

**Description**

Obtains the number of output tensors.

You can obtain the number of output tensors from **executor**, and then use [OH\_NNExecutor\_CreateOutputTensorDesc](#oh_nnexecutor_createoutputtensordesc) to create a tensor description based on the specified tensor index.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [const OH\_NNExecutor](../../structs/oh-nnexecutor/document.md) \*executor | Pointer to the [OH\_NNExecutor](../../structs/oh-nnexecutor/document.md) instance. |
| size\_t \*outputCount | Number of returned output tensors. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode) | Execution result of the function. If the operation is successful, **OH\_NN\_SUCCESS** is returned. If the operation fails, an error is returned. For details about the error codes, see [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode). |

#### \[h2\]OH\_NNExecutor\_CreateInputTensorDesc()

NN\_TensorDesc \*OH\_NNExecutor\_CreateInputTensorDesc(const OH\_NNExecutor \*executor, size\_t index)

**Description**

Creates the description of an input tensor based on the specified index value.

The description contains all types of attribute values of the tensor. If the value of **index** reaches or exceeds the number of input tensors, an error is returned. You can obtain the number of input tensors by calling [OH\_NNExecutor\_GetInputCount](#oh_nnexecutor_getinputcount).

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [const OH\_NNExecutor](../../structs/oh-nnexecutor/document.md) \*executor | Pointer to the [OH\_NNExecutor](../../structs/oh-nnexecutor/document.md) instance. |
| size\_t index | Index value of the input tensor. |

**Returns**

| Type | Description |
| :-- | :-- |
| [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) \* | Pointer to the [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance. If the operation fails, **NULL** is returned. |

#### \[h2\]OH\_NNExecutor\_CreateOutputTensorDesc()

NN\_TensorDesc \*OH\_NNExecutor\_CreateOutputTensorDesc(const OH\_NNExecutor \*executor, size\_t index)

**Description**

Creates the description of an output tensor based on the specified index value.

The description contains all types of attribute values of the tensor. If the value of **index** reaches or exceeds the number of output tensors, an error is returned. You can obtain the number of output tensors by calling [OH\_NNExecutor\_GetOutputCount](#oh_nnexecutor_getoutputcount).

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [const OH\_NNExecutor](../../structs/oh-nnexecutor/document.md) \*executor | Pointer to the [OH\_NNExecutor](../../structs/oh-nnexecutor/document.md) instance. |
| size\_t index | Index value of the output tensor. |

**Returns**

| Type | Description |
| :-- | :-- |
| [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) \* | Pointer to the [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) instance. If the operation fails, **NULL** is returned. |

#### \[h2\]OH\_NNExecutor\_GetInputDimRange()

OH\_NN\_ReturnCode OH\_NNExecutor\_GetInputDimRange(const OH\_NNExecutor \*executor,size\_t index,size\_t \*\*minInputDims,size\_t \*\*maxInputDims,size\_t \*shapeLength)

**Description**

Obtains the dimension range of all input tensors.

If the input tensor has a dynamic shape, the dimension range supported by the tensor may vary according to device. You can call this API to obtain the dimension range supported by the current device. **\*minInputDims** saves the minimum dimension of the specified input tensor (the number of dimensions matches the shape), while **\*maxInputDims** saves the maximum dimension.

For example, if an input tensor has a dynamic shape of \[-1, -1, -1, 3\], **\*minInputDims** may be \[1, 10, 10, 3\], and **\*maxInputDims** may be \[100, 1024, 1024, 3\].

If the value of **index** reaches or exceeds the number of input tensors, an error is returned. You can obtain the number of input tensors by calling [OH\_NNExecutor\_GetInputCount](#oh_nnexecutor_getinputcount).

As output parameters, **\*minInputDims** and **\*maxInputDims** cannot be null pointers. Otherwise, an error is returned. For example, you should define **int32\_t\* minInDims = NULL**, and then pass **&minInDims** as an input parameter.

You do not need to release the memory of **minInputDims** and **maxInputDims**. It is released with **executor**.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [const OH\_NNExecutor](../../structs/oh-nnexecutor/document.md) \*executor | Pointer to the [OH\_NNExecutor](../../structs/oh-nnexecutor/document.md) instance. |
| size\_t index | Index value of the input tensor. |
| size\_t \*\*minInputDims | Pointer to the returned array, which saves the minimum dimension of the specified input tensor (the number of dimensions matches the shape). |
| size\_t \*\*maxInputDims | Pointer to the returned array, which saves the maximum dimension of the specified input tensor (the number of dimensions matches the shape). |
| size\_t \*shapeLength | Number of dimensions of the returned input tensor, which is the same as the shape. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode) | Execution result of the function. If the operation is successful, **OH\_NN\_SUCCESS** is returned. If the operation fails, an error is returned. For details about the error codes, see [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode). |

#### \[h2\]OH\_NNExecutor\_SetOnRunDone()

OH\_NN\_ReturnCode OH\_NNExecutor\_SetOnRunDone(OH\_NNExecutor \*executor, NN\_OnRunDone onRunDone)

**Description**

Sets the callback processing function invoked when the asynchronous inference ends.

For details about the callback function, see [NN\_OnRunDone](../neural-network-runtime-type-h/document.md#nn_onrundone).

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NNExecutor](../../structs/oh-nnexecutor/document.md) \*executor | Pointer to the [OH\_NNExecutor](../../structs/oh-nnexecutor/document.md) instance. |
| [NN\_OnRunDone](../neural-network-runtime-type-h/document.md#nn_onrundone) onRunDone | Handle of the callback function [NN\_OnRunDone](../neural-network-runtime-type-h/document.md#nn_onrundone). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode) | Execution result of the function. If the operation is successful, **OH\_NN\_SUCCESS** is returned. If the operation fails, an error is returned. For details about the error codes, see [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode). |

#### \[h2\]OH\_NNExecutor\_SetOnServiceDied()

OH\_NN\_ReturnCode OH\_NNExecutor\_SetOnServiceDied(OH\_NNExecutor \*executor, NN\_OnServiceDied onServiceDied)

**Description**

Sets the callback processing function invoked when the device driver service terminates unexpectedly during asynchronous inference.

For details about the callback function, see [NN\_OnServiceDied](../neural-network-runtime-type-h/document.md#nn_onservicedied).

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NNExecutor](../../structs/oh-nnexecutor/document.md) \*executor | Pointer to the [OH\_NNExecutor](../../structs/oh-nnexecutor/document.md) instance. |
| [NN\_OnServiceDied](../neural-network-runtime-type-h/document.md#nn_onservicedied) onServiceDied | Handle of the callback function [NN\_OnServiceDied](../neural-network-runtime-type-h/document.md#nn_onservicedied). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode) | Execution result of the function. If the operation is successful, **OH\_NN\_SUCCESS** is returned. If the operation fails, an error is returned. For details about the error codes, see [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode). |

#### \[h2\]OH\_NNExecutor\_RunSync()

OH\_NN\_ReturnCode OH\_NNExecutor\_RunSync(OH\_NNExecutor \*executor,NN\_Tensor \*inputTensor\[\],size\_t inputCount,NN\_Tensor \*outputTensor\[\],size\_t outputCount)

**Description**

Performs synchronous inference.

You need to create input and output tensors by calling [OH\_NNTensor\_Create](#oh_nntensor_create), [OH\_NNTensor\_CreateWithSize](#oh_nntensor_createwithsize), or [OH\_NNTensor\_CreateWithFd](#oh_nntensor_createwithfd). Then, use [OH\_NNTensor\_GetDataBuffer](#oh_nntensor_getdatabuffer) to obtain the pointer to tensor data and copy the input data to it. The executor performs model inference, generates the inference result, and writes the result to the output tensor.

If the output tensor has a dynamic shape, you can obtain the actual shape of the output tensor by calling [OH\_NNExecutor\_GetOutputShape](#oh_nnexecutor_getoutputshape). Alternatively, obtain the tensor description from the input tensor by calling [OH\_NNTensor\_GetTensorDesc](#oh_nntensor_gettensordesc), and then obtain the actual shape by calling [OH\_NNTensorDesc\_GetShape](#oh_nntensordesc_getshape).

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NNExecutor](../../structs/oh-nnexecutor/document.md) \*executor | Pointer to the [OH\_NNExecutor](../../structs/oh-nnexecutor/document.md) instance. |
| [NN\_Tensor](../../structs/nn-tensor/document.md) \*inputTensor\[\] | Array of input tensors. |
| size\_t inputCount | Number of input tensors. |
| [NN\_Tensor](../../structs/nn-tensor/document.md) \*outputTensor\[\] | Array of output tensors. |
| size\_t outputCount | Number of output tensors. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode) | Execution result of the function. If the operation is successful, **OH\_NN\_SUCCESS** is returned. If the operation fails, an error is returned. For details about the error codes, see [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode). |

#### \[h2\]OH\_NNExecutor\_RunAsync()

OH\_NN\_ReturnCode OH\_NNExecutor\_RunAsync(OH\_NNExecutor \*executor,NN\_Tensor \*inputTensor\[\],size\_t inputCount,NN\_Tensor \*outputTensor\[\],size\_t outputCount,int32\_t timeout,void \*userData)

**Description**

Performs asynchronous inference.

You need to create input and output tensors by calling [OH\_NNTensor\_Create](#oh_nntensor_create), [OH\_NNTensor\_CreateWithSize](#oh_nntensor_createwithsize), or [OH\_NNTensor\_CreateWithFd](#oh_nntensor_createwithfd). Then, use [OH\_NNTensor\_GetDataBuffer](#oh_nntensor_getdatabuffer) to obtain the pointer to tensor data and copy the input data to it. The executor performs model inference, generates the inference result, and writes the result to the output tensor.

If the output tensor has a dynamic shape, you can obtain the actual shape of the output tensor by calling [OH\_NNExecutor\_GetOutputShape](#oh_nnexecutor_getoutputshape). Alternatively, obtain the tensor description from the input tensor by calling [OH\_NNTensor\_GetTensorDesc](#oh_nntensor_gettensordesc), and then obtain the actual shape by calling [OH\_NNTensorDesc\_GetShape](#oh_nntensordesc_getshape).

This API works in non-blocking mode and returns the result immediately after being called. You can obtain the inference result and execution return status through the [NN\_OnRunDone](../neural-network-runtime-type-h/document.md#nn_onrundone) callback. If the device driver service stops abnormally during execution, you can use the [NN\_OnServiceDied](../neural-network-runtime-type-h/document.md#nn_onservicedied) callback for exception processing.

You can set the NN\_OnRunDone\](capi-neural-network-runtime-type-h.md#nn\_onrundone) and [NN\_OnServiceDied](../neural-network-runtime-type-h/document.md#nn_onservicedied) callbacks by calling [OH\_NNExecutor\_SetOnRunDone](#oh_nnexecutor_setonrundone) and [OH\_NNExecutor\_SetOnServiceDied](#oh_nnexecutor_setonservicedied).

If the inference times out, it is terminated immediately and the error code [OH\_NN\_TIMEOUT](../neural-network-runtime-type-h/document.md#oh_nn_returncode) is returned through the [NN\_OnRunDone](../neural-network-runtime-type-h/document.md#nn_onrundone) callback.

**userData** is the identifier used to distinguish different asynchronous inferences and is returned as the first parameter in the callback. You can use any data that can distinguish different inferences as the identifier.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NNExecutor](../../structs/oh-nnexecutor/document.md) \*executor | Pointer to the [OH\_NNExecutor](../../structs/oh-nnexecutor/document.md) instance. |
| [NN\_Tensor](../../structs/nn-tensor/document.md) \*inputTensor\[\] | Array of input tensors. |
| size\_t inputCount | Number of input tensors. |
| [NN\_Tensor](../../structs/nn-tensor/document.md) \*outputTensor\[\] | Array of output tensors. |
| size\_t outputCount | Number of output tensors. |
| int32\_t timeout | Timeout interval of asynchronous inference, in ms. For example, **1000** indicates that the timeout interval is 1000 ms. |
| void \*userData | Identifier of asynchronous inference. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode) | Execution result of the function. If the operation is successful, **OH\_NN\_SUCCESS** is returned. If the operation fails, an error is returned. For details about the error codes, see [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode). |

#### \[h2\]OH\_NNDevice\_GetAllDevicesID()

OH\_NN\_ReturnCode OH\_NNDevice\_GetAllDevicesID(const size\_t \*\*allDevicesID, uint32\_t \*deviceCount)

**Description**

Obtains the ID of the device connected to NNRt.

Each device has a unique and fixed ID, which is returned through a uint32\_t array.

When device IDs are returned through the size\_t array, each element of the array is the ID of a single device. Internal management is used for array memory. The data pointer remains valid before this API is called next time.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| const size\_t \*\*allDevicesID | Pointer to the **size\_t** array. The input \*allDevicesID must be a null pointer. Otherwise, the error code [OH\_NN\_INVALID\_PARAMETER](../neural-network-runtime-type-h/document.md#oh_nn_returncode) is returned. |
| uint32\_t \*deviceCount | Pointer of the uint32\_t type, which is used to return the length of **\*allDevicesID**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode) | Execution result of the function. If the operation is successful, **OH\_NN\_SUCCESS** is returned. If the operation fails, an error is returned. For details about the error codes, see [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode). |

#### \[h2\]OH\_NNDevice\_GetName()

OH\_NN\_ReturnCode OH\_NNDevice\_GetName(size\_t deviceID, const char \*\*name)

**Description**

Obtains the name of the specified device.

**deviceID** specifies the device ID used to obtain the device name. The device ID needs to be obtained by calling [OH\_NNDevice\_GetAllDevicesID](#oh_nndevice_getalldevicesid). If the value of **deviceID** is **0**, the first device in the device list is used by default. **\*name** is a C-style string ended with **'\\0'**. **\*name** must be a null pointer. Otherwise, the error code [OH\_NN\_INVALID\_PARAMETER](../neural-network-runtime-type-h/document.md#oh_nn_returncode) is returned. For example, you should define **char\* deviceName = NULL**, and then pass **&deviceName** as an input parameter.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| size\_t deviceID | Device ID. If the value of **deviceID** is **0**, the first device in the device list is used by default. |
| const char \*\*name | Pointer to the char array, which saves the returned device name. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode) | Execution result of the function. If the operation is successful, **OH\_NN\_SUCCESS** is returned. If the operation fails, an error is returned. For details about the error codes, see [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode). |

#### \[h2\]OH\_NNDevice\_GetType()

OH\_NN\_ReturnCode OH\_NNDevice\_GetType(size\_t deviceID, OH\_NN\_DeviceType \*deviceType)

**Description**

Obtains the type of the specified device.

**deviceID** specifies the device ID used to obtain the device type. If the value of **deviceID** is **0**, the first device in the device list is used by default. Currently, the following device types are supported:

-   **OH\_NN\_CPU**: CPU device.
    
-   **OH\_NN\_GPU**: GPU device.
    
-   **OH\_NN\_ACCELERATOR**: machine learning dedicated accelerator.
    
-   -   -   **OH\_NN\_OTHERS**: other device types.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| size\_t deviceID | Device ID. If the value of **deviceID** is **0**, the first device in the device list is used by default. |
| [OH\_NN\_DeviceType](../neural-network-runtime-type-h/document.md#oh_nn_devicetype) \*deviceType | Pointer to the [OH\_NN\_DeviceType](../neural-network-runtime-type-h/document.md#oh_nn_devicetype) instance. The device type information is returned. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode) | Execution result of the function. If the operation is successful, **OH\_NN\_SUCCESS** is returned. If the operation fails, an error is returned. For details about the error codes, see [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode). |
