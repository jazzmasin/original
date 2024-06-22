from django.shortcuts import render, redirect
from .forms import VisionTestForm
from .models import VisionTest

def vision_test(request):
    if request.method == 'POST':
        form = VisionTestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('results')
    else:
        form = VisionTestForm()
    return render(request, 'vision/vision_test.html', {'form': form})

def results(request):
    tests = VisionTest.objects.all().order_by('-date')
    return render(request, 'vision/results.html', {'tests': tests})


