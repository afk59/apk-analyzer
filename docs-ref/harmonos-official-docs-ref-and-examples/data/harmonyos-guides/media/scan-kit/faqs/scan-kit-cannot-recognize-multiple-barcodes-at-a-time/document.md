# Scan Kit Cannot Recognize Multiple Barcodes at a Time

**Problem**

When multiple barcodes are scanned in real time, only one barcode is recognized.

**Solution**

1.  Ensure that the **enableMultiMode** parameter in [ScanOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-scanbarcode-api#section1285191073117) is set to **true**.
2.  Verify that corresponding barcode types have been set in **scanTypes** of **ScanOptions**.
3.  Verify that Scan Kit supports these barcode types.
4.  Currently, at most 4 barcodes can be recognized when multiple barcodes are scanned in real time.
5.  If the fault persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei will get back to you as soon as possible.
