from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

def upload(request):
    return render(request, "upload.html",{})

    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        
#api django for FileSystemStorage
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    
