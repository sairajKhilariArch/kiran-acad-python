from django.shortcuts import render, redirect
from employee.models import Employee






def signup(request):
    if request.method == "POST":
        email = request.POST.get("email", "").strip()

        if not email:
            return render(request, "signup/signup.html", {
                "error": "Email is required."
            })

        if Employee.objects.filter(email=email).exists():
            return render(request, "signup/signup.html", {
                "error": "Email already registered. Please login."
            })

        Employee.objects.create(
            employee_id=request.POST.get("employee_id"),
            name=request.POST.get("name"),
            email=email,
            phone=request.POST.get("phone"),
            department=request.POST.get("department"),
            designation=request.POST.get("designation"),
            salary=request.POST.get("salary"),
            date_of_joining=request.POST.get("date_of_joining"),
        )

        return redirect("login")

    return render(request, "signup/signup.html")
