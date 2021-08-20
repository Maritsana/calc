print("Здравствуйте!")
print("Укажите Ваш пол:")
gender = input()
man = ['М', 'м', 'Муж', 'муж', 'Мужской', 'мужской', 'Мужчина', 'мужчина', 'M', 'm', 'Man', 'man', 'Male', 'male']
woman = ['Ж', 'ж', 'Жен', 'жен', 'Женский', 'женский', 'Женщина', 'женщина', 'W', 'w', 'Woman', 'woman', 'Female', 'female', 'Wife', 'wife', 'Feminine', 'feminine']
if gender in man:
    weight = float(input("Ваш вес: "))
    height = float(input("Ваш рост: "))
    age = int(input("Ваш возраст: "))
    calories = (10*weight+6.25*height-5*age+5)
    print('Вам нужно потреблять', int(calories), 'калорий!')
elif gender in woman:
    weight = float(input("Ваш вес: "))
    height = float(input("Ваш рост: "))
    age = int(input("Ваш возраст: "))
    calories = (10*weight+6.25*height-5*age-161)
    print('Вам нужно потреблять', int(calories), 'калорий!')
else:
    print('Введите корректные данные!')