from django.db import models

# from tinymce.models import HTMLField
# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField




class Category(models.Model):
        name = models.CharField(max_length=32)
        class Meta:
                verbose_name_plural = "Categories"
        def __unicode__(self):
                return self.name

class Tag(models.Model):
        name = models.CharField(max_length=32)
        def __unicode__(self):
                return self.name

class Article(models.Model):
        # author = models.ForeignKey(User)
        # category = models.ForeignKey(Category)
        title = models.CharField(max_length=100,unique=True)
        tags = models.ManyToManyField(Tag)
        # background_image = models.URLField(verify_exists=True)
        slug = models.SlugField(max_length=128)
        # content = models.TextField()
        # content = HTMLField()
        # content = RichTextField(config_name='awesome_ckeditor')
        content = RichTextUploadingField(config_name='awesome_ckeditor')
        
        updated_on = models.DateField(auto_now=True)
        created_on = models.DateField(auto_now_add=True)
        publish_on = models.DateField()
        list_display = ('title', 'category', 'tags', 'author', 'publish_on','created_on','updated_on')
        search_fields = ['title','category','content']
        list_filter = ['publish_on','created_on']
        date_hierarchy = 'pub_date'

        #this function just below is probably the coolest aspect of the model. 
        #When a background image url is added the function python scrapes the 
        #image from the web saves the image to a virtual directory mounted via s3fs 
        #& rewrites the url to match the s3 cached version. it does all this 
        #before saving the model ensuring that foreign urls are not saved in the db. 
        #this process is also repeated for the social and link classes. It doesn't 
        #strictly adhere to the DRY principle in that it repeats 3 times, but I wanted 
        #to leave this code more legible and easily extensible by not adding additional 
        #classes as each model reperesents an entirely different concept.

        # def save(self, *args, **kwargs):
        #         webfile = urllib2.urlopen(self.background_image)
        #         extension = mimetypes.guess_type(self.background_image)[0].split("/")[1]
        #         self.background_image = '%s/image/post/%s.%s' % (settings.BASE_URL,self.slug,extension )
        #         output = open('home/periodic/mnt' + self.background_image ,'w')
        #         output.write(webfile.read())
        #         output.close()
        #         webfile.close()
        #         super(Post, self).save(*args, **kwargs)

        def __unicode__(self):
                return self.title