import json
from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import render
from .models import Todo
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def list_todos(request):
    data = list(
        Todo.objects.order_by('-created_at').values('id', 'title', 'done', 'created_at')
    )
    return JsonResponse({'todos': data})

@csrf_exempt
def create_todo(request):
    if request.method != 'POST':
        return HttpResponseBadRequest('POST required')
    try:
        body = json.loads(request.body.decode('utf-8'))
    except json.JSONDecodeError:
        return HttpResponseBadRequest('invalid Json')

    title = (body.get('title') or '').strip()
    if not title:
        return HttpResponseBadRequest('title is missin')

    t = Todo.objects.create(title=title)
    return JsonResponse(
        { 'id': t.id, 'title': t.title, 'done': t.done, 'created_at': t.created_at }
    )
