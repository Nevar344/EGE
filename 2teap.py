# print("x y z w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                     F = (w <= (not(z<=x)) or y)
#                     if F == 0: #В случае когда у нас F принимает либо 0 либо 1 то смотрим таблицу 0 и 1 и сверяем строчки отталкиваясь на значение функции тоесть если в таблице две 1 по F и 1 по F тогда следует в столбце со значениями 0 отследить строку схожую (например с 3 нулями обычно она там единственная)
#                         print(x, y, z, w)
# print("zxyw") #Otvet


#АВТОКОД!!!

from itertools import product, permutations

# === 1. НАСТРОЙКА ПОД ВАШУ ЗАДАЧУ ===
# Внесите сюда строки из условия задачи (None — если ячейка пустая)
table = [
    [1, 0, 0, 0],  # Строка 1
    [0, 0, 1, 0],  # Строка 2
    [0, 1, 0, 1],  # Строка 3
]

# Значения функции F для каждой строки выше (например, все 0 или все 1)
results = [1, 1, 0]


# ===================================

# Функция, вычисляющая ваше выражение: ¬(w→x) ∨ (¬z→¬y) ∨ z
def f(w, x, y, z):
    return int((x or (y and (not z))) and (not w)) #Пишем условие внутри int


# Генерируем полную эталонную таблицу истинности
full_f_table = {}
for w, x, y, z in product((0, 1), repeat=4):
    full_f_table[(w, x, y, z)] = f(w, x, y, z)

# Ищем подходящую перестановку букв
letters = ['w', 'x', 'y', 'z']
found = False

# Перебираем все возможные варианты порядка столбцов, например ('x', 'w', 'z', 'y')
for p in permutations(letters):
    # Пытаемся найти в полной таблице строки, подходящие под шаблон из задания
    matched_rows = []

    # Для каждой строки из задания ищем совпадение в эталоне
    for row, res in zip(table, results):
        for w, x, y, z in product((0, 1), repeat=4):
            # Если значение функции не совпадает, эта строка нам не подходит
            if full_f_table[(w, x, y, z)] != res:
                continue

            # Распределяем значения по текущему порядку переменных `p`
            current_vals = {'w': w, 'x': x, 'y': y, 'z': z}
            mapped_row = [current_vals[p[0]], current_vals[p[1]], current_vals[p[2]], current_vals[p[3]]]

            # Проверяем, совпадает ли эта строка с маской из задания (игнорируя None)
            if all(r is None or r == m for r, m in zip(row, mapped_row)):
                if (w, x, y, z) not in matched_rows:
                    matched_rows.append((w, x, y, z))
                    break  # Нашли строку для этого шаблона, переходим к следующему шаблону

    # Если мы смогли найти уникальные строки для всех шаблонов из задания
    if len(matched_rows) == len(table):
        print(f"✅ НАЙДЕН ОТВЕТ: {''.join(p)}")
        found = True
        break

if not found:
    print("❌ Решение не найдено. Проверьте правильность заполнения матрицы table и results!")
