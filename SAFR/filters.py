import django_filters

from.models import *


class bookflightFilter(django_filters.FilterSet):
    class Meta:
        model = Bookflight
        fields =['from_city', 'To_city','seat_type','seat_nuper','Data_trib','Airline_type']
        