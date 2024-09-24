from django.template import loader
from django.http import HttpResponse

# Define the programs view
def programs(request):
    template = loader.get_template('courses.html')
    return HttpResponse(template.render())
