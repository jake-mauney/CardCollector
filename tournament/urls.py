from django.urls import path
from . import views

urlpatterns = [
    path("", views.TourHome, name="tourhome"),
    path("create", views.TourCreate, name="tourcreate")

]