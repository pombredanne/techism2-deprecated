from django.conf.urls.defaults import patterns, url, include
from django.contrib import admin
from techism2.rss.feeds import UpcommingEventsRssFeed, UpcommingEventsAtomFeed

admin.autodiscover()

urlpatterns = patterns('',
    # events
    (r'^$', 'techism2.events.views.index'),
    (r'^events/$', 'techism2.events.views.index'),
    url(r'^events/(?P<event_id>\d+)/$', 'techism2.events.views.show', name='event-show'),
    (r'^events/edit/(?P<event_id>\d+)/$', 'techism2.events.views.edit'),
    (r'^events/cancel/(?P<event_id>\d+)/$', 'techism2.events.views.cancel'),
    (r'^events/create/(?P<event_id>\d+)/$', 'techism2.events.views.create'),
    (r'^events/create/$', 'techism2.events.views.create'),
    (r'^events/archive/$', 'techism2.events.views.archive'),
    (r'^events/tags/(?P<tag_name>.+)/$', 'techism2.events.views.tag'),
    
    # organizations
    (r'^organizations/$', 'techism2.organizations.views.index'),
    (r'^organizations/tags/(?P<tag_name>.+)/$', 'techism2.organizations.views.tag'),
    
    # static pages
    (r'^impressum/$', 'techism2.events.views.static_impressum'),
    (r'^about/$', 'techism2.events.views.static_about'),
    
    # iCal
    (r'^feed.ics$', 'techism2.ical.views.ical'),
    
    # Atom
    (r'^feeds/atom/upcomming_events$', UpcommingEventsAtomFeed()),
    
    #RSS
    (r'^feeds/rss/upcomming_events$', UpcommingEventsRssFeed()),
    
    # admin
    (r'^admin/', include(admin.site.urls)),
    
    # login/logout
    (r'^accounts/', include('django_openid_auth.urls')),
    (r'^accounts/logout/$', 'techism2.events.views.logout'),
    url(r'^accounts/google_login/$', 'gaeauth.views.login', name='google_login'),
    url(r'^accounts/google_logout/$', 'gaeauth.views.logout', name='google_logout'),
    url(r'^accounts/google_authenticate/$', 'gaeauth.views.authenticate', name='google_authenticate'),
    
    # cron jobs
    (r'^cron/update_archived_flag', 'techism2.cron.views.update_archived_flag'),
    (r'^cron/update_organization_tags_cache', 'techism2.cron.views.update_organization_tags_cache'),
    (r'^cron/update_event_tags_cache', 'techism2.cron.views.update_event_tags_cache'),
    (r'^cron/tweet_upcoming_events', 'techism2.cron.twitter.tweet_upcoming_events'),
    

)
