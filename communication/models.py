from django.contrib.auth.models import User
from django.db import models


class Ticket(models.Model):
    RESOLVED = 'RESOl'
    UNRESOLVED = 'UNRES'
    FROZEN = 'FROZN'
    STATUS = [
        (RESOLVED, 'Resolved'),
        (UNRESOLVED, 'Unresolved'),
        (FROZEN, 'Frozen')
    ]
    status = models.CharField(max_length=5, choices=STATUS, default=FROZEN, null=False)
    content = models.CharField(max_length=1000000, null=True)
    # client = models.ForeignKey(to=User, on_delete=models.PROTECT)
    new_message = models.CharField(max_length=10000, null=True)
