# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define l = Character('Лилит', color="#b6293c")
define f = Character('Фавнир', color="#2989b6")
define a = Character('???', color="#495f69")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene bg room

    show eileen happy

    'Не'

    e "Вы создали новую игру Ren'Py."

    e "Добавьте сюжет, изображения и музыку и отправьте её в мир!"

    return
