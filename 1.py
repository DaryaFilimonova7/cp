name = input("Введите имя студента: ")
surname = input("Введите фамилию студента: ")
year = int(input("Введите год рождения студента: "))
print(str(name) + "_" + str(surname) + "_" + str(year))
name,surname = surname,name
year = int(year+60)
print(str(name) + "_" + str(surname) + "_" + str(year))