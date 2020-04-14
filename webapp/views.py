from django.contrib.auth import login , authenticate , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.db import IntegrityError
from django.utils import timezone

from webapp.forms import CaseSFForm
from webapp.models import CaseSF


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'webapp/signupuser.html', {'form' : UserCreationForm() })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password = request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('cases')
            except IntegrityError:
                return render(request, 'webapp/signupuser.html', {'form' : UserCreationForm() , 'error':'Username has already been taken. Chose a new username' })
        else:
            return render(request, 'webapp/signupuser.html', {'form' : UserCreationForm() , 'error':'Password did not match' })

def loginuser(request):
    if request.method == 'GET' :
        return render ( request , 'webapp/loginuser.html' , {'form' : AuthenticationForm()} )
    else :
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'webapp/loginuser.html', {'form' : AuthenticationForm(), 'error':'Username and password did not match'})
        else:
            login(request, user)
            return redirect('cases')


def index(request):
    return render(request, 'webapp/index.html')

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')


sumModules = {
    "arch": ["Summit - System level" , "Summit - DB Architecture/Interfaces" ,
              "Summit - User Interface / FT Framework" , "Summit - DB Admin / Upgrade" ,
              "Summit - Extendibility / Meta Data" , "Summit - RT Server Architecture And Admin" ,
              "Summit - Reporting Framework" , "Summit - Performance" ,
              "Summit - User Documentation" , "Summit - Utilities/Static Data" ] ,
    "fo" : ["Summit - Toolkit/Pricing Models" , "Summit - OTC Derivatives" , "Summit - Equities" ,
            "Summit - Fixed Income" , "Summit - Bond Issuance" , "Summit - Cash Management/Settlement Processing" ,
            "Summit - RTF/MKTDATA" , "Summit - Toolkit/Pricing Models", "Summit - Treasury" , "Summit - Fixed Income","Summit - Structured Products/MUST" , "Summit - Equity/Equity Derivatives"  ] ,
    "risk" : ["Summit - Market Risk Limits" , "Summit - Credit risk" , "Summit - Historical VAR" , "Summit - CCP" ,
              "Summit - GAP Analysis / Cash Analysis" , "Summit - APAC - Credit Limit" ,
              "Summit - Risk Management / RT Risk", "Summit - Credit Derivatives"] ,
    "bo" : ["Summit - Buyside" , "Summit - GBO" ,
            "Summit - Operations" , "Summit - Commercial Lending" ,
            "Summit - Collateral Management" , "Summit - Security Finance" ,
            "Summit - Post Trade Booking Processing" , "Summit - Back Office Positioning" ,
            "Summit - Back Office Documentation Engine" ,
            "Summit - Operations/Documentation" , "Summit - Security / STD"] ,
    "acct" : ["Summit - Accounting", "Summit - P&L", "Summit - Hedge Accounting/FAS133"]
}

@login_required
def cases(request):
    cases = CaseSF.objects.filter( datecompleted__isnull=True )

    if request.method == 'GET':
        return render(request, 'webapp/cases.html', {'cases':cases,
                                                 'modules_risk' : sumModules['risk'],
                                                 'modules_acct' : sumModules["acct"],
                                                 'modules_bo' : sumModules["bo"],
                                                 'modules_fo' : sumModules["fo"],
                                                 'modules_arch' : sumModules["arch"]
                                                 })



@login_required
def completedcases(request):
    casessf = CaseSF.objects.filter( datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'webapp/completedcases.html', {'casessf':casessf})

@login_required
def viewcase(request, caseID):
    case = get_object_or_404(CaseSF, caseIDSf=caseID)
    if request.method == 'GET':
        form = CaseSFForm(instance=case)
        return render(request, 'webapp/viewcase.html', {'case':case, 'form':form})


@login_required
def completecase(request, caseID):
    case = get_object_or_404(CaseSF, caseIDSf=caseID)
    if request.method == 'POST':
        case.datecompleted = timezone.now()
        case.completedBy = request.user
        if case.caseModule != request.POST['sumModule']:
            case.caseModule = request.POST['sumModule']
            case.aicorrect = False
        case.save()
        return redirect('cases')

def savecases(request):
    case = CaseSF()
    case.caseIDSf = 'id25'
    case.caseNumber = '25'
    case.caseDescription = ' Desc case2 5'
    case.caseSubject = 'Subj 5'
    case.caseModule = "Summit - Buyside"

    case.save()

    case = CaseSF()
    case.caseIDSf = 'id26'
    case.caseNumber = '26'
    case.caseDescription = ' Desc case 26'
    case.caseSubject = 'Subj 26'
    case.caseModule = "Summit - Risk Management / RT Risk"

    case.save()


    case = CaseSF()
    case.caseIDSf = 'id27'
    case.caseNumber = '27'
    case.caseDescription = ' Desc case 27'
    case.caseSubject = 'Subj 7'
    case.caseModule = "Summit - Performance"

    case.save()



