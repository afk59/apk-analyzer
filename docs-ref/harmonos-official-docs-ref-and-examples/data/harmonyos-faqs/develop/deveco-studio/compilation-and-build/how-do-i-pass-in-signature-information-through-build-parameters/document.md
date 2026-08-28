# How do I pass in signature information through build parameters?

For details about how to pass in signature information through build parameters, see [Preparing Files to Apply for Signature](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-command-line-building-app#section6103553181714).

To build an application on a pipeline, you can pass in signature parameters through the build command lines and obtain the command line build parameters when customizing a build task. However, you cannot modify the signature configuration through a custom task. To sign during compilation and packing, you can add a custom signing task and call the signing tool, which can replace the original singing process. For details, see [API Usage Examples](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-build-expanding-sample).
