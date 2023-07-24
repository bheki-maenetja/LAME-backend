from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_202_ACCEPTED, HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR

from .models import Doc
from .serializers import DocSerializer

# Create your views here.
class SingleDoc(APIView):

    def get(self, _request, pk):
        try:
            doc = Doc.objects.get(pk=pk)
            serial_doc = DocSerializer(doc)
            return Response(serial_doc.data, HTTP_200_OK)
        except Doc.DoesNotExist:
            return Response(
                {"message": "Document not found"}, 
                status=HTTP_404_NOT_FOUND
            )

class ManyDocs(APIView):

    def get(self, _request):
        try:
            docs = Doc.objects.all()
            serial_docs = DocSerializer(docs, many=True)
            return Response(serial_docs.data, HTTP_200_OK)
        except:
            return Response(
                {"message": "Something is wrong"},
                status=HTTP_500_INTERNAL_SERVER_ERROR
            )