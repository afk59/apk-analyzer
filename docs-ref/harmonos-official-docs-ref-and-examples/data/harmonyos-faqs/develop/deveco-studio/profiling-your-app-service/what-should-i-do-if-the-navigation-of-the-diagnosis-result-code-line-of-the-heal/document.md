# What should I do if the navigation of the diagnosis result code line of the health check tool is inaccurate?

1.  Ensure that the version of the application to be checked is the same as that of the current project.
2.  Cleaning the project to delete the sourceMaps file before importing the check report, coupled with failure in compilation and build during the import process, will ultimately lead to inaccuracies in source code navigation. You need to resolve the compilation failure and import the report again.
3.  You are advised to use the debug mode to compile and generate an installation package for detection.
