from django.contrib import admin
from .models import *
# Register your models here.
# class slideAdmin(admin.ModelAdmin):
#     list_display=['tieuDe','noiDung','anhNen']
#     search_fields=['tieuDe']
# admin.site.register(Slide,slideAdmin)
class reviewAdmin(admin.ModelAdmin):
    list_display=['hoTen','noiDung','anhNen']
class discountAdmin(admin.ModelAdmin):
    list_display=['tenDiaDiem','giaGoc','giaGiam','anhDiaDiem']
class teamAdmin(admin.ModelAdmin):
    list_display=['hoTen','anhDaiDien']
class aboutAdmin(admin.ModelAdmin):
    list_display=['address','phone','email']
admin.site.register(Review,reviewAdmin)
admin.site.register(Discount,discountAdmin)
admin.site.register(Team,teamAdmin)
admin.site.register(About,aboutAdmin)
