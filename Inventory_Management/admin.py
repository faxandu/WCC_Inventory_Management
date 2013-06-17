from django.contrib import admin
from Inventory_Management.models import *

class EquipAdmin(admin.ModelAdmin):
	#this line changes what the information given when just eyeing the list shows
	list_display = ('description', 'equip_type', 'model_num', 'serial_num')
	#this does the filters on the right hand side, currently, location does not work if added
	#list_filter = ('equip_type',)
	#	serch currently errors when used
	#search_fields = ['description']

admin.site.register(Equipment, EquipAdmin)
#this permits adding objects of that type when adding new equipment
admin.site.register(Equip_Type)
admin.site.register(Location)
admin.site.register(Ram)
admin.site.register(HardDrive)
admin.site.register(Mother_Board)
admin.site.register(Optical_Drive)
admin.site.register(Flash_Memory)
admin.site.register(Operating_system)
admin.site.register(PSU)

admin.site.register(Computer)