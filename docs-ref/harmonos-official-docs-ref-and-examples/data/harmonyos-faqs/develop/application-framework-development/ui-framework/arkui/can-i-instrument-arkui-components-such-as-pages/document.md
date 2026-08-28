# Can I instrument ArkUI components such as pages?

ArkUI-related APIs are converted during compilation. The objects or methods used in the developing state may not exist at runtime. Since ArkUI components are converted into different forms during compilation, the original declaration cannot be located during running. Therefore, the instrumentation and replacement APIs provided by the **Aspect** class are not applicable to ArkUI components.
