from django.db import models

# Create your models here.
class EmployeeManagement(models.Model):
    employee_code = models.IntegerField()
    name = models.CharField(max_length=45)
    email_id = models.EmailField(max_length=45)
    contact_no = models.CharField(max_length=10)
    class Meta:
        db_table="EmployeeManagement"

