from django_filters import FilterSet, filters
from .models import School, Classroom, Teacher, Student

# code here

class SchoolFilter(FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = School
        fields = ['name']

class ClassroomFilter(FilterSet):
    school = filters.NumberFilter(field_name='school__id')

    class Meta:
        model = Classroom
        fields = ['school']

class TeacherFilter(FilterSet):
    school = filters.NumberFilter(field_name='classrooms__school__id')
    classroom = filters.NumberFilter(field_name='classrooms__id')
    first_name = filters.CharFilter(lookup_expr='icontains')
    last_name = filters.CharFilter(lookup_expr='icontains')
    gender = filters.CharFilter()

    class Meta:
        model = Teacher
        fields = ['school', 'classroom', 'first_name', 'last_name', 'gender']

class StudentFilter(FilterSet):
    school = filters.NumberFilter(field_name='classroom__school__id')
    classroom = filters.NumberFilter(field_name='classroom__id')
    first_name = filters.CharFilter(lookup_expr='icontains')
    last_name = filters.CharFilter(lookup_expr='icontains')
    gender = filters.CharFilter()

    class Meta:
        model = Student
        fields = ['school', 'classroom', 'first_name', 'last_name', 'gender']
