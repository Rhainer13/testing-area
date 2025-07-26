from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import IncidentReport
from .forms import VictimForm, IncidentForm, PerpetratorForm

# Create your views here.
# def form1(request):
#     if request.method == 'POST':
#         form = Model1Form(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('form2')
#     else:
#         form = Model1Form()
#     return render(request, 'app1/form1.html', {'form': form})

# def form2(request):
#     if request.method == 'POST':
#         form = Model2Form(request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request, 'app1/form2_success.html')
#     else:
#         form = Model2Form()
#     return render(request, 'app1/form2.html', {'form': form})

# def form3(request):
#     if request.method == 'POST':
#         form = Model3Form(request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request, 'app1/form3_success.html')
#     else:
#         form = Model3Form()
#     return render(request, 'app1/form3.html', {'form': form})

def victim_step(request):
    if request.method == 'POST':
        form = VictimForm(request.POST)
        if form.is_valid():
            request.session['victim_data'] = form.cleaned_data
            return redirect('incident_step')
    else:
        form = VictimForm()
    return render(request, 'app1/victim_form.html', {'form': form})


def incident_step(request):
    if request.method == 'POST':
        form = IncidentForm(request.POST)
        if form.is_valid():
            incident_data = form.cleaned_data
            # Convert date to string for session storage
            if 'incident_date' in incident_data:
                incident_data['incident_date'] = incident_data['incident_date'].isoformat()
            request.session['incident_data'] = incident_data
            return redirect('perpetrator_step')
    else:
        form = IncidentForm()
    return render(request, 'app1/incident_form.html', {'form': form})


def perpetrator_step(request):
    if request.method == 'POST':
        form = PerpetratorForm(request.POST)
        if form.is_valid():
            victim_data = request.session.get('victim_data')
            incident_data = request.session.get('incident_data')
            perpetrator_data = form.cleaned_data

            # Save to DB
            IncidentReport.objects.create(
                victim_name=victim_data['name'],
                victim_age=victim_data['age'],
                contact_number=victim_data['contact_number'],

                incident_date=incident_data['incident_date'],
                location=incident_data['location'],
                is_electronic=incident_data['is_electronic'],
                electronic_medium=incident_data.get('electronic_medium', ''),

                perpetrator_name=perpetrator_data['name'],
                relationship=perpetrator_data['relationship'],
                description=perpetrator_data['description']
            )

            # Clear session
            request.session.flush()
            return HttpResponse("Report submitted successfully!")

    else:
        form = PerpetratorForm()
    return render(request, 'app1/perpetrator_form.html', {'form': form})