from django.shortcuts import render,redirect
from django.views import View
# Create your views here.
from django.http import HttpResponse
from .models import product

class home(View):
    def get(self,request):
        return render(request,'home.html')

class InsertInput(View):
    def get(self,request):
        return render(request,'product.html')
class Insert(View):
    def get(self,request):
        pid= int(request.GET['t1'])
        pname=request.GET['t2']
        pcost=request.GET['t3']
        pmfdt=request.GET['t4']
        pexpdt=request.GET['t5']
        p=product(pid=pid,pname=pname,pcost=pcost,pmfdt=pmfdt,pexpdt=pexpdt)
        p.save()
        return HttpResponse('product inserted succes')
class Display(View):
     def get(self,request):
      qs=product.objects.all()
      condic= {"records" : qs }
      return render(request,'display.html',context=condic)
class DeleteInput(View):
    def get(self,request):
        de=product.objects.all()
        condic={"records" : de }
        return render(request,'DeleteInput.html',context=condic)

class delete(View):
    def get(self,request):
        pid=request.GET['t1']
        dl=product.objects.get(pid=pid)
        dl.delete()
        return redirect('/display')


class updateInput(View):
      def get(self, request):
          up=product.objects.all()
          condic = {"records": up }
          return render(request, 'updateInpute.html', context=condic)

class updateDetails(View):
    def get(self,request):
        pid=int(request.GET['t1'])
        p=product.objects.get(pid=pid)
        condic={'rec': p }
        return render(request,'update.html',context=condic)

class update(View):
     def get(self, request):
         pid=int(request.GET['t1'])
         p=product.objects.get(pid=pid)
         p.pname=request.GET['t2']
         p.pcost=float(request.GET['t3'])
         p.pmfdt=request.GET['t4']
         p.pexpdt=request.GET['t5']
         p.save()
         return redirect('/display')







