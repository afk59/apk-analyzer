# How do I resolve the "File 'string.json' is missing the required property 'string'." error?

**Symptom**

The "File 'string.json' is missing the required property 'string'." error is reported during compilation.

**Possible Causes**

The **string.json** file of the HSP or HAR on which the HAP module depends does not contain the required **string** property.

**Solution**

Make sure the **string.json** file of the relevant HSP or HAR contains the required **string** property.

**Example**

{
  "string": \[
    {
      "name": "shared\_desc",
      "value": "description"
    }
  \]
}
