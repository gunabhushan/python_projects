from translate import Translator

translator= Translator(to_lang="ja")

try:
    with open('text.txt',mode='r') as my_text:
        text = my_text.read()
        translation = translator.translate(text)
        print(translation)
        with open('text2.txt', mode='w',encoding='utf-8') as my_text2:
            a = translation
            my_text2.write(a)
except FileNotFoundError as e:
    print('nani iithand yoo')