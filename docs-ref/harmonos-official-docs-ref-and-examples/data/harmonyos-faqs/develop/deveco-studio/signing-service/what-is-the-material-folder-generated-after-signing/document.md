# What is the material folder generated after signing?

**Question**

When .p12 and .csr files are generated using the **Generate Key and CSR** feature in DevEco Studio, a **material** folder is also created. What is this **material** folder used for?

**Answer**

This **material** folder is used to store auxiliary files required for signing the application, which encrypt the user's password. The .cer and .p12 files are the actual signing materials required by the signing tools. Though the **material** folder and the signing materials are not in a one-to-one mapping, the files in the folder are important for the signing process. They may be referenced during signing. Therefore, it is recommended that you keep the folder to ensure the signing process goes smoothly.
