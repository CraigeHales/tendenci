from django.conf.urls import url
from . import views
from .feeds import LatestEntriesFeed

urlpatterns = [
    url(r'^chapters/$', views.search, name="chapters.search"),
    url(r'^chapters/add/$', views.add, name='chapters.add'),
    url(r'^chapters/add/(?P<copy_from_id>\d+)/$', views.add, name='chapters.copy_from'),
    url(r'^chapters/edit/(?P<id>\d+)/$', views.edit, name='chapters.edit'),
    url(r'^chapters/edit_app_fields/(?P<id>\d+)/$', views.edit_app_fields, name='chapters.edit_app_fields'),
    url(r'^chapters/edit/meta/(?P<id>\d+)/$', views.edit_meta, name="chapters.edit.meta"),
    url(r'^chapters/delete/(?P<id>\d+)/$', views.delete, name='chapters.delete'),
    url(r'^chapters/feed/$', LatestEntriesFeed(), name='chapters.feed'),
    url(r"^chapters/get_app_fields/$", views.get_app_fields_json,
                            name="chapters.get_app_fields"),

    # chapter memberships
    url(r"^chapters/memberships/(?P<chapter_membership_id>\d+)/$",
        views.membership_details,
        name="chapters.membership_details"),
    url(r"^chapters/memberships/applications/add/pre/$",
        views.chapter_membership_add_pre,
        name="chapters.membership_add_pre"),
    url(r"^chapters/(?P<chapter_id>\d+)/memberships/applications/add/$",
        views.chapter_membership_add,
        name="chapters.membership_add"),
    url(r"^chapters/memberships/applications/add_conf/(?P<id>\d+)/$",
        views.chapter_membership_add_conf,
        name="chapters.membership_add_conf"),
    url(r"^chapters/memberships/edit/(?P<chapter_membership_id>\d+)/$",
        views.chapter_membership_edit,
        name="chapters.membership_edit"),
    url(r"^chapters/memberships/renew/(?P<chapter_membership_id>\d+)/$",
        views.chapter_membership_renew,
        name="chapters.membership_renew"),
    url(r"^chapters/memberships/search/(?P<chapter_id>\d+)/$",
        views.chapter_memberships_search,
        name="chapters.memberships_search_single_chapter"),
    url(r"^chapters/memberships/search/$",
        views.chapter_memberships_search,
        name="chapters.memberships_search"),
    url(r"^chapters/memberships/files/(?P<cm_id>\d+)/$", views.file_display,
            name="chapters.cm_file_display"),

    # chapter memberships import
    url(r"^chapters/memberships/import/$",
        views.chapter_memberships_import_upload,
        name="chapters.memberships_import"),
    url(r"^chapters/memberships/import/(?P<chapter_id>\d+)/$",
        views.chapter_memberships_import_upload,
        name="chapters.memberships_import_single_chapter"),
    url(r"^chapters/memberships/import/preview/(?P<mimport_id>\d+)/$",
        views.chapter_memberships_import_preview,
        name="chapters.memberships_import_preview"),
    url(r"^chapters/memberships/import/process/(?P<mimport_id>\d+)/$",
        views.chapter_memberships_import_process,
        name="chapters.memberships_import_process"),
    url(r"^chapters/memberships/import/status/(?P<mimport_id>\d+)/$",
        views.chapter_memberships_import_status,
        name="chapters.memberships_import_status"),
    url(r"^chapters/memberships/import/get_status/(?P<mimport_id>\d+)/$",
        views.chapter_memberships_import_get_status,
        name="chapters.memberships_import_get_status"),
    url(r"^chapters/memberships/import/check_encode_status/(?P<mimport_id>\d+)/$",
        views.chapter_memberships_import_check_preprocess_status,
        name="chapters.memberships_import_check_preprocess_status"),
    url(r"^chapters/memberships/import/download_recap/(?P<mimport_id>\d+)/$",
        views.chapter_memberships_import_download_recap,
        name="chapters.memberships_import_download_recap"),
    url(r"^chapters/memberships/import/download_template/$",
        views.download_import_template,
        name="chapters.download_import_template"),
    url(r"^chapters/memberships/import/download_template/(?P<chapter_id>\d+)/$",
        views.download_import_template,
        name="chapters.download_import_template_single_chapter"),

    url(r'^chapters/(?P<slug>[\w\-\/]+)/$', views.detail, name="chapters.detail"),
]
