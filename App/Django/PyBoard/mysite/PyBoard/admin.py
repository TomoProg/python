from django.contrib import admin
from PyBoard.models import Board, TopicArticle, UserInfo

# Register your models here.

class UserInfoAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'password', 'create_datetime', 'del_flag',)
admin.site.register(UserInfo, UserInfoAdmin)

class BoardAdmin(admin.ModelAdmin):
	list_display = ('id', 'topic', 'create_user', 'create_datetime', 'del_flag',)
admin.site.register(Board, BoardAdmin)

class TopicArticleAdmin(admin.ModelAdmin):
	list_display = ('id', 'topic_id', 'article_no', 'create_user', 'article', 'create_datetime', 'del_flag',)
admin.site.register(TopicArticle, TopicArticleAdmin)
