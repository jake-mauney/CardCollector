from django.urls import path
from . import views

urlpatterns = [
    path("", views.TourHome, name="tourhome"),
    path("create", views.TourCreate, name="tourcreate"),
    path("<str:tour_id>/", views.TourDetails, name="tourdetail"),
    path("register/<str:tour_id>/", views.Register, name="register"),
    path("start/<str:tour_id>/", views.StartTournament, name='StartTour'),
    path("<str:tour_id>/matches/", views.ViewMatches, name="ViewMatches"),
    path("match/<str:match_id>/", views.ViewOneMatch, name="ViewOneMatch"),
    path("next/<str:tour_id>/", views.NextRound, name='NextRound')
]