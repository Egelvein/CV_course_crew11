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
Заполним после создания и упаковки проекта

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

