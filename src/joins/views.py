from django.shortcuts import render
from django.conf import settings
from .forms import EmailForm, JoinForm
from .models import Join


# Create your views here.


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
    if form.is_valid():
        #new_join = form.save(commit=False)
        email = form.cleaned_data['email']
        new_join, created = Join.objects.get_or_create(email=email)
        if created:
            print "This obj was created"
        #new_join.save()

    context = {
        "name": "sahai",
         "form": form,
    }
    return render(request, "home.html", context)
