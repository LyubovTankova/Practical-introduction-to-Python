## 1. Создайте модуль и напишите в нём функцию, которая получает 
## на вход дату в формате DD.MM.YYYY и возвращает истину, если дата может существовать или ложь, 
## если такая дата невозможна. Для простоты договоримся, что год может быть в диапазоне [1, 9999]. 
## И весь период действует григорианский календарь. 
## Проверку года на високосность вынести в отдельную защищённую функцию.
## 2. В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

from sys import argv


_FIRST_DAY = 1
_LAST_DAY = 31
_FIRST_MONTH = 1
_LAST_MONTH = 12
_FIRST_YEAR = 1
_LAST_YEAR = 9999


def date_calendar(date: str) -> bool:
    day, month, year = list(map(int, date.split('.')))
    return ((_LAST_DAY >= day >= _FIRST_DAY) and 
            (_LAST_MONTH >= month >= _FIRST_MONTH)   and 
            (_LAST_YEAR >= year >= _FIRST_YEAR))


def _intercalary_year(date: str) -> bool:
    day, month, year = list(map(int, date.split('.')))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:    
        return False    


if __name__ == '__main__':
    print(argv)
    print(date_calendar(argv[1]))
    print(_intercalary_year(argv[1]))  