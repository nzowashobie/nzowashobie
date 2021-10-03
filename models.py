from django.db import models
from django.db.models import Model

class Photos(models.Model):
    name = models.CharField(max_length=50,null=True)
    Biography = models.TextField()
    images = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name

#albums
class Catalbum(models.Model):
   
    album = models.CharField(max_length=50,null=True, unique=True)
    art = models.FileField(upload_to='covers') 
    def __str__(self):
        return  self.album

#album songs

class Item(models.Model):
    album = models.CharField(max_length=50,null=True)
    Artist = models.CharField(max_length=50,null=True)
    Songs = models.FileField(upload_to='albums')
    Title = models.CharField(max_length=50,null=True)
    category = models.ForeignKey(Catalbum, on_delete = models.CASCADE)
    genre = models.CharField(max_length=50,null=True)
    year = models.CharField(max_length=50,null=True)
    art = models.FileField(upload_to='albums') 
   

    def __str__(self):
        return  (self.Title)
#hip hop albums
class Catag_hiphop(models.Model):
   
    album = models.CharField(max_length=50,null=True, unique=True)
    art = models.FileField(upload_to='hiphop_covers') 
    def __str__(self):
        return  self.album

#hip hop album songs
class Hip_hop_abums(models.Model):
    album = models.CharField(max_length=50,null=True)
    Artist = models.CharField(max_length=50,null=True)
    Songs = models.FileField(upload_to='hiphop_albums')
    Title = models.CharField(max_length=50,null=True)
    category = models.ForeignKey(Catag_hiphop, on_delete = models.CASCADE)
    genre = models.CharField(max_length=50,null=True)
    year = models.CharField(max_length=50,null=True)
    art = models.FileField(upload_to='hiphop_albums_art') 
   

    def __str__(self):
        return  (self.Title)
     
#videos
class vid(models.Model):
    id= models.CharField(max_length=10,primary_key=True)
    song = models.CharField(max_length=50,null=True)
    artist = models.CharField(max_length=50,null=True)
    genre = models.CharField(max_length=10,null=True)
    video = models.FileField(upload_to='videos')
    poster = models.FileField(upload_to='videos_covers')
    def __str__(self):
        return self.song       

#Live Performance
class Live(models.Model):
    id= models.CharField(max_length=10,primary_key=True)
    song = models.CharField(max_length=50,null=True)
    artist = models.CharField(max_length=50,null=True)
    genre = models.CharField(max_length=10,null=True)
    video = models.FileField(upload_to='videos')
    def __str__(self):
        return self.song       


#movies
class mov(models.Model):
    id= models.CharField(max_length=10,primary_key=True)
    title = models.CharField(max_length=50,null=True)
    comments = models.TextField()
    genre = models.CharField(max_length=10,null=True)
    movie = models.FileField(upload_to='movies')
    poster = models.FileField(upload_to='posters')
   

    def __str__(self):
        return self.title 

#school files
class skool(models.Model):
    id= models.CharField(max_length=10,primary_key=True)
    Title = models.CharField(max_length=100,null=True)
    comments = models.CharField(max_length=1000,null=True)
    file = models.FileField(upload_to='files')
    cover = models.FileField(upload_to='book_cover')
   

    def __str__(self):
        return self.Title      
#rnb
class Tracks(models.Model):
    id= models.CharField(max_length=10,primary_key=True)
    song = models.CharField(max_length=50,null=True)
    artist = models.CharField(max_length=50,null=True)
    genre = models.CharField(max_length=10,null=True)
    audio = models.FileField(upload_to='RnB')
    art = models.FileField(upload_to='RnB_art')

    def __str__(self):
        return self.song

#african music  
class Africa_muzik(models.Model):
    id= models.CharField(max_length=10,primary_key=True)
    song = models.CharField(max_length=50,null=True)
    artist = models.CharField(max_length=50,null=True)
    genre = models.CharField(max_length=10,null=True)
    audio = models.FileField(upload_to='afrobeat')
    art = models.FileField(upload_to='afrobeat_art')

    def __str__(self):
        return self.song

    #zed music  
