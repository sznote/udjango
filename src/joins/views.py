from django.shortcuts import render
from django.conf import settings
from .forms import EmailForm, JoinForm
from .models import Join


# Create your views here.
def get_ip(request):
    try:
        x_forward = request.META.get("HTTP-X_FORWARDED_FOR")
        if x_forward:
            ip = x_forward.split(",")["0"]
        else:
            ip = request.META.get("REMOTE_ADDR")
    except:
        ip = ""
    return ip

# ctr + slash  comment
# ctr + Alt + L reformtting  code

def home(request):
    #   print settings.BASE_DIR

    # This is  using  regular django forms

    # form = EmailForm(request.POST or None)
    # if form.is_valid():
    #     email = form.cleaned_data['Email']
    #     new_join, created =  Join.objects.get_or_create(email=email)
    #     print new_join, created
    #     print new_join.timestamp
    #
    #     if created:
    #         print "This obj was created"

    # This is using model forms

    form = JoinForm(request.POST or None)
    #ip_addr = request.META['REMOTE_ADDR']
    #print request.META.get("HTTP_X_FORWARDED_FOR")

    if form.is_valid():
        #new_join = form.save(commit=False)
        email = form.cleaned_data['email']
        ip_addr=get_ip(request)
        new_join, created = Join.objects.get_or_create(email=email,ip_address=ip_addr)
        if created:
            print "This obj was created"
            #new_join.ip_address = get_ip(request)
            #new_join.save()


    context = {
        "name": "sahai",
         "form": form,
    }
    return render(request, "home.html", context)
