from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label="Имя пользователя", max_length = 5, min_length= 2, help_text = "не менее 2 символов и не более 5" )
    age = forms.IntegerField(label="Возраст пользователя")
    basket = forms.BooleanField(label="Пользователь клиент", required=False)
    choose = forms.NullBooleanField(label="Пользователь является зарплатником?")
    email = forms.EmailField(label = "Электронная Почта", initial = "email@domen.com", disabled = True)
    ip_address = forms.GenericIPAddressField(label = "IP адрес")
