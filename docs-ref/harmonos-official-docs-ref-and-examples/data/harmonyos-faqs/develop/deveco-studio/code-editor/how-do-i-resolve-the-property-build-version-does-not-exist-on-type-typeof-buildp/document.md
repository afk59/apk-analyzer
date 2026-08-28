# How do I resolve the "Property 'BUILD\_VERSION' does not exist on type 'typeof BuildProfile'" error?

**Symptom**

The following error message is displayed regarding **BuildProfile** during project builds:

Property 'BUILD\_VERSION' does not exist on type 'typeof BuildProfile'

**Solution**

After obtaining the build parameters from the code and generating the **BuildProfile** class file, import the file as follows: **import BuildProfile from '${packageName}/BuildProfile';**
