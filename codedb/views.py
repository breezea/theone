from django.shortcuts import render
from django.http import JsonResponse
from .models import CodeModel
from .config import *

# Create your views here.
def demo(requests):

    data = {
        "code": 200,
        "msg": "theone!"
    }
    return JsonResponse(data)

def addCodeSnippets(requests):
    params = requests.GET
    new_item = CodeModel(
        title=params.get('title'), 
        languages=params.get('languages'),
        desc=params.get('desc'), 
        tags=params.get('tags'), 
        code=params.get('code'), 
    ) 
    res = new_item.save()
    if (res) :
        return JsonResponse({ 'code': error_code,'msg': str(res) }) 
    else:
        return JsonResponse({ 'code': ok_code, 'msg': '' })


def retrieveCodeSnippets(requests):
    items = CodeModel.objects.filter()
    # print(items.all())
    print(list(items))
    return JsonResponse({ 'code': ok_code, 'msg': ''})

def deleteCodeSnippets(requests):
    doc_id = requests.POST.get('id')
    # print(requests.POST)
    item = CodeModel.objects.get(id=doc_id)
    status, res = item.delete()
    print(status, res)
    return JsonResponse({'code': ok_code, 'msg': 'delete successful'})

    
# 增删改查

