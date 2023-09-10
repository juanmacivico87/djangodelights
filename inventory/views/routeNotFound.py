from django.utils.translation import gettext as _
from django.views import View
from inventory import helpers

class RouteNotFound(View):
    def get(self, request, exception):
        return helpers.get_response(404, [], _('Error: Route not found'))
