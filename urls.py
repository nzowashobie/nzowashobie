#from project.ninja.models import Africa_muzik
#from project.ninja.models import gospel
#from project.ninja.models import Classic_zed
#from project.ninja.models import beats_Z
#from project.ninja.models import beats_Z
from django.urls import path
from .views import HomePage, Live_Per, classic_r, hiphop, index, throw, z_vidz, zed, zed_old
from .views import Catalbum,classic_hip
from .views import vidz
from .views import movz
from .views import book
from .views import Tracklist
from .views import Item
from .views import SearchResultsView,zed_old,hip_vidz
from .views import afro
from .views import Gospel
from .views import hiphop,Live_Per,throw
from .views import Zed_ResultsView #,player
from . import views
urlpatterns = [
    path('', zed.as_view(), name='zedbeats'),
    path('RNB/zedbeats/', HomePage.as_view(), name='home'),
    path('RNB/throw_back/zedbeats/', HomePage.as_view(), name='home'),
    path('videos/', vidz.as_view(), name='videos'),
    path('movies/', movz.as_view(), name='movies'),
    path('RNB/classic_rnb/school/', book.as_view(), name='school'),
    path('school/', book.as_view(), name='school'),
    path('index/', views.index, name='index'),
    path('index/item', views.index, name='index'),
    path('index/all/', views.jam, name='all'),
    path('RNB/', Tracklist.as_view(), name='RNB'),
    path('item/<int:item_id>/' ,views.item, name='item'),
    #path('song/' ,views.player, name='song'),
    path('all/<int:item_id>/' ,views.hip_hop_abums, name='all'),
    
    path('list/<int:list_id>/' ,views.list, name='list'),
    path('RNB/afrobeats/', afro.as_view(), name='afrobeats'),
    path('RNB/gospel/', Gospel.as_view(), name='gospel'),
    path('videos/zed/', z_vidz.as_view(), name='zed'),
    path('RNB/hiphop/', hiphop.as_view(), name='hiphop'),
    path('RNB/hiphop/classics/', classic_hip.as_view(), name='classics'),
    path('RNB/hiphop/classics/zedbeats', HomePage.as_view(), name='classics'),
    path('RNB/classic_rnb/', classic_r.as_view(), name='classics_rnb'),
    path('classic_zed/', zed_old.as_view(), name='classics_zed'),
    path('RNB/afrobeats/zed/', z_vidz.as_view(), name='zed'),
    path('videos/live_performance/', Live_Per.as_view(), name='live_performance'),
    path('RNB/throw_back/',throw.as_view(), name='throw_back'),
    path('videos/hiphop/', hip_vidz.as_view(), name='hiphop'),  
    path('search/', Zed_ResultsView.as_view(), name='search_results'), 
       
]
