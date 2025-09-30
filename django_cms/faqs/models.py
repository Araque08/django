from django.db import models
from django.utils.text import slugify

class FAQ(models.Model):
    question = models.CharField("Pregunta", max_length=255)
    answer = models.TextField("Respuesta", help_text="Permite HTML seguro (párrafos, listas, enlaces)")
    category = models.CharField("Categoría", max_length=80, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, help_text="Se autogenera a partir de la pregunta")
    published = models.BooleanField("Publicado", default=True)
    updated_at = models.DateTimeField("Actualizado", auto_now=True)
    created_at = models.DateTimeField("Creado", auto_now_add=True)

    class Meta:
        ordering = ['-updated_at']
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

    def __str__(self):
        return self.question

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.question)[:50]
            slug = base
            i = 1
            while FAQ.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                i += 1
                slug = f"{base}-{i}"
            self.slug = slug
        super().save(*args, **kwargs)
