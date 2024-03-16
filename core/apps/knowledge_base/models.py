from django.db import models

class Solution(models.Model):
    problem_type = models.CharField(max_length=100)
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return f"{self.problem_type}: {self.question}"
