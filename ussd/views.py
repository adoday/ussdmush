from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render
import africastalking
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def  Murakaza_Neza(request):
    return render(request, 'index.html')

#  python3 -m pip install africastalking
AfricasUsername='mucyoadonis@gmail.com'
api_key ='d70ce442317ba09027e1572c8e3a9c6c427a21a963f2b25727ac5cfee3890746'
africastalking.initialize(AfricasUsername,api_key)

@csrf_exempt
def ussdApp(request):

    if request.method == 'POST':

        session_id = request.POST.get("sessionId")
        service_code = request.POST.get("serviceCode")
        phone_number =request.POST.get("phoneNumber")
        text = request.POST['text']
        level = text.split('*')
        category = text[:3]
        response =""
        #  main menu for our application
        if text == '':
            response =  "CON Murakaza neza kuri Mushtech \n"
            response += "1. Ikinyarwanda \n"
            response += "2. English\n"
        elif text == '1':

            response = "CON Amakuru ukeneye yose ku gihumyo \n"
            response += "1. igihumyo ni iki? \n"
            response += "2. Amoko y'ibihumyo bihingwa mu Rwanda \n"
            response += "3. Akamaro K'ibihumyo \n"

        elif text == '1*1':
            product="CON Menya igihumyo icyo aricyo"
            response = "Igihumyo ni igihingwa cyihariye; ntikigira indabo cyangwa imbuto.Kigizwe n’ibice bitatu by ingenzi: Umurundugushyu, Umuringa n’ingofero.  Umurundugushu wacyo ntugira imizi, amashami n’amababi. Ibi bisimburwa n’umuringa ndetse n’ingofero. Uyu murundugushu niwo ufata ku mugina aho giteye ukavomamo intungamubiri. "+str(product)+"\n"
        elif category =='1*1' and int(len(level)) == 3 and str(level[2]) in  str(level):
            response = "END Murakoze gusura Mushtech \n"


        elif text == '1*2':
            response ="CON Dore amoko y'ibihumyo bihingwa mu Rwanda \n"
            response += "1. Pleurote ( Soma Pulerote) \n"
            response += "2. Ganoderma ( soma Ganoderima) \n"
        elif text == '1*2*1':
            response = "END Pulerote  ni ubwoko bw'ibihumyo biribwa buhingirwa kugurishwa no kuribwa ku isi hose. Ubu bwoko bw'ibihumyo ntibugoye guteka kandi biraryoha. \n"
        
        elif text == '1*2*2':
            response ="END Ganoderima ni ubwoko bw'ibihumyo bukoreshwa nk'umuti mu buvuzi gakondo bwo ku mugabane wa Aziya. \n"
        
        elif text == '1*3':
            response ="CON Ibihumyo bigira intungamubiri nyinshi cyane, zikubye 2 ugereranije n'inyama ndetse n'ibindi bihingwa duhereye ko bikize ku ntunga mubiri nka proteine, imyunyu ngugu n'amavitamine amwe n'amwe (B1,B2), nk'uko bigaragara mu mbonerahamwe ikurikira : \n"
            response += "1. Mu buzima \n"
            response += "2. Mu rwego rw'ubukungu \n"
        elif text == '1*3*1':
            response ="END Ibihumyo birinda indwara z'imirire mibi,Ibihumyo bituma igifu gikora neza;Ibihumyo byongera ubushobozi bw'umubiri mukwirwanaho, Ibihumyo birinda indwara zijyanye no kugira amaraso make \n"
        elif text == '1*3*2':
            response ="END Gutangira ntibisaba amafaranga menshi, kuko ibihumbi 20000 bishobora guhinga nibura m2 2 kandi ukaba ushobora gusarura umusaruro wagurisha kugeza ku mafaranga ibihumbi ijana na mirongo inani kugeza ku bihumbi magana abiri (180.000-200.000) , ibi rero bikaba byatuma n'abatishoboye babihinga. Ibihumyo ntibisaba ikorana buhanga rihambaye (rihanitse). Ni igihingwa ngenga bukungu kuko ku masoko asanzwe mu gihugu igiciro k'ibihumyo kiri hagati ya 1000 na 2000 frw ; Ibihumyo bifasha urubyiruko n'abagore kwihangira imirimo kandi bishobora kuba igisubizo cyo kurandura ubukene mu Rwanda. \n"
        else:
            response = "END Ukanze ibitaribyo, ongera mukanya"
        return HttpResponse(response)
    else:
        return HttpResponse('we are on ussd app')
       
