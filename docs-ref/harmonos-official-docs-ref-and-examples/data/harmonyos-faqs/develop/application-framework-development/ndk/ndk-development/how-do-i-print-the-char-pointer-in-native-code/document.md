# How do I print the char pointer in native code?

You can print the char pointer after importing the HiLog library. When printing it, add {public}.

OH\_LOG\_INFO(LOG\_APP, "%{public}s," path); // In this case, the char pointer can be printed.

OH\_LOG\_INFO(LOG\_APP, "%s," path); // In this case, the char pointer cannot be printed.

Sample code:

char \*path = "abc";
OH\_LOG\_INFO(LOG\_APP, "path: %{public}s", path);
