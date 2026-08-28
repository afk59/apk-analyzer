# ArkTS Compilation Error Codes

#### 00309001 External File Import Using a Relative Path

**Error Message**

Cannot import files outside of the current module using relative paths. Import statement: XXX. At file: YYY.

**Symptom**

Files outside the current module are not allowed to be imported using relative paths.

**Possible Causes**

The import statement attempts to import a file outside the current module using a relative path.

**Solution**

Ensure that no files outside the current module are imported using relative paths.

#### 00309002 Absolute Path Detected in an import Statement

**Error Message**

Avoid absolute paths in imports. Import statement: XXX. At file: YYY.

**Symptom**

An absolute path is detected in the import statement.

**Possible Causes**

An absolute path is used in the import statement in the specified file.

**Solution**

Check the import statement to ensure that no files are imported using absolute paths.

#### 00309003 Failed to Resolve the import Statement

**Error Message**

Cannot resolve import statement XXX.

**Symptom**

The import statement cannot be resolved.

**Possible Causes**

-   When the case-sensitive check is enabled (that is, the **caseSensitiveCheck** field is set to **true** in the project-level **build-profile.json5** file), the folder being imported only contains **Index.ets** or **Index.ts**, but only folders that include **index.ets** or **index.ts** can be imported.
-   When the case-sensitive check is enabled, the case of the file name specified in the **import** statement does not match the case of the actual file name.

**Solution**

-   Import a specific file instead of a folder. If you need to import a folder, ensure the folder contains **index.ets** or **index.ts** (with lowercase "i").
-   Ensure that the case of the file name specified in the **import** statement matches the case of the actual file name.
