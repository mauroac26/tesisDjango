from xhtml2pdf import pisa
from django.template.loader import get_template
from io import BytesIO
from django.http import HttpResponse

def render_pdf(template_src, contexto={}):
    template = get_template(template_src)
    html = template.render(contexto)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("iso-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None