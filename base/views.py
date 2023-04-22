from django.contrib.auth.models import User
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from base.serializers import quizdataserializer,registerserializer,addquestionsserializer
from base.models import quizdata
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny
from rest_framework.authtoken.models import Token
# Create your views here.


@api_view(["GET"])
def getquestions(request):
    if request.method == "GET":
        obj_questions = quizdata.objects.all()
        serialized_questions = quizdataserializer(obj_questions,many=True)
        print(serialized_questions.data)
        return Response({"msg":serialized_questions.data})


@api_view(["POST"])
def registerkar(request):
    if request.method == "POST":
        serialized_data = registerserializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            uname = request.data["username"]
            user_object = User.objects.get(username=uname)
            usertoken = Token.objects.create(user=user_object)
            print(usertoken)
            return Response({"msg":"Successfully Registered and token generated","usertoken":str(usertoken)})
        else:
            return Response({"msg":serialized_data.errors})
    else:
        return Response({"msg":"Do a post Request"})
            



@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def test(request,id):
    if request.method == "POST":
        rans = quizdata.objects.get(id=id).answer
        print(rans)
        uans = request.data["answer"]
        print(uans)
        if rans==uans:
            return Response({"msg":"The answer is correct"})
        else:
            return Response({"msg":"Answer is incorrect"})    
        
    else:
        return Response({"msg":"Make a POST request"})
    


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def addquestions(request):
    if request.method == "POST":
        serialized_question = addquestionsserializer(data=request.data)
        if serialized_question.is_valid():
            serialized_question.save()
            print(serialized_question.data)
            return Response({"msg":"The question and answers are added to database"})
        else:
            return Response({"msg":serialized_question.data})
    else:
        return Response({"msg":"Make a POST Request"})
    