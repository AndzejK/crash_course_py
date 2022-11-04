from django.shortcuts import render

from Django.learning_log import learning_logs

# Create your views here.
def index(request):
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Show all topics"""
    topics=Topic.objects.order_by('date_added')
    context={'topipcs':topics}
    return render(request,'learning_logs/topics.html', context)