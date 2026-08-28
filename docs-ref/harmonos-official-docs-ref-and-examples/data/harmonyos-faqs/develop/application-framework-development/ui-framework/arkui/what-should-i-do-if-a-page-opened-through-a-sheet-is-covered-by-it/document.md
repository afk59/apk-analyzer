# What should I do if a page opened through a sheet is covered by it?

**Question**

When the **NavPathStack** and **NavDestination** combination solution is used in the routing framework, Page A opens a sheet W via **bindSheet**. Then, in sheet W, clicking a button opens Page B, and at this point, it is found that Page B opens below sheet W. What should I do to ensure that the new page is not covered by the sheet?

**Solution**

By default, the sheet is displayed on the top of the current UIContext, on top of all pages. You can set the [mode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-sheet-transition#sheetmode12) attribute in [SheetOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-sheet-transition#sheetoptions) of the sheet to make the opened page cover the sheet.
