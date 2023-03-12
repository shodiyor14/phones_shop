from django.db import models


class PhonesModelsCategory(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class PhonesColorModel(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'color'
        verbose_name_plural = 'colors'


class PhonesBrandModel(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brands'


class PhonesTagModel(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'


class PhonesModel(models.Model):
    title = models.CharField(max_length=100)
    price = models.CharField(max_length=60)
    os = models.CharField(max_length=30)
    long_descriptions = models.TextField()
    short_descriptions = models.TextField()
    ram = models.CharField(max_length=50)
    memory_card = models.CharField(max_length=50)
    image = models.ImageField(upload_to='phone')
    number_of_sim_cards = models.CharField(max_length=50)
    category = models.ForeignKey(PhonesModelsCategory, on_delete=models.PROTECT, related_name='phone')
    color = models.ManyToManyField(PhonesColorModel, related_name='phone')
    brand = models.ForeignKey(PhonesBrandModel, on_delete=models.PROTECT, related_name='phone')
    tag = models.ManyToManyField(PhonesTagModel, related_name='phone')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'phone'
        verbose_name_plural = 'phones'
