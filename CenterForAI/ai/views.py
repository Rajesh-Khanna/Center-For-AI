from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import *
from datetime import date
from .forms import ApplicationForm,AdminLoginform 
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.http import HttpResponse

def errorPage(request):
    return render(request, 'ai/error_page.html', None)

class HomeView(generic.ListView):
    template_name = 'ai/index.html'

    def get_new_notices(self):
        today = date.today()
        return notice.objects.all().filter(notice_end_date__gte=today)

    def get_past_notices(self):
        return notice.objects.all().filter(notice_end_date__lte=date.today())

    def get_queryset(self):
        context = {
            'notice_list' : self.get_new_notices()
        }
        return context

class PeopleView(generic.ListView):
    template_name = 'ai/people.html'

    def get_queryset(self):
        context = {
            'faculty_list' : faculty.objects.all(),
            'staff_list' : staff.objects.all(),
            'student_list' : student.objects.all()
        }
        return context

class CCourseView(generic.ListView):
    template_name = 'ai/ccourses.html'

    def get_queryset(self):
        context = {
            'certi_list' : certificate.objects.all(),
            'question_list' : FAQ.objects.all()
        }
        return context

class ACourseView(generic.ListView):
    template_name = 'ai/acourses.html'

    def get_queryset(self):
        context = {
            'certi_list' : certificate.objects.all(),
            'question_list' : FAQ.objects.all()
        }
        return context

class ResearchView(generic.ListView):
    template_name = 'ai/research.html'

    def get_queryset(self):
        context = {
            'projects_list' : project.objects.all()
        }
        return context

class PartnerView(generic.ListView):
    template_name = 'ai/partner.html'

    def get_queryset(self):
        return None

class JoinView(generic.ListView):
    template_name = 'ai/joinUs.html'

    def get_queryset(self):
        return None

class EventView(generic.ListView):
    template_name = 'ai/events.html'

    def get_new_events(self):
        today = date.today()
        return event.objects.all().filter(event_date__gte = today)

    def get_past_events(self):
        return event.objects.all().filter(event_date__lte = date.today())


    def get_queryset(self):
        context = {
            'upcommingEvents' : self.get_new_events(),
            'pastEvents' : self.get_past_events()
        }
        return context

class ApplyView(generic.CreateView):
    model = applicant
    fields = ['first_name','last_name','email','mobile','experience','company','designation','city']

class ApplyResponseView(generic.TemplateView):
    template_name = 'ai/applyResponse.html'

# class ApplyView(generic.UpdateView):
#     model = applicant
#     fields = ['first_name','last_name','email','mobile','experience','company','designation','city','fee_status','amount_paid','applicant_status']

# class AdminLoginView(generic.TemplateView):
#     model = applicant
#     template_name = 'ai/adminLogin.html'

    # def get(self,request):
    #     form = AdminLoginform()
    #     return render(request,self.template_name,{'form':form})
        
    # def post(self,request):
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     user = authenticate(request, username=username, password=password)
    #     if True:
    #         login(request, user)
    #         # Redirect to a success page.
    #         ...

    #     else:
    #         # Return an 'invalid login' error message.
    #         # ...