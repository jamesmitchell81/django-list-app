from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^add', views.create_new_list),
	url(r'^list/(\d{1,2})', views.single_list),
	url(r'^list/add/(\d{1,2})', views.add_item_to_list),
	url(r'^toggle/(\d{1,2})', views.toggle_list_item),
	url(r'^edit/(\d{1,2})', views.edit_list_item),
	url(r'^delete/(\d{1,2})', views.delete_list_item),
]