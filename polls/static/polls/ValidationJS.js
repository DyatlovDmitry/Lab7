function ValidMail() {
    var regex = /^[\w-\.]+@[\w-]+\.[a-z]{2,4}$/i;
    var email = document.getElementById('email').value;
    var valid = regex.test(email);
    if (valid) output = 'Адрес эл. почты введен правильно!';
    else output = 'Адрес электронной почты введен неправильно!';
    document.getElementById('message').innerHTML = output;
    return valid;
}
function ValidName(){
    var name = document.getElementById('name').value;
    var regex=/[A-Z][A-Za-z]+/;
    var valid = regex.test(name);
    if (valid) output = 'Верный формат имени!';
    else output = 'Неверный формат имени!';
    document.getElementById('message').innerHTML = document.getElementById('message').innerHTML+'<br />'+output;
    return valid;
}
