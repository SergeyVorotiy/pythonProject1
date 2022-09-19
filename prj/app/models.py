from django.db import models

# Create your models here.
class FileWordCounts(models.Model):
    text = models.TextField(default='', blank=True)
    file = models.FileField(upload_to='media/', default='', blank=False)

    def set_text(self):
        file = open(self.file.path, 'r')
        textk = ''
        text_l = file.readlines()
        for i in text_l:
            textk += i
        self.text = textk
        self.save()
        file.close()

    @classmethod
    def word_count(cls, word):
        count = 0
        for obj in cls.objects.all():
            count += obj.text.split(' ').count(word)
        return count

    @classmethod
    def uni_count(cls):
        unicount = 0
        text_l = []
        for obj in cls.objects.all():
            text_l.extend(obj.text.split(' '))
        for word in text_l:
            if text_l.count(word) == 1:
                unicount += 1
        return unicount
