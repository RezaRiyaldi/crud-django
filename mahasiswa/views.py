from django.shortcuts import render, redirect, get_object_or_404
from .forms import BiodataMhs
from .models import Data_mhs

# Create your views here.

def index(request):
    hasil = Data_mhs.objects.all()
    print(hasil)
    data = {
        'data':hasil,
    }
    return render(request, 'index.html', data)

def tambah(request):    
    form = BiodataMhs(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/')
        pass
    return render(request, 'tambah.html', {'form':form})

def edit(request, id_mhs):
    obj = get_object_or_404(Data_mhs, id_mhs = id_mhs)

    form = BiodataMhs(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    data = {
        'mhs':obj,
    }
    return render(request, 'editdata.html', data)

def hapus(request, id_mhs):
    dt = Data_mhs.objects.get(id_mhs = id_mhs)
    dt.delete()
    return redirect('/')