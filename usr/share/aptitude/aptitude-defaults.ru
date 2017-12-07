// -*-c++-*-
//
// This file defines the names of sections known by aptitude for ru.

Aptitude::Sections
{
  Descriptions {
    Unknown	"Пакеты с необъявленным разделом\n В этих пакетах не указан раздел. Возможно, это ошибка в файле Packages?";
    Virtual	"Виртуальные пакеты\n Эти пакеты не существуют; они указывают на другие пакеты, которые нужно использовать или которые предоставляют схожие функции.";
    Tasks	"Пакеты, которые установлены на вашем компьютере, выполняют определённые задачи\n Пакеты в разделе 'Задачи' не содержат файлов; они просто зависят от других пакетов. Эти пакеты предлагают лёгкий путь выбора заранее определённых наборов пакетов для специфических задач.";

    admin	"Утилиты администрирования (установка ПО, управл. пользователями, и т.д.)\n Пакеты в разделе 'admin' позволяют вам выполнять административные задачи, такие как установка программ, управление пользователями, настройка и мониторинг вашей системы, анализ сетевого трафика и так далее.";
    alien	"Пакеты, преобразованные из других форматов (rpm, tgz и т.д.)\n Пакеты в разделе'alien' созданы программой 'alien' из пакетов не-Debian формата,таким как RPM";
    base	"Базовая система Debian \n Пакеты в разделе 'base' являются частью начальной установки системы.";
    comm	"Программы для факс-модемов и других устройств связи\n Пакеты в разделе 'comm' используются для управления модемами и другой аппаратурой связи. Сюда включены программы для управления факс-модемами(например, PPP для соединения с Интернет и программы изначально написанные для работы с протоколами zmodem/kermit), сотовыми телефонами, интерфейс с FidoNet и для запуска BBS.";
    devel	"Утилиты и программы для разработки ПО\n Пакеты в разделе 'devel' используются для написания нового программного обеспечения и работы над существующим программным обеспечением. Не-программистам, которым не нужно компилировать свои собственные программы, вероятно нужно немного программ из этого раздела.\n .\n Сюда включены компиляторы, средства отладки, редакторы для программирования, утилиты обработки исходного кода и другие вещи, относящиеся к разработке программного обеспечения.";
    doc		"Документация и специальные программы просмотра документации\n Пакеты в разделе 'doc' документируют части системы Debian или содержат программы просмотра документов в различных форматах.";
    editors	"Текстовые редакторы и текстовые процессоры\n Пакеты в раздела 'editors' позволяют вам редактировать простой ASCII текст. Для этого не нужно текстовых процессоров, хотя несколько текстовых процессоров можно найти в этом разделе.";
    electronics	"Программы для работы со схемами и электроникой\n Пакеты в разделе 'electronics' содержат инструменты разработки схем, симуляторы и ассемблеры для микроконтроллеров и другое программное обеспечение по этой теме.";
    embedded	"Программы для встроенных систем\n Пакеты в разделе 'embedded' предназначены для запуска на встроенных устройствах. Встроенные устройства -- это специализированные аппаратные устройства с намного меньшим потреблением электроэнергии чем обычные настольные системы: например PDA, мобильный телефон или Tivo.";
    gnome	"Настольная система GNOME\n GNOME это набор программ, которые предоставляют лёгкую в использовании настольную среду для Linux. Пакеты в разделе 'gnome' являются частью среды GNOME или тесно с ней связаны.";
    games	"Игры, развлечения и забавные программы\n Пакеты в разделе 'games' предназначены, главным образом для .развлечения.";
    graphics	"Утилиты для создания, просмотра и редактирования графических файлов\n Пакеты в разделе 'graphics' содержат программы просмотра графических файлов, обработки и манипулирования изображениями, программное обеспечение для взаимодействия с графическим аппаратным обеспечением (таким как видеокарты, сканеры и цифровые камеры), и инструменты программиста для работы с графикой.";
    hamradio	"Программное обеспечение для операторов ham radio\n Пакеты в разделе 'hamradio' предназначены для, главным образом для ham radio операторов.";
    interpreters "Интерпретаторы интерпретируемых языков\n Пакеты в разделе 'interpreters' содержат интерпретаторы языков, таких как Python, Perl, и Ruby, и библиотеки этих же языков.";
    kde		"Настольная система KDE\n KDE это набор программ, которые предоставляют лёгкую в использовании настольную среду для Linux. Пакеты в разделе 'kde' являются частью среды KDE или тесно с ней связаны.";
    libdevel	"Файлы библиотек для разработки\n Пакеты в разделе 'libdevel' содержат файлы, необходимые для сборки программ, которые используют библиотеки из раздела 'libs'. Вам не нужны пакеты из этого раздела, если вы не хотите сами компилировать программы.";
    libs	"Библиотеки подпрограмм\n Пакеты в раздела 'libs' предоставляют необходимую функциональность для других программ на компьютере. За некоторым исключением, вам не нужно явно устанавливать пакеты из этого раздела; система обработки пакетов будет сама устанавливать их как того требуют зависимости.";
    perl	"Интерпретатор Perl и библиотеки\n Пакеты в разделе 'perl' предоставляют язык программирования Perl и много сторонних библиотек для него. Если вы не программист на Perl, то вам не нужно явно устанавливать пакеты из этого раздела; система обработки пакетов будет устанавливать их по мере необходимости.";
    python	"Интерпретатор Python и библиотеки\n Пакеты в разделе 'python' предоставляют язык программирования Python и много сторонних библиотек для него. Если вы не программист на Python, то вам не нужно явно устанавливать пакеты из этого раздела; система обработки пакетов будет устанавливать их по мере необходимости.";
    mail	"Программы для написания, отправки и перенаправления сообщений электронной почты\n Пакеты в разделе 'mail' содержат программы для чтения почты, демоны передачи почты, программы работы со списками рассылки и спам фильтры, а также всё остальное ПО относящееся к электронной почте.";
    math	"Численный анализ и другое математическое ПО\n Пакеты в разделе 'math' содержат калькуляторы, языки для математических вычислений (подобных Mathematica), пакеты булевой алгебры и программы визуализации математических объектов.";
    misc	"Различное программное обеспечение\n Пакеты в разделе 'misc' выполняют слишком необычные функции, чтобы их классифицировать.";
    net		"Программы для подключения и предоставления различных сервисов\n Пакеты в разделе 'net' содержат клиенты и серверы многих протоколов, инструменты для управления и отладки низкоуровневых сетевых протоколов,IM системы, другое сетевое ПО.";
    news	"Клиенты и серверы Usenet\n Пакеты в разделе 'news' относятся к системе распространения новостей Usenet. К ним относятся программы чтения почты и серверы новостей.";
    oldlibs	"Устаревшие библиотеки\n Пакеты в разделе 'oldlibs' устарели и не должны больше использоваться новым программным обеспечением. Они предоставлены для совместимости или потому что ПО распространяемому Debian они ещё нужны.\n .\nЗа некоторым исключением, вам не нужно явно устанавливать пакеты из этого раздела; система обработки пакетов будет сама устанавливать их как того требуют зависимости.";
    otherosfs	"Эмуляторы и ПО для чтения чужих файловых систем\n Пакеты в разделе 'otherosfs' эмулируют аппаратуру и операционные системы и предоставляют инструменты для передачи данных между различными операционными системами и аппаратными платформами. (например, утилиты чтения дискет DOS, и утилиты для связи с Palm Pilots)\n .\nСтоит упомянуть, что ПО для записи CD включено в ЭТОТ раздел.";
    science	"ПО для научных работ\n Пакеты в разделе 'science' содержат инструменты для астрономии, биологии и химии, а также другое ПО, относящееся к науке.";
    shells	"Командные оболочки и альтернативные консольные среды\n Пакеты в разделе 'shells' содержат программы, предоставляющие интерфейс командной строки.";
    sound	"Утилиты для воспроизведения и записи звука\n Пакеты в разделе 'sound' содержат звуковые проигрыватели, программы записи и кодирования звука для многих форматов, микшеры и регуляторы громкости, MIDI секвенсеры и программы генерации нотной записи, драйверы для звуковых устройств и ПО для обработки звука.";
    tex		"Типографская система TeX\n Пакеты в разделе 'tex' относятся к TeX, системе для производства печати типографского качества. Сюда входит сам TeX, пакеты TeX, редакторы,разработанные для TeX, утилиты преобразования TeX и файлов вывода TeX в различные форматы, шрифты TeX и другое ПО, относящееся к TeX.";
    text	"Утилиты обработки текста\n Пакеты в разделе 'text' содержат фильтры и процессоры обработки текста, проверку орфографии, словари, утилиты преобразования между кодировками, форматами файлов (например, Unix иDOS), утилиты форматирования текста и вывода на печать, и другое ПО, обрабатывающее простой текст.";
    utils	"Различные системные утилиты\n Пакеты в разделе 'utils' содержат утилиты для разных задача, которые трудно классифицировать.";
    web		"Веб браузеры, сервера, прокси и другие инструменты\n Пакеты в разделе 'web' содержат Веб браузеры, Веб сервера и прокси,программы для написания сценариев CGI  или программ для Веб, уже написанные программы для Веб и другое ПО относящееся к World Wide Web.";
    x11		"X window system и ПО для неё\n Пакеты в разделе 'x11' содержат базовые пакеты для X window system, оконные менеджеры, программные утилиты для X, и разнообразные программы с графическим интерфейсом пользователя под X, размещённые здесь, потому что они не попали в другой раздел.";

    main	"Главный архив Debian\n Дистрибутив Debian состоит из пакетов раздела 'main'. Каждый пакет в 'main' является Свободным ПО.\n .\n Более подробно о том, как в Debian решают Свободное ПО или нет, смотрите здесьhttp://www.debian.org/social_contract#guidelines";
    contrib	"Программы, которые зависят от ПО, не являющегося частью Debian\n Пакеты в разделе 'contrib' не являются частью Debian.\n .\n Эти пакеты являются Свободным ПО, но они зависят от программ, которые не являются частью Debian. Это может быть из-за того что, они не являются Свободным ПО, но имеются в разделе non-free , т.к. Debian совсем не имеет прав их распространять, или (в редких случаях) потому что ещё не собраны в пакет.\n .\n Более подробно о том, как в Debian решают Свободное ПО или нет, смотрите здесьhttp://www.debian.org/social_contract#guidelines";
    non-free	"Программы, не являющиеся Свободным ПО\n Пакеты в разделе 'non-free' не являются частью Debian.\n .\n Эти пакеты не удовлетворяют одному или нескольким критериям Debian по определению Свободного ПО (смотрите ниже). Вы должны прочитать лицензию на программы из этого раздела, чтобы убедиться, что вам позволено использовать их так как вы хотите.\n .\n Более подробно о том, как в Debian решают Свободное ПО или нет, смотрите здесь http://www.debian.org/social_contract#guidelines";
    non-US	"Программы, размещённые за пределами США, из-за контроля за экспортом\n Пакеты в разделе 'non-US' вероятней всего содержат реализацию нескольких запатентованных алгоритмов шифрования. По этой причине, они не могут экспортироваться за пределы США, и следовательно размещаются на сервере в ''свободном мире''.\n .\n Замечание: Проект Debian в данный момент объединил программы шифрования с архивами расположенными в США после консультации с юристами экспертами в новых изменениях экспортных правил. Большинство пакетов, которые ранее были в этом разделе, теперь в 'main'.";
  };
};

