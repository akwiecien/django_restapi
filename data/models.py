# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DataContinent(models.Model):
    id = models.AutoField(primary_key=True)
    iso_code = models.CharField(max_length=3)
    name = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'data_continent'
    
    def __unicode__(self):
        return '%d: %s' % (self.name, self.iso_code)

class DataCountry(models.Model):
    id = models.AutoField(primary_key=True)
    iso_code = models.CharField(max_length=3)
    name = models.CharField(max_length=250)

    continent_id = models.ForeignKey(DataContinent, models.CASCADE, related_name='countries')

    class Meta:
        managed = False
        db_table = 'data_country'
    
    def __unicode__(self):
        return '%d: %s' % (self.name, self.iso_code)


class DataCity(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    type = models.CharField(max_length=1)
    
    country_id = models.ForeignKey('DataCountry', models.CASCADE, related_name='cities')

    class Meta:
        managed = False
        db_table = 'data_city'

    def __unicode__(self):
        return '%d: %s' % (self.name, self.type)
