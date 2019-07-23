from django.shortcuts import render
from django.http import HttpResponse

def test(request):
	context = {
	"msg":"hello Jeddah",
	"title":"yaaaaaaaay"
	}
	# return HttpResponse("<h1> hello</h1>")
	return render(request, 'hello.html', context)