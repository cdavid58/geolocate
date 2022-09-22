from django.shortcuts import render
import requests, json

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def Home(request):
	url = "http://ip-api.com/json/"+get_client_ip(request)
	print(get_client_ip(request))
	a = 5
	while True:
		if a == 0:
			break 
		print(get_client_ip(request))
		a -= 1
	
	# data = {}
	# headers = {
 #      'Content-Type': 'application/json',
 #      'Accept': 'application/json'
 #    }
	# response = requests.request('GET',url,headers = headers, data = data)
	# print(response.text)

	return render(request,'indexs.html')
