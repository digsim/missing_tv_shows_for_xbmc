# -*- coding: utf-8 -*-

from unittest import TestCase
from mtvs.Kodi.missing_tvshows import TVShows   # noqa: F401


class TestDBQueries(TestCase):
    def test_series_query(self):
        self.assertTrue(True, "This test should always pass")