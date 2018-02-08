from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect


from .forms import PostForm
from .models import Post

def post_create(request):
	form=PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		print form.cleaned_data.get("title")
		instance.save()
		messages.success(request,"Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	
	context = {
		"form":form,
	}
	return render(request,"post_form.html",context)

def post_detail(request,id):
	instance = get_object_or_404(Post,id=id)
	context = {
		"title": instance.title,
		"instance": instance,
	}
	return render(request,"post_detail.html",context)
	#return HttpResponse("<h1>Detail</h1>")

def post_list(request):
	queryset_list =Post.objects.all()#.order_by("-timestamp")
	paginator = Paginator(queryset_list, 5) # Show 25 contacts per page

	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset=paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)
	context = {
		"object_list": queryset,
		"title": "List"
	}
	return render(request,"post_list.html",context)

	
    
    
	#return HttpResponse("<h1>List</h1>")

def post_update(request,id=None):
	instance = get_object_or_404(Post,id=id)
	form=PostForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		
		instance.save()
		messages.success(request,"Successfully Creted")
		return HttpResponseRedirect(instance.get_absolute_url())


	context = {
		"title": instance.title,
		"instance": instance,
		"form":form,
		}
	#return HttpResponse("<h1>Update</h1>")
	return render(request,"post_form.html",context)


def post_delete(request,id=None):
	instance=get_object_or_404(Post,id=id)
	instance.delete()
	messages.success(request,"Successfully Deleted")
	return redirect("posts:list")



	#return HttpResponse("<h1>Delete</h1>")