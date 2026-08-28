# How do I define an object of an unknown type?

You can use the Record type, with as many type parameters as there are variables, as shown in the following example:

const asd: Record<string, number | string> = {
  'name': 'xc',
  'age': 29
}
