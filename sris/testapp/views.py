from django.shortcuts import render

# Create your views here.

def homeintro_view(request):
    return render(request,'testapp/homeintro.html')
def photos_view(request):
    return render(request,'testapp/photos.html')
def introduce_view(request):
    return render(request,'testapp/introduce.html')
def brand_view(request):
    return render(request,'testapp/brand.html')
def aboutme_view(request):
    return render(request,'testapp/illustration.html')
def pricing_view(request):
    return render(request,'testapp/pricing.html')
# Create your views here.

from django.shortcuts import redirect


###eeeee

















from testapp import forms

# Create your views here.
def thanksview(request):
    return render(request,'testapp/thanks.html')
def contactview(request):
    form=forms.ContactForm()
    if request.method=='POST':
        form=forms.ContactForm(request.POST)
        if form.is_valid:
            form.save(commit=True)
            return thanksview(request)
            print("message send  sucess fully")
    return render(request,'testapp/reg.html',{'form':form})



def Introview(request):



    return render(request,'testapp/introduce.html')
