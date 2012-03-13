from django.db import models
from django.db.models import Count

class Parish(models.Model):
    name=models.CharField(max_length=100, blank = True)
    address_line1 = models.CharField("Address line 1", max_length = 45, blank = True)
    address_line2 = models.CharField("Address line 2", max_length = 45, blank = True)
    city = models.CharField("City", max_length = 50, blank = True)
    state_province = models.CharField("State/Province", max_length = 40, blank = True)
#    member_id = models.ForeignKey(Members)

    def __unicode__(self):
        return self.name+" "+self.address_line1+" "+self.address_line2+" "+self.city
    
# Create your models here.
class Member(models.Model):
    last_name = models.CharField("Last name", max_length=50, blank = False)
    first_name = models.CharField("First name", max_length=50, blank = False)
    middle_name = models.CharField("Middle name", max_length=50, blank = True)
    dob = models.DateField("Date of birth", blank = True, null = True)
    cell = models.CharField("Cell", max_length=20, blank = True)
    phone = models.CharField("Phone", max_length=20, blank = True)
    email = models.EmailField("Email", blank = True)
    address_line1 = models.CharField("Address line 1", max_length = 45, blank = True)
    address_line2 = models.CharField("Address line 2", max_length = 45, blank = True)
    city = models.CharField("City", max_length = 50, blank = True)
    postal_code = models.CharField("ZIP/Postal code", max_length = 10, blank = True)
    state_province = models.CharField("State/Province", max_length = 40, blank = True)
    country = models.CharField("Country", max_length = 40, blank = True)
    prayer_group_code = models.CharField("Area Prayer Group Number", max_length=10, blank = True)
    house_name=models.CharField("House name", max_length=50, blank=True)
    parish_id = models.ForeignKey(Parish)
    

    class meta:
        ordering = ['last_name']
        
    def get_fulladdress(self):
        return self.address_line1 +" "+self.address_line2 +" "+ self.city+" "+self.postal_code+" "+self.state_province
    get_fulladdress.short_description = 'Address'
    
    #===========================================================================
    # def get_familycount(self):
    #    membersfamily.member_count = self.objects.annotate(family_count=Count(''))
    #===========================================================================
        
    def __unicode__(self):
        return self.last_name+" "+self.first_name+" "+self.middle_name
  

class FamilyMember(models.Model):
    relationship_choices = (
        (u'C', u'Child'),
        (u'P', u'Parent'),
        (u'S', u'Spouse'),
        (u'B', u'Sibling'),
        
    )
    last_name = models.CharField("Last name", max_length=50, blank = True)
    first_name = models.CharField("First name", max_length=50, blank = True)
    middle_name = models.CharField("Middle name", max_length=50, blank = True)
    dob = models.DateField("Date of birth", blank = True, null = True)
    email = models.EmailField("Email", blank = True)
    relationship = models.CharField(max_length=1, choices=relationship_choices)
    member_id = models.ForeignKey(Member)

    def __unicode__(self):
        return self.last_name+" "+self.first_name+" "+self.middle_name
        