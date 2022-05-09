from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import Post
from django.contrib import messages
from django.views.generic import DetailView

# Create your views here.

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    if request.method == 'POST':
        name = request.POST.get('Name')
        phone = request.POST.get('Phone')
        email = request.POST.get('Email')
        message = request.POST.get('Message')

        data = {
            'name': name,
            'phone': phone,
            'email': email,
            'message': message,
        }

        message = "the message is:\n{data['message']}\nfrom: {data['name']} with email: {data['email']}\nhis/her number is: {data['phone']}"
        # send_mail('contact',message,'',['michealuzer@gmail.com'])
        messages.success(request, 'thank you for getting in touch with us' )

        return redirect('home')

    return render(request, 'blog/home.html', context)

def about(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        phone = request.POST.get('Phone')
        email = request.POST.get('Email')
        message = request.POST.get('Message')

        data = {
            'name': name,
            'phone': phone,
            'email': email,
            'message': message,
        }

        message = "the message is:\n{data['message']}\nfrom: {data['name']} with email: {data['email']}\nhis/her number is: {data['phone']}"
        send_mail('contact',message,'',['michealuzer@gmail.com'])
        messages.success(request, 'thank you for getting in touch with us' )

        return redirect('home')
    return render(request, 'blog/about.html')


class PostDetailView(DetailView):
    model=Post