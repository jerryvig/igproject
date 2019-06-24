from django.contrib import admin
from igimageview.models import IGPost
from igimageview.models import IGImage

# Register your models here.
#admin.site.register(IGPost)
#admin.site.register(IGImage)

@admin.register(IGPost)
class IGPostAdmin(admin.ModelAdmin):
    pass


@admin.register(IGImage)
class IGImageAdmin(admin.ModelAdmin):
    pass

