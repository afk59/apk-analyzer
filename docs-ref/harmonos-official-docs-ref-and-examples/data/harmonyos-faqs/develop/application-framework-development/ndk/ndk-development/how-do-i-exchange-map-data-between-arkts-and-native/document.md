# How do I exchange map data between ArkTS and native?

Currently, there is no API for converting **map** data between ArkTS and native. To implement interaction of **map** (2D array) data, you need to read data from **map** and pass the obtained data to the native side for reassembly.

Sample code:

Declare **HashMap** in ArkTS, obtain data, and pass the obtained data to the native side.

let hashmap: HashMap<string, number> = new HashMap()
hashmap.set("Abc", 123)
hashmap.set("Bcd", 234)
hashmap.set("Cde", 345)
for (let key of hashmap.keys()) {
  testNapi.mapDemo(key, hashmap.get(key))
  console.info(\`key is ${key}, value is ${hashmap.get(key)}\`)
}

Obtain data and reassemble the **map** data.

#define LOG\_DOMAIN 0x3200 // Global domain macro, identifying the business domain
#define LOG\_TAG "MY\_TAG"  // Global tag macro, identifying module log tag 
#include "NativeMap.h"
#include "hilog/log.h"
#include <map>
#include <string>
std::map<std::string, int> testmap;
napi\_value NativeMap::MapDemo(napi\_env env, napi\_callback\_info info) {
    size\_t requireArgc = 2;
    size\_t argc = 2;
    napi\_value args\[2\] = {nullptr};

    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    char str1\[1024\];
    size\_t str1\_len;
    napi\_get\_value\_string\_utf8(env, args\[0\], str1, 100, &str1\_len);
    int num;
    napi\_get\_value\_int32(env, args\[1\], &num);
    testmap.insert(std::make\_pair(str1, num));
    for(auto e: testmap){
        OH\_LOG\_ERROR(LOG\_APP, "key is: %{public}s, value is  %{public}d", (e.first).c\_str(), e.second);
    }
    
    return nullptr;
}
