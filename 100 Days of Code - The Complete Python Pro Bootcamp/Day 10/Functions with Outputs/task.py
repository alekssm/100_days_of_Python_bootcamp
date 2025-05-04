import re

def titlecase(text):
    return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
                  lambda mo: mo.group(0).capitalize(),
                  text)



def format_name(f_name, l_name):
    first_name = titlecase(f_name)
    last_name = titlecase(l_name)

print(2000 % 400)