from rest_framework import serializers
from .models import Question, Answer

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question', 'author', 'is_answered', 'created_date', 'modified_date', 'upvotes', 'downvotes']

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'answer', 'question', 'user', 'host', 'answered_by_host', 'upvotes', 'downvotes']
