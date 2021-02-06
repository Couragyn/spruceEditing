from django.db import models
from django.contrib.auth.models import User
import uuid

CURRENCY = (
    (0,"CAD"),
    (1,"USD"),
    (2,"EUR"),
    (3,"AUD"),
    (4,"GBP"),
    (5,"DKK"),
    (6,"HKD"),
    (7,"HUF"),
    (8,"ILS"),
    (9,"JPY"),
    (10,"MXN"),
    (11,"TWD"),
    (12,"NZD"),
    (13,"NOK"),
    (14,"PHP"),
    (15,"PLN"),
    (16,"CZK"),
    (17,"RUB"),
    (18,"SGD"),
    (19,"SEK"),
    (20,"CHF"),
    (21,"THB"),
)

class Pay(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey(User, on_delete=models.RESTRICT)
    amount = models.DecimalField(decimal_places=2, max_digits=100)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    paid = models.BooleanField(default=False)
    currency = models.IntegerField(choices=CURRENCY, default=0)
    description = models.CharField(max_length=200, default='Editing Services')