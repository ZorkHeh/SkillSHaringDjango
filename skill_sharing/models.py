from django.contrib.auth.models import User
from django.db import models
from django.db.models import ForeignKey


class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def get_total_likes(self):
        return self.articlelike_set.filter(is_liked=True).count()

    def get_total_dislikes(self):
        return self.articlelike_set.filter(is_liked=False).count()

    def get_total_comments(self):
        return self.comment_set.count()

    def get_comments(self):
        return self.comment_set.all()

    def get_excerpt(self, length=1300):
        if len(self.content) > length:
            return self.content[:length] + "..."
        elif len(self.content) < length:
            return self.content


class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)

    date = models.DateTimeField(auto_now_add=True)

    def get_total_likes(self):
        return self.commentlike_set.filter(is_liked=True).count()

    def get_total_dislikes(self):
        return self.commentlike_set.filter(is_liked=False).count()

class ArticleLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    is_liked = models.BooleanField()


class CommentLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    is_liked = models.BooleanField()
