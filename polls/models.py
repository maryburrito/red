from django.db import models


class Question(models.Model):
    active = models.BooleanField(default=True)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def active_str(self):
        if self.active:
            return "[ACTIVE]"
        else:
            return "[INACTIVE]"

    def __str__(self):
        return self.active_str() + ' ' + self.question_text 


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Cat(models.Model):
    legal_name = models.CharField(max_length=17)
    nickname = models.CharField(max_length=13)
    birth_date = models.DateField(null=True, blank=True)