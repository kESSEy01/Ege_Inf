print('Введите тему для сочинения:')
tema = input()
print(f'Тема сочинения {tema}')
print("Введите текст:")
# text = input()
lines = list()
while True:
    line = input()
    if line == 'конец':
        break
    else:
        lines.append(line)
text = list()
for line in lines:
    if ('\n' not in line ):
        text.append(line)
print()
print('Текст загружен')
print()
print(f'напиши сочинение в формате ЕГЭ по русскому языку на тему "{tema}",')
print(f'опираясь на следующий текст: "{''.join(text)}" ,')
print(f'по следующему плану: ')
print(f'1. начало сочинения (Текст (ФИО) посвящен одной из наиболее актуальных проблем современности - (чего?)). ')
print(f'2. позиция автора (Позиция автора заключается в том, что...). ')
print(f'3. первый аргумент + пояснение к примеру. (Автор обращает внимание на...)')
print(f'4. второй аргумент + пояснение к примеру. (Также автор подчеркивает...)')
print(f'5. собственная позиция (Нельзя не согласиться с позицией автора. Действительно, ...) + обоснование собственной позиции. ')
print(f'6. заключение (В заключение хочу подчеркнуть...).')