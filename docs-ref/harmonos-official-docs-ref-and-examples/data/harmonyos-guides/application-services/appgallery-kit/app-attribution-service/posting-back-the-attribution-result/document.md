# Posting Back the Attribution Result

The app attribution result meeting privacy requirements will be posted back to the developer, the winning distribution platform, and the attribution monitoring platform working with the distribution platform. For details about the postback, please refer to [Posting Back the Attribution Result](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-rest-recive). Distribution platforms, developers, and attribution monitoring platforms must adhere to specified postback requirements when implementing an API.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/gKbu7Cy4SK-BHSmUzrb_qw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062058Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=78E525B05B37CB00A49AE4BC9DF159A5987414D77138BB04F186AA82FBDF7E6B)

The URL for attribution postback should be the same as that entered during attribution role registration.

To ensure information validity, distribution platforms, developers, or attribution monitoring platforms need to perform signature verification (signing algorithm: SHA256withRSA/PSS) on the returned attribution result.

#### Calculation Rule of Signature Verification

1.  Concatenate relevant fields as follows to obtain a character string for signature verification:
    
    ad\_tech\_id + '\\u2063' + campaign\_id + '\\u2063' + source\_id + '\\u2063' + destination\_id + '\\u2063' + trigger\_data + '\\u2063' + nonce + '\\u2063' + timestamp
    
    Optional fields are included only when the postback conditions are met. The signature verification should be performed on the character string obtained through the concatenated fields contained in the received request. For example, when the returned message structure contains only fields **ad\_tech\_id** and **destination\_id**, the character string for signature verification is constructed as follows:
    
    ad\_tech\_id + '\\u2063' + destination\_id + '\\u2063' + nonce + '\\u2063' + timestamp
    
2.  Use the public key provided by the app attribution service to perform signature verification on the character string obtained in step 1. For details about the signature verification method, please refer to [Postback Result Signature Verification Method](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-rest-recive#section114341820105218).
    
    Public key provided by the app attribution service:
    
    \====================public key====================
    MIIBojANBgkqhkiG9w0BAQEFAAOCAY8AMIIBigKCAYEA0IgrEtIR1kVF/ImKIo3/5AxEFZzL156jLn2CilqGQmFByiMlpa2G0dotCK1mj9bdhDJbUPd3Plx1zVX9WoW/L/mg25+ng0iPlcItqhUuTIVi+0N50BHlVKPFWG/vYxCkR1ABU44zHyg2XAmqs2L6nUA9Hjbmwn5WX9JUWFF3RF4ja6GJRDkq0HFQ6ouM8Vpm3ZnnRTCuEzOpUcG+FMYAa9M9coRMMM3w0M/IgbYL4n86tQ6ybicaeadSwJIzXExLL0bSf1tYZ7CWvdK0V2ftLWC7Wmho64/g/AjqXc5d2nq88Cn+Vm48jLW1gibI1sPLjFhcfgRg0EOHD/FeUHLxhGeLc4KZ7hrcaW+IuVaTpHxbxJ9WiIokf6blQSEyPHx4w95IdGYNe/BGFhYaf3AhCe6b62e//0JdaYPKNDUKOpTf60vAhqQeibx4iaRZh8dEAU1m9lD0aR6+0trNCzdsC0iPCRLCXcFJXN2/ZJRug39xuJoSEkCxUsJdcoYknbRxAgMBAAE=
