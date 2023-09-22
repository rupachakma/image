from django.shortcuts import render
from herapp.models import Office

# Create your views here.
def home(request):
    data={}
    if request.method=="POST":
    
        a=request.POST.get('n1')
        b=request.POST.get('a1')
        img=request.FILES.get('imagefile')
        data={
            'x':a,
            'y':b,
        }

        info=Office()
        info.name=a
        info.department=b
        info.profileImg=img
        info.save()
        return render(request,"index.html",data)


    return render(request,"index.html")

def view_data(request):
    office_data = Office.objects.all()
    return render(request,'view_data.html', {'office_data': office_data})