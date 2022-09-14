import datetime

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from base.models import Driver, Pedestrian
from base.serializers import DriverSerializer, PedestrianSerializer
from base.utils import get_road_info_api, get_distance, get_latest


class DriverAPIVIew(APIView):
    def get(self, request):
        # query string에 필요한 정보가 없을 경우
        if 'lat' not in request.GET:
            return Response("lat bad", status=status.HTTP_400_BAD_REQUEST)
        if 'lon' not in request.GET:
            return Response("lon bad", status=status.HTTP_400_BAD_REQUEST)
        if 'limit' not in request.GET:
            return Response("limit bad", status=status.HTTP_400_BAD_REQUEST)
        if request.GET['limit'] not in ["0", "1"]:
            return Response("bad", status=status.HTTP_400_BAD_REQUEST)

        # tmap api 호출하여 위도, 경도에 가장 가까운 도로에 대한 정보(dict)
        res = get_road_info_api(request.GET['lon'], request.GET['lat'])

        # serialize 데이터
        data = {
            "user_id": "asdf",
            "limit_speed": res['resultData']['header']['speed'],
            "road_name": res['resultData']['header']['roadName'],
            'longitude': float(request.GET['lon']),
            'latitude': float(request.GET['lat']),
            'do_limit': request.GET['limit']
        }

        serializer = DriverSerializer(data=data)

        # 데이터가 유효한지 확인한다.
        if serializer.is_valid():
            # 100m 이내의 보행자 정보 반환
            r_data = []
            check_id = []
            serializer.save()
            # created_at__gte=datetime.datetime.now()-datetime.timedelta(minutes=1)
            queries = Pedestrian.objects.filter(longitude__gte=data['longitude']-0.005,
                                                longitude__lte=data['longitude']+0.005,
                                                latitude__gte=data['latitude']-0.005,
                                                latitude__lte=data['latitude']+0.005,
                                                created_at__gte=datetime.datetime.now() - datetime.timedelta(minutes=50)
                                                )
            print(queries)
            for query in queries:
                distance = get_distance(data['longitude'], data['latitude'], query.longitude, query.latitude)
                if distance <= 100:
                    check_id.append(query)
                    r_data.append({'user_id': query.user_id,
                                   'longitude': query.longitude,
                                   'latitude': query.latitude,
                                   'distance': distance,
                                   'created_at': query.created_at
                                   })

            r_data = get_latest(r_data)
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(r_data, status=status.HTTP_201_CREATED)

        return Response("bad", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# 차량이 현재 도로 정보 요청시 가져옴.. 추후 APIkey 사용??
class RoadInfoAPIView(APIView):
    def get(self, request):
        # id가 틀렸을 경우
        if 'id' not in request.GET:
            return Response("id bad", status=status.HTTP_400_BAD_REQUEST)

        # 일치하는 id중 가장 최근것
        query = Driver.objects.filter(user_id__iexact=request.GET['id']).latest("created_at")
        serializer = DriverSerializer(query)
        # print(serializer.data)

        return Response(serializer.data, status=status.HTTP_200_OK)


# 보행자 위치 저장
class PedestrianAPIView(APIView):
    def get(self, request):
        # query string에 필요한 정보가 없을 경우
        if 'lat' not in request.GET:
            return Response("lat bad", status=status.HTTP_400_BAD_REQUEST)
        if 'lon' not in request.GET:
            return Response("lon bad", status=status.HTTP_400_BAD_REQUEST)

        # serialize 데이터
        data = {
            "user_id": "temp2",
            'longitude': float(request.GET['lon']),
            'latitude': float(request.GET['lat']),
        }

        serializer = PedestrianSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({"is_success": "success"}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)