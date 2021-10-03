from os import name
from django.core import paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Africa_muzik, Catag_hiphop, Classic_Hiphop, Classic_Rnb, Classic_zed, Hip_hop_abums, Hiphop, Live, Photos, Throw_back, beats_Z, gospel, hiphop_vid,vid,mov,skool,Tracks, zed_vid
from django.template import loader
from ninja.models import Catalbum,Item
from django.core.paginator import PageNotAnInteger,EmptyPage, Paginator
from django.db.models import Q
import pyodbc


class HomePage(ListView):
    paginate_by=6
    model = Photos
    template_name = 'homage.html'

class SearchResultsView(ListView):
    paginate_by=6
    model = Photos
    template_name = 'biography.html'


#search format
def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Photos.objects.filter(
            Q(name=query)
        )
        return object_list
    
#albums
#class albums-(ListView):
   #model = album
   #template_name = 'audio.html'



#albums_songs
#class album_hits(albums):
    
    #model =  album_songs
    
    #template_name = 'album_hits.html'    
def index(request):
   #post =  get_object_or_404(album_songs, code=code)
    template = loader.get_template('index.html')
    context = {
        'categories' : Catalbum.objects.all() 
       
    }   
    return HttpResponse(template.render(context, request))
#item
def item(request, item_id):
    template = loader.get_template('item.html')
    context = {
        'item' : Item.objects.get(id=item_id)  
              
    }   
    return HttpResponse(template.render(context, request))

#hiphop

  #list
def list(request, list_id):
    
    template = loader.get_template('list.html')
    context = {
        'list' : Item.objects.get(id=list_id)  
              
    }   
    return HttpResponse(template.render(context, request))

 #videos   
class vidz(ListView):
    paginate_by=6
    model = vid
    template_name = 'videos.html'

 #movies   
class movz(ListView):
    paginate_by=6
    model = mov
    template_name = 'movies.html'

 #school  
class book(ListView):
    paginate_by=6
    model = skool
    template_name = 'school.html' 
#rnb
class Tracklist(ListView):
    paginate_by=6
    model = Tracks
    template_name = 'RNB.html' 

#ZED BEATS

def check(request,check_id): 
  
    # getting all the objects of hotel. 
    check_s = Photos.objects.get(name=check_id)
    #check_s = get_object_or_404(Book, id=book_id) 
    print('myoutput',check_s) 
    return render(request, 'bioz.html',{'bio' : check_s})

#movielist

def play(request,name_id): 
    # getting all the objects of hotel. 
    check_s = mov.objects.get(title=name_id)
    #check_s = get_object_or_404(Book, id=book_id) 
    print('myoutput',check_s) 
    return render(request, 'movieplay.html',{'list' : check_s})

#african musik
class afro(ListView):
    paginate_by=7
    model = Africa_muzik
    template_name = 'african.html' 
 #zed musik   
class zed(ListView):
    paginate_by=7
    model = beats_Z
    template_name = 'zed1.html'

 #gospel   
class Gospel(ListView):
    paginate_by=7
    model = gospel
    template_name = 'gospel.html'

#hiphop
class hiphop(ListView):
    paginate_by=7
    model = Hiphop
    template_name = 'hiphop.html'

#zed video
class z_vidz(ListView):
    paginate_by=6
    model = zed_vid
    template_name = 'zedvideo.html'

#Live Performance
class Live_Per(ListView):
    paginate_by=6
    model = Live
    template_name = 'performance.html'

#classic hihop
class classic_hip(ListView):
    paginate_by=7
    model = Classic_Hiphop
    template_name = 'classics.html'

#classic rnb
class classic_r(ListView):
    paginate_by=7
    model = Classic_Rnb
    template_name = 'classic_rnb.html'

#classic zed
class zed_old(ListView):
    paginate_by=7
    model = Classic_zed
    template_name = 'classic_zed.html'

#classic zed
class hip_vidz(ListView):
    paginate_by=6
    model = hiphop_vid
    template_name = 'hiphopvideos.html'

#album
def jam(request):
   #post =  get_object_or_404(album_songs, code=code)
    template = loader.get_template('hiphop_albums.html')
    context = {
        'categories' : Catag_hiphop.objects.all() 
       
    }   
    return HttpResponse(template.render(context, request))
#item
def hip_hop_abums(request, item_id):
    template = loader.get_template('all.html')
    context = {
        'hip_hop_abums' : Hip_hop_abums.objects.get(id=item_id)  
              
    }   
    return HttpResponse(template.render(context, request))
    
#throwback
class throw(ListView):
    paginate_by=6
    model = Throw_back
    template_name = 'throw_back.html'

# zed search form.
class Zed_ResultsView(ListView):
    paginate_by=6
    model = beats_Z
    template_name = 'zeds.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = beats_Z.objects.filter(
            Q(artist=query)
        )
        return object_list

def bio(request,check_id): 
  
    # getting all the objects of hotel. 
    check_s = Photos.objects.get(name=check_id)
    #check_s = get_object_or_404(Book, id=book_id) 
    print('myoutput',check_s) 
    return render(request, 'bioz.html',{'bio' : check_s})

#ZED BEATS

#def player(request, song_id):
    
 #   template = loader.get_template('zedplay.html')
  #  context = {
   #     'player' : beats_Z.objects.get(id=song_id)  
              
    #}   
    #return HttpResponse(template.render(context, request))

 







 