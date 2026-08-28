# What should I do if the PC does not respond during the C++ project compilation?

**Symptom**

When a large C++ project is being compiled, the CPU usage is high, which may cause the computer to freeze and respond slowly.

**Solution**

Try the following method:

Open the **build-profile.json5** file in the module and add the following configuration to the **arguments** parameter. Change the values of **compile** and **link** based on the CPU configuration of the PC. You are advised to set the sum of the values of **compile** and **link** to half of the number of CPU cores. For example, if the CPU has eight cores, set both **compile** and **link** to **2**.

"arguments": "-DCMAKE\_JOB\_POOL\_COMPILE:STRING=compile -DCMAKE\_JOB\_POOL\_LINK:STRING=link -DCMAKE\_JOB\_POOLS:STRING=compile=2;link=2",

After the values of **compile** and **link** are changed, the compilation time may be prolonged.
