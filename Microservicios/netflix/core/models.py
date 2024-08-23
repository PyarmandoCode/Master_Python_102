from django.db import models

class TypePerson(models.Model):
    type_person=(
        ('Actor_Actress','Actor_Actress'),
        ('Director','Director'),
        ('Producer','Producer')
    )
    type_id=models.AutoField(primary_key=True)
    type=models.CharField(max_length=15,choices=type_person)
    state=models.BooleanField(default=True)
    created_at=models.DateTimeField('created_at',auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % self.type

    class Meta:
        verbose_name="TypePerson"    
        verbose_name_plural="Tipo_de_Personas"
        ordering=['type']

class Person(models.Model):
    person_id=models.AutoField(primary_key=True)
    lastname=models.CharField(max_length=180)
    firstname=models.CharField(max_length=180)
    aliases=models.CharField(max_length=80,blank=True,null=True)
    typepersona=models.ForeignKey(TypePerson,on_delete=models.CASCADE,related_name='person')
    photo=models.ImageField(upload_to='person',blank=True,null=True)
    state=models.BooleanField(default=True)
    created_at=models.DateTimeField('created_at',auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s' % (self.lastname , self.firstname)

    class Meta:
        verbose_name="Person"    
        verbose_name_plural="Personas"
        ordering=['firstname']


class Movie(models.Model):
    genre_options = (
        ('Horro','Horro'),
        ('Drama','Drama'),
        ('Comedy','Comedy'),
        ('Scifi','Scifi'),
        ('Action','Action'),
    )
    movie_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=180)
    sipnosis=models.TextField(blank=True,null=True)
    release_year=models.IntegerField()
    language=models.CharField(max_length=20)
    genre=models.CharField(max_length=10,choices=genre_options)
    Actor_Actress=models.ManyToManyField(Person,related_name='actor_actress')
    Director=models.ManyToManyField(Person,related_name='director')
    Producer=models.ManyToManyField(Person,related_name='producer')
    top=models.ImageField(upload_to='movies',blank=True,null=True)
    state=models.BooleanField(default=True)
    created_at=models.DateTimeField('created_at',auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % self.title 

    class Meta:
        verbose_name="Movie"    
        verbose_name_plural="Peliculas"
        ordering=['title']









