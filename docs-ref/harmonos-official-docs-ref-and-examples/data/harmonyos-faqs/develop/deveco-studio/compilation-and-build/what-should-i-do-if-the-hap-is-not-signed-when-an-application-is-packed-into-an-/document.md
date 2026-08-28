# What should I do if the HAP is not signed when an application is packed into an .app file?

During application release, AppGallery will unpack and re-sign the application package. The application can be released after being signed. After the application signature is verified, AppGallery decompresses the package to obtain all HAPs and then signs the HAPs. Therefore, the application does not need to be signed in DevEco Studio.
