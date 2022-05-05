from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from communication.models import Ticket
from communication.permissions import IsAdmin
from communication.serializer import TicketSerializer


class TicketAPIAdmin(generics.ListAPIView, generics.RetrieveDestroyAPIView, generics.UpdateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly,)


class TicketAPIAuth(generics.ListAPIView, generics.CreateAPIView, generics.UpdateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly,)


class TicketAPINotAuth(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    # permission_classes = (IsOwnerOrReadOnly,)


class TicketAPIList(generics.ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

#
# def index(request):
#     if request.method == "POST":
#         date_time = request.POST['date_time'] + ':000'
#         new = Date(date_time=date_time)
#         new.save()
#         date_time_obj = datetime.strptime(date_time, '%Y-%m-%dT%H:%M:%S')
#         date_time_obj -= timedelta(hours=correct_timezone(date_time_obj))
#         adding_task.apply_async(args=(date_time,), eta=date_time_obj)
