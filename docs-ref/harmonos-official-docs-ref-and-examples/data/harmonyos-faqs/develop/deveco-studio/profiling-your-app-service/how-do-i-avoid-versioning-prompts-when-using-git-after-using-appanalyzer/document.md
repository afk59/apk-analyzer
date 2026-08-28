# How do I avoid versioning prompts when using git after using AppAnalyzer?

**Symptom**

1.  After performing quality assessment on applications/atomic services using AppAnalyzer, git prompts that versioning is required.
2.  The files referenced in the prompt are located under the **/.appanalyzer** directory in the project root directory.

**Possible Causes**

After AppAnalyzer completes quality assessment, it generates data in the final report. The data is stored under the **/.appanalyzer** directory in the project root directory.

**Solution**

Add the following directories to the .gitignore file:

/.appanalyzer
