from django.db import models

# Create your models here.
class Accounts(models.Model):

	username = models.CharField(max_length=30)
	email = models.EmailField()
	password = models.CharField(max_length=30)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)


class Project(models.Model):
    prj_name = models.CharField(max_length=140)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    accounts = models.ForeignKey(Accounts, on_delete=models.CASCADE)

    def __str__(self):
        return self.title