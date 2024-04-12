#pip install transliterate
from transliterate import translit

def translit_to_eng(s):
    slug = translit(s.lower(), 'ru', reversed=True)
    return slug.replace(' ', '-')

while True:
    s = input("Введите строку: ")
    if not s:
        break
    print("Slug:", translit_to_eng(s))
