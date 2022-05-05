from django.contrib import admin
from django.urls import path

from communication.views import TicketAPIAdmin, TicketAPIAuth, TicketAPINotAuth, TicketAPIList

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
#     TokenVerifyView,
# )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listticket/', TicketAPIList.as_view()),  # все тикеты доступ администратор
    path('createticket/', TicketAPINotAuth.as_view()),  # отдельный тикет для общения доступ не авторизованный по-тель
    path('ticket/<int:pk>', TicketAPIAuth.as_view()),  # отдельный тикет для общения доступ пользователь
    path('adminticket/<int:pk>', TicketAPIAdmin.as_view()),  # отдельный тикет для общения доступ администратор
    # path('v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
