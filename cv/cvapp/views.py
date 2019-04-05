from django.shortcuts import render
from django.shortcuts import HttpResponse
def index(request):
	context = {}
	return render(request,"index.html",context)

'''def contact(request):
    thank = False
    if request.method=="POST":
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('sub', '')
        message = request.POST.get('msg', '')
        contact = Contact(name=name, phone=phone, email=email, subject=sub, message=msg)
        contact.save()
        thank = True
    return render(request, 'shop/contact.html', {'thank': thank})	'''