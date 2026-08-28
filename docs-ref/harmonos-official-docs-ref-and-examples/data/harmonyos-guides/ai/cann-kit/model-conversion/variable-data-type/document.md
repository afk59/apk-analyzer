# Variable data\_type

#### Overview

Variable **data\_type** is a function supported by the OMG tool. With this function, you do not need to modify a trained model for different input and output data types. When performing [model conversion](../offline-model-conversion/omg-parameters/document.md) using the OMG tool, specify the input and output data type so that the model can be applicable to different scenarios.

#### Instruction

Set **input\_type** and **output\_type** of [OMG parameters](../offline-model-conversion/omg-parameters/document.md) to specify the input and output data types during model conversion.

Sample code:

./omg --model=./model.pb --framework=3 --output=./model --input\_shape="inputs:1,512,512,1" --out\_nodes="outputs:0" --input\_type="inputs:FP16" --output\_type="outputs:UINT8"
