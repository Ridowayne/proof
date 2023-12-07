import uuid
from django.db import models
import datetime

# Create your models here.
class Agent(models.Model):
    agent_name = models.CharField(max_length=200)
    agent_phone = models.CharField(max_length=20)
    agent_email = models.EmailField(unique= True, null=False)
    password = models.CharField(max_length=20)
    reqion = models.CharField(max_length=100)
    ahq = models.CharField(max_length=100)
    location = models.CharField(max_length=100)


class Issue(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    issuue_type = models.CharField(max_length=150)
    issues_description = models.TextField()
    product_type = models.CharField(max_length=200)
    unit_no = models.CharField(max_length=20)
    customer_name = models.CharField(max_length=200)
    customer_phone = models.CharField(max_length=20)
    reported_by = models.CharField(max_length=300)
    agent_id = models.CharField(max_length=50)
    agent_phone = models.CharField(max_length=20)
    agent_email = models.EmailField(null=False)
    resolved = models.BooleanField(default=False)
    agent_response = models.TextField()
    reported_at = models.DateField(default=datetime.date.today)