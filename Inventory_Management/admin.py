from django.contrib import admin
from Inventory_Management.models import *

#class EquipAdmin(admin.ModelAdmin):
	#this line changes what the information given when just eyeing the list shows
	#list_display = ('description', 'equip_type', 'model_num', 'serial_num')
	#this does the filters on the right hand side, currently, location does not work if added
	#list_filter = ('equip_type',)
	#	serch currently errors when used
	#search_fields = ['description']

#admin.site.register(Equipment, EquipAdmin)
#this permits adding objects of that type when adding new equipment
#admin.site.register(Equip_Type)


#class ComputerAdmin(admin.ModelAdmin):
#	fieldsets = [
#		(None, {'fields':['cpu']}),
#	]

#admin.site.register(Computer, ComputerAdmin)	

admin.site.register(Equipment)
admin.site.register(Unit)
admin.site.register(Component)
admin.site.register(Location)
admin.site.register(Manufacturer)
admin.site.register(Vendor)
admin.site.register(ModelNumber)
admin.site.register(Memory)
admin.site.register(Ram)
admin.site.register(Flash_Memory)
admin.site.register(HardDrive)
admin.site.register(Mother_board)
admin.site.register(Central_processing_unit)
admin.site.register(Optical_drive)
admin.site.register(Operating_system)
admin.site.register(Power_supply_unit)
admin.site.register(Service_contract)
admin.site.register(Router)
admin.site.register(Firewall)
admin.site.register(Switch)
admin.site.register(Computer)
