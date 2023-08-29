from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import ProcessMaster
from .serializers import ProcessMasterSerializer

@api_view(['GET'])
def getdata(request):
    processmasters = ProcessMaster.objects.all()
    serializer = ProcessMasterSerializer(processmasters, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getprocessmaster(request, pk):
    processmasters = ProcessMaster.objects.get(id=pk)
    serializer = ProcessMasterSerializer(processmasters, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def addprocessmaster(request):
    serializer = ProcessMasterSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['PUT'])
def updateprocessmaster(request, pk):
    processmasters = ProcessMaster.objects.get(id=pk)
    serializer = ProcessMasterSerializer(instance=ProcessMaster, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteprocessmaster(request, pk):
    processmaster = ProcessMaster.objects.get(id=pk)
    processmaster.delete()
    return Response('ProcessMaster successfully deleted!')
