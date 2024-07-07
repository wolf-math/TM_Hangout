from django.urls import path
from . import views

app_name = 'planner'

urlpatterns = [
    path('planner/', views.planner, name='planner'),
    # path converters
    path('planner/<int:year>/<str:month>/', views.month, name="planner"),
    path('events/', views.all_events, name="list-events"),
]
