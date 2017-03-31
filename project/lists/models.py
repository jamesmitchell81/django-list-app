from django.db import models
from django.utils import timezone

class List(models.Model):
    name = models.CharField(max_length=255)

    def get_absolute_url(self):
        return "/lists/list/%i" % self.id


class Item(models.Model):
    list = models.ForeignKey(List)
    value = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    current = models.BooleanField(default=True)
    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return "/lists/list/%i/item/%i" % (self.list_id, self.id)

    def time_since_creation(self):
        created = self.created
        now = timezone.now()
        difference = now - created
        seconds = difference.total_seconds()
        minutes = seconds / 60
        hours = minutes / 60
        days = hours / 24

        display_seconds = seconds % 60
        display_minutes = minutes % 60
        display_hours = hours % 24
        return "%d days, %d hours, %d minutes, %d seconds" % (int(days), int(display_hours), int(display_minutes), int(display_seconds))

    class Meta:
        ordering = ('-created',)
    	# if less then a minute
    	# return in seconds.

    	# if less then an hour
    	# return in minutes

    	# if less then a day
    	# return in hours and minutes

    	# if less then a week
    	# return as days, hours

    	# if less then a month
    	# return as weeks and days

    	# if less than a year
    	# return as months, weeks/days