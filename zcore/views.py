import json
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

class Home(APIView):
	"""
	Home details
	"""
	def get(self, request, *args, **kwargs):
		"""
		Returns biodata information
		"""
		data = {
			"message": "Hello, world",
			"slackUsername": "cutejosh2",
			"backend": True,
			"age":21,
			"bio": "some bio data"
		}
		return Response(data, status=status.HTTP_200_OK)

home = Home.as_view()