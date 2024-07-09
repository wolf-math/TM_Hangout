from django.urls import path
from . import views

app_name = 'planner'

urlpatterns = [
    path('planner/', views.planner, name='planner'),
    path('planner/<int:year>/<str:month>/', views.month, name="planner"),
    path('events/', views.all_events, name="all_events"),
    path('events/<int:event_id>/', views.event, name='event'),
    path('add_event', views.add_event, name="add_event"),
    path('edit_event/<int:event_id>/', views.edit_event, name='edit_event'),
    path('delete_event/<int:event_id>', views.delete_event, name='delete_event'),
    path('events/<int:event_id>/join', views.join_event, name='join_event'),
    path('events/<int:event_id>/leave', views.leave_event, name='leave_event')
]
