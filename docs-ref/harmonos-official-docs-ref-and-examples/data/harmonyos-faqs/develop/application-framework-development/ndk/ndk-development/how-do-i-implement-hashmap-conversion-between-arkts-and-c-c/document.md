# How do I implement HashMap conversion between ArkTS and C/C++?

**Question**

How do I convert the HashMap in ArkTS to a value in C/C++?

**Solution**

-   Method 1: pass an array.
    
    Obtain the key and value of HashMap as arrays, pass the two arrays to C/C++, and assemble them into a map.
    
    Pass arrays from ArkTS.
    
    let hashMap: HashMap<string, number> = new HashMap();
    hashMap.set("Abc", 123);
    hashMap.set("Bcd", 234);
    hashMap.set("Cde", 345);
    
    let keysArray: Array<string> = Array.from(hashMap.keys());
    let valuesArray: Array<number> = Array.from(hashMap.values());
    testNapi.tsPutMap(keysArray, valuesArray, hashMap.length);
    
    Assemble the map in C/C++.
    
    // Convert value to string and return
    std::string HashMap::value2String(napi\_env env, napi\_value value) {
        size\_t stringSize = 0;
        napi\_get\_value\_string\_utf8(env, value, nullptr, 0, &stringSize); // Obtain the string length.
        std::string valueString;
        valueString.resize(stringSize + 1);
        napi\_get\_value\_string\_utf8(env, value, &valueString\[0\], stringSize + 1, &stringSize); // Convert the value into a string based on the length.
        return valueString;
    }
    napi\_value HashMap::TsPutMap(napi\_env env, napi\_callback\_info info) {
        std::map<std::string, int> myMap;
        size\_t argc = 3;
        napi\_value args\[3\] = {nullptr};
        napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
        napi\_value mapKey = args\[0\]; // key
        napi\_value mapVal = args\[1\]; // value
        napi\_value mapNum = args\[2\]; // length
    
    
        uint32\_t mapCNum = 0;
        napi\_get\_value\_uint32(env, mapNum, &mapCNum);
        for (uint32\_t i = 0; i < mapCNum; i++) {
            napi\_value keyNIndex, valNIndex;
            napi\_get\_element(env, mapKey, i, &keyNIndex);
            napi\_get\_element(env, mapVal, i, &valNIndex);
            std::string keyIndex = value2String(env, keyNIndex);
            int valIndex = 0;
            napi\_get\_value\_int32(env, valNIndex, &valIndex);
            myMap\[keyIndex\] = valIndex;
            OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0x0000, "Pure", "%{public}s %{public}d", keyIndex.c\_str(), myMap\[keyIndex\]);
        }
        return nullptr;
    }
    
-   Method 2: Pass JSON.
    
    Convert **HashMap** into JSON data and pass it to C/C++. Then, deserialize the JSON data to Map.
    
    Convert HashMap to JSON format in ArkTS.
    
    1.  **JSON.stringify** does not support **HashMap** operations. You need to convert it to a record first.
        
        map2rec(map: HashMap<string, ESObject>): Record<string, ESObject> {
          // Map to Record
          let Rec: Record<string, ESObject> = {}
          map.forEach((value: ESObject, key: string) => {
            if (value instanceof HashMap) {
              //Value may be HashMap
              let vRec: Record<string, ESObject> = this.map2rec(value)
              value = vRec
            }
            Rec\[key\] = value
          })
          return Rec
        }
        
    2.  Use **JSON.stringify** to serialize the data.
        
        let myRec: Record<string, ESObject> = this.map2rec(hashMap);
        let str: string = JSON.stringify(myRec);
        testNapi.mapJson(str);
        
    
    Deserialize the JSON data in C/C++.
    
    C++ does not provide the API for deserialization. You need to use a third-party library. This demo uses the lycium tool to compile the third-party JSON library.
    
    napi\_value HashMap::MapJson(napi\_env env, napi\_callback\_info info) {
    
        size\_t argc = 1;
        napi\_value args\[1\] = {nullptr};
        napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    
        std::string jsonStr = value2String(env, args\[0\]);
    
        std::map<std::string, int> myMap = nlohmann::json::parse(jsonStr.c\_str());
    
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0x0000, "Pure", "%{public}d %{public}d %{public}d", myMap\["Abc"\], myMap\["Bcd"\],
                     myMap\["Cde"\]);
    
        return nullptr;
    }
