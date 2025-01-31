from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title[:15]


class Post(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts'
    )
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True)
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL,
        related_name="posts", blank=True, null=True
    )

    def __str__(self):
        return self.text[:15]


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)


class Follow(models.Model):
    """
    User(follower-подписчик) подписавшийся на некого Author(following)
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='followers',
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='followings',
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='follow_unique',
            ),
            models.CheckConstraint(
                check=~models.Q(following=models.F('user')),
                name="following_not_user"
            ),
        ]
