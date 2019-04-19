from django.shortcuts import render

def sitemap(request):

   context = {
      'sitemap': sitemap
   }


   return render(request, 'sitemap/sitemap.xml', context) 
