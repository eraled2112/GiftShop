from django.db import models


class Products(models.Model):
    id = models
    title = models.CharField(max_length=123)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')
    content = models.TextField("Описание", default='Empty')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-created_at']


class Application(models.Model):
    name = models.CharField(max_length=123)
    email = models.EmailField()
    phone = models.CharField(max_length=123)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Заявка от: {self.name} - {self.email}'

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
