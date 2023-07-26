from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_202_ACCEPTED, HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND, HTTP_406_NOT_ACCEPTABLE, HTTP_422_UNPROCESSABLE_ENTITY, HTTP_500_INTERNAL_SERVER_ERROR

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
    
    def put(self, request, pk):
        try:
            # Finding, serialising and getting data from relevant document
            doc = Doc.objects.get(pk=pk)
            serial_doc = DocSerializer(doc)
            doc_data = serial_doc.data

            # Updating document information
            doc_data.update(request.data)
            updated_doc = DocSerializer(doc, data=doc_data)

            if updated_doc.is_valid():
                updated_doc.save()
                return Response(updated_doc.data, status=HTTP_202_ACCEPTED)
            return Response({"message": "Request object is invalid"}, status=HTTP_406_NOT_ACCEPTABLE)
        except Doc.DoesNotExist:
            return Response(
                {"message": "Document not found"},
                status=HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"message": f"Something is wrong\nError: {e}"},
                status=HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def delete(self, _request, pk):
        try:
            # Finding, serialising and getting data from relevant document
            doc = Doc.objects.get(pk=pk)
            doc.delete()
            return Response(status=HTTP_204_NO_CONTENT)
        except Doc.DoesNotExist:
            return Response(
                {"message": "Document not found"},
                status=HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"message": f"Something is wrong\nError: {e}"},
                status=HTTP_500_INTERNAL_SERVER_ERROR
            )

class ManyDocs(APIView):

    def get(self, _request):
        try:
            docs = Doc.objects.all()
            serial_docs = DocSerializer(docs, many=True)
            return Response(serial_docs.data, HTTP_200_OK)
        except Exception as e:
            return Response(
                {"message": f"Something is wrong\nError: {e}"},
                status=HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def post(self, request):
        try:
            new_doc = DocSerializer(data=request.data)
            if new_doc.is_valid():
                new_doc.save()
                return Response(new_doc.data, status=HTTP_201_CREATED)
            return Response(new_doc.errors, status=HTTP_422_UNPROCESSABLE_ENTITY)
        except Exception as e:
            return Response(
                {"message": f"Something is wrong\nError: {e}"},
                status=HTTP_500_INTERNAL_SERVER_ERROR
            )