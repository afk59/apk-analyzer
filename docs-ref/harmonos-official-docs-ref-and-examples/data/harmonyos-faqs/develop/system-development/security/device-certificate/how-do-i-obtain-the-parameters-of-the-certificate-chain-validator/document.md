# How do I obtain the parameters of the certificate chain validator?

You can use [getSubjectName](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-cert#getsubjectname) and [getPublicKey](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-cert#getpublickey) to obtain **CASubject** and **CAPubKey**, and then pass their values to **CertChainValidationParameters**.
