#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.contrib.sitemaps import Sitemap
from techism2.orgs import org_service
from datetime import datetime


class OrgIndexSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.3

    def items(self):
        return ['/orgs/']
    
    def location(self, obj):
        return obj

    def lastmod(self, obj):
        return datetime.now()


class OrgTagsSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.3

    def items(self):
        return org_service.get_tags()

    def location(self, obj):
        return '/orgs/tags/' + obj['name'] + '/'
