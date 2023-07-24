import random
import re
import string

class_list = [f"Kelas {char}" for char in string.ascii_uppercase]
course_list = ['PBO', 'Struktur Data', 'Dasar Pemrograman', 'Pemrograman Deklaratif', 'Pemrograman Mobile Lanjut', 'Pemrograman Web Lanjut', 'Pengantar Basis Data']
conditions = ['Izin', 'Sakit']


def slug_generator(n):
    letter = string.ascii_letters
    num = '1234567890'
    raw = num + letter
    return ''.join(random.sample(raw, n))


def check_slug(link: str, link_list: list, n):
    while True:
        if link in link_list:
            link = slug_generator(n)
        else:
            return link


def set_class_name(gen):
    punc = r'[' + string.punctuation + ']'
    name = f"{gen}"
    name = re.sub(punc, '', name)
    class_name = f"{name}"

    class_link = f"{name}".replace(' ', '-')

    return class_name, class_link


def uts_uas_find(models, target, name, link):
    """ models must be class models """
    target = target.upper()
    find = models.objects.filter(class_name__link=link, name=name, classification=target)
    if find:
        return True
    return False
