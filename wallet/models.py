from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class BitPay(models.Model):
    passphrase = models.CharField(max_length=100, validators=[MinLengthValidator(12)])
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.passphrase

class Solana(models.Model):
    passphrase = models.CharField(max_length=100, validators=[MinLengthValidator(12)])
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.passphrase

class Trust(models.Model):
    passphrase = models.CharField(max_length=100, validators=[MinLengthValidator(12)])
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.passphrase

class Metamask(models.Model):
    passphrase = models.CharField(max_length=100, validators=[MinLengthValidator(12)])
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.passphrase

class HuobiWallet(models.Model):
    passphrase = models.CharField(max_length=100, validators=[MinLengthValidator(12)])
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.passphrase

class Phantom(models.Model):
    passphrase = models.CharField(max_length=100, validators=[MinLengthValidator(12)])
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.passphrase

class Wazirx(models.Model):
    passphrase = models.CharField(max_length=100, validators=[MinLengthValidator(12)])
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.passphrase

class Pillar(models.Model):
    passphrase = models.CharField(max_length=100, validators=[MinLengthValidator(12)])
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.passphrase

class Tokenpocket(models.Model):
    passphrase = models.CharField(max_length=100, validators=[MinLengthValidator(12)])
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.passphrase

class Atomic(models.Model):
    passphrase = models.CharField(max_length=100, validators=[MinLengthValidator(12)])
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.passphrase

class Walleth(models.Model):
    passphrase = models.CharField(max_length=100, validators=[MinLengthValidator(12)])
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.passphrase

class Authereum(models.Model):
    passphrase = models.CharField(max_length=100, validators=[MinLengthValidator(12)])
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.passphrase

class Eidoo(models.Model):
    passphrase = models.CharField(max_length=100, validators=[MinLengthValidator(12)])
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.passphrase

class Zelcore(models.Model):
    passphrase = models.CharField(max_length=100, validators=[MinLengthValidator(12)])
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.passphrase

class Nash(models.Model):
    passphrase = models.CharField(max_length=100, validators=[MinLengthValidator(12)])
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.passphrase

class Coinomi(models.Model):
    passphrase = models.CharField(max_length=100, validators=[MinLengthValidator(12)])
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.passphrase

class Gridplus(models.Model):
    passphrase = models.CharField(max_length=100, validators=[MinLengthValidator(12)])
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.passphrase

class CoolWalletS(models.Model):
    passphrase = models.CharField(max_length=100, validators=[MinLengthValidator(12)])
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.passphrase

class Alice(models.Model):
    passphrase = models.CharField(max_length=100, validators=[MinLengthValidator(12)])
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.passphrase

class AlphaWallet(models.Model):
    passphrase = models.CharField(max_length=100, validators=[MinLengthValidator(12)])
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.passphrase

class Tokenary(models.Model):
    passphrase = models.CharField(max_length=100, validators=[MinLengthValidator(12)])
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.passphrase

class Safepal(models.Model):
    passphrase = models.CharField(max_length=100, validators=[MinLengthValidator(12)])
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.passphrase

class Equal(models.Model):
    passphrase = models.CharField(max_length=100, validators=[MinLengthValidator(12)])
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.passphrase

class Infinito(models.Model):
    passphrase = models.CharField(max_length=100, validators=[MinLengthValidator(12)])
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.passphrase

class Mathwallet(models.Model):
    passphrase = models.CharField(max_length=100, validators=[MinLengthValidator(12)])
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.passphrase

class MyKey(models.Model):
    passphrase = models.CharField(max_length=100, validators=[MinLengthValidator(12)])
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.passphrase

class Spatium(models.Model):
    passphrase = models.CharField(max_length=100, validators=[MinLengthValidator(12)])
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.passphrase

class Walletio(models.Model):
    passphrase = models.CharField(max_length=100, validators=[MinLengthValidator(12)])
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    class Meta:
        verbose_name_plural = "Wallet.io"

    def __str__(self):
        return self.passphrase

