from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label="Имя пользователя", max_length = 5, min_length= 2, help_text = "не менее 2 символов и не более 5" )
    age = forms.IntegerField(label="Возраст пользователя")
    basket = forms.BooleanField(label="Пользователь клиент", required=False)
    choose = forms.NullBooleanField(label="Пользователь является зарплатником?")
    email = forms.EmailField(label = "Электронная Почта", initial = "email@domen.com", disabled = True)
    ip_address = forms.GenericIPAddressField(label = "IP адрес")
    reg_text = forms.RegexField(label="Текст", regex = "^[0-9]$", max_length = 5)
    slug_text = forms.SlugField(label="Введите текст")
    url_text = forms.URLField(label="Введите URL", help_text="Например http://www.google.com")
    uuid_text = forms.UUIDField(label="Введите UUID")
    combo_text = forms.ComboField(label="Введите URL", fields=[forms.URLField(), forms.CharField(max_length=5)])
    file_path = forms.FilePathField(label="Выберите файл", path="C:/Users/sergeevra/Downloads/QAGuru/", recursive=True)