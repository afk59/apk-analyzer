# What should I do if "ohpm ERROR: JSON5: invalid end of input at 1:1" is displayed?

**Symptom**

The computer is not connected to the network. After DevEco Studio is upgraded to 5.0.1.600, the error message "ohpm ERROR: JSON5: invalid end of input at 1:1" is displayed.

**Solution**

Delete the **oh-package-lock.json5** file in the project directory and run the **ohpm clean**, **ohpm cache clean**, and **ohpm install --all** command.
