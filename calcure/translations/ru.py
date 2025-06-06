"""Russian translations of the program interface"""

MSG_WELCOME_1 = "Добро пожаловать в Calcure"
MSG_WELCOME_2 = "Ваш новый календарь и менеджер задач!"
MSG_WELCOME_3 = "Файлы конфигурации и данных созданы в:"
MSG_WELCOME_4 = "Информация об участии, поддержке, и функционале доступна в репозитории:"
MSG_WELCOME_5 = "Нажмите ? для вызова списка клавиш или любую клавишу для продолжения."

TITLE_KEYS_GENERAL  = "ОБЩИЕ КЛАВИШИ"
TITLE_KEYS_CALENDAR = "КЛАВИШИ КАЛЕНДАРЯ"
TITLE_KEYS_JOURNAL  = "КЛАВИШИ ЖУРНАЛА"

KEYS_GENERAL = {
        " Space ": "Переключать между календарём и журналом",
        "   /   ": "Переключать режим разделённого экрана",
        "   *   ": "Переключать приватность",
        "   ?   ": "Вызвать экран помощи",
        "   Q   ": "Перезагрузить",
        "   q   ": "Выйти",
        }

KEYS_CALENDAR = {
        "  a(A) ": "Добавить (повторяющееся) событие",
        "   n   ": "Следующий месяц (день)",
        "   p   ": "Предыдущий месяц (день)",
        "   x   ": "Удалить событие",
        "   r   ": "Переименовать событие",
        "  m(M) ": "Переместить событие",
        "   v   ": "Переключать дневной/месячный вид",
        "  g(G) ": "Открыть определённый день",
        "   h   ": "Переключать высокий приоритет",
        "   l   ": "Переключать низкий приоритет",
        "   d   ": "Переключать статус завершено",
        "   .   ": "Переключать приватность события",
        "   C   ": "Импортировать события из calcurse",
        "   R   ": "Вернуться к текущему месяцу (дню)",
        }

KEYS_TODO = {
        "  a(A) ": "Добавить новую (под)задачу",
        "  h(H) ": "Переключать приоритет одной (всех) задач как высокий",
        "  l(L) ": "Переключать приоритет одной (всех) задач как низкий",
        "  d(D) ": "Переключать приоритет одной (всех) задач как завершено",
        "  u(U) ": "Убрать все метки с одной (всех) задач",
        "  x(X) ": "Удалить одну (все) задачи (со всеми подзадачами)",
        "  t(T) ": "Запустить/приостановить (удалить) таймер задачи",
        "   r   ": "Переименовать задачу",
        "   s   ": "Переключать между задачей и подзадачей",
        "   .   ": "Переключать приватность задачи",
        "  f(F) ": "Изменить (удалить) дедлайн задачи",
        "   m   ": "Переместить задачу",
        "   C   ": "Импортировать задачи из calcurse",
        }

MSG_NAME          = "CALCURE"
MSG_VIM           = "Стрелки и Vim клавиши (j, k, ZZ, ZQ) работают!"
MSG_INFO          = "Больше информации вы найдёте на:"
MSG_SITE          = "https://anufrievroman.gitbook.io/calcure"
MSG_EXIT          = "Действительно выйти? (y/n) "

