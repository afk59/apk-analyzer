# How do I resolve the "The name of the 'xxx' module must be a string, but received a value of type 'xxx'." error?

**Symptom**

The "The name of the 'xxx' module must be a string, but received a value of type 'xxx'." error is reported during compilation.

**Possible Causes**

The module name configured in the **oh-package.json5** file of the module is not a string.

**Solution**

Open the **oh-package.json5** file located in the module directory and change the value of **name** to a string.
