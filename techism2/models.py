from django.contrib.auth.models import User
from django.db import models
from techism2 import fields
from techism2 import utils

class Location(models.Model):
    name = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    
    def __unicode__(self):
        return self.name;
    
class Event(models.Model):
    title = models.CharField(max_length=200)
    date_time_begin = models.DateTimeField()
    date_time_end = models.DateTimeField(blank=True, null=True)
    url = models.URLField()
    description = models.TextField()
    location = models.ForeignKey(Location, blank=True, null=True)
    tags = fields.CommaSeparatedListField(models.CharField(max_length=20), blank=True, null=True)
    user = models.ForeignKey(User, blank=True, null=True)
    date_time_created = models.DateTimeField(auto_now_add=True, null=True)
    date_time_modified = models.DateTimeField(auto_now=True, null=True)
    
    def __unicode__(self):
        return self.title
    
    def get_date_time_created_utc(self):
        "Gets the 'Created' date/time in UTC."
        return utils.localize_to_utc(self.date_time_created);
    
    def get_date_time_modified_utc(self):
        "Gets the 'Modifed' date/time in UTC."
        return utils.localize_to_utc(self.date_time_modified);
    
    def get_date_time_begin_utc(self):
        "Gets the 'Begin' date/time in UTC."
        return utils.localize_to_utc(self.date_time_begin);
    
    def get_date_time_begin_cet(self):
        "Gets the 'Begin' date/time in CET/CEST."
        return utils.utc_to_cet(self.date_time_begin);
    
    def set_date_time_begin_cet(self, date_time_begin_cet):
        "Sets the 'Begin' date/time in CET/CEST timezone. Internally the date/time is saved in UTC timezone."
        self.date_time_begin = utils.cet_to_utc(date_time_begin_cet)
    
    def get_date_time_end_utc(self):
        "Gets the 'End' date/time in UTC."
        return utils.localize_to_utc(self.date_time_end);
    
    def get_date_time_end_cet(self):
        "Gets the 'End' date/time in CET/CEST."
        return utils.utc_to_cet(self.date_time_end);
    
    def set_date_time_end_cet(self, date_time_end_cet):
        "Sets the 'End' date/time, expecting CET/CEST timezone. Internally the date/time is saved in UTC timezone"
        self.date_time_end = utils.cet_to_utc(date_time_end_cet)
    
    
