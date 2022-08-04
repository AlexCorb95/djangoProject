from rest_framework import serializers

from trainer.models import Trainer


class TrainerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trainer
        fields = ['first_name', 'last_name']
