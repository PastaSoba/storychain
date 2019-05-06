from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Story, Storybone
from .forms import StoryForm, StoryboneForm

def index(request):
    storybone = Storybone.objects.get()
    storys = Story.objects.all().order_by('created_at').order_by('id')[0:20]
    return render(request, 'app/index.html', {'storys': storys, 'storybone': storybone})

def aboutus(request):
    return render(request, 'app/aboutus.html')

def submit(request):
    if request.method == 'POST':
        form = StoryForm(request.POST, request.FILES)
        if form.is_valid() and Story.objects.all().count() < 50:
            story = form.save()
            messages.success(request, "投稿が完了しました")
        else:
            messages.error(request, "保存されるメッセージ数の上限に達しています。")
        return redirect('app:index')
    else:
        form = StoryForm()
    return render(request, 'app/submit.html', {'form':form})

@login_required
def master(request):
    if request.method == 'POST':
        form = StoryboneForm(request.POST, request.FILES)
        if form.is_valid():
            storys = Story.objects.all()
            storys.delete()
            prev_storybone = Storybone.objects.all()
            prev_storybone.delete()
            storybone = form.save()
            messages.success(request, "物語の骨子が作成されました。")
        return redirect('app:index')
    else:
        form = StoryboneForm()
    return render(request, 'app/master.html', {'form':form})