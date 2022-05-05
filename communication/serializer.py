from rest_framework import serializers

from communication.models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Ticket
        # fields = ('status', 'new_message', 'user')
        fields = '__all__'
