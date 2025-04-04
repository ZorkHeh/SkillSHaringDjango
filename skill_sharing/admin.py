from django.contrib import admin

from skill_sharing.models import Article, Comment, CommentLike, ArticleLike
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(CommentLike)
admin.site.register(ArticleLike)
