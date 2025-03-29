from AdminFacing.models import App
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import CustomUser, OTP
from .utills import generate_otp, send_otp
from django.db.models import Sum
import re


# home page for user login 
def index(request):
    # check if the user is already loggedin
    if request.user.is_authenticated and not request.user.is_superuser:
        return redirect('user_dashboard')

# user authentication
    if request.method == "POST":
        phone_number = request.POST.get('phone')
        username = request.POST.get('username')

        # Clean and validate the phone number
        if phone_number:
            phone_number = re.sub(r'\D', '', phone_number)
            if not len(phone_number) == 10:
                messages.error(request, 'Invalid phone number. Please enter a 10-digit number.')
                return render(request, 'user_login_signup.html')
        else:
            messages.error(request, 'Phone number is required.')
            return render(request, 'user_login_signup.html')
        # create the user 
        try:
            user = CustomUser.objects.get(phone_number=phone_number)
        except CustomUser.DoesNotExist:
            user = CustomUser.objects.create_user(
                phone_number=phone_number,
                username=username,
                email='' 
            )
            messages.success(request, 'User created. Please verify your phone number.')
            
# creating OTP for the USER Auth 
        otp_value = generate_otp()
        send_otp(phone_number, otp_value)
        OTP.objects.create(user=user, otp=otp_value)
        request.session['user_id'] = user.id
        return redirect('verify_otp')

    else:
        return render(request, 'user_login_signup.html')
    
#  funtion for user varification with OTP verification
def verify_otp(request):
    user_id = request.session.get('user_id')
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST':
        otp1 = request.POST.get('otp1')
        otp2 = request.POST.get('otp2')
        otp3 = request.POST.get('otp3')
        otp4 = request.POST.get('otp4')
        otp5 = request.POST.get('otp5')
        otp6 = request.POST.get('otp6')
        otp_value = otp1+otp2+otp3+otp4+otp5+otp6
        try:
            otp_obj = OTP.objects.filter(user=user).latest('timestamp')
            if otp_obj.otp == otp_value and otp_obj.is_valid():
                login(request, user)
                # Set is_verified to True
                user.is_verified = True
                user.save()
                messages.success(request, 'Welcome to Rewards App.')
                return redirect('user_dashboard')
            else:
                messages.error(request, 'Invalid OTP.')
                return render(request, 'verify_otp.html')
        except OTP.DoesNotExist:
            messages.error(request, 'OTP not found.')
            return render(request, 'verify_otp.html')
    return render(request, 'verify_otp.html')


#  function for user dashboard
@login_required
def user_dashboard(request):
    # getting the downlaoded apps in user homer
    downloaded_app_ids = UserDownload.objects.filter(user=request.user, is_downloaded=True).values_list('app_id', flat=True)
    downloaded_apps = App.objects.filter(id__in=downloaded_app_ids).order_by('-created_at')
    not_downloaded_apps = App.objects.exclude(id__in=downloaded_app_ids).order_by('-created_at')
    total_points = downloaded_apps.aggregate(total_points=Sum('points'))['total_points'] or 0
    
    # using for user profile information updation
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        user = CustomUser.objects.get(uid = request.user.uid)
        user.first_name = name
        user.email = email
        user.save()
        messages.success(request, "Your information has been updated.")
        return redirect('user_dashboard')
    context = {
        'downloaded_apps': downloaded_apps,
        'not_downloaded_apps': not_downloaded_apps,
        'total_points':total_points
    }

    return render(request, 'user_panel.html', context)


# function for get the app info and download or upload section
@login_required
def app_info(request, id):
    app = get_object_or_404(App, id=id)
    if request.method == "POST":
        image = request.FILES.get("SS_proof") #correct way to get image.

# using for image uploadation of app screenshot
        if image: #check if image exist
            userdownload = UserDownload(
                user=request.user,
                app=app,
                screenshot=image,
                is_downloaded=True,
            )
            userdownload.save()
            messages.success(request, "You will receive the reward shortly after we review the image you uploaded.")
            return redirect('user_dashboard')
        else:
            messages.error(request,"Please upload a screenshot.")
            return render(request, 'app_info.html', {'app': app})
    return render(request, 'app_info.html',{'app':app})

@login_required
def userlogout(request):
    logout(request)
    messages.success(request, "You're logged out")
    return redirect("/")
