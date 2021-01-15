import django_filters
from blog.models import BlogPostDB
from django_filters import CharFilter
class FiltersPost(django_filters.FilterSet):
	title = CharFilter(field_name='title', lookup_expr='icontains')
	class Meta:
		model = BlogPostDB
		fields = '__all__'
		