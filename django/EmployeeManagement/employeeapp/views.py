from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from employeeapp.models import EmployeeManagement
import xlrd
import openpyxl
from .fusioncharts import FusionCharts


def index(request):
    return render(request, 'index.html')

def add(request):
    if request.method == 'GET':
        return render(request, 'add_emp_info.html')
    elif request.method == 'POST':
        employeeCode = request.POST.get("employeeCode")
        name = request.POST.get("name")
        emailId = request.POST.get("emailId")
        contactNo = request.POST.get("contactNo")
        employee_details = EmployeeManagement(
            employee_code=employeeCode, name=name, email_id=emailId, contact_no=contactNo)
        employee_details.save()
        return redirect('/show')


def show(request):
    employee_details = EmployeeManagement.objects.all()
    return render(request, 'show_emp_info.html', context={'employee': employee_details})


def edit(request, employee_code):
    if request.method == 'GET':
        employee_details = EmployeeManagement.objects.get(
            employee_code=employee_code)
        show = {
            "employee_code": employee_details.employee_code,
            "name": employee_details.name,
            "email_id": employee_details.email_id,
            "contact_no": employee_details.contact_no,
        }
        return render(request, 'edit_emp_info.html', context=show)

    elif request.method == 'POST':
        email_id = request.POST.get("emailId")
        contact_no = request.POST.get("contactNo")
        employee_details = EmployeeManagement.objects.get(
            employee_code=employee_code)
        employee_details.email_id = email_id
        employee_details.contact_no = contact_no
        employee_details.save()
        return redirect("/show")


def delete(request, employee_code):
    employee_details = EmployeeManagement.objects.get(
        employee_code=employee_code)
    employee_details.delete()
    return redirect('/show')

# file upload


def upload_file(request):
    if "GET" == request.method:
        return render(request, 'upload_file.html', {})
    else:
        excel_file = request.FILES['excel_file']
        wb = openpyxl.load_workbook(excel_file)
        worksheet = wb["Sheet1"]
        print(worksheet)
        excel_data = list()
        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))
            excel_data.append(row_data)
            employee_detail = EmployeeManagement(
                employee_code=row_data[0], name=row_data[1], email_id=row_data[2], contact_no=row_data[3])
            employee_detail.save()
            employee_detail = EmployeeManagement.objects.all()
        return render(request, 'show_emp_info.html', context={'employee': employee_detail})


def search(request):
    if request.method == 'GET':
        return render(request, "search_emp_info.html")
    elif request.method == 'POST':
        name_to_search = request.POST.get("name")
        employee_details = EmployeeManagement.objects.filter(
            name__iregex=name_to_search)
    return render(request, "search_emp_info.html", context={"employee": employee_details})

def chart(request):
   chartObj = FusionCharts( 'pyramid', 'ex1', '600', '400', 'chart', 'json', """{
  "chart": {
    "theme": "fusion",
    "caption": "Employee Management System",
    "subcaption": "Chart analysis",
    "showvalues": "1",
    "numbersuffix": " trn",
    "numberprefix": "$",
    "plottooltext": "<b>$label</b> of world population owns <b>$dataValue</b> of global wealth",
    "is2d": "0"
  },
  "data": [
    {
      "label": "year 2019",
      "value": "128.7"
    },
    {
      "label": "year 2018",
      "value": "111.4"
    },
    {
      "label": "year 2017",
      "value": "32.5"
    },
    {
      "label": "year 2016",
      "value": "7.6"
    }
  ]
}""")
   return render(request, 'chart.html', {'output': chartObj.render()})