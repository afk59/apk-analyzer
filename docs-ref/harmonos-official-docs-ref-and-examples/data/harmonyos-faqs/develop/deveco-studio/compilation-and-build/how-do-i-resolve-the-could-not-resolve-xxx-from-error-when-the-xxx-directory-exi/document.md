# How do I resolve the "Could not resolve 'xxx' from" error when the 'xxx' directory exists?

**Symptom**

The error message "Could not resolve '_xxx_' from" is displayed during compilation, even though the _xxx_ directory is present and contains an **Index** file.

**Possible Causes**

When referencing a directory, the compiler automatically concatenates a lowercase **index** file, but the directory contains an uppercase **Index** file. During compilation in a case-sensitive environment, the **index** file cannot be found, resulting in an error.

**Solution**

When referencing a directory, explicitly specify the reference to the **Index** file in the directory, for example, **xxx/Index**.
