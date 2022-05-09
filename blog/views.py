from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import Post
from django.contrib import messages as m
from django.views.generic import DetailView

# Create your views here.

def home(request):
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
        m.success(request,f'thank you for getting in touch with us')
        return redirect('home')
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')


class PostDetailView(DetailView):
    model=Post