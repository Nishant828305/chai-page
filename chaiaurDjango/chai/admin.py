from django.contrib import admin
from .models import chaivariety,chaiReview,chaiCertificate,store
# Register your models here.

class chaiReviewInline(admin.TabularInline):
   model =chaiReview
   extra = 2
   
class chaivarietyAdmin(admin.ModelAdmin):
  list_display =('name','chai_type')
  inlines =[chaiReviewInline] 
  
class storeAdmin(admin.ModelAdmin):
  list_display =('name','location')
  filter_horizontal =('chai_varieties',)
  
class chaiCertificateAdmin(admin.ModelAdmin):
  list_display= ('chai','certificate_number')   
     
admin.site.register(chaivariety,chaivarietyAdmin)
admin.site.register(store,storeAdmin)
admin.site.register(chaiCertificate,chaiCertificateAdmin)