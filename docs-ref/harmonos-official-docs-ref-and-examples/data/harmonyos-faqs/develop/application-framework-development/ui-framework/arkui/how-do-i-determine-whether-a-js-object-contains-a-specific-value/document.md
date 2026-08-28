# How do I determine whether a JS object contains a specific value?

Use **Object.values(_objectName_).indexOf(_valueToCheck_)**. If **\-1** is returned, the corresponding value is not included. Otherwise, the corresponding value is included.

var res = array.indexOf(val)
