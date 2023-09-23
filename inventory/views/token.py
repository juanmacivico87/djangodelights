from operator import contains
from django.middleware.csrf import get_token
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.utils.translation import gettext as _
from django.views import View
from inventory import helpers
from json import loads

@method_decorator(csrf_exempt, name='dispatch')
class Token(View):
    create_path = 'token/'
    
    def post(self, request):
        if request.path_info != helpers.format_url(self.create_path, '', '', '/api'):
            return helpers.get_response(404, [], _('Error: Route not found'))
        
        body = request.body.decode('utf-8')
        
        if body == '':
            return helpers.get_response(400, [], _('Error: Requested body cannot be empty'))
        
        body = loads(body)
        
        if not ('username' in body) or not ('password' in body):
            return helpers.get_response(400, [], _('Error: User and password are mandatory parameters'))
    
        username = body['username']
        password = body['password']

        user = authenticate(request, username=username, password=password)

        if user is None:
            return helpers.get_response(401, [], _('Error: Failed to authenticate the user'))
        
        login(request, user)
        csrf_token = get_token(request)
        
        return helpers.get_response(200, {'token': csrf_token})
