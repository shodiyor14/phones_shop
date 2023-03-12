from django.contrib import admin
from phones.models import PhonesBrandModel, PhonesTagModel, PhonesColorModel, PhonesModelsCategory, PhonesModel

admin.site.register(PhonesBrandModel)
admin.site.register(PhonesTagModel)
admin.site.register(PhonesColorModel)
admin.site.register(PhonesModelsCategory)
admin.site.register(PhonesModel)
