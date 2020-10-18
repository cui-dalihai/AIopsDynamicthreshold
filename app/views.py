from django.shortcuts import render
from django.views import View
from django.shortcuts import HttpResponse

# Create your views here.


class MonitorMgrView(View):

    def get(self, request):
        return render(request, 'monitorMgr.html')


class ParmConfView(View):

    def get(self, request):
        return render(request, 'paramConf.html')


class AlertHistoryView(View):

    def get(self, request):
        return render(request, 'alertHistory.html')


class ThresholdView(View):

    def get(self, request):
        return render(request, 'threshold.html')


class SysConfView(View):

    def get(self, request):
        return render(request, 'sysConf.html')


class ApiConfView(View):

    def get(self, request):
        return render(request, 'apiConf.html')

