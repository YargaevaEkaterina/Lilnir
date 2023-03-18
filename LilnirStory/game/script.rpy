﻿# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define l = Character('Лилит', color="#b6293c")
define f = Character('Фавнир', color="#2989b6")
define a = Character('???', color="#495f69")

image l n = "images/char/lil_norm.png"
image f n = "images/char/fav_norm.png"
image cg f_morning  = "images/cg/f_morning.png"
image cg f_cup  = "images/cg/f_cup.png"
image bg valley = "images/bg/valley.png"
image bg cave = "images/bg/cave.png"
image bg hill = "images/bg/hill.png"

transform cr:
    xalign 0.75
    yalign 1.00

transform cl:
    xalign 0.25
    yalign 1.00

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    centered "Глава 0. Падение"
    "Сверкающие осколки разлетаются, раня и звеня."
    "Первое чувство - пронзающая боль. Первый звук - собственный крик."
    "Все происходящее будто со стороны - неосознанное, неконтролируемое."
    "Через мгновение новое чувство - сырость и запах травы после дождя на щеке и руках. 
    Она открывает глаза сквозь гудящую в висках боль."
    l "..."
    scene bg valley
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
    scene cg f_morning
    a "С пробуждением... Я так ждал тебя"
    l "..." 
    "Она не знала что сказать и как, но кажется понимала этот мягкий, словно влажная трава, голос"
    "Из горла издался только хрип"
    "Он поднес ей теплый отвар из трав и ягод в чаше из дерева."
    scene cg f_cup
    a "Я не хочу причинить тебе зла.
    Прошу выпей, это поможет твоему горлу"
    "Немного подумав, она жадно выпила все, постаравшись отползти в сторону и выпрямиться. 
    Нечто мягко улыбнулось, наблюдая за этим"
    "Горлу и правда стало намного лучше и внутри потеплело, а разум и зрение наконец начали проясняться."
    scene bg cave
    show l n at cl
    show f n at cr
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
    scene bg hill
    "Он вышел за ней, прикрывав ее какой-то тканью"
    f "Они улетели и не появлялись много солнц. Не переживай"
    l "..."
    f "...Ты не простудишься?"
    l "Это невозможно. Ангелы не подтвержены болезни"
    hide l n
    hide f n
    "Бесконечные равнины, холмы, горы и дождь. Теперь это все такое необычное и чужое, ее дом"
    "Нужно подготовиться к возможным опасностям."
    "Она посмотрела на странного незнакомца. Его как будто совсем ничего не заботило и не пугало"
    "Может быть он был глуп и ни о чем не думал?"
    "Или может он уже знал все что нужно"
    "В любом случае незаметная улыбка не сходила с его лица все это время. И теплая рука слегка приобнимала за плечо"
    "Странно, но это не вызывало желания защищаться и убежать"
    scene black
    "Вдруг она поняла что новое мягкое тепло приятнее надоевшего пронизывающего холода"
    "Она осторожно прислонилась к нему ближе, приобняв за талию и наконец укрывшись в ткани от дождя"

    # Глава от лица фавнира 
    centered "Глава 1. Одинокий странник"

    "С момента прибытия я много бродил по этому чудному миру."
    "Необычные зелёные, цветные, тёплые и холодные, мягкие и колючие, агрессивные и дружелюбные существа населяли эту планету."
    "Бескрайнее раздолье для прогулок и знаний, бесконечное поле для фантазии."
    "Каждая песчинка и каждая глыба мне была одинакова интересна, пока я не встретил ту, что упала с небес."
    "Что-то привлекло меня в ней, первое существо в этом мире, что показалось мне близким и равным."
    "Побоявшись потерять её в тот же миг, что и нашёл, я позволил себе вмешаться и укрыть её от тех, кому она была нужна тоже."
    "Не сомневаюсь что это было правильным решением, но теперь я не знаю как завоевать её доверие."
    "И я так заинтригован!"
    "..."
    "Ведь это не плохо?"
    scene bg cave
    f "Доброе утро, хорошо спалось?"
    scene cg f_cup
    "Я с улыбкой подаю ей очередную чашу отвара из ягод."
    "Она незаметно кивает и  берет её уже не так неохотно и это отзывается во мне маленькой радостью."
    "Её тяжело разговорить, но это завораживает меня."
    "Я совсем не знаю кем она могла бы быть и собираю этот пазл по частицам, принося ей самые красивые цветы и ягоды."
    "Пусть пока она и не замечает этого."
    scene bg cave
    "А когда ей стало лучше я решил немного поиграть."
    show f n at cr
    f "Амм~"
    "Я кладу самую сладкую ягодку себе в рот и внимательно слежу за ней."
    "Она начинает заметно злиться, когда я делаю вид что кладу следующую себе тоже."
    f "Хочешь ягодку?"
    show l n at cl
    l "..."
    "Она молчит внутри пылая огнём, от неё начинает исходить искристый жар."
    menu:       
        "Ах, совру, если скажу что это мне совсем не нравится."   
        "Подразнить её ещё немного":          
            "Я протягиваю ей ягодку и тут же отдергиваю руку от чего она клацает зубами передо мной"
            "Пару секунд в ее глазах растет непонимание, но вдруг она срывается с места и выбегает из пещеры"
            "Это первый раз когда она сама скрылась с моих глаз"
            "Сначала я подумал что скоро она вернется, поэтому промедлил и не пошел за ней"
            "Но теперь я не могу найти ее след"
            "Мне оставалось лишь смиренно ждать"
            "..."
            "Через несколько дней или может даже недель она вернулась..."
            "С окрававленой тушкой волка"
            "Так я понял что она еще и хищница, но меня это не отпугнуло"
            "Единственное о чем я жалел, так о том что дразнил ее хрупкое доверие"
            "Ведь когда она вернулась, перепачканная в крови и грязи, она сказала мне:"
            l "...Я не твоя зверушка чтобы играть со мной"
            "Ушло много времени чтобы увидеть искорку доверия в ее глазах снова"
        "Отдать сладкую ягодку":  
            "Я протягиваю ей ягодку и она тут же сьедает ее прямо из моих рук"
            "Кажется, это была последняя"
            "Она оглядывает меня и все вокруг в поисках еды"
            "Глупо с моей стороны, но до этого момента я не задумывался что ей нужно больше еды..."
            "Я растерянно пожал плечами взяв ее за руку"
            "Эта планета была нова для меня, наверное для нее тоже"
            "Но наши потребности отличались и я не знал как удовлетворить ее"
            "Неожиданно она взглянула мне в глаза, будто прощалась и аккуратно убрав мою руку с ее руки, скрылась в бесконечном дожде"
            "И вдруг я почувствовал себя одиноко впервые за долгое время"
            "Раньше, я бы тут же заинтересовался чем-то другим..."
            "Но сейчас все стало тусклым и серым как небо все это время"
            "Бывает ли оно другого цвета на этой планете?"
            "..."
            "Через несколько недель она вернулась"
            "Ее волосы слегка покраснели..." 
    
    "Время шло, она крепчала и все увереннее стояла на ногах"
    "В ее глазах и осанке росла величественность и сила"
    "Она перестала нуждаться в моих ягодках и отварах"
    "Но когда она была в хорошем настроении или в особенно унылые и холодные ночи она с удовольствием принимала их"
    "Не ради выживания, но ради комфорта"
    "Она даже улыбалась и говорила со мной сама"
    "С тех пор она продолжала уходить в поле высокой травы и лес без страха"
    "И небо начинало проснятся все больше как ее волосы заполнялись глубоким цветом"
    "Совсем скоро дождь перестал затапливать равнины и солнце дало рост чудесной зеленой жизни"
    "Новые виды этой планеты снова увлекли меня, когда беспокойство о Лилит спало"
    "Но появилось новое теплое и трепетное чувство"
    "Я скучал по ней, когда она скрывалась вдали, но мысленно желал ей удачи и поскорее вернуться домой"

    # Глава от лица лилит про появление фавна
    centered "Глава 2. Поход в снегах"
    "Время шло быстро"
    "Скоро травы потеряли цвет, а потом вовсе завяли"
    "Я с интересом наблюдал за этим циклом жизни, все было так необычно для меня"
    "Так я узнал что травы и деревья не всегда полны цвета и свежести на этой планете"
    "Для меня даже это было праздником любопытства, но кажется не для моей спутницы"
    "Лилит сидела на холодных камнях и смотрела вдаль"
    "Я присел рядом, наслаждаясь размеренным танцем небесных белоснежных хлопьев"
    f "Они напоминают мне о дне, когда я встретил тебя. Ты кружилась в воздухе так же легко"
    l "По моему больше похоже было на это."
    "Она кинула камешек и он полетел вниз, сталкиваясь с другими и звонко сбивая их со скалы"
    "Я засмеялся и кивнул"
    f "О чем ты так задумалась? Сидишь здесь целый день"
    l "В лесу не осталось еды."
    "И правда, как опала листва и каждый день с неба сыпалась застывшая вода, вокруг стало слишком тихо"
    l "Звери и растения замерли под снегом... Я не смогла ничего добыть за последние несколько дней"
    f "Точно..."
    "За собственным любопытством я совсем не заметил проблемы этого белого пейзажа"
    l "Мне придется уйти в новые охотничьи угодья... Надеюсь ты понимаешь."
    f "Я же могу пойти с тобой?"
    l "Охотиться с хвостом тяжело. Лучше поищи новое пристанище"
    "В моей душе еле заметно разлилось очередное неведомое чувство"
    "Горьковатое и тягучее, но я кивнул, вернувшись в глубь пещеры" 
    "Лилит скоро покинула меня, накинув шкуру волка и захватив с собой длинную заостренную ветвь"
    "Помню как она сидела много дней над заточкой, злясь и произнося все новые причудливые слова"
    "Я не запомнил их все, поэтому был бы рад послушать снова..."
    "Мне пришлось оставить здесь множество чудесных фигурок, которые я вырезал вечерами у костра"
    "Собрав самые дорогие мне вещи и повязав мешочек с ними на длинную палку, я отправился вдаль, куда смотрела Лилит"
    "Туда, где ее нет"
    "..."
    "Пейзаж с приходом белого времени совсем переменился"
    "Сейчас мне бы стоило большого труда найти то место, где мы впервые встретились с Лилит"
    "Так было даже интереснее, я будто снова исследую неизвестность, но и тревога росла в моем сердце"
    "Больше не видно было нашего дома и вдруг ветер принес мне отголоски живых существ"
    "Я шел по этому следу в снегах пока не заметил дым и искрящийся теплый свет на снегу"
    "То были существа, на которых я не натыкался прежде, но они были так похожи на Лилит"
    "Люди"
    "Подсказало эхо внутри"
    "Я осторожно подошел к ним и не заметил как остался с ними"
    "Что-то подсказывало мне что я провел с Лилит намного больше времени чем мне казалось"
    "И было радостно найти еще кого-то кому я мог помочь"




    
    # Глава от лица лилит про появление фенрира
    centered "Глава 3. Охотница и сокровище"

    # Глава от лица лилит про появление василинки
    centered "Глава 4. Охотница и сокровище"

    return
