# Sorting by Indexes

#### Use Cases

When there are many options in a list, users need to slide the window to search for the target option. Sorting by indexes is here to help them quickly find the target option by way of creating an index for each option. It is actually a kind of labeling. For example, labels A, B, C, and D on the right of the contact page correspond to the initial letters of contact names. If you want to find John, clicking J will direct you to a list of names starting with J. Such labels are called indexes, which help to quickly navigate to the corresponding range and find the target option.

#### How to Develop

For details about how to use related APIs, see [IndexUtil](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-i18n#indexutil8).

1.  Import the related modules.
    
    import { i18n } from '@kit.LocalizationKit';
    
2.  Obtain the index list and index values.
    
    // Create indexes in a single language.
    let indexUtil: i18n.IndexUtil = i18n.getInstance('zh-CN');
    let indexList = indexUtil.getIndexList(); // indexList = \['…', 'A', 'B', 'C', ... 'X', 'Y', 'Z', '…'\]
    
    // Create indexes in multiple languages.
    indexUtil.addLocale('ru-RU');
    // indexList = \['...', 'A', 'B', 'C', ... 'X', 'Y', 'Z', '...', 'А', 'Б', 'В', ... 'Э', 'Ю', 'Я', '...'\]
    indexList = indexUtil.getIndexList();
    
    // Obtain the index of the string.
    let index = indexUtil.getIndex('Hello'); // index = 'N'
