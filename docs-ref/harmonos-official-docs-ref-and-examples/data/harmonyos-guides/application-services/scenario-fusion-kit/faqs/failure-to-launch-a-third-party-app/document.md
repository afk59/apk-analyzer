# Failure to Launch a Third-Party App

**Problem**

Error log example:

startAbility failed, code is 16000018, message is The application is not allow jumping to other applications when api version is above 11.

**Solution**

Run the following command to enable app launch.

hdc shell param set persist.sys.abilityms.support.start\_other\_app true
