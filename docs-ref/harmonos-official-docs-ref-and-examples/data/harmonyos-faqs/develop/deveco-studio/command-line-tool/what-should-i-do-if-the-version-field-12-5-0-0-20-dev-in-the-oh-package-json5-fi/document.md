# What should I do if "The version field: 12.5.0.0-20-dev in the oh-package.json5 file does not satisfy the SemVer specification" is displayed when ohpm is used to release a HAR?

**Symptom**

When the HAR of the player library constructed online is published using ohpm, an error message is displayed to indicate that the version field in the oh-package.json5 file does not comply with the SemVer specification.

**Solution**

Make sure the version number complies with the SemVer specification. Currently, only the three-segment version format like 1.0.0-XXXX is supported. For details, see [Semantic Versioning Specification (SemVer)](https://semver.org/#semantic-versioning-specification-semver).
