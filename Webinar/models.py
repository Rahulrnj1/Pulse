from enum import unique
from django.db import models

# Create your models here.


class Cities(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=200)
    state_id = models.IntegerField()

    def __str__(self):
        return "{} - {}-{} ".format(self.id,
                                    self.state_id,
                                    self.city,)


class State(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return "{} - {} ".format(self.id,
                                 self.name,
                                 )


class User(models.Model):
    user_type = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70, unique=True)
    mobile = models.CharField(max_length=15)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {} - {}".format(self.user_type,
                                     self.state,
                                     self.email,)


class HCPConnect(models.Model):
    Blog_title = models.CharField(max_length=255, null=True)
    Blog_author = models.CharField(max_length=255, null=True)
    Blog_date = models.DateTimeField(auto_now_add=True, null=True)
    Blog_description = models.TextField()
    Blog_image = models.ImageField(upload_to='image')

    def __str__(self):
        return "{} - {} - {}".format(self.Blog_title,
                                     self.Blog_author,
                                     self.Blog_date)


class WebinarList(models.Model):
    webinar_title = models.CharField(max_length=255, null=True)
    webinar_link = models.CharField(max_length=255, null=True)
    webinar_date = models.DateTimeField()
    webniar_image = models.ImageField(upload_to='image')

    def __str__(self):
        return "{} - {} - {}".format(self.webinar_title,
                                     self.webinar_link,
                                     self.webinar_date)


class Livewebinar(models.Model):
    webinar_title = models.CharField(max_length=255, null=True)
    webinar_link = models.CharField(max_length=255, null=True)
    webinar_date = models.DateTimeField()
    webniar_image = models.ImageField(upload_to='image')

    def __str__(self):
        return "{} - {} - {}".format(self.webinar_title,
                                     self.webinar_link,
                                     self.webinar_date)

class ClinicalTool(models.Model):
    id = models.AutoField(primary_key=True)
    ages = [
        (1,"<65(0 Score)"),
        (2,"65-74(+1 Score)"),
        (3,">=75(+2 Score"),
        ]
    patient_name = models.CharField(max_length=25,null=True )
    score_date = models.DateField(null=True )
    age = models.IntegerField(choices=ages)
    def __str__(self):
        return "{} - {} - {}".format(self.patient_name,
                                     self.score_date,
                                     self.age)


class Clinic(models.Model):
    patient_name = models.CharField(max_length=25,null=True )
    score_date = models.DateField(null=True )


