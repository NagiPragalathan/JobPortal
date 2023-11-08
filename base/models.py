from django.db import models
from datetime import datetime
# Create your models here.



class UserData(models.Model):
    userdata_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=255)
    mailid = models.EmailField()
    linkedin = models.URLField(blank=True)
    githublink = models.URLField(blank=True)
    skills = models.CharField(max_length=255, blank=True)# python, sql, java
    experience=models.CharField(max_length=255, blank=True)# 3, 2, 4
    location = models.CharField(max_length=255)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True)
    resume = models.FileField(upload_to='resumes/', blank=True)
    dateofbirth = models.DateField()
    about = models.TextField(blank=True)
    phone_no = models.CharField(max_length=15, blank=True)
    job_nature_looking_for = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    education = models.CharField(max_length=100)

    def __str__(self):
        return self.user_name
    
    
class CompanyDetails(models.Model):
    company_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    company_name = models.CharField(max_length=100)
    company_ceo_name = models.CharField(max_length=100)
    company_mail = models.EmailField()
    company_site = models.URLField()
    company_description = models.TextField(null=True, blank=True)
    company_logo = models.ImageField(upload_to='company_logos/', null=True, blank=True)
    company_linkedin = models.URLField(null=True, blank=True)
    company_location = models.CharField(max_length=100, null=True, blank=True)
    starting_year = models.DateField()
    employees = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.company_name
    
    
class JobPost(models.Model):
    post_id = models.IntegerField(primary_key=True)
    company_id = models.IntegerField()
    user_id = models.IntegerField()
    job_title = models.CharField(max_length=100)  # New field for job title
    job_description = models.CharField(max_length=300)
    posted_date = models.DateField()
    location = models.CharField(max_length=100)
    vacancy = models.PositiveIntegerField()
    job_nature = models.CharField(max_length=100)
    salary_from = models.PositiveIntegerField()
    salary_to = models.PositiveIntegerField()
    application_date = models.DateField()
    skills_req = models.CharField(max_length=300)
    experience = models.PositiveIntegerField()
    education = models.CharField(max_length=100)
    posted_time = models.DateField(default=datetime.now())
    def __str__(self):
        return self.job_title
    
    