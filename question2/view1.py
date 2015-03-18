from django.shortcuts import render
from question2.models import *

def RepresentsInt(s):
	try:
		int(s)
		return (True)
	except ValueError:
		return (False)

def fibo(request, fibonum):
	n = fibonum
	res = [0]
	if RepresentsInt(n) == False:
		res = "Please input an integer!"
	elif int(n) <= 0:
		res = "Please input a positive integer!"
	elif int(n) == 1:
		res = str(res)[1:-1]
	else:
		if Result.objects.filter(num = n):
			cur_record = Result.objects.get(num = n)
			res = cur_record.res
		else:
			prev = 1
			pprev = 0
			res.append(1)
			for i in range(int(n) - 2):
				tmp = prev + pprev
				res.append(tmp)
				pprev = prev
				prev = tmp

			res = str(res)[1:-1]
			result = Result(
				num = n,
				res = res
			)
			result.save()

	context = {'res':res}
	return render(request, 'fibo.html', context)