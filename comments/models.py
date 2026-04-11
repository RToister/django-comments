from django.db import models
from django.core.validators import RegexValidator
import bleach
from PIL import Image


class Comment(models.Model):
    username = models.CharField(
        max_length=50,
        validators=[
            RegexValidator(regex=r"^[a-zA-Z0-9]+$", message="Тільки латиниця і цифри")
        ],
    )

    email = models.EmailField()
    homepage = models.URLField(blank=True, null=True)
    text = models.TextField()

    file = models.FileField(upload_to="uploads/", blank=True, null=True)

    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="replies"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        allowed_tags = ["a", "code", "i", "strong"]
        allowed_attributes = {"a": ["href", "title"]}

        self.text = bleach.clean(
            self.text, tags=allowed_tags, attributes=allowed_attributes, strip=True
        )

        super().save(*args, **kwargs)

        # тільки resize картинки
        if self.file:
            file_path = self.file.path

            if file_path.lower().endswith((".jpg", ".jpeg", ".png", ".gif")):
                img = Image.open(file_path)
                img.thumbnail((320, 240))
                img.save(file_path)

    def __str__(self):
        return self.username
