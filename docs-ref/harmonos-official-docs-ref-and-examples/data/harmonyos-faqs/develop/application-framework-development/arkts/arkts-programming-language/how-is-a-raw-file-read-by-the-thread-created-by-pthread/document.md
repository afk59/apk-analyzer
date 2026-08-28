# How is a raw file read by the thread created by pthread?

The raw file can be read by a thread-safe function:

1.  Obtain and save a resource file object in the UI main thread.
2.  Create a thread-safe function.
3.  Call the thread-safe function in a non-main UI thread.
4.  Read the file resources in **rawfile** via the thread-safe function.
