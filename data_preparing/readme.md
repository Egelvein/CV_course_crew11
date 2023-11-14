## Dataset
The link to the dataset is at the bottom of the readme in the root directory. 
The dataset contains 10668 images of 6 different classes. Originally there were 2,667 images,
but they were preprocessed (by the authors of the dataset), each image is presented in 4 views (original, rotated by 90 and 270 degrees, darkened).

1. Missing hole - 1832 images
2. Mouse bite - 1852 images
3. Open circuit - 1740 images
4. Short - 1732 images
5. Spur - 1752 images
6. Spurious copper - 1760 images

We used ClearML to version the dataset, you can clone our repository directly from there by executing the following code in the terminal:

```clearml-data get --id 4b1238c8112121244b8588510687832ad98f```.

Regarding the markup of our dataset, we can operate with the following numbers:

*Dataset markup = 2,667(number of photos) * 4(image versions) * 2(average number of defects) * 1 ruble (cost of markup of 1 defect) = 21,336 rubles (if we take the data on markup cost from [this article](https://yandex.ru/blog/toloka/case-study-japan))* 
