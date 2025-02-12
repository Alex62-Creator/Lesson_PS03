import requests
from bs4 import BeautifulSoup
from translate import Translator


# Создаём функцию, которая будет получать информацию
def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)

        # Создаём объект Soup
        soup = BeautifulSoup(response.content, "html.parser")
        # Получаем слово. text.strip удаляет все пробелы из результата
        english_words = soup.find("div", id="random_word").text.strip()
        # Получаем описание слова
        word_definition = soup.find("div", id="random_word_definition").text.strip()
        # Возвращаем словарь
        return {
            "english_words": english_words,
            "word_definition": word_definition
        }
    # Проверка, которая сообщит об ошибке, но не остановит программу
    except:
        print("Произошла ошибка")

# Создаём функцию, которая будет переводить на русский
def translate_to_rus(text):
    # Создаём объект Translator
    translator = Translator(to_lang="ru")
    # Переводим
    result = translator.translate(text)
    # Возвращаем результат перевода
    return result

# Создаём функцию, которая будет делать саму игру
def word_game():
    print("Добро пожаловать в игру")
    ln = input("Введите 1, если вы хотите играть на русском языке, 0 - на английском: ")
    while True:
        # Получаем слово и его описание в виде словаря
        word_dict = get_english_words()
        # Выделяем слово
        word = word_dict.get("english_words")
        # Выделяем описание
        word_definition = word_dict.get("word_definition")
        # Если надо, переводим на русский
        if ln == '1':
            word = translate_to_rus(word)
            word_definition = translate_to_rus(word_definition)

        # Начинаем игру
        print(f"Значение слова - {word_definition}")
        user = input("Что это за слово? ")
        if user == word:
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {word}")

        # Создаём возможность закончить игру
        play_again = input("Хотите сыграть еще раз? 1-да/0-нет: ")
        if play_again != "1":
            print("Спасибо за игру!")
            break

# Запускаем игру
word_game()
