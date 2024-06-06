from django.shortcuts import render, get_object_or_404, redirect
from .models import Portfolio
from .forms import PortfolioForm

# Create your views here.
def home_view(request):
    return render(request, 'index.html')


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
        return redirect('home')

    return render(request, 'portfolio-create.html', {'form': form})