from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.models import auth
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Patient,Doctor
from django.contrib.auth.hashers import make_password




def signin(request):
    if request.method == 'POST':
        user_type = request.POST.get('user_type')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        profile_picture = request.FILES.get('profile_picture')
        address_line1 = request.POST.get('address_line1')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        if password1 == password2:
                # Check if the username already exists
                if User.objects.filter(username=username).exists():
                    messages.error(request, 'Username already exists!')
                    return render(request,"index.html")
                
                else:
                    try:
                        user = User.objects.create(
                            username=username,
                            email=email,
                            #password=password1,  # Directly pass the password
                            first_name=first_name,
                            last_name=last_name,
                        )
                        user.password = make_password(password1)
                        user.save()
                        
                        if user_type=="patient":
                            Patient_o = Patient.objects.create(
                                user=user,
                            profile_picture=profile_picture,
                            address_line1=address_line1,
                            city=city,
                            state=state,pincode=pincode
                            )
                            Patient_o.save()
                            messages.success(request, ' member added successfully!')
                        
                            return redirect('login')
                        else:
                            Doctor_o = Doctor.objects.create(
                                user=user,
                              
                            profile_picture=profile_picture,
                            address_line1=address_line1,
                            city=city,
                            state=state,pincode=pincode
                            )
                            Doctor_o.save()
                        
                            messages.success(request, ' member added successfully!')
                            return redirect('login')
                    except Exception as e:
                        
                        messages.error(request, f'An error occurred while saving the data: {e}')
                        return redirect('signin')
        else:
            messages.error(request, 'Passwords do not match!')
            return redirect('signin')
    else:
        return render(request, "index.html")
    

     
def Patient1(request):
    patients = Patient.objects.all()
    return render(request, 'Patient.html', {'patients': patients})

def Doctor1(request):
    doctor = Doctor.objects.all()
    return render(request,"Doctor.html", {'doctor' : doctor})


def login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user_type = request.POST.get('user_type')

        user=auth.authenticate(request,username=username,password=password)
    
        if user is not None:
            userRole=user_type
            if userRole=='patient':
                auth.login(request,user)
                return redirect('Patient1')
            elif userRole=='doctor':
               auth.login(request,user)
               return redirect('Doctor1')
            else:
                messages.error(request,'Invalid Credentials! Please try again with correct credentials.')
                return redirect('login')

        else:
            messages.info(request,"invalid credentials...")
            return redirect('login')
    else:
        return render(request,"login.html")


def logout(request):
    auth.logout(request)
    return redirect("login")
