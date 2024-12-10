from django.db import models

class menu_items(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    login_logout = models.CharField(max_length=200, choices=[('LOGIN', 'Login'), ('LOGOUT', 'Logout')])
    def __str__(self):
        return self.title
