from django.shortcuts import render, redirect, get_object_or_404, reverse, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from LGS.models import LGS

temporaryDictionary = {}


def SaveResults(request, id):
    user = get_object_or_404(User,id = id)
    results = LGS(
        ogrenci = user,
        lgspuan = temporaryDictionary[id]["lgspuan"]
    )
    results.save()
    messages.success(request, message="Puan Başarıyla Kaydedildi")
    return redirect(reverse("LGS:dashboard",kwargs={"id":id}))

def dashboard(request, id): 
    results = LGS.objects.filter(ogrenci_id = id)
    checking = request.GET.get("checking")

    data = list()
    labels = list()

    if checking == "on":
        for result in results.order_by("created_date"):
            data.append(float(result.lgspuan))
            labels.append(str(result.created_date.day)+'/'+str(result.created_date.month)+'/'+str(result.created_date.year))

        context = {
            "results" : results,
            "data" : data,
            "labels" : labels
        }
        return render(request, "chartForLGS.html", context)
    else:
        context = {
            "results" : results,
        }
        return render(request, "dashboardForLGS.html", context)


def DeleteResult(request,id):
    context = {
        "lgs" : "lgs",
        "id" : id
    }
    return render(request, "questionForDelete.html", context)


def SureToDeleteResult(request,id):
    user_id = LGS.objects.get(id = id).ogrenci_id
    result = get_object_or_404(LGS, id = id)
    result.delete()
    return redirect(reverse("LGS:dashboard",kwargs={"id":user_id}))    


def calculate(request,id):
    if request.method == "POST":

        values = {
            "tTurkce": request.POST.get("tTurkce"),
            "tInk" :   request.POST.get("tInk"),
            "tDkab" :  request.POST.get("tDkab"),
            "tDil" :   request.POST.get("tDil"),
            "tMat" :   request.POST.get("tMat"), 
            "tFen" :   request.POST.get("tFen"), 
            "fTurkce": request.POST.get("fTurkce"),
            "fInk" :   request.POST.get("fInk"),
            "fDkab" :  request.POST.get("fDkab"),
            "fDil" :   request.POST.get("fDil"),
            "fMat" :   request.POST.get("fMat"), 
            "fFen" :   request.POST.get("fFen") 
        }

        for key in values.keys():
            if values[key] == '':
                values[key] = 0

        def calculateLGS(tTurkce,tInk,tDkab,tDil,tMat,tFen,fTurkce,fInk,fDkab,fDil,fMat,fFen):
            netTurkce = (tTurkce - fTurkce * 0.333333) * (16/3)
            netInk = (tInk - fInk * 0.33333) * (8/3)
            netDkab = (tDkab - fDkab * 0.33333) * (8/3)
            netDil = (tDil - fDil * 0.33333) * (8/3)
            netMat = (tMat - fMat * 0.33333) * (16/3)
            netFen = (tFen - fFen * 0.33333) * (16/3)
            
            lgspuan = netTurkce + netInk + netDkab + netDil + netMat + netFen + 100
            return lgspuan
        
        lgspuan = calculateLGS(
            int(values["tTurkce"]),
            int(values["tInk"]),
            int(values["tDkab"]),
            int(values["tDil"]),
            int(values["tMat"]), 
            int(values["tFen"]), 
            int(values["fTurkce"]),
            int(values["fInk"]),
            int(values["fDkab"]),
            int(values["fDil"]),
            int(values["fMat"]), 
            int(values["fFen"]) 
        )

        context = {
            "lgspuan" : str(format(lgspuan, ".3f")),
        }

        temporaryDictionary[id] = context

        return render(request,"LGSsonuclar.html", context)
        
    else:
        return render(request, "LGS.html")
