from django.db import models

# Create your models here.
class EmployeeManagement(models.Model):
    employee_code = models.CharField(max_length=20)
    name = models.CharField(max_length=45)
    email_id = models.EmailField(max_length=45)
    contact_no = models.CharField(max_length=40)
    class Meta:
        db_table="EmployeeManagement"

