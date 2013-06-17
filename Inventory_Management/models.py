from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

#number is implied
class Equip_Type(models.Model):
        eType = models.CharField(max_length=20, unique=True)

        def __unicode__(self):
                return unicode(self.eType)

class Location(models.Model):
        room = models.CharField(max_length=4)
        building = models.CharField(max_length=2)
        def __unicode__(self):
                return unicode(self.building + self.room)

class Equipment(models.Model):
        manufacturer = models.CharField(max_length = 30)
        model_num = models.CharField(max_length = 35, unique = True)
        serial_num = models.CharField(max_length = 35, unique = True)
        equip_type = models.ForeignKey(Equip_Type)
        location = models.ForeignKey(Location)
        description = models.TextField()
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

class Mother_Board(Equipment):
        x = 2 #filler

class CPU(Equipment):
        clock_speed = models.IntegerField()

class Optical_Drive(Equipment):
        x = 2 #filler

class Flash_Memory(Equipment):
        x = 2 #filler

class Operating_system(Equipment):
        x = 2 #filler

class PSU(Equipment):
        x = 2 #filler

class Cisco_Router(Equipment):
        IS_tag = models.IntegerField()
        seller = models.TextField()
        ram = models.ForeignKey(Ram)
        ram_count = models.IntegerField()
        flash_mem = models.ForeignKey(Flash_Memory)
        num_ports = models.IntegerField()
        service = models.TextField()

class Computer(Equipment):
        optical_drive = models.ForeignKey(Optical_Drive)
        ram = models.ForeignKey(Ram)
        psu = models.ForeignKey(PSU)
        cpu = models.ForeignKey(CPU)
        service = models.CharField(max_length = 15)

