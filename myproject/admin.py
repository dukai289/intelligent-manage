# myapp/admin.py
from django.contrib import admin
from .models import (
      FoodData
    , CqMpdProfile
    , CqMpdDetail
    , CqMpdInfo
    , FoodList
    , FoodDetail
    )

class FoodDataAdmin(admin.ModelAdmin):
    list_display = ('id'
                    ,'name'
                    , 'calory'
                    , 'protein'
                    , 'fat'
                    , 'carbohydrate'
                    , 'type_1'
                    , 'type_2'
                    , 'type_3'
                    , 'lights'
                    , 'health_light'
                    , 'in_replace_use'
                    , 'bound_l'
                    , 'bound_u'
                    ) 



admin.site.register(FoodData, FoodDataAdmin)
admin.site.register(CqMpdProfile)
admin.site.register(CqMpdDetail)
admin.site.register(CqMpdInfo)
admin.site.register(FoodList)
admin.site.register(FoodDetail)
