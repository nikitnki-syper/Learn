print("введите числа")
print("данная версия не последняя")
print()
x = input("---->")
print("")
y = input("---->")
print("укажите действие с этими числами")
print("1—сложение\n2—отбавление\n3—умножение\n4—деление\n5—возведение в степень\n6—//\n7—%\n8—credits")
print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
print("0—завершение")
print()
print("by Komap")
print()
g = input("------>")
print()
i = 1
v = int(g) + int(i)
if v == 2:
	d = int(x) + int(y)
	print("ваш ответ: " + str(d))
else:
	if v == 3:
		d = int(x) - int(y)
		print("ваш ответ: " + str(d))
	else:
		if v == 4:
			d = int(x) * int(y)
			print("ваш ответ: " + str(d))
		else:
			if v == 5:
				u = int(x) / int(y)
				print("ваш ответ: " + str(u))
			else:
				if v == 6:
					d = int(x) ** int(y)
					print("ваш ответ: " + str(d))
				else:
					if v == 7:
						d = int(x) // int(y)
						print("ваш ответ: " + str(d))
					else:
						if v == 8:
							d = int(x) % int(y)
							print("ваш ответ: " + str(d))
						else:
							if v == 1:
								print("пака")
								print("купите мне кофе")
							else:
								if v > 9:
									print("введите корректное действие")
								else:
									if v == 9:
										print("данный калькулятор был сделан для получения опыта\nпри обучении python")
										print("права захуярены")