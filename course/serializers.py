from rest_framework import serializers
from .models import CourseModel, LessonModel, QuizModel, QuizProgress, QuizAnswerModel
from user.models import User


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseModel
        fields = '__all__'


class CourseRetrieveSerializer(serializers.ModelSerializer):
    is_bookmarked = serializers.SerializerMethodField(method_name="get_is_starred")

    def get_is_starred(self, course):
        user_id = self.context['user_id']
        course_id = course.id
        user = User.objects.get(id=user_id)
        if user.bookmarked_courses.filter(id=course_id).exists():
            return True
        else:
            return False

    class Meta:
        model = CourseModel
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonModel
        fields = '__all__'


class QuizAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizAnswerModel
        fields = '__all__'


class QuizSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField(method_name="get_answers")

    def get_answers(self, quiz):
        answers = QuizAnswerModel.objects.filter(quiz_id=quiz.id)
        serializer = QuizAnswerSerializer(answers, many=True, read_only=True)

        return serializer.data

    class Meta:
        model = QuizModel
        fields = ['id', 'course_id', 'question', 'answers']


class QuizProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizProgress
        fields = '__all__'


class LeaderBoardSerializer(serializers.ModelSerializer):
    grade = serializers.SerializerMethodField(method_name="get_grade")

    def get_grade(self, course):
        user_id = self.context['user_id']
        course_id = course.id
        progress = QuizProgress.objects.filter(user_id=user_id)
        the_progress = progress.get(course=course_id)

        return the_progress.grade

    class Meta:
        model = CourseModel
        fields = ['id', 'name', 'category', 'course_num', 'module', 'grade']
