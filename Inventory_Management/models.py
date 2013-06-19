from django.db import models
import datetime
from django.utils import timezone



#Base Model
class Equipment(models.Model):
        manufacturer = models.ForeignKey('Manufacturer')
        model_num = models.CharField(max_length = 35, unique = True)
        serial_num = models.CharField(max_length = 35, unique = True)
        purchaseDate = models.DateField()

#For all in one's ... ex: A PC, Router, or Server
class Unit(Equipment):
        location = models.ForeignKey('Location', blank=False)

#For each individual item... ex: Ram stick, CPU, or PSU
class Component(Equipment):
        location = models.ForeignKey('Location', blank=True)


class Manufacturer(models.Model):
        manufacturer = models.CharField(max_length= 25)
        def __unicode__(self):
                return unicode(self.manufacturer)

class Location(models.Model):
        building = models.CharField(max_length=2)
        room = models.CharField(max_length=4)
        def __unicode__(self):
                return unicode(self.building + self.room)


class Ram(Component):
        clock_speed = models.CharField(max_length = 5, blank=True)
        series = models.CharField(max_length = 25, blank=True)
        _type = models.CharField(max_length = 10, blank=True)
        pins = models.IntegerField()
        cas_latency = models.IntegerField()
        timing = models.CharField(max_length = 11, blank=True)
        voltage = models.IntegerField()
        multi_channel = models.CharField(max_length = 11, blank=True)




class HardDrive(Component):
        size = models.IntegerField()
        def __unicode__(self):
                return unicode(str(self.manufacturer) + " " + str(self.size))

class Mother_board(Component): pass

class Central_processing_unit(Component):
        clock_speed = models.FloatField()
        def __unicode__(self):
                return unicode(str(self.manufacturer) +  " " + str(self.clock_speed))

class Optical_drive(Component): pass

class Flash_memory(Component): pass

class Operating_system(Component):
        name = models.CharField(max_length = 11, blank=True)
        def __unicode__(self):
                return unicode(self.name)

class Power_supply_unit(Component):
        power_rating = models.CharField(max_length = 8, blank=True)

class Cisco_router(Unit):
        IS_tag = models.IntegerField()
        seller = models.TextField()
        ram = models.ForeignKey(Ram)
        flash_mem = models.ForeignKey(Flash_memory)
        num_ports = models.IntegerField()
        service = models.TextField()

class Computer(Unit):
        cpu = models.ForeignKey(Central_processing_unit)
        optical_drive = models.ForeignKey(Optical_drive)
        hdd = models.ForeignKey(HardDrive)
        ram = models.ForeignKey(Ram)
        psu = models.ForeignKey(Power_supply_unit)
        #service = models.CharField(max_length = 15)





