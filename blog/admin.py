from django.contrib import admin

from .models import Article, Tag, Category

admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(Category)

# formfield_overrides = {
#     Article.content: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
# }