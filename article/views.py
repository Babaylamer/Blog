from django.contrib import messages
from django.shortcuts import redirect, render,get_object_or_404
from .models import Article,Comment
from .forms import ArticleForm
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
@login_required(login_url="user:login")
def dashBord(request):
    articles = Article.objects.filter(author= request.user)
    return render(request,"dashbord.html",{"articles":articles})
@login_required(login_url="user:login")
def AddArticle(request):
    form = ArticleForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        try:
            uploaded_file = request.FILES['article_img']
            fs = FileSystemStorage()
            name = fs.save(uploaded_file.name, uploaded_file)
        except:
            uploaded_file = "anonymon.jpg"
        article = form.save(commit=False)
        article.author = request.user
        article.article_img = str(uploaded_file)
        article.save()
        messages.success(request,"makale başarı ile oluşturuldu")
        return redirect("article:dashbord")
    return render(request,"addArticle.html",{"form":form})
def detail(request,id):
    #article = Article.objects.filter(id=id).first()
    article = get_object_or_404(Article,id=id)
    comments = article.comments.all()
    return render(request,"detail.html",{"article":article,"comments":comments})
@login_required(login_url="user:login")
def updateArticle(request,id):
    article = get_object_or_404(Article,id=id)
    form = ArticleForm(request.POST or None,request.FILES or None,instance=article)
    if form.is_valid():
        article = form.save(commit=False)

        article.author = request.user
        article.save()
        messages.success(request,"Makale başarı ile güncellendi")
        return redirect("article:dashbord")
    return render(request,"update.html",context={"form":form})
@login_required(login_url="user:login")
def deleteArticle(request,id):
    article = get_object_or_404(Article,id = id)
    article.delete()
    messages.success(request,"Makale Başarı ile Silindi")
    return redirect("article:dashbord")
def articles(request):
    keyword = request.GET.get("keyword")
    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        return render(request,"articles.html",context={"articles":articles})
    else:
        articles = Article.objects.all()

    return render(request=request,template_name="articles.html",context={"articles":articles})
@login_required(login_url="user:login")
def addComment(request,artid):
    article = get_object_or_404(Article,id=artid)
    if request.method == "POST":
        comment = request.POST.get("comment")
        newComment = Comment(comment_author=request.user,comment_content=comment)
        newComment.article = article
        newComment.save()
        messages.success(request,"Yorum Başarı ile yapıldı")
    return redirect("/articles/article/"+str(artid))