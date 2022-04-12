from django.shortcuts import render

# Create your views here.
from Post_app.forms import FilesUpload
from Post_app.models import UploadFiles


def upload_files(request):
    if request.method=="POST":
        form=FilesUpload(request.POST,request.FILES)
        file=request.FILES.getlist('files')
        print(file)
        print(request.FILES)
        if form.is_valid():
            for f in file:
                file_instance=UploadFiles(files=f)
                file_instance.save()
    else:
        form=FilesUpload()
    return render(request,'post/test.html',{'form':form})