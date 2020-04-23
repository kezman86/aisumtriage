from django.db import models
from django.contrib.auth.models import User

# Create your models here.
SUM_MODULES = [
    #ARCH
    ("Summit - System level", "Summit - System level"),
    ("Summit - DB Architecture/Interfaces" , "Summit - DB Architecture/Interfaces"),
    ("Summit - User Interface / FT Framework", "Summit - User Interface / FT Framework"),
    ("Summit - DB Admin / Upgrade", "Summit - DB Admin / Upgrade") ,
    ("Summit - Extendibility / Meta Data", "Summit - Extendibility / Meta Data" ) ,
    ("Summit - RT Server Architecture And Admin", "Summit - RT Server Architecture And Admin" ),
    ("Summit - Reporting Framework", "Summit - Reporting Framework") ,
    ( "Summit - Performance", "Summit - Performance" ),
    ("Summit - User Documentation", "Summit - User Documentation") ,
    ("Summit - Utilities/Static Data", "Summit - Utilities/Static Data" ) ,

    #FO
    ("Summit - Toolkit/Pricing Models", "Summit - Toolkit/Pricing Models") ,
    ("Summit - OTC Derivatives", "Summit - OTC Derivatives") ,
    ("Summit - Equities", "Summit - Equities") ,
    ("Summit - Fixed Income", "Summit - Fixed Income") ,
    ("Summit - Bond Issuance", "Summit - Bond Issuance" ),
    ("Summit - Cash Management/Settlement Processing", "Summit - Cash Management/Settlement Processing") ,
    ("Summit - RTF/MKTDATA", "Summit - RTF/MKTDATA" ),
    ("Summit - Toolkit/Pricing Models", "Summit - Toolkit/Pricing Models"),
    ("Summit - Treasury", "Summit - Treasury") ,
    ("Summit - Fixed Income", "Summit - Fixed Income"),
    ("Summit - Structured Products/MUST", "Summit - Structured Products/MUST" ),
    ("Summit - Equity/Equity Derivatives", "Summit - Equity/Equity Derivatives"),

    #RISK
    ("Summit - Market Risk Limits" , "Summit - Market Risk Limits" ),
    ("Summit - Credit risk", "Summit - Credit risk" ),
    ("Summit - Historical VAR", "Summit - Historical VAR") ,
    ("Summit - CCP", "Summit - CCP") ,
    ("Summit - GAP Analysis / Cash Analysis", "Summit - GAP Analysis / Cash Analysis" ),
    ("Summit - APAC - Credit Limit", "Summit - APAC - Credit Limit") ,
    ("Summit - Risk Management / RT Risk", "Summit - Risk Management / RT Risk"),
    ("Summit - Credit Derivatives", "Summit - Credit Derivatives") ,

 #BO
    ("Summit - Buyside", "Summit - Buyside" ),
    ("Summit - GBO", "Summit - GBO") ,
    ("Summit - Operations", "Summit - Operations" ),
    ("Summit - Commercial Lending", "Summit - Commercial Lending") ,
    ("Summit - Collateral Management", "Summit - Collateral Management") ,
    ("Summit - Security Finance", "Summit - Security Finance" ),
    ("Summit - Post Trade Booking Processing", "Summit - Post Trade Booking Processing" ),
    ("Summit - Back Office Positioning", "Summit - Back Office Positioning") ,
    ("Summit - Back Office Documentation Engine" , "Summit - Back Office Documentation Engine") ,
    ("Summit - Operations/Documentation" , "Summit - Operations/Documentation") ,
    ("Summit - Security / STD" , "Summit - Security / STD") ,

    #ACCT
    ("Summit - Accounting" , "Summit - Accounting") ,
    ("Summit - P&L" , "Summit - P&L"),
    ("Summit - Hedge Accounting/FAS133" , "Summit - Hedge Accounting/FAS133")
  ]

class CaseSF(models.Model):
    caseIDSf = models.CharField(primary_key=True, max_length = 18)
    caseNumber = models.CharField(max_length = 18)
    caseSubject = models.CharField(max_length = 256)
    caseDescription = models.TextField(blank = None)
    caseModule = models.CharField( choices=SUM_MODULES, max_length = 128)
    aicorrect = models.BooleanField(default = True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    completedBy = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    status = models.IntegerField(default = 0)
