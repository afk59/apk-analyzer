# How do I set the TextInput component to accept only certain characters?

Set the **inputFilter** attribute of the **TextInput** component to a regular expression to validate the characters being entered. If the validation fails, the input will be considered invalid. The code snippet is as follows:

@Entry
@Component
struct Index {
  controller: TextInputController = new TextInputController();

  build() {
    Column() {
      TextInput({ placeholder: 'Please input a password', text: '123456', controller: this.controller })
        .type(InputType.Password)
        .placeholderColor(Color.Gray)
        .inputFilter('\[0-9\]', (val) => { //Only allow the input of characters 0-9, other characters are invalid
          console.error('TextInputExample : ' + val);
          // Invalid input return 0
          return 0;
        })
    }
  }
}
