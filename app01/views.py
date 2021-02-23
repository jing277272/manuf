from django.shortcuts import render

# Create your views here.

#取模板数据
def findinfo(request):
    	return render(request,'app01/templates/test.html')
 
def findresult(request):
	id = request.GET['id']
	items = []
	testline = {}
 
	cursor = connection.cursor()
 
	if (id == ""):
		cursor.execute("SELECT id,name from tmp_info")
	else:
		cursor.execute("SELECT id,name from tmp_info where id ='" + id + "'")
    
	rows = cursor.fetchall()
	for row in rows:
		testline['id'] = row[0]
		testline['name'] = row[1]
		items.append(testline.copy())
	cursor.close()
	
	return HttpResponse(str(items))
