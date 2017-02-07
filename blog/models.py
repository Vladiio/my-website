from django.db import models


class Category(models.Model):
    category_title = models.CharField(max_length=30)

    def __str__(self):
        return self.category_title

class Post(models.Model):
    post_title = models.CharField(max_length=100)
    post_body = models.TextField()
    post_date = models.DateTimeField()
    post_category = models.ForeignKey(Category)

    def __str__(self):
        return self.post_title


class Comment(models.Model):
    comment_text = models.TextField(verbose_name='Add comment:')
    comment_post = models.ForeignKey(Post)