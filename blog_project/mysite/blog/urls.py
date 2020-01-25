from django.conf.urls import urls
from blog import views

urlpatterns = [
    url(r'^$',views.PostListView.as_view(),name='post_list'),
    url(r'^about/$',views.AboutView.as_view(),name='about'),
    url(r'^post/(?P<pk>\d+)$',view.PostDetailView.as_view(),name='post_detail'),
    url(r'^post/new/$',views.CreatePostView.as_view(),name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$',view.PostUpdateView.as_view(),name='post_edit'),
    url(r'^post/(?P<pk>\d+)/remove/$',views.PostDeleteView.as_view(),name='post_remove'),
    url(r'^drafts/$',views.DraftListView.as_view(),name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/comment/$',view.add_comment_to_post,name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$',views.comment_approve,name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$',view.comment_remove,name='comment_remove'),
    url(r'^comment/(?P<pk>\d+)/publish/$',view.post_publish,name='post_publish'),
]
