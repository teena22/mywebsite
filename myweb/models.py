from django.db import models

class Msg(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=500)
    subject = models.CharField(max_length=500)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    checked = models.BooleanField(default=False)
    
    def __unicode__(self):
        return ("%s (%s)" % (self.name, self.email))

