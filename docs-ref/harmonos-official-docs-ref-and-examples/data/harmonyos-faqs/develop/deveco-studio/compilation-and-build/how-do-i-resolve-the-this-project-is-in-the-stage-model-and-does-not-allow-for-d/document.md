# How do I resolve the "This project is in the stage model and does not allow for dependencies of modules in the FA model." error?

**Symptom**

The "This project is in the stage model and does not allow for dependencies of modules in the FA model." error is reported during compilation.

**Possible Causes**

In the **build-profile.json5** file of the project developed in the stage model, the value of the **srcPath** field contains a reference to a project module developed in the FA model.

**Solution**

In the **build-profile.json5** file located in the project root directory, identify and remove any references to project modules developed in the FA model.
