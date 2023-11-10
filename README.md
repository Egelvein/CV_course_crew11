# Проект по нахождению дефектов на электронных платах
Наша программа распознаёт 6 дефектов на печатных платах, такие как:
1. Missing hole
2. Mouse bite
3. Open circuit
4. Short
5. Spur
6. Spurious copper

## Содержание
- [Технологии](#технологии)
- [Системные требования](#системные-требования)
- [Architecture](#architecture)
- [Deploy](#deploy)
- [Использование](#использование)
- [Dataset](#dataset)
- [Ограничения](#ограничения)
- [Метрика успеха](#метрика-успеха)
- [Contributing](#contributing)
- [FAQ](#faq)
- [Команда проекта](#команда-проекта)
- [Ссылки](#ссылки)


### Технологии
- [YOLOv5](https://github.com/ultralytics/yolov5)
- [YOLOv8](https://github.com/ultralytics/ultralytics)
- [Django](https://www.djangoproject.com)
- [ClearML](https://clear.ml)

### Системные требования 
Заполним после создания и упаковки проекта

### Architecture 

![ml_pipeline.jpg](images/ml_pipeline.jpg)

### Deploy
Система состоит из трёх сервисов: 

- Django — веб-приложение которое предоставит возможность пользователю загрузки фотографии микросхемы
- RabbitMQ — как broker задач для организации очереди сообщений между моделью и приложением
- Fast API — программный интерфейс для отправки результатов работы модели YOLO

С помощью Docker compose систему можно запустить по следующим шагам:

- Склонируйте данной репозиторий
- Запустите docker на своей машине
- ```sudo docker-compose build```
- ```sudo docker-compose -d```

⚠️ **disclaimer:** эта версия является тестовой, и выполняет задачу демонстрации итогов курса по компьютерному зрению.
### Пример запроса

`**POST` /file/**

Метод принимает файл изображения

```json
{
	"file": "chip.jpg",
}

```

И возвращает результаты детекции модели

```json
{
	"results": [
        {
            "contour": [
                218.35411071777344,
                0.08491215109825134,
                263.51812744140625,
                27.211015701293945
            ],
            "probability": 0.9038012623786926,
            "class": "missing_hole"
        },
        {
            "contour": [
                190.349609375,
                267.39935302734375,
                223.65646362304688,
                305.36553955078125
            ],
            "probability": 0.8265805244445801,
            "class": "missing_hole"
        }
    ]
}

```
### Использование
Здесь будет инструкция для пользователя, что и как делать

### Dataset
Ссылка на датасет находится внизу файла. 
Датасет содержит в себе 10668 изображений 6 разных классов. Изначально изображений было 2 667,
но над ними была проведена предобработка (составителями датасета), каждое изображение представлено в 4 видах (исходное, повернутые на 90 и 270 градусов, затемненное).

1. Missing hole - 1832 изображения
2. Mouse bite - 1852 изображения
3. Open circuit - 1740 изображений
4. Short - 1732 изображения
5. Spur - 1752 изображения
6. Spurious copper - 1760 изображений

Для версионирования датасета использовали ClearML, можете склонировать наш репозиторий напрямую оттуда, выполнив в терминале следующий код:

```clearml-data get --id 4b1238c811244b8588510687832ad98f```

Касательно разметки нашего датасета можно оперировать следующими цифрами:

*Разметка датасета = 2 667(количество фото) * 4(версии изображения) * 2(усредненное количество дефектов) * 1 рубль(стоимость разметки 1 дефекта) = 21 336 рубля (если брать данные о стоимости разметки из [этой статьи](https://yandex.ru/blog/toloka/case-study-japan))* 

### Ограничения
В качестве огрничений на данный момент можно выделить следующие вещи:
1. Частота кадров в секунду - 4 (т.к. время отклика модели составляет 200-250 мс)

### Метрика успеха
В качестве бизнес-метрики мы используем сокращение расходов предприятия и времени обследования платы за счет замещения контролеров 
РЭА разрабатываемым сервисом.

В качестве метрики оценки успешности экспериментов использовалась mAP50-95 (mean Average Precision в диапазоне [0.50: 0.05: 0.95]: от 0,5 до 0,95 с размером шага 0,05. Изначально была поставлена цель добиться её значения не ниже 0,9, что и получилось в эксперименте 8 - добились mAP50-95 = 0.9289

### Contributing
Если Вы желаете принять участие в разработке проекта, дать обратную связь или пожаловаться на возникающие ошибки - пишите на почту кому-нибудь из команды проекта (ниже).

### FAQ
Будем заполнять по мере появления ошибок при использовании проекта

### Команда проекта
- DE + ML + PM - [Елизавета Талынкова]
- ML + Back-end - [Мулхам Шахин](https://www.linkedin.com/in/mulham-shaheen-684352206/)
- DE + ML - [Синяев Вячеслав](https://www.linkedin.com/in/vyacheslavsinyaev/) 

### Ссылки
- Ссылка на исходный датасет - [здесь](https://www.dropbox.com/s/h0f39nyotddibsb/VOC_PCB.zip?dl=0)
- Описание датасета на kaggle - [здесь](https://www.kaggle.com/datasets/sudharshann/pcb-defect-dataset)
- Ссылка на получившийся датасет - [здесь](https://drive.google.com/drive/folders/1RbKRm6jYgw1rHkB8_KPg4Eu-Q_fVcrPc?usp=sharing)

