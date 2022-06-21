from typing import List, Dict


class Int_input(object):

    def __new__(cls, quest_text, error_text: str = 'Вы ввели некорректное число'):
        return cls.int_input(quest_text, error_text)

    @staticmethod
    def int_input(quest_text, error_text):
        while True:
            a = input(quest_text)
            try:
                return int(a)
            except ValueError:
                print(error_text)


class Str_input(object):
    def __new__(cls, quest_text):
        return cls.str_input(quest_text=quest_text)

    @staticmethod
    def str_input(quest_text):
        a = input(quest_text)
        return a


class Variable_input(object):
    def __new__(cls, options: List[str],
                error_text: str = 'Пожалуйста, выберите вариант из списка!'):
        return cls.variable_input(options, error_text)

    @staticmethod
    def variable_input(options, error_text):
        while True:
            a = input(f'Введите один из вариантов {", ".join(options)}: ')
            if a in options:
                return a
            else:
                print(error_text)


class All_in_one(object):
    def __new__(cls, text, method_list: Dict):
        print(text)
        return cls.all_in_one(method_list)

    @staticmethod
    def all_in_one(method_list):
        a = []
        for i in method_list:
            res = i(method_list[i])
            a.append(res)
        return tuple(a)


class Range_input(Int_input):
    def __new__(cls, min_int, max_int, error_text):
        return cls.range_input(min_int, max_int, error_text)

    @staticmethod
    def range_input(min_int, max_int, error_text):
        check = True
        while check:
            a = Int_input(quest_text=f'Введите число из диапазона от {min_int} до {max_int}: ')
            if min_int <= a <= max_int:
                print(a)
                return a
            else:
                print(error_text)


class DictCreator(object):
    def __new__(cls, tries, quest_text1, quest_text2):
        return cls.dictcreator(tries, quest_text1, quest_text2)

    @staticmethod
    def dictcreator(tries, quest_text1, quest_text2):
        custom_dict = {}
        for i in range(tries):
            a = input(quest_text1)
            b = input(quest_text2)
            custom_dict[a] = b
        return custom_dict