MSG_EVENT_HIGH    = "Отметить как высокоприоритетное событие номер: "
MSG_EVENT_LOW     = "Отметить как низкоприоритетное событие номер: "
MSG_EVENT_DONE    = "Отметить как завершенное событие номер: "
MSG_EVENT_RESET   = "Обнулить статус событие номер: "
MSG_EVENT_DEL     = "Удалить событие номер: "
MSG_EVENT_REN     = "Переименовать событие номер: "
MSG_NEW_TITLE     = "Введите новое название: "
MSG_EVENT_MV      = "Переместить событие номер: "
MSG_EVENT_MV_TO   = "Переместить событие на (YYYY/MM/DD): "
MSG_EVENT_MV_TO_D = "Переместить событие на: "
MSG_EVENT_DATE    = "Введите дату: "
MSG_EVENT_TITLE   = "Введите название: "
MSG_EVENT_REP     = "Сколько раз повторить событие: "
MSG_EVENT_FR      = "Повторить событие каждый день (d), неделю (w), месяц (m) или год(y)? "
MSG_EVENT_IMP     = "Импортировать события из Calcurse? (y/n)"
MSG_EVENT_PRIVACY = "Изменить приватность события номер: "
MSG_TM_ADD        = "Запустить/приостановить таймер для задачи: "
MSG_TM_RESET      = "Удалить таймер для задачи номер: "
MSG_TS_HIGH       = "Установить высокий приоритет для задачи номер: "
MSG_TS_LOW        = "Установить низкий приоритет для задачи номер: "
MSG_TS_RES        = "Обнулить статус задачи номер: "
MSG_TS_DONE       = "Отметить как завершенную задачу номер: "
MSG_TS_DEL        = "Удалить задачу номер: "
MSG_TS_DEL_ALL    = "Действительно удалить все задачи? (y/n)"
MSG_TS_EDT_ALL    = "Подтвердить операцию? (y/n)"
MSG_TS_MOVE       = "Переместить задачу номер: "
MSG_TS_MOVE_TO    = "Переместить задачу на номер: "
MSG_TS_EDIT       = "Переименовать задачу номер: "
MSG_TS_TOG        = "Переключить уровень задачи номер: "
MSG_TS_SUB        = "Добавить подзадачу к задачу номер: "
MSG_TS_TITLE      = "Введите название подзадачи: "
MSG_TS_IM         = "Импортировать задачи из Calcurse? (y/n)"
MSG_TS_TW         = "Импортировать задачи из Taskwarrior? (y/n)"
MSG_TS_NOTHING    = "Ничего не запланировано..."
MSG_TS_PRIVACY    = "Переключать приватность задачи номер: "
MSG_TS_DEAD_ADD   = "Добавить дедлайн к задаче номер: "
MSG_TS_DEAD_DEL   = "Удалить дедлайн задачи номер: "
MSG_TS_DEAD_DATE  = "Установить дедлайн на (YYYY/MM/DD): "
MSG_WEATHER       = "Загружается информации о погоде..."
MSG_ERRORS        = "Возникли ошибки. Детали в info.log файле в конфиг директории."
MSG_GOTO          = "Перейти к дате (YYYY/MM/DD): "
MSG_GOTO_D        = "Перейти к дате: "
MSG_INPUT         = "Некорректный ввод."

CALENDAR_HINT     = "Пробел · Переключить на журнал   a · Новое событие  n/p · Сменить месяц   ? · Клавиши"
CALENDAR_HINT_D   = "Пробел · Переключить на журнал   a · Новое событие  n/p · Сменить день   ? · Клавиши"
JOURNAL_HINT      = "Пробел · Переключить на календарь   a · Новая задача   d · Выполнено   h · Важно   ? · Клавиши"

DAYS         = ["ПОНЕДЕЛЬНИК", "ВТОРНИК", "СРЕДА", "ЧЕТВЕРГ", "ПЯТНИЦА", "СУББОТА", "ВОСКРЕСЕНЬЕ"]
DAYS_PERSIAN = ["SHANBEH", "YEKSHANBEH", "DOSHANBEH", "SESHANBEH", "CHAHARSHANBEH", "PANJSHANBEH", "JOMEH"]

MONTHS         = ["ЯНВАРЬ", "ФЕВРАЛЬ", "МАРТ", "АПРЕЛЬ", "МАЙ", "ИЮНЬ", "ИЮЛЬ", "АВГУСТ", "СЕНТЯБРЬ", "ОКТЯБРЬ", "НОЯБРЬ", "ДЕКАБРЬ"]
MONTHS_PERSIAN = ["FARVARDIN", "ORDIBEHESHT", "KHORDAD", "TIR", "MORDAD", "SHAHRIVAR", "MEHR", "ABAN", "AZAR", "DEY", "BAHMAN", "ESFAND"]
