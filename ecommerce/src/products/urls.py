from django.conf.urls import url

from .views import (
        ProductListView, 
        #product_list_view, 
        #ProductDetailView,
        ProductDetailSlugView, 
        #product_detail_view,
        #ProductFeaturedListView,
        #ProductFeaturedDetailView
        )


urlpatterns = [
    url(r'^$', ProductListView.as_view()),
    #url(r'^products-fbv/$', product_list_view),
    #url(r'^products/(?P<pk>\d+)/$', ProductDetailView.as_view()),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view()),
    #url(r'^products-fbv/(?P<pk>\d+)/$', product_detail_view),
]

