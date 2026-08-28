# What is the certificate verification logic of the HTTP module?

When the HTTP module performs certificate verification, it uses system CA certificates for one-way authentication by default. When developers set the parameter **caPath**, the specified CA certificate is preferentially used for authentication. If the authentication fails, the default CA certificate is used for authentication. Either of them passes the authentication, the certificate verification is successful.
