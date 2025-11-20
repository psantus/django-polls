import datetime

from django.db import models, connection
from django.utils import timezone


class Question(models.Model):
    id = models.IntegerField(primary_key=True)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def save(self, *args, **kwargs):
        if not self.pk:
            with connection.cursor() as cursor:
                cursor.execute("SELECT COALESCE(MAX(id), 0) + 1 FROM polls_question")
                self.pk = cursor.fetchone()[0]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    id = models.IntegerField(primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, db_constraint=False, db_index=False)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.pk:
            with connection.cursor() as cursor:
                cursor.execute("SELECT COALESCE(MAX(id), 0) + 1 FROM polls_choice")
                self.pk = cursor.fetchone()[0]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.choice_text

