from datetime import datetime
from django.shortcuts import render


def dateInfo(request):
    current_date = datetime.now()
    my_context = {
        'date': current_date,
    }

    return render(request=request, template_name='nurseryApp/index.html', context=my_context)
