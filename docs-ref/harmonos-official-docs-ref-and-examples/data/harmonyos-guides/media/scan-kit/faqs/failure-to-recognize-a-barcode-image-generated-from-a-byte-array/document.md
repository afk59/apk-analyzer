# Failure to Recognize a Barcode Image Generated from a Byte Array

**Problem**

When Scan Kit scans a barcode image generated from a byte array, the recognized content is garbled characters and cannot be decoded.

**Solution**

If the content that Scan Kit recognizes from a barcode image generated from a byte array is garbled characters, a dedicated decoder is required to decode the data. Such cases include barcode recognition of subway turnstiles.
