# HMAC Overview and Algorithm Specifications

A message authentication code (MAC) is used for verifying the authenticity and integrity of information transmitted or stored on unreliable media. A hash-based message authentication code (HMAC) is a MAC involving a cryptographic hash function and a secret cryptographic key. The HMAC can be used with any cryptographic hash function, such as SHA-256 and SM3. HUKS supports the use of HMAC with mainstream message digest (MD) algorithms.

#### Supported Algorithms

The following table lists the HMAC specifications supported by the system.

| MD Algorithm | Supported Key Length (Bit) | API Version |
| :-- | :-- | :-- |
| SHA-256 | 192 to 1024 | 8+ |
| SHA-384, SHA-512 | 256 to 1024 | 8+ |
| SM3 | 80 - 1024 | 8+ |
