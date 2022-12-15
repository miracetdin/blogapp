from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)

    # slug oluşturma
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

# Create your models here.
class Blog(models.Model):
    # charField -> inputText (html)
    # charField da 2. parametre olarak null=True gönderilirse bu özelliğe herhangi
    # bir değer atanmadan bu kayıt oluşturulabilir, varsayılan -> null=False
    title = models.CharField(max_length=200)
    # image = models.CharField(max_length=50)
    image = models.ImageField(upload_to="blogs")
    # bool attribute ler için default ile varsayılan value atanabilir
    is_active = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)
    # textField -> TextArea
    # description = models.TextField()
    description = RichTextField()
    # url slug; blank=True ile admin paneli üzerinde slug girilmesi zorunluluğu kalkar
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=True)
    # many-to-many e çevrildi
    # category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)

    # temsil
    def __str__(self):
        return f"{self.title}"

    # slug oluşturma
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)