from django.db import models
from django.urls import reverse

# Create your models here.
class faculty(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(blank=True,null=True,max_length=50)
    position = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    Research_Areas = models.TextField()
    email = models.EmailField()
    contact_number = models.CharField(max_length=20)
    img = models.ImageField(blank=True,null=True,upload_to="profil_images")

    def __str__(self):
        return self.name

class staff(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    email = models.EmailField()
    contact_number = models.CharField(max_length=20)
    img = models.ImageField(blank=True,null=True,upload_to="profil_images")

    def __str__(self):
        return self.name

class student(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50,blank=True,null=True)
    email = models.EmailField()
    contact_number = models.CharField(max_length=20)
    img = models.ImageField(blank=True,null=True,upload_to="profil_images")

    def __str__(self):
        return self.name

class event(models.Model):
    event_title = models.CharField(max_length=50)
    event_link = models.URLField(null=True,blank=True)
    event_subTitle = models.CharField(null=True,blank=True,max_length=100)
    event_description = models.TextField(max_length=1000)
    event_date = models.DateField(null=True,blank=True)
    event_location = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.event_title

class certificate(models.Model):
    certi_img = models.ImageField(null=True,blank=True,upload_to="certi_images")
    certi_title = models.CharField(max_length=50)

class FAQ(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField(null=True,blank=True)

class project(models.Model):
    title = models.CharField(max_length=100)
    field = models.CharField(max_length=100)
    description = models.TextField()
    sponsor = models.CharField(max_length=100)
    Principal_Investigator = models.CharField(max_length=100)
    link = models.URLField(null=True,blank=True)

    def __str__(self):
        return self.title

class applicant(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.CharField(max_length=12)
    experience = models.IntegerField()
    company = models.CharField(max_length=100)
    designation = models.CharField(max_length=200)
    city_choice = (('Bgl','Bengaluru'),('kgp','Kharagpur'))
    city = models.CharField(
        max_length = 3,
        choices = city_choice,
        default = 'Kharagpur'
    )
    fee_status_chioces = (('NP','Not paid'),('PP','Partially Paid'),('FP','Fully Paid'))
    fee_status = models.CharField(null=True,blank=True,
        max_length=2,
        choices=fee_status_chioces,
        default='NP',
    )
    amount_paid = models.IntegerField(null=True,blank=True)
    applicant_status_choices = (('NV','Not yet verified'),('AV','Application verified'),('CC','Course completed'))
    applicant_status = models.CharField(null=True,blank=True,
        max_length=2,
        choices=applicant_status_choices,
        default='NV',
    )
    
    def __str__(self):
        return self.first_name + " " + self.last_name + "-fee-|" + self.fee_status + "|- -|"+ self.applicant_status + "|+" 

    def get_absolute_url(self):
        return reverse('applyResponse')

class notice(models.Model):
    topic = models.CharField(max_length=20,null=True,blank=True)
    message = models.TextField()
    link = models.URLField(null=True,blank=True)
    notice_end_date = models.DateField(null=True,blank=True)

