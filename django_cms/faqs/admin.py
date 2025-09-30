from django.contrib import admin
from .models import FAQ

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question", "category", "published", "updated_at")
    list_filter  = ("published", "category")
    search_fields = ("question", "answer", "category", "slug")
    readonly_fields = ("updated_at", "created_at")
    prepopulated_fields = {"slug": ("question",)}
