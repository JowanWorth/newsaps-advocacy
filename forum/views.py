from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import ForumCategory, ForumTopic, ForumPost
from .forms import TopicForm, PostForm

def forum_home(request):
    categories = ForumCategory.objects.all()
    return render(request, 'forum/home.html', {'categories': categories})

def category_detail(request, category_id):
    category = get_object_or_404(ForumCategory, id=category_id)
    topics = ForumTopic.objects.filter(category=category)
    return render(request, 'forum/category_detail.html', {'category': category, 'topics': topics})

@login_required
def create_topic(request, category_id):
    category = get_object_or_404(ForumCategory, id=category_id)
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.category = category
            topic.created_by = request.user
            topic.save()
            return redirect('topic_detail', topic_id=topic.id)
    else:
        form = TopicForm()
    return render(request, 'forum/create_topic.html', {'form': form, 'category': category})

def topic_detail(request, topic_id):
    topic = get_object_or_404(ForumTopic, id=topic_id)
    posts = ForumPost.objects.filter(topic=topic)
    return render(request, 'forum/topic_detail.html', {'topic': topic, 'posts': posts})

@login_required
def create_post(request, topic_id):
    topic = get_object_or_404(ForumTopic, id=topic_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()
            return redirect('topic_detail', topic_id=topic.id)
    else:
        form = PostForm()
    return render(request, 'forum/create_post.html', {'form': form, 'topic': topic})
