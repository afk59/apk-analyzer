# How do I use regular expressions?

Use new **RegExp()** to define a regular expression.

const reg = new RegExp('ba');

Then, use the **test()** method to check whether a string matches. If the string contains matched value, **true** is returned. Otherwise, **false** is returned.

const res = reg.test('bar');
console.info('result', res);
