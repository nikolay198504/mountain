from django.urls import path
from .views import PassSubmitView

urlpatterns = [
    path('submitData/', PassSubmitView.as_view(), name='submitData'),
]
