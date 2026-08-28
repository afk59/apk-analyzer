# How do I resolve the "Cannot add xxxx items to index" error?

**Symptom**

The error message "Cannot add xxxx items to index" is displayed during compilation.

**Possible Causes**

There is a function within the compiled file that contains a large number of object literals, array literals, and strings, causing the number of items to exceed the limit (65536).

**Solution**

Check the relevant files and split the functions that have the aforementioned causes.
