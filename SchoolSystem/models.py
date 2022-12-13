from django.db import models
from django.utils import timezone

# Create your models here.
class Trade(models.Model):
    trade = models.CharField(max_length=63)
    
    def __str__(self):
        return self.trade

class Graduate_year(models.Model):
    g_year = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return self.g_year

class Fixed_Fee(models.Model):
    first_fixed_fee = models.CharField(max_length=255, blank=True, null=True)
    second_fixed_fee = models.CharField(max_length=255, blank=True, null=True)
    third_fixed_fee = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return f"School Fees : 1st Term = {self.first_fixed_fee}, 2nd Term = {self.second_fixed_fee}, 3rd Term = {self.third_fixed_fee}"


class Fixed_Fee_Day(models.Model):
    first_fixed_fee_day = models.CharField(max_length=255, blank=True, null=True)
    second_fixed_fee_day = models.CharField(max_length=255, blank=True, null=True)
    third_fixed_fee_day = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return f"School Fees : 1st Term = {self.first_fixed_fee_day}, 2nd Term = {self.second_fixed_fee_day}, 3rd Term = {self.third_fixed_fee_day}"



class Student(models.Model):
    # Student Personal Info
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    dob = models.DateField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True)
    index_no = models.CharField(max_length=255, null=True, blank=True)
    trade = models.CharField(max_length=255, null=True, blank=True)
    level = models.CharField(max_length=255, blank=True, null=True)
    start_year = models.CharField(max_length=255, blank=True, null=True)
    graduated = models.CharField(max_length=255, null=True, blank=True)
    g_year = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    
     
    # Student's Parent Info
    father_names = models.CharField(max_length=255, null=True, blank=True)
    mother_name = models.CharField(max_length=255, null=True, blank=True)
    father_id = models.CharField(max_length=255, null=True, blank=True)
    father_tel = models.CharField(max_length=255, null=True, blank=True)
    mother_tel = models.CharField(max_length=255, null=True, blank=True)
    
    # Student's Location Info
    province = models.CharField(max_length=255, null=True, blank=True)
    district = models.CharField(max_length=255, null=True, blank=True)
    sector = models.CharField(max_length=255, null=True, blank=True)
    village = models.CharField(max_length=255, null=True, blank=True)
    
    # Financial Section 
    
    first_term_fee = models.CharField(max_length=255, null=True, blank=True, default=0)
    second_term_fee = models.CharField(max_length=255, null=True, blank=True, default=0)
    third_term_fee = models.CharField(max_length=255, null=True, blank=True, default=0)
    
    
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"



# class PaymentInfo(models.Model):
#     student_first_name = models.CharField(max_length=255)
#     student_last_name = models.CharField(max_length=255)

#     payment_date = models.DateField(auto_now_add=True)

#     first_term_payment = models.CharField
