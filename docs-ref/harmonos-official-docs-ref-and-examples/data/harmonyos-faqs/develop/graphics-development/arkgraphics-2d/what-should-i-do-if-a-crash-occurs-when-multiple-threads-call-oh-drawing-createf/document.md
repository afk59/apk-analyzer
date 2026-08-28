# What should I do if a crash occurs when multiple threads call OH\_Drawing\_CreateFontCollection?

**Symptom**

When calling the **OH\_Drawing\_TypographyCreate** function is called in a multithreaded scenario, the code **handler = OH\_Drawing\_CreateTypographyHandler(typoStyle, OH\_Drawing\_CreateFontCollection())** tends to lead to a crash. However, this problem does not happen when the function is called in a single-threaded context.

**Solution**

This API does not support multithreaded concurrency but can be invoked in asynchronous threads.