class beats_Z(models.Model):
    id= models.CharField(max_length=10,primary_key=True)
    song = models.CharField(max_length=50,null=True)
    artist = models.CharField(max_length=50,null=True)
    genre = models.CharField(max_length=10,null=True)
    audio = models.FileField(upload_to='zedbeat')
    art = models.FileField(upload_to='zedbeat_art')

    def __str__(self):
        return self.song

  #gospel  
class gospel(models.Model):
    id= models.CharField(max_length=10,primary_key=True)
    song = models.CharField(max_length=50,null=True)
    artist = models.CharField(max_length=50,null=True)
    genre = models.CharField(max_length=10,null=True)
    audio = models.FileField(upload_to='gospel')
    art = models.FileField(upload_to='gospel_art')

    def __str__(self):
        return self.song

  #hiphop 
class Hiphop(models.Model):
    id= models.CharField(max_length=10,primary_key=True)
    song = models.CharField(max_length=50,null=True)
    artist = models.CharField(max_length=50,null=True)
    genre = models.CharField(max_length=10,null=True)
    audio = models.FileField(upload_to='Hiphop')
    art = models.FileField(upload_to='Hiphop_art')

    def __str__(self):
        return self.song

#zed videos
class zed_vid(models.Model):
    id= models.CharField(max_length=10,primary_key=True)
    song = models.CharField(max_length=50,null=True)
    artist = models.CharField(max_length=50,null=True)
    genre = models.CharField(max_length=10,null=True)
    video = models.FileField(upload_to='zed_videos')
    poster = models.FileField(upload_to='zed_vidz_covers')
    def __str__(self):
        return self.song 

#hiphop videos
class hiphop_vid(models.Model):
    id= models.CharField(max_length=10,primary_key=True)
    song = models.CharField(max_length=50,null=True)
    artist = models.CharField(max_length=50,null=True)
    genre = models.CharField(max_length=10,null=True)
    video = models.FileField(upload_to='hiphop_videos')
    def __str__(self):
        return self.song 

  #hiphop 
class Classic_Hiphop(models.Model):
    id= models.CharField(max_length=10,primary_key=True)
    song = models.CharField(max_length=50,null=True)
    artist = models.CharField(max_length=50,null=True)
    genre = models.CharField(max_length=10,null=True)
    audio = models.FileField(upload_to='classic_Hiphop')
    art = models.FileField(upload_to='classic_Hip_art')
    def __str__(self):
        return self.song 
#rnb 
class Classic_Rnb(models.Model):
    id= models.CharField(max_length=10,primary_key=True)
    song = models.CharField(max_length=50,null=True)
    artist = models.CharField(max_length=50,null=True)
    genre = models.CharField(max_length=10,null=True)
    audio = models.FileField(upload_to='classic_RnB')
    art = models.FileField(upload_to='classic_RnB_art')
    def __str__(self):
        return self.song 
#class hiphop 
class Classic_zed(models.Model):
    id= models.CharField(max_length=10,primary_key=True)
    song = models.CharField(max_length=50,null=True)
    artist = models.CharField(max_length=50,null=True)
    genre = models.CharField(max_length=10,null=True)
    audio = models.FileField(upload_to='classic_zed')
    art = models.FileField(upload_to='classic_zed_art')
    def __str__(self):
        return self.song 
#throw back
class Throw_back(models.Model):
    id= models.CharField(max_length=10,primary_key=True)
    song = models.CharField(max_length=50,null=True)
    artist = models.CharField(max_length=50,null=True)
    genre = models.CharField(max_length=10,null=True)
    audio = models.FileField(upload_to='throw_back')
    art = models.FileField(upload_to='throw_art')

    def __str__(self):
        return self.song










   