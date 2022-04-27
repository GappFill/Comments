# Как запустить проект
1 - Создать новый проект в PyCharm <br/>
2 - Скачать репозиторий <br/>
3 - Добавить скачанный репозиторий в проект(можно без папки .idea) <br/>
4 - Установить зависимости из файла req.txt, это можно сделать командой <br/> 
pip install -r req.txt <br/>
5 - Подключить базу данных в файле settings.py <br/>
6 - Провести миграции, команды: <br/>
python manage.py makemigrations <br/>
python manage.py migrate <br/>
7 - Зарегестрировать администратора, для этого используем команду <br/> 
python manage.py createsuperuser <br/> 
Следуем инструкции в консоли <br/> 
8 - Запустить сервер командой: <br/> 
python manage.py runserver
9 - Перейти по ссылке в консоли <br/> 
10 - Необходимо добавить запись, для этого заходим в админку, дописав в адрестной строке страницы /admin, водим данные, которые использовали для регистрации в шаге 7. <br/> 
11 - Добовляем новую статью <br/> 
12 - Выходим из панели администратора <br/> 
13 - Обновляем страницу, у нас появляет новость, кликаем на ссылку <br/> 
14 - Теперь мы можем добовлять комментарии, отвечать на комментари и так далее... <br/> 
15 - Ура!!!!!
