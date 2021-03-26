from rest_framework import generics
from .serializers import PostSerializer
from .models import Posts

class PostList(generics.ListCreateAPIView):

    # Anything that inherits from ListAPI View is going to need 2 things.
    # What is the collection of things, aka the queryset
    # Serializer_class
    queryset = Posts.objects.all()
    serializer_class = PostSerializer


# The postDetail needs the same things
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer