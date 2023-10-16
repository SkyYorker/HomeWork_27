from datetime import date

from django.forms import ValidationError

def check_date_for_user(value: date):
    today = date.today()
    age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
    if age < 9:
        raise ValidationError("Вы должны быть старше 9 лет.")
    

def check_email_for_user(value):
    if value == 'rambler.ru':
        raise ValidationError("С этого домена регистрация запрещенна")