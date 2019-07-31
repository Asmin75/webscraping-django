from django.db import models

# Create your models here.
# from jsonfield import JSONField


class ScrapyItem(models.Model):
    # unique_id = models.CharField(max_length=100, null=True)
    # quotes_data = JSONField()
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    # tags = models.CharField(max_length=500)