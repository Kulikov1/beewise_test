# beewise_test
Тестовое задание, выполненное для компании Bewise.ai.
 Сервис принимает на вход POST запросы с содержимым вида {"questions_num": integer} и получать англоязычные вопросы для викторин и сохранять их в базе данных.

## Установка проекта

### Установите докер
для Windows
```
https://docs.docker.com/desktop/install/windows-install/
```
для Mac
```
https://docs.docker.com/desktop/install/mac-install/
```
для Linux
```
https://docs.docker.com/desktop/install/linux-install/
```
### Развертывание проекта
Клонируйте репозиторий
```
git clone https://github.com/Kulikov1/bewise_test.git
```
Перейдите в папку с проектом
```
cd bewise_test
```
Из директории с проектом запустите сборку контейнеров
```
docker-compose up -d --build
```

## Пример запроса
**POST** http://127.0.0.1:8004/
```
{
  "questions_num ": 3,
}
```
### Ответ:
```
{
  "question_id": 0,
  "question_text": "string",
  "answer_text": "string",
  "created_at": "2023-10-19T06:51:44.663Z"
}
```
Для более детального просмотра запросов запустите проект и перейдите по адресу
```
http://127.0.0.1:8004/docs/
```