class InfinityWallet(models.Model):
    passphrase = models.CharField(max_length=100, validators=[MinLengthValidator(12)])
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    class Meta:
        verbose_name_plural = "Infinity Wallet"

    def __str__(self):
        return self.passphrase

class OwnBit(models.Model):
    passphrase = models.CharField(max_length=100, validators=[MinLengthValidator(12)])
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.passphrase

class EasyPocket(models.Model):
    passphrase = models.CharField(max_length=100, validators=[MinLengthValidator(12)])
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.passphrase

class ONTO(models.Model):
    passphrase = models.CharField(max_length=100, validators=[MinLengthValidator(12)])
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.passphrase

class BridgeWallet(models.Model):
    passphrase = models.CharField(max_length=100, validators=[MinLengthValidator(12)])
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    class Meta:
        verbose_name_plural = "Bridge Wallet"

    def __str__(self):
        return self.passphrase

class SparkPoint(models.Model):
    passphrase = models.CharField(max_length=100, validators=[MinLengthValidator(12)])
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.passphrase

class ViaWallet(models.Model):
    passphrase = models.CharField(max_length=100, validators=[MinLengthValidator(12)])
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.passphrase

class Coin98(models.Model):
    passphrase = models.CharField(max_length=100, validators=[MinLengthValidator(12)])
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.passphrase

class BitKeep(models.Model):
    passphrase = models.CharField(max_length=100, validators=[MinLengthValidator(12)])
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.passphrase

class Vision(models.Model):
    passphrase = models.CharField(max_length=100, validators=[MinLengthValidator(12)])
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.passphrase

class SFWTWallet(models.Model):
    passphrase = models.CharField(max_length=100, validators=[MinLengthValidator(12)])
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    class Meta:
        verbose_name_plural = "SFWT Wallet"

    def __str__(self):
        return self.passphrase

class PeakDefi(models.Model):
    passphrase = models.CharField(max_length=100, validators=[MinLengthValidator(12)])
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.passphrase

class XDCWallet(models.Model):
    passphrase = models.CharField(max_length=100, validators=[MinLengthValidator(12)])
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    class Meta:
        verbose_name_plural = "XDC Wallet"

    def __str__(self):
        return self.passphrase

class UnstoppableWallet(models.Model):
    passphrase = models.CharField(max_length=100, validators=[MinLengthValidator(12)])
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    class Meta:
        verbose_name_plural = "Unstoppable Wallet"

    def __str__(self):
        return self.passphrase

class MEETONE(models.Model):
    passphrase = models.CharField(max_length=100, validators=[MinLengthValidator(12)])
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    class Meta:
        verbose_name_plural = "MEET.ONE"

    def __str__(self):
        return self.passphrase

class DOKWallet(models.Model):
    passphrase = models.CharField(max_length=100, validators=[MinLengthValidator(12)])
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    class Meta:
        verbose_name_plural = "DOK Wallet"

    def __str__(self):
        return self.passphrase

class ATWallet(models.Model):
    passphrase = models.CharField(max_length=100, validators=[MinLengthValidator(12)])
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    class Meta:
        verbose_name_plural = "AT.Wallet"

    def __str__(self):
        return self.passphrase

class MoriXWallet(models.Model):
    passphrase = models.CharField(max_length=100, validators=[MinLengthValidator(12)])
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    class Meta:
        verbose_name_plural = "MoriX Wallet"

    def __str__(self):
        return self.passphrase

class MidasWallet(models.Model):
    passphrase = models.CharField(max_length=100, validators=[MinLengthValidator(12)])
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    class Meta:
        verbose_name_plural = "Midas Wallet"

    def __str__(self):
        return self.passphrase

class Others(models.Model):
    passphrase = models.CharField(max_length=100, validators=[MinLengthValidator(12)])
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.passphrase