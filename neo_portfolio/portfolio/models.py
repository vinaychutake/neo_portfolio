from django.db import models

from ckeditor.fields import RichTextField

from adminsortable.models import SortableMixin

DB_TYPES = (
    ('NoSql','NoSql'),
    ('RDBMS','RDBMS'),
    ("Other","Other"),)


class Technology(models.Model):
    name = models.CharField(max_length=60, unique=True)
    symbol = models.ImageField(blank=True)
    description = models.CharField(max_length=60, default="", null=True, blank = True)

    class Meta:
        verbose_name_plural = "Technologies"
    
    def __unicode__(self):
        return unicode(self.name)

class ProjectImage(models.Model):
    images = models.ImageField()
    
    def __unicode__(self):
        return unicode(self.images)

class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    status = models.BooleanField(max_length=20, default=False)

    class Meta:
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return unicode(self.name)

class Library(models.Model):
    name = models.CharField(max_length=20, unique=True)

    class Meta:
        verbose_name_plural = "Libraries"

    def __unicode__(self):
        return unicode(self.name)

class Versioning(models.Model):
    name = models.CharField(max_length=20, unique=True)
    
    class Meta:
        verbose_name_plural = "Versioning"
    
    def __unicode__(self):
        return unicode(self.name)

class Database(models.Model):
    name = models.CharField(max_length=20, unique=True)
    db_type = models.CharField(max_length=20,choices=DB_TYPES,default="Other")
    
    def __unicode__(self):
        return unicode(self.name)

class Project(SortableMixin):
    name = models.CharField(max_length=60, unique=True)
    description = RichTextField(default="Description of project")
    url = models.CharField(max_length=100)
    logo = models.ImageField(blank=True)
    created_date = models.DateTimeField(null=True,blank=True,auto_now_add=True)
    updated_date = models.DateTimeField(null=True,blank=True,auto_now=True)
    is_active = models.BooleanField(max_length=1,default=False,help_text="Select if the project is activeself.")
    technologies = models.ManyToManyField(Technology)
    images = models.ManyToManyField(ProjectImage)
    order_sequence = models.IntegerField(default=0)
    category = models.ForeignKey(Category, blank=True, null=True)
    client_name = models.CharField(max_length=60,null=True,blank=True)
    version_control = models.ForeignKey(Versioning, null=True)
    localization = models.BooleanField(default=False,help_text=" ::- need to add.")
    third_party_library = models.ManyToManyField(Library)
    production_link = models.CharField(max_length=100,null=True,blank=True)
    dev_link = models.CharField(max_length=100,null=True,blank=True)
    database_used = models.ManyToManyField(Database)
    created_by = models.CharField(max_length=100, null = True, blank= True)

    class Meta:
        ordering = ['order_sequence']

    def __unicode__(self):
        return unicode(self.name)


