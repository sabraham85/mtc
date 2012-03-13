from django.contrib import admin
from mtc.membership.models import Member, Parish, FamilyMember

class FamilyMemberInline(admin.TabularInline):
    model = FamilyMember
    extra = 1
    
class MemberAdmin(admin.ModelAdmin):
    inlines = [FamilyMemberInline]
    list_display = ('__unicode__', 'cell', 'phone', 'get_fulladdress')   

admin.site.register(Member, MemberAdmin)
admin.site.register(Parish)
