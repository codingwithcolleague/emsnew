from .models import Question

def poll_count(request):
    count = Question.objects.count()
    return {"poolcount" : count}