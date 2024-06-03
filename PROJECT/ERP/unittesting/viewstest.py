from django.test import TestCase ,Client
from django.urls import reverse
from returnpack.models import *
import json

class TestViews(TestCase):
    def setUp(self):
        self.client=Client()
        self.customer=Customer.objects.create(
            type="individual",
            firstname="karim",
            lastname="el fil",
            email="karim@gmail.com",
            website="www.com",
            workphone=5565688,
            phone=741852,
            contact="president",
        )
