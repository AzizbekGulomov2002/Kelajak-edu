from django.db import models

# Create your models here.

class Markaz(models.Model):
    rasm = models.ImageField(upload_to='jamoa_rasm')
    markaz_nomi = models.CharField(max_length=200)
    malumot = models.TextField()
    
    
    email = models.CharField(max_length=100, null=True, blank=True)
    telefon = models.IntegerField(null=True, blank=True)
    telegram = models.CharField(max_length=200)
    instagram = models.CharField(max_length=200)
    youtube = models.CharField(max_length=200)

    oquvchilar = models.IntegerField()
    yonalishlar = models.IntegerField()
    kurslar = models.IntegerField()
    hodimlar = models.IntegerField()
    def __str__(self):
        return f"{self.markaz_nomi} | {self.email} | {self.telefon}"
    class Meta:
        verbose_name = 'Markaz'
        verbose_name_plural = "Markaz"
        
        

class Kurslar(models.Model):
    rasm = models.ImageField(upload_to='jamoa_rasm')
    nomi = models.CharField(max_length=200)
    kurs_davomiyligi = models.CharField(max_length=200)
    dars_davomiyligi = models.CharField(max_length=200)
    narxi = models.CharField(max_length=100)
    oqituvchi = models.CharField(max_length=13)
    boglanish = models.CharField(max_length=13)
    
    def __str__(self):
        return f"{self.nomi} | {self.kurs_davomiyligi} | {self.narxi}"
    class Meta:
        verbose_name = 'Kurs'
        verbose_name_plural = "Kurslar"
        

class Xizmatlar(models.Model):
    rasm = models.ImageField(upload_to='jamoa_rasm')
    nomi = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.nomi}"
    class Meta:
        verbose_name = 'Xizmat'
        verbose_name_plural = "Xizmatlar"
        
        
        

class Galereya(models.Model):
    rasm = models.ImageField(upload_to='jamoa_rasm')
    def __str__(self):
        return "Rasmlar"
    class Meta:
        verbose_name = 'Galereya'
        verbose_name_plural = "Galereyalar"
        
        
        

class Jamoa(models.Model):
    rasm = models.ImageField(upload_to='jamoa_rasm')
    ism_sharif = models.CharField(max_length=200)
    vazifa = models.CharField(max_length=200)
    telegram = models.CharField(max_length=200,null=True, blank=True)
    telefon = models.CharField(max_length=200,null=True, blank=True)
    instagram = models.CharField(max_length=200,null=True, blank=True)
    def __str__(self):
        return f"{self.ism_sharif}"
    class Meta:
        verbose_name = 'Jamoa'
        verbose_name_plural = "Jamoa"
        
        

# class Bitiruvchi(models.Model):
#     rasm = models.ImageField(upload_to='jamoa_rasm')
#     ism_sharif = models.CharField(max_length=200)
#     tarix = models.TextField(null=True, blank=True)
#     def __str__(self):
#         return f"{self.ism_sharif}"
#     class Meta:
#         verbose_name = 'Bitiruvchi'
#         verbose_name_plural = "Bitiruvchilar"
        
        

class Blog(models.Model):
    rasm = models.ImageField(upload_to='jamoa_rasm')
    nom = models.CharField(max_length=200)
    sana = models.DateTimeField()
    batafsil = models.TextField(null=True, blank=True)
    viewed = models.IntegerField(default=1)
    def __str__(self):
        return f"{self.nom}"
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = "Bloglar"
        


# class VideoKontent(models.Model):
#     nomi = models.CharField(max_length=500)
#     sana = models.DateTimeField()
#     link = models.URLField(help_text="youtu.be ning o'rniga youtube.com/embed so'zini kiriting")
#     def __str__(self):
#         return f"{self.nomi}"
#     class Meta:
#         verbose_name = 'Video Kontent'
#         verbose_name_plural = "Video kontentlar"
        
