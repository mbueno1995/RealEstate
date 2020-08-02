from django.contrib import admin
from property.models import Property
from property.models import Contact
from property.models import Customer

# Register your models here.
class PropertyAdmin(admin.ModelAdmin):
    list_display=('name','BDS','BA','location','state','city','zipcode','price','purpose','images','type')
    list_filter=('state','city','zipcode','purpose')
    list_editable=('BDS','BA','location','state','city','zipcode','price','purpose','images','type')
admin.site.register(Property,PropertyAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display=('agentID','agentLname','agentFname','contactNum','emailAddr','requirements')
    list_filter=('agentLname','agentFname','contactNum','emailAddr','requirements')
    list_editable=('agentLname','agentFname','contactNum','emailAddr','requirements')
admin.site.register(Contact,ContactAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display=('custEmail','custFname','custLname','occupation','custZipcode','custPhone')
    list_filter=('custFname','custLname','occupation','custZipcode','custPhone')
    list_editable=('custFname','custLname','occupation','custZipcode','custPhone')
admin.site.register(Customer,CustomerAdmin)
