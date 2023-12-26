from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *


@api_view(['POST'])
def student_create(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    phone = request.POST['phone']
    status = request.POST['status']
    student = Student.objects.create(first_name=first_name, last_name=last_name, phone=phone, status=status)
    serialized_data = StudentSerializer(student).data
    return Response(serialized_data)


@api_view(['POST'])
def direction_create(request):
    name = request.POST['name']
    price = request.POST['price']
    direction = Direction.objects.create(name=name, price=price)
    serialized_data = DirectionSerializer(direction).data
    return Response(serialized_data)


@api_view(['GET'])
def get_directions(request):
    serialized_data = DirectionSerializer(Direction.objects.all(), many=True).data
    return Response(serialized_data)


@api_view(['POST'])
def group_create(request):
    direction = request.POST['direction']
    students = request.POST.getlist('students')
    name = request.POST['name']
    gr = Group.objects.create(
        direction_id=direction,
        name=name
    )
    for i in students:
        gr.students.add(Student.objects.get(id=i))
        student = Student.objects.get(id=i)
        student.status = 2
        student.save()
    ser = GroupSerializer(gr)
    return Response(ser.data)


@api_view(['GET'])
def students_get(request):
    serialized_data = StudentSerializer(Student.objects.all(), many=True).data
    return Response(serialized_data)


@api_view(['GET'])
def groups_get(request):
    serialized_data = GroupSerializer(Group.objects.all(), many=True).data
    return Response(serialized_data)


@api_view(['POST'])
def payment_create(request):
    student = request.POST['student']
    money = request.POST['money']
    payment = Payment.objects.create(student_id=student, money=money)
    student = Student.objects.get(id=student)
    student.is_payed = True
    student.save()
    serialized_data = PaymentSerializer(payment, many=False).data
    return Response(serialized_data)


@api_view(['GET'])
def get_group_by_id(request, pk):
    serialized_data = GroupSerializer(Group.objects.get(id=pk), many=False).data
    return Response(serialized_data)


@api_view(['GET'])
def payed_students(request):
    serialized_data = StudentSerializer(Student.objects.filter(is_payed=True), many=True).data
    return Response(serialized_data)


@api_view(['GET'])
def get_waiting_students(request):
    serialized_data = StudentSerializer(Student.objects.filter(status=1), many=True).data
    return Response(serialized_data)


@api_view(['GET'])
def get_quantity_of_students(request):
    data = {
        "Quantity of students": Student.objects.all().count()
    }
    return Response(data)


@api_view(['GET'])
def get_groups_name(request):
    groups = Group.objects.all()
    groups_name = GroupNameSerializer(groups, many=True).data
    return Response(groups_name)