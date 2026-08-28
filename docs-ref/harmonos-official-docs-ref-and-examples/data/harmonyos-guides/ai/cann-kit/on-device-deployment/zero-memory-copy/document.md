# Zero Memory Copy

#### Overview

Zero memory copy is applicable when GPU texture data or model input data already exists in the ION memory. It allows the ION memory where data is stored to be encapsulated into input and output tensors for direct inference, without data copy from the input and output tensors. This helps save the memory and make inference more efficient.

#### Instruction

After a model is loaded, call [OH\_NNTensor\_CreateWithFd](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-core-h#oh_nntensor_createwithfd) to encapsulate the ION memory into input tensor (**input\_tensor**) and output tensor (**output\_tensor**) and initiate model inference.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/Fn3lfGztTfayvHuAiAB4pg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062125Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6E39988DFA08C12E283D06D5B5AACC73E567F43CBC07F6945F3030D5C0E4C89F)

If the value of **size** is the model output size, you are advised to set the size of the ION memory to ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/7N3pYERSRsS2GL9n1MXZnw/en-us_formulaimage_0000002496568524.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062125Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8474633FA3A8A333AF27D675CA444AEF4463430E93B3D072E4D353F1ABE497D3) for the output tensor.
