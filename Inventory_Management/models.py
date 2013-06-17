from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

#number is implied
#class Equip_Type(models.Model):
        #eType = models.CharField(max_length=20, unique=True)

 #      def __unicode__(self):
 #               return unicode(self.eType)
class Manufacturer(models.Model):
        manufacturer = models.CharField(max_length= 25)
        def __unicode__(self):
                return unicode(self.manufacturer)


class Location(models.Model):
        building = models.CharField(max_length=2)
        room = models.CharField(max_length=4)
        def __unicode__(self):
                return unicode(self.building + self.room)



class Equipment(models.Model):
        manufacturer = models.ForeignKey(Manufacturer)
        model_num = models.CharField(max_length = 35, unique = True)
        serial_num = models.CharField(max_length = 35, unique = True)
        #equip_type = models.ForeignKey(Equip_Type)
        location = models.ForeignKey(Location)
        #description = models.TextField()
        purchaseDate = models.CharField(max_length = 10)

        def __unicode__(self):
                return unicode(self.description)

class Ram(Equipment):
        clock_speed = models.CharField(max_length = 5)
        series = models.CharField(max_length = 25)
        _type = models.CharField(max_length = 10)
        pins = models.IntegerField()
        cas_latency = models.IntegerField()
        timing = models.CharField(max_length = 11)
        voltage = models.IntegerField()
        multi_channel = models.CharField(max_length = 11)




class HardDrive(Equipment):
        size = models.IntegerField()
        def __unicode__(self):
                return unicode(self.manufacturer + " " + self.size)

class Mother_board(Equipment): pass

class Central_processing_unit(Equipment):
        clock_speed = models.IntegerField()
        def __unicode__(self):
                return unicode(self.manufacturer +  " " + clock_speed)

class Optical_drive(Equipment): pass

class Flash_memory(Equipment): pass

class Operating_system(Equipment): 
        name = models.CharField(max_length = 11)
        def __unicode__(self):
                return unicode(self.name)

class Power_supply_unit(Equipment): 
        power_rating = models.CharField(max_length = 8)

class Cisco_router(Equipment):
        IS_tag = models.IntegerField()
        seller = models.TextField()
        ram = models.ForeignKey(Ram)
        ram_count = models.IntegerField()
        flash_mem = models.ForeignKey(Flash_memory)
        num_ports = models.IntegerField()
        service = models.TextField()

class Computer(Equipment): 
        cpu = models.ForeignKey(Central_processing_unit)
        optical_drive = models.ForeignKey(Optical_drive)
        hdd = models.ForeignKey(HardDrive)
        ram = models.ForeignKey(Ram)
        psu = models.ForeignKey(Power_supply_unit)
        #service = models.CharField(max_length = 15)

