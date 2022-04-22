from django.db import models


# class User(models.Model):

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
