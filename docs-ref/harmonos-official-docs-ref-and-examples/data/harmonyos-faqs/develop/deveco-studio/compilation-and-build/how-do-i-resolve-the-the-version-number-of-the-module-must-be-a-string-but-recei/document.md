# How do I resolve the "The version number of the module must be a string, but received a xxx." error?

**Symptom**

The "The version number of the module must be a string, but received a xxx." error is reported during compilation.

**Possible Causes**

The module version configured in the **oh-package.json5** file of the module is not a string.

**Solution**

Open the **oh-package.json5** file located in the module directory and change the value of **version** to a string.
