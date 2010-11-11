#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.core.cache import cache
from techism2.models import Organization
from techism2 import service

tags_cache_key = "organization_tags"

def update_tags_cache():
    dict_list = __get_base_organization_query_set().values('tags')
    tags = service.fetch_tags(dict_list)
    cache.set(tags_cache_key, tags, 3600) # expire after 60 min
    return tags

def __get_base_organization_query_set():
    return Organization.objects.all()