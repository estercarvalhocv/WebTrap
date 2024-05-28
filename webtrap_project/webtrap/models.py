from django.db import models

class RequestLog(models.Model):
    method = models.CharField(max_length=10)
    url = models.CharField(max_length=255)
    headers = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return f"{self.menthod} {self.url}-{self.timestamp}"

class HoneypotSubmission(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.menthod} {self.url}-{self.timestamp}"