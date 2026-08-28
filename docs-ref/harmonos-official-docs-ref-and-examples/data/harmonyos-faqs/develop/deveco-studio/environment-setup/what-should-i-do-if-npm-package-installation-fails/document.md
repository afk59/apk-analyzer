# What should I do if npm package installation fails?

**Symptom**

Running the **npm install** command to install an npm package returns an error message.

**Solution**

Run the following command to set the URL of the npm repository and then try the installation again:

npm config set @ohos:registry=https://repo.harmonyos.com/npm/
