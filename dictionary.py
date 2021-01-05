from fail_fucntions import *
import random
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')

while True:

    def dictionary_test():
        print("добро пожаловать в тест!")
        eng = create_fail("eng.txt")
        rus = create_fail("rus.txt")
        test_type = int(input("1 - тест (рус - англ) 2 - тест (англ - рус)\n:"))
        right = 0
        if test_type == 1:
            for i in range (5):
                first = (random.choice(rus))
                print(first)
                ndx_1 = rus.index(first)
                second = input("введите перевод\n")
                if second in eng:
                    ndx_2 = eng.index(second)
                else:
                    ndx_2 = ndx_1 - 1
                if ndx_2 == ndx_1:
                    right = right + 1
        elif test_type == 2:
            for i in range (5):
                first = (random.choice(eng))
                print(first)
                ndx_1 = eng.index(first)
                second = input("введите перевод\n")
                if second in rus:
                    ndx_2 = rus.index(second)
                else:
                    ndx_2 = ndx_1 - 1
                if ndx_2 == ndx_1:
                    right = right + 1
        else:
            print("такого варианта не существует!")
        if right != 0:
            procent_result = 5 / right * 100
            print(f"у вас - {procent_result} %")
        else:
            print("ни одного правильного ответа")




    def eng_to_rus():
        eng = create_fail("eng.txt")
        rus = create_fail("rus.txt")
        dictionary_to_rus = dict()
        for i in range(len(rus)):
            dictionary_to_rus[eng[i]] = rus[i]
        word = input("какое слово хотите перевести?\n:")
        index_eng = eng.index(word)
        word = rus[index_eng]
        print(word)
        engine.setProperty('voice', 'ru')
        engine.say(word)
        engine.runAndWait()


    def rus_to_eng():
        eng = create_fail("eng.txt")
        rus = create_fail("rus.txt")
        dictionary_to_rus = dict()
        for i in range(len(rus)):
            dictionary_to_rus[rus[i]] = eng[i]
        word = input("какое слово хотите перевести?\n:")
        index_rus = rus.index(word)
        word = eng[index_rus]
        print(word)
        engine.say(word)
        engine.runAndWait()
    def addwords():
        rus = create_fail("rus.txt")
        word = input("какое слово хотите добавить (вводите на русском 1 - ое слово)\n:")
        word_translate = input("Введите его перевод а англ. (проверьте корректность перевода)\n:")
        if word in rus:
            print("такое слово уже есть")
            addwords()
        else:
            save_file("rus.txt", word)
            save_file("eng.txt", word_translate)

    def mistakechecking():
        print("показываем существующие слова с переводом.....\n")
        eng = create_fail("eng.txt")
        rus = create_fail("rus.txt")
        dictionary_to_rus = dict()
        for i in range(len(rus)):
            dictionary_to_rus[rus[i]] = eng[i]
        print(dictionary_to_rus)
        checkword = input("Введите слово которое хотите проверить/добавить...\n:")
        if checkword not in dictionary_to_rus:
            print("такого слова нет!")
            add_or_check = int(input("Хотите ли добавить новое слово или же заново проверить слова?\n1 - добавить\n 2 "
                                     "- проверить заново\n:"))
            if add_or_check == 1:
                addwords()
            elif add_or_check == 2:
                mistakechecking()
            else:
                print("перезагружаемся....\n.....\n....\n...\n..\n.")
        else:
            dictionary_type = int(input("Введите 1 - русский словарь, 2 - английский словарь 3 - для выхода в главное "
                                        "меню\n:"))
            if dictionary_type == 1:
                print(rus)
                correction = input("введите слово, которое хотите исправить\n:")
                if correction in rus:
                    rewrite_file("rus.txt", correction)
                else:
                    print("такого слова нету!")
                    mistakechecking()
            elif dictionary_type == 2:
                print(eng)
                correction = input("введите слово, которое хотите исправить\n:")
                if correction in eng:
                    rewrite_file("eng.txt", correction)
                else:
                    print("такого слова нету!")
                    mistakechecking()

            else:
                print("перезагружаемся......")


    def translation():
        translatechoice = int(input("Добро пожаловать!"
                                    "\n хотите перевести с англ. - рус. введите - '1'"
                                    "\nхотите перевести с рус. - англ. введите - '2'"
                                    "\n для выхода любое другое число\n:"))
        if translatechoice == 1:
            eng_to_rus()
        elif translatechoice == 2:
            rus_to_eng()
        else:
            print("возвращаемся в меню.....\n")


    operationchoice = int(input("Добро пожаловать в программу тестирования и перевода eng-rus rus-eng\n1 - перевод "
                                "слова\n2 - проверка/исправление/добавление слов\n3 - тест на знания слов\n:"))
    if operationchoice == 1:
        translation()
    elif operationchoice == 2:
        mistakechecking()
    elif operationchoice == 3:
        dictionary_test()
    else:
        print("к сожалению под этим символом нет никакой операции\nследите за обновлениями!")



