﻿# Вы можете расположить сценарий своей игры в этом файле.

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

    "Падение."
    "Сверкающие осколки разлетаются, раня и звеня."
    "Первое чувство - пронзающая боль. Первый звук - собственный крик."
    "Все происходящее будто со стороны - неосознанное, неконтролируемое."
    "Через мгновение новое чувство - сырость и запах травы после дождя на щеке и руках. 
    Она открывает глаза сквозь гудящую в висках боль."
    l "..."
    "Ветер пронзает насквозь льдом, сбивая с мысли и истязая тело. 
    Но внимательный слух еще способен уловить взмах крыльев.
    Она поднимается, собирая остатки сил и готовясь противостоять как в последний раз."
    "Погоня кажется длится уже вечность. Безуспешная и бессмысленная."
    "Но вдруг странный свет заполняет все вокруг, а потом тьма, которой так не хватало уставшим глазам."

    "...Что-то мягкое и теплое касается лица"
    "Она вздрагивает и хватает нечто расскрывая глаза."
    "Это оказалась чужая рука, но странная. Руки ангелов холодны как камень, такие же какими были ее руки совсем недавно"
    "На нее с успокаивающей улыбкой смотрело нечто иное, не ангел. 
    Оно совсем не испугалось и казалось не хотело принуждать ни к чему"
    a "С пробуждением... Я так ждал тебя"
    l "..." 
    "Она не знала что сказать и как, но кажется понимала этот мягкий, словно влажная трава, голос"
    "Из горла издался только хрип"
    "Он поднес ей теплый отвар из трав и ягод в чаше из дерева."
    a "Я не хочу причинить тебе зла.
    Прошу выпей, это поможет твоему горлу"
    "Немного подумав, она жадно выпила все, постаравшись отползти в сторону и выпрямиться. 
    Нечто мягко улыбнулось, наблюдая за этим"
    "Горлу и правда стало намного лучше и внутри потеплело, а разум и зрение наконец начали проясняться."
    l "...Кто ты?"
    a "Я не отсюда" 
    "Он снова улыбнулся, кажется он очень ждал этого момента. 
    Момента первого контакта и момента услышать голос, той кого спас"
    l "Я задала другой вопрос. Отвечай"
    "Это не стерло расслабленную улыбку с его лица"
    "Она постаралась вернуть былое хладнокровие, осматривая пещеру в поисках оружия, 
    но руки леденели и сердце раздражающе громко стучало в груди. 
    Вокруг не было ничего особенного, кроме кучки светящихся осколков в крови."
    "Их вид вызывал в ней только отвращение"
    f "Прости, можешь звать меня Фавнир. 
    Я не из тех кто гнался за тобой, но ты это наверняка и так знаешь"
    f "А как мне звать тебя?"
    l "Лилит. Зачем ты притащил это сюда?"
    f "Ах... Мне показалось что это может быть чем-то важным для тебя"
    "Она резко встала и вышла прямо под ледяной дождь и ветер. 
    Небо будто плакало о чем-то, дождь шел уже вечность."
    "Он вышел за ней, прикрывав ее какой-то тканью"
    f "Они улетели и не появлялись много солнц. Не переживай"
    l "..."
    f "...Ты не простудишься?"
    l "Это невозможно. Ангелы не подтвержены болезни"
    "Бесконечные равнины, холмы, горы и дождь. Теперь это все такое необычное и чужое, ее дом"
    "Нужно подготовиться к возможным опасностям."
    "Она посмотрела на странного незнакомца. Его как будто совсем ничего не заботило и не пугало"
    "Может быть он был глуп и ни о чем не думал?"
    "Или может он уже знал все что нужно"
    "В любом случае незаметная улыбка не сходила с его лица все это время. И теплая рука слегка приобнимала за плечо"
    "Странно, но это не вызывало желания защищаться и убежать"
    "Вдруг она поняла что новое мягкое тепло приятнее надоевшего пронизывающего холода"
    "Она осторожно прислонилась к нему ближе, приобняв за талию и наконец укрывшись в ткани от дождя"



    return
