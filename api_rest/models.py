from django.db import models

class User(models.Model):
    user_login = models.TextField(primary_key=True, default='')
    user_password = models.TextField(default='')

    def __str__(self):
        return f'login: {self.user_login} | password: {self.user_password}'