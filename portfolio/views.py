from django.shortcuts import render, get_object_or_404, redirect
from .models import Portfolio
from .forms import PortfolioForm
import pdfkit
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.conf import settings

# Create your views here.
def portfolio_list(request):
    portfolios = Portfolio.objects.all()
    return render(request, 'portfolio-list.html', {'portfolios': portfolios})


def portfolio_detail(request, id):
    portfolio = get_object_or_404(Portfolio, id=id)
    return render(request, 'portfolio-detail.html', {'portfolio': portfolio})


def portfolio_create(request):
    form = PortfolioForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('portfolio:list')

    return render(request, 'portfolio-create.html', {'form': form})


def portfolio_pdf(request, id):
    portfolio = Portfolio.objects.get(id=id)
    html = render_to_string('portfolio-pdf.html', {'portfolio': portfolio})
    pdf = pdfkit.from_string(html, False, configuration=settings.PDFKIT_CONFIG, options=settings.PDFKIT_OPTIONS)

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{portfolio.name}_{portfolio.surname}_portfolio.pdf"'

    return response