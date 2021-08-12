# Discord-RPC-for-WarThunder

Для русской версии прокрутите ниже

## python app that will add your WT status to Discord

### Setup:

1. run:

        pip3 install -r requirements.txt

2. Read guide for https://pypi.org/project/discordsdk/
3. Create your own app on https://discord.com/developers/applications
   1. copy APPLICATION ID and paste it in config.cfg on 1st line
   2. load image to assets in "Rich Presence Assets" tab, and call it "logo", if you want to show it in user status.
4. in config.cfg replace 2nd line on your warthunder nickname.
5. You can edit run.bat, and run WarThunder with this app both automatically by running run.bat
6. Run WarThunder
7. Run "main.py"
8. see your status, (wait about 30s)


## программа, которая добавит ваш статус WT в Discord

### Установка и настройка:

1. запустите:

          pip3 install -r requirements.txt

2. Прочтите руководство  https://pypi.org/project/discordsdk/.
3. Создайте собственное приложение на https://discord.com/developers/applications.
     1. скопируйте APPLICATION ID и вставьте его в config.cfg в первую строку
     2. Загрузите изображение в вкладке "Rich Presence Assets" и назовите его "logo", если хотите, чтобы оно отображалось в статусе пользователя.
4. в config.cfg замените 2 строку на свой ник в warthunder.
5. Вы можете редактировать run.bat и запускать WarThunder вместе с приложением автоматически, запустив run.bat.
6. Запустите WarThunder.
7. Запустите "main.py"
8. посмотрите свой статус в дискорде (подождите около 30 секунд)