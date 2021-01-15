from django.shortcuts import render,get_object_or_404
from blog.models import BlogPostDB
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from blog.filters import FiltersPost

BLOG_POSTS_PER_PAGE = 6

def home_screen_view(request):
	context={}
	posts = BlogPostDB.objects.all()
	myFilter = FiltersPost(request.GET, queryset=posts)
	posts = myFilter.qs
	context['myFilter']=myFilter
	# Pagination
	page = request.GET.get('page', 1)
	blog_posts_paginator = Paginator(posts, BLOG_POSTS_PER_PAGE)

	try:
		posts = blog_posts_paginator.page(page)
	except PageNotAnInteger:
		posts = blog_posts_paginator.page(BLOG_POSTS_PER_PAGE)
	except EmptyPage:
		posts = blog_posts_paginator.page(blog_posts_paginator.num_pages)
	context['posts']=posts	
	return render(request,'blog/home_screen_view.html',context)

def detail_blog_view(request, slug):
	context = {}

	blog_post = get_object_or_404(BlogPostDB, title=slug)
	context['blog_post'] = blog_post
	another_blog_post = BlogPostDB.objects.exclude(title=slug)[0:6]
	context['another_blog_post'] = another_blog_post
	return render(request, 'blog/detail_blog.html', context)
