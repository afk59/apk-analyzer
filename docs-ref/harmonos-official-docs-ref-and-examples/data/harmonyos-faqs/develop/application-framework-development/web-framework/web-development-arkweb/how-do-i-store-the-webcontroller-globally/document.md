# How do I store the WebController globally?

**Symptom**

Multiple **WebController** objects need to be stored globally, but it is failed to save the map data to the AppStorage.

**Solution**

Currently, AppStorage does not support the data of the map type because the data cannot be serialized by JSON. You can store data of the array type or convert the map type to the string type because the AppStorage can store only data of the string type.
