from django.shortcuts import render,get_object_or_404
from .forms import RequestForm
from .models import Request
from django.utils import timezone

# Create your views here.
def request_list(request):
    print(Request.objects.all)
    requests = Request.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'leave/request_list.html', {'requests': requests})
    

def request_new(request):
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            requests = form.save(commit=False)
            requests.author = request.user
            requests.published_date = timezone.now()
            requests.save()
            return redirect('request_detail', pk=requests.pk)
    else:
        form = RequestForm()
    return render(request, 'leave/request_edit.html', {'form': form})


def request_detail(request, pk):
    requests = get_object_or_404(Request, pk=pk)
    return render(request, 'leave/request_detail.html', {'requests': requests})
