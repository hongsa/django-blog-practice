from django.contrib import admin
from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    # 어드민에서 보여지는 필드 설정
    # 직접 def 지정해서 원하는 내용 따로 설정 가능
    list_display = ('id','title','title_length','title_world_length','created_at','updated_at')

    def title_world_length(self,post):
        return len(post.title.split())


admin.site.register(Post,PostAdmin)

# Register your models here.
