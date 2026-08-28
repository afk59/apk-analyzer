# How do I release an ArkTS object on the native side?

Use the **napi\_wrap** API. If the value of the last parameter **result** is not **nullptr** in **napi\_wrap**, use **napi\_remove\_wrap** at a proper time to delete the created **napi\_ref** object.

// Usage 1: Napi\_wrap does not need to receive the created napi\_ref, and the last parameter is passed as nullptr. The created napi\_ref is a weak reference, managed by the system, and does not require manual release by the user
napi\_wrap(env, jsobject, nativeObject, cb, nullptr, nullptr);

// Usage 2: napi\_wrap needs to receive the created napi\_ref, the last parameter is not null ptr, and the returned napi\_ref is a strong reference that needs to be manually released by the user, otherwise it will cause memory leakage
napi\_ref result;
napi\_wrap(env, jsobject, nativeObject, cb, nullptr, &result);
// When jsobject and result are no longer used in the future, promptly call napi\_remove\_wrap to release result
void\*\* result1;
napi\_remove\_wrap(env, jsobject, result1);
