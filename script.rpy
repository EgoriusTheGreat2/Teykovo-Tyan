# Персонажи, ебать
define a = Character(_("arinochka"), color="#ffb3f4") # Ариночка. Неее ну это биседзе + цендуре. Лучшая девочка в игре, да... меганэкко наверно да.....
define z = Character(_("zhenechka"), color="#ffc299") # Женечка. Нее, ну это биседзе. Тупо идеальная девочка, но после начала рута начнет посылать тебя нахуй по кд. но почему?
define k = Character(_("katechka"), color="#ff7d7d") # Катечка. Пошел нахуй, это цундере. Покрывает героя матом по кд, но после начала отношений с ГГ раскрывается как человек. либо становится янгире и убивает всех нахуй
define l = Character(_("lerochka"), color="#ffdea0") # Лерочка. Ухххх, дандере... Вообще не общается ни с кем, т.к. но на самом деле очень общительна. какая дандере нахуй,  если кудере...
define v = Character(_("veronichka"), color="#c2ffa1") # Вероничка. Ухх, ну это тоже дандере. Общается только на японском языке.
define p = Character(_("polinochka"), color="#ffd177") # Полиночка. Без комментариев. а может цунахо? или...
define i = Character(_("ilya"), color="#a1d5ff") # Илюха. Альфонс, ебать. Мечта мужиков. Чел из Яой рута. я бы трахнул его кста
define m = Character(_("me"), color="#a1f7ff") # ГГ

image bg winterday = "winterday.jpg"
image bg schoolhall = "schoolhall.jpg"
image bg schooldoor = "schooldoor.jpg"
image bg sports = "sports.jpg"
image ilya green normal = "Ilya_neutral.png"
image polinochka green normal = "polina_neutral.png"
image ilya green smile = "ilya_smile.png"
image ilya green joy = "ilya_laugh.png"

# Начало игры, ебать. Через каждую строчку диалога возникает окно монолога гг где будет единственная фраза - хочу тяночку, происходит это только при разговоре с тяночками
label start:

    # Старт музла, ебать.
    play music "audio/daystarts.mp3"

    scene bg winterday # Сцена зимнего утра, надо нарисовать
    with fade

    "Знаете, жизнь часто подкидывает мне сюрпризы. Я могу сколько угодно говорить о случившихся со мной неожиданностях."

    "Впрочем, среди всех этих неожиданностей ни разу мне не встречалась любящая меня девушка, но что мне об этом говорить?"

    "Как будто нет у меня других дел и забот, не так ли? Да... Пожалуй, и правда я и так занятой человек, чего уж греха таить"

    "Все эти экзамены, факультеты по английскому языку... Разве можно это отбросить? Да нет конечно!"

    "Да что я все думаю и думаю, пора бы уж в школу собираться. До занятий хоть и осталось пол часа, но по гололеду идти мне явно придется долго..."

    "Долго и больно..."

    scene bg schooldoor # Сцена где-то у школьных ворот, надо нарисовать
    with fade

    "Как я и думал, с кем-нибудь я и пересекусь пока в школу иду. Прямо у школьных ворот меня встретила Аико-тян"

    show polinochka green normal # Вывести на экран обычную Полину

    p "Привет! Смотрю, ты тоже опаздываешь, ха-ха!"

    m "Э-э, ну как видишь... Да и что с того? Это же всего-лишь физкультура, меня и не заметят. Так что все идет по плану!"

    p "Эх ты, планировщик! Ну давай, пошли быстрее!"

    scene bg schoolhall # Сцена школьного вестибюля, надо нарисовать
    with fade
    play music "audio/schoolday.mp3" volume 0.2 # Музыка внутри школы

    "Ну и наконец, я в самом привычном месте - в школе. Здесь, должно быть, уже прошла половина моей жизни."

    "Правда, не совсем понятно, зачем я это вам говорю - как будто у других бывает иначе, а?"

    scene bg sports # Школьный спортзал, надо нарисовать
    with fade

    "Спортивный зал - мое самое нелюбимое место в школе. Уж так сложилось, что я с самого детства рабенок... сиделый, в общем говоря.."

    show ilya green normal # Вывести на экран Илюху

    i "О, а вот и ты, чего-то ты как-то поздно!"

    "Это - Акио. Мой лучший друг, мы с нем еще с пеленок дружим."

    m "Разве? Смотри, до звонка еще целых 5 минут - сейчас переоденемся и все!"

    show ilya green smile # Вывести на экран улыбающегося Илюху

    i "Ты чего, дружище? Совсем уже переспал? Куда ты переодеваться собрался, ты же и так переоделся."

    m "Я переспал? Да разве что ты! Предлагаешь мне в школьной форме заниматься?"

    i "Конечно, не будешь же ты в спортивной одежде на японском сидеть!"

    m "Э, в смысле японском? Сейчас же у нас физкультура по расписанию..."

    show ilya green joy # Вывести на экран ржущего Илюху

    i "Да-а, видать и правда переспал лишнего. Целых два первых урока. Надеюсь, теперь понимаешь о чем речь?"
