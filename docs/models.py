from django.db import models

# Create your models here.
class Doc(models.Model):
    title = models.CharField(max_length=10000)
    content = models.CharField(max_length=1000000)
    word_count = models.IntegerField(null=False, blank=False)
    char_count = models.IntegerField(null=False, blank=False)
    creation_date = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"Id {self.id} | Title: {self.title}"