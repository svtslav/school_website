from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views import View
from .models import Page

# Create your views here.
class PageView(View):
    def get(self, request, page_url, *args, **kwargs):
        page = get_object_or_404(Page, url=page_url)

        context = { 'page': page }
        template = 'pages/page.html'
        return render(request, template, context)
