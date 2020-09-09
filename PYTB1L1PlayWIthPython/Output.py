Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 2 + 2
4
>>> 3 * 10
30
>>> 100 - 10
90
>>> 25 / 5
5.0
>>> 10 / 3
3.3333333333333335
>>> 10 // 3
3
>>> print('Mijn naam is William')
Mijn naam is William
>>> naam = 'William'
>>> print(naam)
William
>>> print(naam.upper())
WILLIAM
>>> print(naam[0:2])
Wi
>>> print(naam[::-1])
mailliW
>>> leeftijd = 16
>>> print('Hallo ' + naam + ' ben je al ' + str(leeftijd) + ' jaar?')
Hallo William ben je al 16 jaar?
>>> leeftijd = leeftijd + 1
>>> leeftijd
17
>>> leeftijd-=1
>>> leeftijd
16
>>> if leeftijd < 18:
...     hoelang_tot18jaar = 18 - leeftijd
...     print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
... elif leeftijd > 18:
...     hoelang_al18jaar = leeftijd - 18
...     print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
... else:
...     print('Je bent precies ' + str(leeftijd) + ' jaar')
...
Over 2 jaar wordt je 18
>>> from random import randint
>>> randint(0,1000)
601
>>> willekeurig_getal = randint(0,1000)
>>> willekeurig_getal
915
>>> print('Willekeurig getal tussen 0 en 1000: ' + str(willekeurig_getal))
Willekeurig getal tussen 0 en 1000: 915
>>> from datetime import datetime
>>> datum = datetime.now()
>>> print(datum)
2020-09-09 14:17:20.564249
>>> datum.strftime('%A %d %B %Y')
'Wednesday 09 September 2020'
>>> import locale
>>> locale.setlocale(locale.LC_TIME, 'nl_NL')
'nl_NL'
>>> datum.strftime('%A %d %B %Y')
'woensdag 09 september 2020'
>>> locale.setlocale(locale.LC_TIME, 'it_IT')
'it_IT'
>>> datum.strftime('%A %d %B %Y')
'mercoledì 09 settembre 2020'
>>>
>>> Save as = output.py
  File "<stdin>", line 1
    Save as = output.py
         ^
SyntaxError: invalid syntax
>>> Save output.py
  File "<stdin>", line 1
    Save output.py
         ^
SyntaxError: invalid syntax
>>> save
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'save' is not defined
>>> datum.strftime('%A %d %B %Y')
'mercoledì 09 settembre 2020'
>>> datum.strftime('%A %d %B %Y')
'mercoledì 09 settembre 2020'
>>> help
Type help() for interactive help, or help(object) for help about object.
>>> help(save)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'save' is not defined
>>> help()

Welcome to Python 3.8's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.8/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> save
No Python documentation found for 'save'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help>