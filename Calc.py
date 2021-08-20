man = ['М', 'м', 'Муж', 'муж', 'Мужской', 'мужской', 'Мужчина', 'мужчина', 'M', 'm', 'Man', 'man', 'Male', 'male']
woman = ['Ж', 'ж', 'Жен', 'жен', 'Женский', 'женский', 'Женщина', 'женщина', 'W', 'w', 'Woman', 'woman', 'Female', 'female', 'Wife', 'wife', 'Feminine', 'feminine']
print("Здравствуйте!")
while True:
    print("Укажите Ваш пол:")
    gender = input()
    if gender in man:
        # def wha():
        while True:
            weight = float(input("Ваш вес: "))
            if 0 < weight < 350:
                break
            else:
                print('Введите корректные данные!')
                continue
        while True:
            height = float(input("Ваш рост: "))
            if 0 < height < 250:
                break
            else:
                print('Введите корректные данные!')
                continue
        while True:
            age = int(input("Ваш возраст: "))
            if 0 < age < 120:
                break
            else:
                print('Введите корректные данные!')
                continue
        calories = (10*weight+6.25*height-5*age+5)
        print('Вам нужно потреблять', int(calories), 'калорий!')
        # break
    elif gender in woman:
        while True:
            weight = float(input("Ваш вес: "))
            if 0 < weight < 350:
                break
            else:
                print('Введите корректные данные!')
                continue
        while True:
            height = float(input("Ваш рост: "))
            if 0 < height < 250:
                break
            else:
                print('Введите корректные данные!')
                continue
        while True:
            age = int(input("Ваш возраст: "))
            if 0 < age < 120:
                break
            else:
                print('Введите корректные данные!')
                continue
        calories = (10*weight+6.25*height-5*age-161)
        print('Вам нужно потреблять', int(calories), 'калорий!')
        # break
    else:
        print('Введите корректные данные!')
        continue