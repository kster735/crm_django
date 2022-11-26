from django.db import models

from django.db import connection

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    @staticmethod
    def fetch_all():
        cursor = connection.cursor()
        cursor.execute("SELECT question_text FROM polls_question")
        # # with connection.cursor() as cursor:
        # #     cursor.execute("SELECT * FROM question WHERE id = %s", 1)
        # #     row = cursor.fetchone()
        result = Question.dictfetchall(cursor)
        return result

    @staticmethod
    def dictfetchall(cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

    def __str__(self):
        return str(self.pub_date) + "    " + self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

