from programminglanguage import ProgrammingLanguage


ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
print(ruby)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
print(python)
vb = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(vb)

language_list = [ruby, python, vb]
print("The dynamically typed languages are:")
for each_lang in language_list:
    if each_lang.is_dynamic():
        print(each_lang.name)