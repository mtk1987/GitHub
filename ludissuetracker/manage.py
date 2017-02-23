#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ludissuetracker.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

INSTALLED_APPS = (
	'django.contrib.admin', 'ludissues',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.messages',
	'django.contrib.staticfiles',
)

#We are importing the user authentication module so that we use the built in authentication model in this app
from django.contrib.auth.models import User

#We would also create an admin interface for our app 
from django.contrib import admin

#A tuple to hold the multi choice char fields. First represents the field name the second one represents the display name
ISSUE_STATUS_CHOICES = (
	('new', 'New'),
	('accepted','Accepted'),
	('reviewed','Reviewed'),
	('started','Started'),
	('closed','Closed'),
)

class Issue(models.Model):
	#owner will be a foreign key to the User model which is already built-in Django
	owner = models.ForeignKey(User,null=True,blank=True)
	#multichoice with defaulting to "new"
	status = models.CharField(max_length=25,choices=ISSUE_STATUS_CHOICES,default='new')
	summary = models.TextField()
	#date time field which will be set to the date time when the record is created
	opened_on = models.DateTimeField('date modified',auto_now=True)

def name(self):
	return self.summary.split('\n',1)[0]

#Admin front end for the app. We are also configuring some of the built in attributes for the admin interface on how to display the list, how it will be sorted, what are the search fields etc.
class IssueAdmin(admin.ModelAdmin):
	date_hierarchy = 'opened_on'
	list_filter = ('status','owner')
	list_display = ('id','name','status','owner','modified_on')
	search_fields = ['description','status']

#register our site with the Django admin interface
admin.site.register(Issue,IssueAdmin)
