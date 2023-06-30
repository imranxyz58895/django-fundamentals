from datetime import datetime
from django.shortcuts import render, HttpResponse

def timeinfo(request):
   today = datetime.today()
   current_date = today.strftime("%B %d, %Y")
   message = f'''Hello Friends!! Good evening,
   Today is {current_date}
   '''
   return HttpResponse(f'{message}')



