# How do I unify HSP version numbers?

**Symptom**

In a development model where multiple teams work on separate modules, it's challenging to maintain consistent HSP version numbers across teams. If one team updates their version number, all other teams need to update and repackage, regardless of whether they change the code or not.

**Solution**

When an HSP is installed with the host HAP, the verification is strict, which requires matching bundle names, version numbers, SDK version numbers, and release types. Use the packing tool's version normalization command ([versionNormalize](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/packing-tool#versionnormalize-command)) to standardize the versions of multiple HAPs and HSPs.

Example:

java -jar path\\app\_packing\_tool.jar --mode versionNormalize --input-list 1.hap,2.hsp --version-code 1000001 --version-name 1.0.1 --out-path path\\out\\
