from django.http import JsonResponse

def format_url(url, string, param, prefix = ''):
    url = f'{prefix}/{url}'
    
    if type(param) is not str:
        param = str(param)
    
    return url.replace(string, param)

def get_response(status, data, message = ''):
    response = {
        'num_items': len(data),
        'data': data,
    }
    
    if message != '':
        response['message'] = message
        
    return JsonResponse(response, status=status, safe=False)