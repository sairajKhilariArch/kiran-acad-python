
from django.shortcuts import render, redirect,get_object_or_404
from .models import Employee
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator




def is_admin(user):
    return user.is_staff or user.is_superuser





@login_required
@user_passes_test(is_admin)
def employee_list(request):
    q = request.GET.get("q", "")
    employees = Employee.objects.filter(name__icontains=q)

    paginator = Paginator(employees, 5)
    page = request.GET.get("page")
    employees = paginator.get_page(page)

    return render(request, "employee/list.html", {"employees": employees, "q": q})



def profile(request):
    emp_id = request.session.get("employee_id")

    if not emp_id:
        return redirect("login")

    employee = Employee.objects.get(id=emp_id)
    return render(request, "employee/profile.html", {"employee": employee})



@login_required
@user_passes_test(is_admin)
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, "employee/list.html", {"employees": employees})





@login_required
@user_passes_test(is_admin)
def employee_detail(request, pk):
    emp = get_object_or_404(Employee, pk=pk)
    return render(request, "employee/detail.html", {"employee": emp})




@login_required
@user_passes_test(is_admin)
def employee_create(request):
    if request.method == "POST":
        Employee.objects.create(
            employee_id=request.POST["employee_id"],
            name=request.POST["name"],
            email=request.POST["email"],
            phone=request.POST["phone"],
            department=request.POST["department"],
            designation=request.POST["designation"],
            salary=request.POST["salary"],
            date_of_joining=request.POST["date_of_joining"],
        )
        return redirect("employee_list")

    return render(request, "employee/form.html")



@login_required
@user_passes_test(is_admin)
def employee_update(request, pk):
    emp = get_object_or_404(Employee, pk=pk)

    if request.method == "POST":
        emp.employee_id = request.POST["employee_id"]
        emp.name = request.POST["name"]
        emp.email = request.POST["email"]
        emp.phone = request.POST["phone"]
        emp.department = request.POST["department"]
        emp.designation = request.POST["designation"]
        emp.salary = request.POST["salary"]
        emp.date_of_joining = request.POST["date_of_joining"]
        emp.save()
        return redirect("employee_list")

    return render(request, "employee/form.html", {"employee": emp})



@login_required
@user_passes_test(is_admin)
def employee_delete(request, pk):
    emp = get_object_or_404(Employee, pk=pk)

    if request.method == "POST":
        emp.delete()
        return redirect("employee_list")

    return render(request, "employee/confirm_delete.html", {"employee": emp})




@login_required
@user_passes_test(is_admin)
def dashboard(request):
    return render(request, "employee/dashboard.html", {
        "total": Employee.objects.count(),
    })
