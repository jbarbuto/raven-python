# -*- coding: utf-8 -*-

from unittest2 import TestCase
from sentry_client.base import SentryClient

class TempStoreClient(SentryClient):
    def __init__(self):
        self.events = []

    def send(self, **kwargs):
        self.events.append(kwargs)

class ClientTest(TestCase):
    def setUp(self):
        self.client = TempStoreClient()

    # def test_long_urls(self):
    #     # Fix: #6 solves URLs > 200 characters
    #     self.client.create_from_text('hello world', url='a'*210)

    #     event = self.client.events.pop(0)

    #     self.assertEquals(event['url'], 'a'*200)