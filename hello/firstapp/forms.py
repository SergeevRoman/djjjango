from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label="Имя пользователя", max_length = 5, min_length= 2, help_text = "не менее 2 символов и не более 5" )
    comment = forms.CharField(label="Комментарий", widget = forms.Textarea)
    age = forms.IntegerField(label="Возраст пользователя", help_text = 'вспомогательный текст')
    basket = forms.BooleanField(label="Пользователь клиент", required=False, help_text = 'вспомогательный текст')
    choose = forms.NullBooleanField(label="Пользователь является зарплатником?", help_text = 'вспомогательный текст')
    email = forms.EmailField(label = "Электронная Почта", initial = "email@domen.com", disabled = True, help_text = 'вспомогательный текст')
    ip_address = forms.GenericIPAddressField(label = "IP адрес", help_text = 'вспомогательный текст')
    reg_text = forms.RegexField(label="Текст", regex = "^[0-9]$", max_length = 5, help_text = 'вспомогательный текст')
    slug_text = forms.SlugField(label="Введите текст", help_text = 'вспомогательный текст')
    url_text = forms.URLField(label="Введите URL", help_text="Например http://www.google.com")
    uuid_text = forms.UUIDField(label="Введите UUID", help_text = 'вспомогательный текст')
    combo_text = forms.ComboField(label="Введите URL", fields=[forms.URLField(), forms.CharField(max_length=5)])
    file_path = forms.FilePathField(label="Выберите файл", path="C:/Users/sergeevra/Downloads/QAGuru/", recursive=True)
    file = forms.FileField(label="Файл")
    image = forms.ImageField(label='Изображение')
    date = forms.DateField(label='Введите дату')
    time = forms.DateField(label='Введите время')
    date_time = forms.DateTimeField(label='Введите дату и время')
    time_data = forms.DurationField(label='Введите промежуток времени')
    DateTime = forms.SplitDateTimeField(label='Введите дату и время')
    dec_digit = forms.DecimalField(label='Введите десятичное число', max_value = 100, decimal_places=3)
    float_num = forms.FloatField(label='Введите число', help_text = 'Введите число с плавающей запятой')
    ling = forms.ChoiceField(label='Выберите язык', choices = ((1, "Английский"), (2, "Немецкий"), (3, "Французский")))
    city = forms.TypedChoiceField(label='Выберите город', empty_value=None, choices = ((1, "Москва"), (2, "Воронеж"), (3, "Сургут")))
    country = forms.MultipleChoiceField(label='Выберите страны', choices=((1,"Англия"),(2,"Германия"),(3,"Испания"),(4,"Турция")))
    multi_city = forms.TypedMultipleChoiceField(label='Выберите города', empty_value=None, choices=((1, "Москва"), (2, "Воронеж"), (3, "Сургут"), (4, "Орел")))
    field_order=["age", "name"] # задает порядок отобрадения полей на форме
    #страница 224
class NameForm(forms.Form):
    name = forms.CharField(label="Имя пользователя", max_length=5, min_length=2,
                           help_text="не менее 2 символов и не более 5")