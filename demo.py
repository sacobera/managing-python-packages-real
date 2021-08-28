#example of python package importing
from babel.numbers import format_number

number = 123456

print("In the Netherlands we write", 
format_numer(number, locale='en_US'),
"as",
format_number(number, locale="n1_NL")
)