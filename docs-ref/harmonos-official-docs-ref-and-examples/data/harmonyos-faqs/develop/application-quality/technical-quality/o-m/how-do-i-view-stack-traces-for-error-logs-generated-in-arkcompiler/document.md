# How do I view stack traces for error logs generated in ArkCompiler?

To view stack traces for exceptions thrown during native code execution, run the following commands:

Enable backtrace:

hdc shell param set persist.ark.properties 0x125c 
hdc shell reboot

Restore defaults:

hdc shell param set persist.ark.properties 0x105c 
hdc shell reboot
