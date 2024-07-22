from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import DonorForm
from .models import Donor, Donation
# Create your views here.
def donor_create(request):
   
    donors = Donor.objects.all()
    if request.method == 'POST':
        form = DonorForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'donor_list.html',{
                'donors': donors
            })
    else:
        form = DonorForm()
    return render(request, 'donations.html', {'form': form})

def list_donations(request):
    search = request.GET.get('search')
    donors = Donor.objects.all()
    if search:
        donors = Donor.objects.filter(name__icontains=search)
    else:
        
       # print(search)
    
        donors = Donor.objects.all()
    
    
    return render(request, 'donor_list.html', {
        'donors': donors,
    
                                               
                                               })

def donor_info(request, id):
    donor = Donor.objects.filter(identification=id).first()
    last_donation = donor.donations.all()
    print(last_donation)
    if donor:
        print(donor.name)
    return render(request, 'donor_info.html', {
        'donor': donor
        
                                               
                                               })

def home(request):
    return render(request, 'home.html')
    
