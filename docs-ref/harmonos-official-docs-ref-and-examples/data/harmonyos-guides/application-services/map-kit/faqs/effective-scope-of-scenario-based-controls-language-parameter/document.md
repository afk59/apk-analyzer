# Effective Scope of Scenario-based Controls' language Parameter

1\. If **language** is not passed, the UI, base map, and reverse geocoding results use the system language.

2\. If **language** is passed, the UI and map use the system language, and the result returned from the cloud uses the language specified by **language**. Language support varies across APIs. When a requested language is not supported by a specific API, the API returns data in English by default.
