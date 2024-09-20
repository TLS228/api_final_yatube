from django.contrib.auth import get_user_model  # type: ignore
from django.db import models  # type: ignore
from django.db.models import F, Q
from django.db.models import UniqueConstraint, CheckConstraint

User = get_user_model()


class Group(models.Model):
    """Модель для групп, используется для объединения постов по тематикам"""
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Post(models.Model):
    """Модель для постов, хранит информацию о тексте, авторе,
    изображении и группе"""
    text = models.TextField()
    pub_date = models.DateTimeField(
        'Дата публикации', auto_now_add=True
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts'
    )
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='posts',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.text[:15]


class Comment(models.Model):
    """Модель для комментариев,используется для хранения текста комментария,
    автора и поста"""
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments'
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments'
    )
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True
    )


class Follow(models.Model):
    """Модель для подписки на авторов"""
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user'
    )
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following'
    )

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['user', 'following'],
                name='unique_follow'),
            CheckConstraint(
                check=~Q(user=F('following')),
                name='prevent_self_following'),
        ]
