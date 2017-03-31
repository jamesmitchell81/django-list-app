from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from django.utils import timezone

from .models import List, Item
from .forms import NewItemForm, NewListForm, EditItemForm

# All the lists.
def index(request):
	template = loader.get_template('lists/index.html')
	context = {
		'title': 'This is the title',
		'lists': List.objects.all(),
		'form': NewListForm()
	}
	return HttpResponse(template.render(context, request))

def single_list(request, id):
	template = loader.get_template('lists/list.html')
	context = {
		'items': Item.objects.filter(list_id=id, active=True),
		'list': List.objects.get(id=id),
		'form': NewItemForm()
	}
	return HttpResponse(template.render(context, request))

def create_new_list(request):
	if request.method == 'POST':
		form = NewListForm(request.POST)
		if form.is_valid():
			value = form.cleaned_data['new_list']
			list = List(name=value)
			list.save()
			redirect = '/lists/list/%s' % list.id
			return HttpResponseRedirect(redirect)
		else:
			template = loader.get_template('lists/index.html')
			context = {
				'form': form,
				'title': "This is the title",
				'lists': List.objects.all()
			}
			return HttpResponse(template.render(context, request))
	else:
		redirect = '/'
		return HttpResponseRedirect(redirect)

def add_item_to_list(request, id):
	if request.method == 'POST':
		form = NewItemForm(request.POST)
		if form.is_valid():

			value = form.cleaned_data['new_item']
			item = Item(list_id=id, value=value, created=timezone.now(), completed=False)
			item.save()

			redirect = '/lists/list/%s' % id
			return HttpResponseRedirect(redirect)
	# template = loader.get_template('lists/list.html')
	# context = {
	# 	'items': Item.objects.filter(list_id=id),
	# 	'list': List.objects.get(id=id)
	# }
	return render(context, context=context, context_instance=RequestContext(request))

def toggle_list_item(request, id):
	item = Item.objects.get(id=id)
	item.current = not item.current
	item.save()
	redirect = '/lists/list/%i' % item.list_id
	return HttpResponseRedirect(redirect)

def edit_list_item(request, id):
	template = loader.get_template('lists/edit-item.html')
	item = Item.objects.get(id=id)
	list = List.objects.get(id=item.list_id)
	context = {
		'form': EditItemForm({
				'item_value': item.value,
				'complete': item.completed
			}),
		'item': item,
		'list': list
	}
	return HttpResponse(template.render(context))

def delete_list_item(request, id):
	item = Item.objects.get(id=id)
	item.active = False
	item.save()
	redirect = '/lists/list/%i' % item.list_id
	return HttpResponseRedirect(redirect)



