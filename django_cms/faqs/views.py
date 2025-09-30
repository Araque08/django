from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET
from .models import FAQ

def faq_page(request):
    # Sirve la plantilla fyq.html
    return render(request, "faqs/fyq.html")

@require_GET
def faqs_api(request):
    """
    GET /api/faqs?published=true|false&limit=200
    Responde JSON: items: [ { id, slug, title, answer, category, updated_at, published } ]
    """
    qs = FAQ.objects.all()
    published_param = request.GET.get("published")
    if published_param is not None:
        if published_param.lower() in ("true", "1", "yes", "y"):
            qs = qs.filter(published=True)
        elif published_param.lower() in ("false", "0", "no", "n"):
            qs = qs.filter(published=False)

    limit = int(request.GET.get("limit", "200"))
    qs = qs[:max(1, min(limit, 1000))]  # tope

    items = [{
        "id": faq.id,
        "slug": faq.slug,
        "title": faq.question,
        "question": faq.question,
        "answer": faq.answer,           # HTML permitido (del admin)
        "category": faq.category or "",
        "updated_at": faq.updated_at.isoformat(),
        "published": faq.published,
    } for faq in qs]

    return JsonResponse({"items": items}, status=200, json_dumps_params={"ensure_ascii": False})
