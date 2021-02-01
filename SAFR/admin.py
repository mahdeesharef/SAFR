
# Register your models here.
from django.contrib import admin

# Register your models here.
from.models import Bookflight
from.models import Visa
from.models import CustomUser
from.models import Ordertrip



admin.site.register(Bookflight)
admin.site.register(Visa)
admin.site.register(CustomUser)
admin.site.register(Ordertrip)