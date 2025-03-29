from django.shortcuts import render,redirect,get_object_or_404
from .models import App
from UserFacing.models import CustomUser,UserDownload
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages

#home page function 
def home(request):
    # check if user already admin
    if request.user.is_authenticated and request.user.is_superuser:
        return redirect(admin_dashboard)
    
    #using this for login admin with admin cradentials only
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            messages.success(request, "You're logged in as a admin!")
            return redirect(admin_dashboard)
        else:
            messages.error(request, "Enter valid admin credentials")
            return redirect('home')
        
    return render(request, 'admin_login_signup.html')

# dashboard function for ADMIN
@login_required
def admin_dashboard(request):
    apps = App.objects.all().order_by('-created_at')
    users = CustomUser.objects.all().order_by('-created_at')
    categories = [choice[0] for choice in App.CATEGORY_CHOICES]
    subcategories = [choice[0] for choice in App.SUBCATEGORY_CHOICES]
    context = {
        'apps': apps,
        'categories': categories,
        'subcategories': subcategories,
        'users':users
    }
    return render(request, 'admin_panel.html', context)


#  function for add app to the website
@login_required
def add_app(request):
    if request.method == "POST":
        appimage = request.FILES.get("app_image")
        appname = request.POST.get("appName")
        applink = request.POST.get("appLink")
        appcategory = request.POST.get("appCategory")
        subcategory = request.POST.get("subcategory")
        points = request.POST.get("points")

        #  validation for adding an app
        if appimage and appname and applink and appcategory and subcategory and points:
            app = App(
                app_image=appimage,
                app_name=appname,
                download_link=applink,
                app_category=appcategory,
                subcategory=subcategory,
                points=int(points), 
            )
            app.save()
            messages.success(request, "App added successfully!")
            return redirect("admin_dashboard")
        else:
            messages.error(request, "All fields are required.")

    return render(request,"add_app.html")


# fuction for update app
@login_required
def update_app(request, id):
    app = get_object_or_404(App, id=id)
    
    if request.method == "POST":
        appimage = request.FILES.get("app_image")
        appname = request.POST.get("appName")
        applink = request.POST.get("appLink")
        appcategory = request.POST.get("appCategory")
        subcategory = request.POST.get("subcategory")
        points = request.POST.get("points")

        # Update fields
        app.app_name = appname
        app.download_link = applink
        app.app_category = appcategory
        app.subcategory = subcategory
        app.points = int(points) if points else app.points

        # Update image only if a new one is provided
        if appimage:
            app.app_image = appimage

        app.save()
        messages.success(request, "App updated successfully!")
        return redirect("admin_dashboard")

    return render(
        request,
        "update_app.html",
        {
            "app": app,
            "categories": [choice[0] for choice in App.CATEGORY_CHOICES],
            "subcategories": [choice[0] for choice in App.SUBCATEGORY_CHOICES],
        },
    )
    

#  function for get userdetails
@login_required
def userInfo(request, id):
    user = get_object_or_404(CustomUser, uid=id)
    userdownloadapps = UserDownload.objects.filter(user = user).order_by('-downloaded_at') 
    return render(request, 'user_info.html',{'apps':userdownloadapps})


# fuction for check the validatet image
@login_required
def app_not_valid(request, app_id):
    user_download = get_object_or_404(UserDownload, id=app_id)
    targetuser_id = user_download.user.uid
    user_download.delete()
    messages.success(request, "App Reward is deleted from the User account.")
    return redirect('userinfo', id=targetuser_id)


# function for delete an App 
@login_required
def deleteApp(request, id):
    app = get_object_or_404(App, id=id)
    app.delete()
    messages.success(request, f"{app.app_name} deleted successfully!")
    return redirect(admin_dashboard)


# logout functiom
@login_required
def adminlogout(request):
    logout(request)
    messages.success(request, "You're logged out")
    return redirect("/")