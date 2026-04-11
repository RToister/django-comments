from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["username", "email", "homepage", "text", "file"]

    def clean_file(self):
        file = self.cleaned_data.get("file")

        if not file:
            return file

        name = file.name.lower()

        if not name.endswith((".jpg", ".jpeg", ".png", ".gif", ".txt")):
            raise forms.ValidationError("Дозволені тільки JPG, PNG, GIF, TXT")

        if name.endswith(".txt"):
            if file.size > 100 * 1024:
                raise forms.ValidationError("TXT файл більше 100KB")

        return file
