from django.db import models

# 1-klass: Faqat Shashliklar uchun
class Shashlik(models.Model):
    name = models.CharField(max_length=150, verbose_name="Shashlik nomi")
    price = models.CharField(max_length=50, verbose_name="Narxi")
    description = models.TextField(verbose_name="Tarkibi va ma'lumot")
    image_url = models.URLField(max_length=500, verbose_name="Rasm linki")

    def __str__(self):
        return self.name

# 2-klass: Faqat Salatlar uchun
class Salat(models.Model):
    name = models.CharField(max_length=150, verbose_name="Salat nomi")
    price = models.CharField(max_length=50, verbose_name="Narxi")
    description = models.TextField(verbose_name="Tarkibi va ma'lumot")
    image_url = models.URLField(max_length=500, verbose_name="Rasm linki")

    def __str__(self):
        return self.name

# 3-klass: Faqat Yaxna ichimliklar uchun
class YaxnaIchimlik(models.Model):
    name = models.CharField(max_length=150, verbose_name="Ichimlik nomi")
    price = models.CharField(max_length=50, verbose_name="Narxi")
    description = models.TextField(verbose_name="Ma'lumot")
    image_url = models.URLField(max_length=500, verbose_name="Rasm linki")

    def __str__(self):
        return self.name