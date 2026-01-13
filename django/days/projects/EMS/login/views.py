from django.shortcuts import render, redirect
from employee.models import Employee
from django.contrib.auth import logout




def logout_view(request):
    logout(request)
    return redirect("login")



def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        employee_id = request.POST.get("employee_id")

        try:
            emp = Employee.objects.get(email=email, employee_id=employee_id)
            request.session["employee_id"] = emp.id
            return redirect("employee_profile")
        except Employee.DoesNotExist:
            return render(request, "login/login.html", {
                "error": "Invalid credentials"
            })

    return render(request, "login/login.html")
