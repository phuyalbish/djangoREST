import json
from django.shortcuts import render
from django.http import JsonResponse
from  django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    if request.method=="GET":
       return get_All(request)
    elif request.method=="DELETE":
        res = {
            
            "message":"User Id required",
        }
        return JsonResponse(res, safe=False, status=400)
    elif request.method=="PATCH":
        res = {
            
            "message":"User Id required",
        }
        return JsonResponse(res, safe=False, status=400)
    elif request.method=="POST":
        return post(request)
    else:
        data = {
        "message": "No Method Found"
        }
        return JsonResponse(data, safe=False, status=400)
    

@csrf_exempt
def index2(request, **kwargs):
    if request.method=="GET":
       return get_User(request, **kwargs)
    elif request.method=="PATCH":
        return patch(request,**kwargs)
    elif request.method=="DELETE":
        return delete(request,**kwargs)
    else:
        data = {
        "message": "No Method Found"
        }
    return JsonResponse(data, safe=False, status=400)


def get_All(request):
    data = list(User.objects.all().values())
    # print(data)
    # print("...............................")
    # print(data.values())
    # return
    return  JsonResponse(data, safe=False, status=200)

def get_User(request, **kwargs):
    user_id = kwargs["user_id"]
    data = User.objects.values().get(pk=user_id)
    return  JsonResponse(data, safe=False, status=200)

def delete(request, **kwargs):
    user_id = kwargs.get("user_id")
    deleteduser = User.objects.get(pk=user_id).delete()

    res = {
        "data": deleteduser,
        "message": f"User {user_id} deleted"
    }
    return  JsonResponse(res, safe=False, status=200)

def post(request):
        
        data = json.loads(request.body)

        username = data.get("username")
        password = data.get("password")

        print(username)
        print(password)
        User.objects.create(username=username, password=password)
        res = {
                "data": data,
                "message": f"New User {username } created"
            }
        return  JsonResponse(res, safe=False, status=200)

def patch(request, **kwargs):
    user_id = kwargs.get("user_id")
    data = json.loads(request.body)
    updateuser = User.objects.get(pk=user_id)
    updateuser.__dict__.update(data)
    updateuser.save()
    res = {
                "data": data,
                "message": "User Updated"
            }
    return  JsonResponse(res, safe=False, status=200)
