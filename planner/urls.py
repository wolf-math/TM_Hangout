from django.urls import path
from . import views

app_name = 'planner'

urlpatterns = [
    path('planner/', views.planner, name='planner'),
    # path converters
    path('planner/<int:year>/<str:month>/', views.month, name="planner"),
    path('events/', views.all_events, name="all_events"),
    path('add_event', views.add_event, name="add_event"),
    path('events/<int:event_id>/', views.event, name='event'),
]
