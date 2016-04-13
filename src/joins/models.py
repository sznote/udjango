from django.db import models


# Create your models here.

class Join(models.Model):
    email = models.EmailField()
    ref_id = models.CharField(max_length=120,default='ABC')
    ip_address = models.CharField(max_length=120,null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        # return "Hi %s %s" % (self.email, self.email)
        return self.email

    class Meta:
        unique_together = ("email", "ref_id", )