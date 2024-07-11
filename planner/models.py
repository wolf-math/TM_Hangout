from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Event(models.Model):
    name = models.CharField(max_length=200)
    event_date = models.DateTimeField()
    manager = models.ForeignKey(
        User, related_name='events', on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=20, default='unknown')
    multi_person = models.BooleanField(default=False)
    max_attendees = models.PositiveIntegerField(default=1, blank=True, null=True)  # Maximum number of attendees
    attendees = models.ManyToManyField(User, through='Attendance', related_name='attended_events')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def attendee_count(self):
        return self.attendance_set.count()

    def can_add_attendee(self):
        return self.attendee_count() < self.max_attendees

class Attendance(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    attendance_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.event.name}"

    def save(self, *args, **kwargs):
        if not self.event.can_add_attendee():
            raise ValueError("The attendee limit for this event has been reached.")
        super().save(*args, **kwargs)


# from planner.models import Event, User, Attendance

# # Create or get an event and a user
# event = Event.objects.get(id=1)
# user = User.objects.get(id=1)

# # Attempt to create an Attendance entry
# try:
#     attendance = Attendance(event=event, user=user)
#     attendance.save()
#     print("Attendance successful.")
# except ValueError as e:
#     print(e)