from django.db import models


# Create your models here.

class Join(models.Model):
    email = models.EmailField()

    friends = models.ForeignKey("self", related_name="referral", \
                                null=True,blank=True)

    ref_id = models.CharField(max_length=120,default='ABC')
    ip_address = models.CharField(max_length=120,null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        # return "Hi %s %s" % (self.email, self.email)
        return self.email

    class Meta:
        unique_together = ("email", "ref_id", )

#
# class JoinFriends(models.Model):
#     email = models.OneToOneField(Join, related_name="Shared")
#     friends = models.ManyToManyField(Join, related_name="Friend", \
#                                      null=True, blank=True)
#
#     emailall = models.ForeignKey(Join, related_name='emailall')
#
#     def __unicode__(self):
#         print "friends are ", self.friends.all()
#         print  self.emailall
#         print  self.email
#         return self.email.email
