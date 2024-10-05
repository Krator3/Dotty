<h1 align="center">Dotty</h1>

Dotty — простой менеджер точечных файлов для Linux на ЯП Python.
Если вам понравится данная сборка, поставьте :star2: этому репозиторию!

## Предупреждение
В программе присутствует довольно много недоработок, поэтому расценивайте этот софт как демонстративный образец.
За его использование ответственность несёте вы сами!

## Установка

### Предварительные условия
Для того чтобы Dotty работал корректно, требуется лишь наличие ЯП Python в системе.
В большинстве дистрибутивов Linux он установлен по умолчанию.
Однако если вы наткнулись на исключение, установить Python можно с официальных репозиториев вашего дистрибутива.

*Теперь вы готовы к следующему этапу!*

###  Установка Dotty
Для установки данной сборки выполните команду ниже:
```shell
git clone --depth 1 https://github.com/Krator3/Dotty ~/.dotty/ && rm -rf ~/.dotty/.git
```
Также для корректной работы Dotty не требуются файлы `LICENSE` и `README.md`, поэтому можете удалить их, если они вам не нужны.

На данный момент программа работает только внутри обозначенного каталога при запуске файла `main.py`.
Чтобы запускать Dotty в любом каталоге, создайте символьную ссылку на основной файл программы в `/usr/bin/` и сделайте ее исполняемой:
```shell
sudo ln -s ~/.dotty/src/main.py /usr/bin/dotty
chmod +x /usr/bin/dotty
```
P.S: Если вы желаете использовать `su -` вместо `sudo`, не забудьте заменить `~` на путь к вашему пользователю!

## Работа с Dotty
Посмотреть функционал Dotty можно при помощи команды `dotty -h/--help`:
```shell
usage: dotty [-h] [-v] [init ...] [add ...] [restore ...] [deploy ...]

Dotty - Менеджер точечных файлов

positional arguments:
  init           Базовая настройка программы
  add            Создать символическую ссылку
  restore        Удалить символическую ссылку и вернуть файл/каталог на место
  deploy         Воссоздать символьные ссылки по данным файла

options:
  -h, --help     show this help message and exit
  -v, --version  Отобразить версию программы
```

`init` не требует ничего для своей работы. Если вы хотите использовать другое название для каталога-агрегатора, измените значение переменной `need_folder` в `~/.dotty/src/config.py`

`add` принимает путь до файла, который будет добавлен в отслеживание программы

`restore` требует указать путь до файла, который будет удален из отслеживания программой и возвращен в свое исходное местоположение

`deploy` не использует никаких параметров

---

Ну и само собой данный софт имеет общепринятые опции: `-h/--help` и `-v/--version`.

## Удаление Dotty
Для того чтобы полностью удалить Dotty из вашей системы, выполните следующую команду в терминале:
```shell
sudo rm -rf ~/.dotty/ /usr/bin/dotty
```
P.S: Если вы желаете использовать `su -` вместо `sudo`, не забудьте заменить `~` на путь к вашему пользователю!

## Содействие
Любая помощь со стороны категорически приветствуется!
Если вы хотите сообщить о найденных ошибках или предложить нововведение без готового решения, просто откройте новую проблему с соответствующей темой.
Если же вы хотите внести изменения в сборку (например, исправить ошибку, улучшить документацию и так далее), не стесняйтесь и смело создавайте свои PR!
В независимости от того, какую помощь вы решили оказать, важно подробно описать ее.

## Лицензия
Этот проект лицензируется по лицензии MIT — подробности см. в файле [LICENSE](LICENSE).