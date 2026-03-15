from django.shortcuts import render
from .serializers import *
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response  import Response
from rest_framework.permissions import AllowAny
# Create your views here.
class RegisterView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
    
class GoogleLoginView(APIView):
    permission_classes = [AllowAny]
    
    def post(self,request):
        serializer = GoogleLoginSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)   
    
class BlogView(generics.ListCreateAPIView):
    queryset = PostBlog.objects.all()
    serializer_class = BlogSerializer
class BlogRetreiveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostBlog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [AllowAny]
class TechnologyView(generics.ListCreateAPIView):
    queryset = TechnologyPost.objects.all()
    serializer_class = TechnologySerializer
class TechnologyRetreiveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TechnologyPost.objects.all()
    serializer_class = TechnologySerializer
    permission_classes = [AllowAny]
class DesignView(generics.ListCreateAPIView):
    queryset = DesignPost.objects.all()
    serializer_class = BlogSerializer
class DesignRetreiveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DesignPost.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [AllowAny]
class ProgrammingView(generics.ListCreateAPIView):
    queryset = ProgrammingPost.objects.all()
    serializer_class = ProgrammingSerializer
class ProgrammingRetreiveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProgrammingPost.objects.all()
    serializer_class = ProgrammingSerializer
    permission_classes = [AllowAny]
class LifesyleView(generics.ListCreateAPIView):
    queryset = LifestylePost.objects.all()
    serializer_class = LifesyleSerializer
class LifesyleRetreiveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LifestylePost.objects.all()
    serializer_class = LifesyleSerializer
    permission_classes = [AllowAny]
    
    
class ContactView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
class ContactRetreiveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [AllowAny]