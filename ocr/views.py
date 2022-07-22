from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import AnalysisImage
from .ocr import ocrDriver, get_result
from .translation import translationDriver, get_translated_ocr
from rest_framework.parsers import MultiPartParser
class OCR(APIView):
    parser_classes = [MultiPartParser]
    def get(self, request):
        return Response({"":""})
    def post(self, request):
        print(1)
        analysisimage = request.FILES['image']
        try:
            print(2)
            recvedimg = AnalysisImage.objects.create(imagetitle=str(analysisimage),analysisimage=analysisimage)
            print(f"image: {recvedimg}")
        except Exception as e:
            print(e)
            
        ocrDriver(f"media/{recvedimg}")
        print(3)
        ocrresults = get_result()
        print(4)
        print(f" from ocr {ocrresults}")
        print(5)
        translationDriver()
        print(6)
        print(get_translated_ocr())
        return JsonResponse(get_translated_ocr(), safe=False)
