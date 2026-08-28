# How do I improve the code obfuscation rate?

**Symptom**

How do I ensure the closed-source security of closed-source libraries?

Currently, closed-source libraries can only implement basic field obfuscation, with an obfuscation rate of lower than 20%. The actual logic cannot be obfuscated. In contrast, the code obfuscation effect after packaging using Webpack is obvious. The internal logic cannot be viewed even after formatting. There is a huge gap between our tool and Webpack in this regard.

If there is a plan, what are the details in the plan? How do I ensure the closed-source security of banking and financial SDKs?

**Solution**

The possible causes for a lower obfuscation rate are as follows:

1\. Options such as attribute obfuscation, exported content obfuscation, and top-level scope obfuscation are not enabled.

2\. If the preceding main obfuscation options have been enabled but the obfuscation rate is still low, the defined variables, attribute names, function names, or method names may overlap with the names in the system whitelist. As a result, these names are not obfuscated. You are advised to add a prefix or suffix to the name to avoid the system whitelist. The cache path of the system whitelist is **build/cache/{...}/release/obfuscation/systemApiCache.json**.
