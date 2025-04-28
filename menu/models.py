from django.db import models
from django.urls import reverse, NoReverseMatch


class Menu(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, null=True, default=None)

    def get_absolute_url(self):
        return reverse('menu', kwargs={'menu_slug': self.slug})

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    title = models.CharField(max_length=100)
    # url = models.CharField(max_length=200, blank=True)
    # named_url = models.CharField(max_length=100, blank=True)

    # def get_absolute_url(self):

        # if self.named_url:
        #     try:
        #         return reverse(self.named_url)
        #     except NoReverseMatch:
        #         return self.url
        # return self.url

    def __str__(self):
        return self.title
