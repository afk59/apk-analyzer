# FAQs

#### How do I prepare data and modify the configuration file if a model has multiple inputs?

If the model defines multiple inputs, you need to prepare a calibration set in image or binary format for each input node. If the inputs are specific to nodes, the binary format is recommended to prevent unexpected behavior caused by different image reading sequences. When modifying the quantization configuration file, the number of preprocessing parameters to be defined must be the same as that of input nodes, and the sequence of preprocessing parameters must be the same as the **input\_shape** sequence specified when running the tool.

#### What should I do if the message "Unsupported image format! Unsupported image: xxx" is displayed?

This is because the image calibration set contains an image of an unsupported format. You only need to delete the image. Pay attention to the hidden files in the folder.
