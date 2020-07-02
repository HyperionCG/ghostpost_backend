from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework.viewsets import ModelViewSet

from ghost_app.serializers import VoteChoiceSerializer
from ghost_app.models import VoteChoice

# Create your views here.

class VoteChoiceViewSet(ModelViewSet):
    serializer_class = VoteChoiceSerializer
    basename = 'vote'
    queryset = VoteChoice.objects.all()

    @action(detail=True, methods=['get'])
    def upvote(self, request, pk=None):
        post = self.get_object()
        post.upvotes += 1
        post.save()
        return Response({'status': 'upvote'})
    
    @action(detail=True, methods=['get'])
    def downvote(self, request, pk=None):
        post = self.get_object()
        post.downvotes += 1
        post.save()
        return Response({'status': 'downvote'})