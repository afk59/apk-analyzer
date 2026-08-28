# App Occasionally Exits When a User Attempts to Recognize a Barcode from a Saved Image on the Custom Barcode Scanning UI

**Problem**

When a user taps the gallery icon and selects a saved image for barcode recognition on the custom barcode scanning UI, the app may exit unexpectedly.

**Solution**

The custom UI-based barcode scanning API and the API for recognizing barcodes from a saved image cannot be called concurrently.

When a user taps the gallery icon, call the customScan.[stop](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-customscan-api#section6949611114915) and customScan.[release](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-customscan-api#section1109456134917) APIs to stop and release the camera stream respectively, and then start saved image barcode recognition.
