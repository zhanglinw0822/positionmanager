from django.shortcuts import render
from manager.utils import strategymanager,bitmex

# Create your views here.
def home(request):
    context = {}
    list = []
    name = request.GET['strategy_name']
    strategymanager.init()
    if name != None:
        for strategy in strategymanager.strategys:
            if (name==strategy['name']):
                for account in strategy.get('accounts'):
                    # client = bitmex.bitmex(test=False, api_key=account.get('key'), api_secret=account.get('secret'))
                    client = bitmex.bitmex(test=True, api_key=account.get('key'), api_secret=account.get('secret'))
                    positionresult = client.position().result()
                    list.extend(positionresult)
    context['list'] = list

    return render(request, 'manager/home.html', context)
