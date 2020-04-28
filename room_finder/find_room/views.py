from django.shortcuts import render,get_object_or_404,redirect
from .forms import FindRooMModelForm,UploadRoomModelForm,ContactUsModelForm

# Create your views here.

def find_room_view(request):

	findroom_form = FindRooMModelForm(request.POST or None)
	contactus_form = ContactUsModelForm(request.POST or None)


	if findroom_form.is_valid():
	   print(findroom_form.cleaned_data)
	   findroom_form = FindRooMModelForm()

	if contactus_form.is_valid():
	   print(contactus_form.cleaned_data)
	   contactus_form = ContactUsModelForm()

	template_name = 'find_room/find_room_main.html'
	context = {
	    'findroom_form': findroom_form,
	    'contactus_form': contactus_form,
	}

	return render(request,template_name,context)

def upload_room_view(request):

	uploadroom_form = UploadRoomModelForm(request.POST or None, request.FILES or None)
	contactus_form = ContactUsModelForm(request.POST or None)


	if uploadroom_form.is_valid():
	   print(uploadroom_form.cleaned_data)
	   uploadroom_form = UploadRoomModelForm()

	if contactus_form.is_valid():
	   print(contactus_form.cleaned_data)
	   contactus_form = ContactUsModelForm()

	template_name = 'find_room/upload_room_main.html'
	context = {
	    'uploadroom_form': uploadroom_form,
	    'contactus_form': contactus_form,
	}

	return render(request,template_name,context)

def about_us_view(request):

	contactus_form = ContactUsModelForm(request.POST or None)

	if contactus_form.is_valid():
	   print(contactus_form.cleaned_data)
	   contactus_form = ContactUsModelForm()

	template_name = 'find_room/about_us_main.html'
	context = {
	    'contactus_form': contactus_form,
	}

	return render(request,template_name,context)

def available_rooms_view(request):

	contactus_form = ContactUsModelForm(request.POST or None)

	if contactus_form.is_valid():
	   print(contactus_form.cleaned_data)
	   contactus_form = ContactUsModelForm()

	template_name = 'find_room/available_rooms_main.html'
	context = {
	    'contactus_form': contactus_form,
	}

	return render(request,template_name,context)


















