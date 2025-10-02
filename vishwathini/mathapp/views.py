from django.shortcuts import render

def power_calc(request):
    context = {"I": "0", "R": "0", "P": "0"}
    
    if request.method == 'POST':
        try:
            I = float(request.POST.get('intensity', '0'))
            R = float(request.POST.get('resistance', '0'))
            
            P = I**2 * R  
            
            context["I"] = I
            context["R"] = R
            context["P"] = round(P, 2)  
        except:
            context["P"] = "Error"
    
    return render(request, 'mathapp/math.html', context)
