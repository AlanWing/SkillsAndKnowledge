from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin


class CheckIsLoginMiddleware(MiddlewareMixin):
    def process_request(self,request):
        if not request.user.is_active and "login" not in request.path:
            response = {
                "code":1,
                "data":"未登录"
            }
            return JsonResponse(response)