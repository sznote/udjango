from django.shortcuts import render, HttpResponseRedirect
from django.conf import settings
from .forms import EmailForm, JoinForm
from .models import Join
import uuid


def get_ref_id():
    ref_id = str(uuid.uuid4())[:11].replace('-', '').lower()
    try:
        id_exists = Join.objects.get(ref_id=ref_id)
        get_ref_id()

    except:
        return ref_id

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


def share(request,ref_id):

    #print ref_id
    context = {
        "ref_id": ref_id,
    }
    return render(request, "share.html", context)


def home(request):

    try:
        refer_id = request.session['ref']
        obj = Join.objects.get(id=refer_id)
    except:
        refer_id = None
        obj = None

    print "Refer id is: %s %s" % (refer_id, obj)


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

        '''
        new_join = form.save(commit=False)
        email = form.cleaned_data['email']
        ip_addr=get_ip(request)
        user_ref_id = get_ref_id()
        print user_ref_id

        new_join, created = Join.objects.get_or_create(email=email,ip_address=ip_addr,ref_id=user_ref_id)
        if created:
            print "This obj was created"
            #new_join.ip_address = get_ip(request)
            #new_join.save()
        '''
        #new_join = form.save(commit=False)
        email = form.cleaned_data['email']

        new_join_old, created = Join.objects.get_or_create(email=email)
        if created:
            new_join_old.ref_id  = get_ref_id()
            new_join_old.ip_address = get_ip(request)
            new_join_old.save()
        return HttpResponseRedirect("/%s" %( new_join_old.ref_id ))

    context = {
        "name": "sahai",
         "form": form,
    }
    return render(request, "home.html", context)
