from rest_framework.decorators import api_view
from rest_framework.response import Response
from gallery_app.serializers import ImageSerializer
from django.shortcuts import render,redirect
from gallery_app.form import ImgForm
from .models import imageModel
# Create your views here.
def home(request):
    data = imageModel.objects.all()
    form=ImgForm()
    if request.method=='POST':
        form=ImgForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'index.html',{'form':form,'data':data})

# @api_view(['POST'])
# def ImgUpload(request):
#     if request.method == 'POST':
#         serializer=ImageSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response('image added')
#     else:
#         return Response('Failed')

@api_view(['POST'])
def ImgUpload(request):
    serializer= ImageSerializer(data = request.data)
    serializer.image = request.FILES.get('image')
    if serializer.is_valid():
        serializer.save()
        return Response('Image was uploaded')
