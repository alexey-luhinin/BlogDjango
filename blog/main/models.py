from django.db import models


class Category(models.Model):
    title = models.CharField('Название', max_length=255)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Articles(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    title = models.CharField('Название', max_length=100)
    description = models.CharField('Описание', max_length=255)
    text = models.TextField('Текст статьи')
    image = models.ImageField('Изображение', upload_to='img/%Y/%m/%d/')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Comments(models.Model):
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    text = models.TextField('Добавить комментарий')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'

    def __str__(self):
        return str(self.article)
