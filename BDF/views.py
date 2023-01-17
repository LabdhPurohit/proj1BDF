from django.shortcuts import render, redirect
import requests
import json

# Create your views here.
def scrap():
      try:
            global title, RD, error, all_quotes, all_quotes_trans
            error = "Sorry unable to Find this movie :("
            title = ""
            RD = ""
            all_quotes = []
            all_quotes_trans = []

            # Fetch the JSON data from the URL
            url = 'https://labdhpurohit.github.io/Files/Quotes.json'
            response = requests.get(url)

            ii = d
            # Load the JSON data
            data = json.loads(response.text)

            # Print the JSON data
            quotes = json.dumps(data, indent=4)

            # print(len(quotes))

            for row in range(6964):
                  q = json.dumps(data[row]["Title"], indent=4)
                  if '"'+ii+'"'.lower()==q.lower():
                        title = json.dumps(data[row]["Title"], indent=4)
                        RD = json.dumps(data[row]["Year"], indent=4)
                        all_quotes.append(json.dumps(data[row]["Quote"], indent=4))
                        all_quotes_trans.append(json.dumps(data[row]["Trans"], indent=4))
                        # print(json.dumps(data[row], indent=4))

            print(title)
            if RD=="":
                  print(error)
            else:
                  print(RD)
            print(all_quotes, all_quotes_trans)
      except Exception as e:
            print(e)



def home(request):
    context = {}
    global d
    if request.method == "POST":
        context1 = {}
        d = request.POST.get('name')
        scrap()
        if len(all_quotes) == 4:
            context1 = {'Title': title, 'RD': RD, 'quote1':all_quotes[0], 'quote_tran1':all_quotes_trans[0], 'quote2':all_quotes[1], 'quote_tran2':all_quotes_trans[1], 'quote3':all_quotes[2], 'quote_tran3':all_quotes_trans[2], 'quote4':all_quotes[3], 'quote_tran4':all_quotes_trans[3]}
            context=context1
        elif len(all_quotes) == 3:
            context1 = {'Title': title, 'RD': RD, 'quote1':all_quotes[0], 'quote_tran1':all_quotes_trans[0], 'quote2':all_quotes[1], 'quote_tran2':all_quotes_trans[1], 'quote3':all_quotes[2], 'quote_tran3':all_quotes_trans[2]}
            context=context1
        elif len(all_quotes) == 2:
            context1 = {'Title': title, 'RD': RD, 'quote1':all_quotes[0], 'quote_tran1':all_quotes_trans[0], 'quote2':all_quotes[1], 'quote_tran2':all_quotes_trans[1]}
            context=context1
        elif len(all_quotes) == 1:
            context1 = {'Title': title, 'RD': RD, 'quote1':all_quotes[0], 'quote_tran1':all_quotes_trans[0]}
            context=context1
        else:
            context1 = {'Error': error}
            context=context1
    return render(request, "BDF/index.html", context)


    # if request.method =="POST":
    #     try:
    #         context2 = {}
    #         user=" "
    #         sub=" "
    #         desc=" "
    #         user = request.POST.get('user_name')
    #         sub = request.POST.get('subject')
    #         desc = request.POST.get('description')
    #         feed=" "
    #         TOKEN = "5660813685:AAGRG9ci-ZB4uRn9U1g4fX_sRUJViPVI5uY"
    #         chat_id = "-827826970"
    #         message = f"Name: {user} \nSubject: {sub} \nDescription: {desc}"
    #         if user==" " or sub==" " or desc==" ":
    #             feed="Please Fill Form" 
    #         elif user!=" " and sub!=" " and desc!=" ":
    #             url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    #             print(requests.get(url).json())
    #             feed="Thank you for your Feedback."
    #         else:
    #             feed=" "
    #         context2 = {'feedback':feed}
    #         context = context2
    #     except:
    #         context2 = {'feedback': "Sorry can't send Feedback"}
    #         context = context2
    #     return render(request, "BDF/index.html", context)
    # return render(request, "BDF/index.html")

# def show(request):
#     return render(request, "BDF/show.html", {'data': data})
# def home(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             # Do something with the form data
#             pass
#     else:
#         form = ContactForm()

#     return render(request, 'BDF/index.html', {'form': form})
