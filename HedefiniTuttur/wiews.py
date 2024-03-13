from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from YKSsiralama import YKSsiralama
import os

path = os.getcwd()

def index(request):
    return render(request, "index.html")

def nonuseryks(request):
    if request.method == "POST":
        values = {
            "tTurkce" : request.POST.get("tTurkce"),
            "tMatematik" : request.POST.get("tMatematik"),
            "tSos" : request.POST.get("tSos"),
            "tFen" : request.POST.get("tFen"),
            "fTurkce" : request.POST.get("fTurkce"),
            "fMatematik" : request.POST.get("fMatematik"),
            "fSos" : request.POST.get("fSos"),
            "fFen" : request.POST.get("fFen"),
            "tMat" : request.POST.get("tMat"),
            "tFiz" : request.POST.get("tFiz"),
            "tKim" : request.POST.get("tKim"),
            "tBio" : request.POST.get("tBio"),
            "tEde" : request.POST.get("tEde"),
            "tTar1" : request.POST.get("tTar1"),
            "tCog1" : request.POST.get("tCog1"),
            "tTar2" : request.POST.get("tTar2"),
            "tCog2" : request.POST.get("tCog2"),
            "tFel" : request.POST.get("tFel"),
            "tDkab" : request.POST .get("tDkab"),
            "fMat" : request.POST.get("fMat"),
            "fFiz" : request.POST.get("fFiz"),
            "fKim" : request.POST.get("fKim"),
            "fBio" : request.POST.get("fBio"),
            "fEde" : request.POST.get("fEde"),
            "fTar1" : request.POST.get("fTar1"),
            "fTar2" : request.POST.get("fTar2"),
            "fCog1" : request.POST.get("fCog1"),
            "fCog2" : request.POST.get("fCog2"),
            "fFel" : request.POST.get("fFel"),
            "fDkab" : request.POST.get("fDkab"),
            "tDil" : request.POST.get("tDil"),
            "fDil" : request.POST.get("fDil"),
        }

        for key in values.keys():
            if values[key] == '':
                values[key] = 0
    
        checking = request.POST.get("checking")
        diplomaPuani = request.POST.get("diplomaPuani")

        def calculate_tyt(tTurkce,fTurkce,tMatematik,fMatematik,tSos,fSos,tFen,fFen):
            netTurkce = (tTurkce - fTurkce * 0.25) * 4.125
            netMatematik = (tMatematik - fMatematik * 0.25) * 4.25
            netSosyal = (tSos - fSos * 0.25) * 4.125
            netFen = (tFen - fFen * 0.25) * 4.25
            tyt_puan = netFen + netMatematik + netSosyal + netTurkce
            tyt_puan = tyt_puan - ((tyt_puan * 2.5) / 500)
            return tyt_puan

        def calculate_ayt_40(tTurkce,fTurkce,tMatematik,fMatematik,tSos,fSos,tFen,fFen):
            netTurkce = (tTurkce - fTurkce * 0.25) * 1.625
            netMatematik = (tMatematik - fMatematik * 0.25) * 1.75
            netSosyal = (tSos - fSos * 0.25) * 1.625
            netFen = (tFen - fFen * 0.25) * 1.75
            ayt_puan_40 = netFen + netMatematik + netSosyal + netTurkce
            ayt_puan_40 = ayt_puan_40 - ((ayt_puan_40 * 2.5) / 200)
            return ayt_puan_40

        def calculate_ayt_sayisal(tMat,tFiz,tKim,tBio,fMat,fFiz,fKim,fBio):
            netMat = (tMat - fMat * 0.25) * 3.75
            netFiz = (tFiz - fFiz * 0.25) * 3.57143
            netKim = (tKim - fKim * 0.25) * 3.84615
            netBio = (tBio - fBio * 0.25) * 3.84615
            ayt_puan_40 = calculate_ayt_40(
                int(values["tTurkce"]),
                int(values["fTurkce"]),
                int(values["tMatematik"]),
                int(values["fMatematik"]),
                int(values["tSos"]),
                int(values["fSos"]),
                int(values["tFen"]),
                int(values["fFen"])
            )
            ayt_puan_sayisal = netMat + netFiz + netKim + netBio + ayt_puan_40
            return ayt_puan_sayisal    

        def calculate_ayt_ea(tMat,tEde,tTar1,tCog1,fMat,fEde,fTar1,fCog1):
            netMat = (tMat - fMat * 0.25) * 3.75
            netEde = (tEde - fEde * 0.25) * 3.75
            netTar1 = (tTar1 - fTar1 * 0.25) * 3.5
            netCog1 = (tCog1 - fCog1 * 0.25) * 4.1666667
            ayt_puan_40 = calculate_ayt_40(
                int(values["tTurkce"]),
                int(values["fTurkce"]),
                int(values["tMatematik"]),
                int(values["fMatematik"]),
                int(values["tSos"]),
                int(values["fSos"]),
                int(values["tFen"]),
                int(values["fFen"])
            )
            ayt_puan_ea = netMat + netEde + netTar1 + netCog1 + ayt_puan_40
            return ayt_puan_ea

        def calculate_ayt_sozel(tEde ,tTar1,tCog1,tTar2,tCog2,tFel ,tDkab,fEde ,fTar1,fCog1,fTar2,fCog2,fFel ,fDkab):
            netEde = (tEde - fEde * 0.25) * 3.75
            netTar1 = (tTar1 - fTar1 * 0.25) * 3.5
            netCog1 = (tCog1 - fCog1 * 0.25) * 4.16666667
            netTar2 = (tTar2 - fTar2 * 0.25) * 3.636363636
            netCog2 = (tCog2 - fCog2 * 0.25) * 3.636363636
            netFel = (tFel - fFel * 0.25) * 3.75
            netDkab = (tDkab - fDkab * 0.25) * 4.16666667
            ayt_puan_40 = calculate_ayt_40(
                int(values["tTurkce"]),
                int(values["fTurkce"]),
                int(values["tMatematik"]),
                int(values["fMatematik"]),
                int(values["tSos"]),
                int(values["fSos"]),
                int(values["tFen"]),
                int(values["fFen"])
            )
            ayt_puan_sozel = netEde + netTar1 + netCog1 + netTar2 + netCog2 + netFel + netDkab + ayt_puan_40
            return ayt_puan_sozel

        def calculate_ydt(tDil,fDil):
            netDil = (tDil - fDil * 0.25) * 3.75
            ayt_puan_40 = calculate_ayt_40(
                int(values["tTurkce"]),
                int(values["fTurkce"]),
                int(values["tMatematik"]),
                int(values["fMatematik"]),
                int(values["tSos"]),
                int(values["fSos"]),
                int(values["tFen"]),
                int(values["fFen"])
            )
            ydt_puan = netDil + ayt_puan_40
            return ydt_puan

        tyt_puan_ham = calculate_tyt(
            int(values["tTurkce"]),
            int(values["fTurkce"]),
            int(values["tMatematik"]),
            int(values["fMatematik"]),
            int(values["tSos"]),
            int(values["fSos"]),
            int(values["tFen"]),
            int(values["fFen"])
        )

        ayt_puan_sayisal_ham = calculate_ayt_sayisal(
            int(values["tMat"]),
            int(values["tFiz"]),
            int(values["tKim"]),
            int(values["tBio"]),
            int(values["fMat"]),
            int(values["fFiz"]),
            int(values["fKim"]),
            int(values["fBio"])
        )
        ayt_puan_ea_ham = calculate_ayt_ea(
            int(values["tMat"]),
            int(values["tEde"]),
            int(values["tTar1"]),
            int(values["tCog1"]),
            int(values["fMat"]),
            int(values["fEde"]),
            int(values["fTar1"]),
            int(values["fCog1"])
        )
        ayt_puan_sozel_ham = calculate_ayt_sozel(
            int(values["tEde"]),
            int(values["tTar1"]),
            int(values["tCog1"]),
            int(values["tTar2"]),
            int(values["tCog2"]),
            int(values["tFel"]),
            int(values["tDkab"]),
            int(values["fEde"]),
            int(values["fTar1"]),
            int(values["fCog1"]),
            int(values["fTar2"]),
            int(values["fCog2"]),
            int(values["fFel"]),
            int(values["fDkab"])
        )
        ydt_puan_ham = calculate_ydt(
            int(values["tDil"]),
            int(values["fDil"])
        )

        if diplomaPuani == '':
            diplomaPuani = 0

        diplomaPuani = int(diplomaPuani) * 0.6
        tyt_puan_yer = tyt_puan_ham + diplomaPuani
        ayt_puan_sayisal_yer = ayt_puan_sayisal_ham + diplomaPuani
        ayt_puan_ea_yer = ayt_puan_ea_ham + diplomaPuani
        ayt_puan_sozel_yer = ayt_puan_sozel_ham + diplomaPuani
        ydt_puan_yer  = ydt_puan_ham + diplomaPuani

        if checking == "on":
            tyt_puan_ham = tyt_puan_ham - 50
            tyt_puan_yer = tyt_puan_yer - 50 
            ayt_puan_sayisal_ham = ayt_puan_sayisal_ham - 50
            ayt_puan_sayisal_yer = ayt_puan_sayisal_yer - 50
            ayt_puan_ea_ham -= 50
            ayt_puan_ea_yer -= 50
            ayt_puan_sozel_ham = ayt_puan_sozel_ham - 50
            ayt_puan_sozel_yer = ayt_puan_sozel_yer - 50
            ydt_puan_ham = ydt_puan_ham - 50
            ydt_puan_yer = ydt_puan_yer - 50


        context = {
            "tyt_ham" : str(format(tyt_puan_ham ,".3f")),
            "ayt_sayisal_ham" : str(format(ayt_puan_sayisal_ham, ".3f")),
            "ayt_ea_ham" : str(format(ayt_puan_ea_ham, ".3f")),
            "ayt_sozel_ham" : str(format(ayt_puan_sozel_ham, ".3f")),
            "ydt_ham" : str(format(ydt_puan_ham, ".3f")),
            "tyt_yer" : str(format(tyt_puan_yer ,".3f")),
            "ayt_sayisal_yer" : str(format(ayt_puan_sayisal_yer, ".3f")),
            "ayt_ea_yer" : str(format(ayt_puan_ea_yer, ".3f")),
            "ayt_sozel_yer" : str(format(ayt_puan_sozel_yer, ".3f")),
            "ydt_yer" : str(format(ydt_puan_yer, ".3f")),
            "siralamalar" : {
                "tyt_sir_2018_ham" : YKSsiralama.ham2018(tyt_puan_ham,1,path),
                "tyt_sir_2019_ham" : YKSsiralama.ham2019(tyt_puan_ham,1,path),
                "tyt_sir_2018_yer" : YKSsiralama.yer2018(tyt_puan_yer,1,path),
                "tyt_sir_2019_yer" : YKSsiralama.yer2019(tyt_puan_yer,1,path),
                "ayt_sir_sayisal_2018_ham" : YKSsiralama.ham2018(ayt_puan_sayisal_ham,3,path),
                "ayt_sir_sayisal_2019_ham" : YKSsiralama.ham2019(ayt_puan_sayisal_ham,2,path),
                "ayt_sir_sayisal_2018_yer" : YKSsiralama.yer2018(ayt_puan_sayisal_yer,3,path),
                "ayt_sir_sayisal_2019_yer" : YKSsiralama.yer2019(ayt_puan_sayisal_yer,2,path),
                "ayt_sir_ea_2018_ham" : YKSsiralama.ham2018(ayt_puan_ea_ham,2,path),
                "ayt_sir_ea_2019_ham" : YKSsiralama.ham2019(ayt_puan_ea_ham,3,path),
                "ayt_sir_ea_2018_yer" : YKSsiralama.yer2018(ayt_puan_ea_yer,2,path),
                "ayt_sir_ea_2019_yer" : YKSsiralama.yer2019(ayt_puan_ea_yer,3,path),
                "ayt_sir_sozel_2018_ham" : YKSsiralama.ham2018(ayt_puan_sozel_ham,4,path),
                "ayt_sir_sozel_2019_ham" : YKSsiralama.ham2019(ayt_puan_sozel_ham,4,path),
                "ayt_sir_sozel_2018_yer" : YKSsiralama.yer2018(ayt_puan_sozel_yer,4,path),
                "ayt_sir_sozel_2019_yer" : YKSsiralama.yer2019(ayt_puan_sozel_yer,4,path),
                "ydt_sir_2018_ham" : YKSsiralama.ham2018(ydt_puan_ham,5,path),
                "ydt_sir_2019_ham" : YKSsiralama.ham2019(ydt_puan_ham,5,path),
                "ydt_sir_2018_yer" : YKSsiralama.yer2018(ydt_puan_yer,5,path),
                "ydt_sir_2019_yer" : YKSsiralama.yer2019(ydt_puan_yer,5,path),
            }
        }

        return render(request, "YKSsonuclar.html", context)

    else:
        return render(request, "YKS.html")


def nonuserlgs(request):
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
        return render(request,"LGSsonuclar.html", context)
        
    else:
        return render(request, "LGS.html")


def AAsystem(request):
    if request.method == "POST":
        return HttpResponse("hesaplıcam")
    
    else:
        return render(request, "AAsystem.html")

def A1system(request):
    if request.method == "POST":
        return HttpResponse("hesaplıcam")
    
    else:
        return render(request, "A1system.html")

