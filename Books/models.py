from django.db import models


class Books(models.Model):
 
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=30)
    publication_date = models.DateTimeField('publication date')
    genre = models.CharField(max_length=200)
    pages = models.IntegerField()


    def __str__(self):
        return f"{self.title} by {self.author}"

class Feedback(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    feedback_text = models.TextField()

    def __str__(self):
        return f"Feedback for {self.book.title}"
