from rest_framework.views import APIView
from rest_framework.response import Response
from .models import AnalysisImage
from .ocr import driver, get_result

class OCR(APIView):
    def get(self, request):
        return Response({"":""})
    def post(self, request):
        analysisimage = request.FILES['image']
        try:
            recvedimg = AnalysisImage.objects.create(imagetitle=str(analysisimage),analysisimage=analysisimage)
            print(f"image: {recvedimg}")
        except Exception as e:
            print(e)
        driver(f"media/{recvedimg}")
        ocrresults = get_result()
        print(f" from ocr {ocrresults}")
        return Response(ocrresults)
