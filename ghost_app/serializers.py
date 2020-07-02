from rest_framework.serializers import HyperlinkedModelSerializer

from ghost_app.models import VoteChoice

class VoteChoiceSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = VoteChoice
        fields = (
            'choice',
            'text',
            'time',
            'upvotes',
            'downvotes',
            )
