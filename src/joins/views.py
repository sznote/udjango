from django.shortcuts import render
from django.conf import settings
# Create your views here.


# ctr + slash  comment
# ctr + Alt + L reformtting  code

def home(request):
    print settings.BASE_DIR
    context = {
        "name": "sahai",
    }
    return render(request, "home.html", context)
