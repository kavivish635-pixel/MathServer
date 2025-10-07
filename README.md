# Ex.05 Design a Website for Server Side Processing
## Date:07-10-2025

## AIM:
 To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side. 


## FORMULA:
P = I<sup>2</sup>R
<br> P --> Power (in watts)
<br> I --> Intensity
<br> R --> Resistance

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :

```

math.html
<html>
<title>Body Mass Index</title>
<style>
body
{
background-color:rgb(0, 252, 206);
}
.edge {
width: 1650px;
margin-left: auto;
margin-right: auto;
padding-top: 400px;
padding-left: 350px;
}
.box {
display:block;
border: solid 7px peru;
width: 700px;
min-height: 400px;
font-size: 40px;
background-color: rgb(130, 191, 238);
}
.formelt{
color: blue;
text-align: center;
margin-top: 7px;
margin-bottom: 7px;
}
</style>
</head>
<body>
<div class= "edge">
<div class= "box">
<h1>Body Mass Index</h1>
<h2>k.vishwathini(25016664)</h2>
<form method="POST">
{% csrf_token %}
<div class= "formelt">
Weight: <input type= "text" name="Weight" value="{{Weight}}"></input>(in kg)<br/>
</div>
<div class= "formelt">
Height: <input type="text" name="Height" value="{{Height}}"></input>(in m)<br/>
</div>
<div class= "formelt">
<input type="submit" value="Calculate"><br/>
</div>
<div class= "formelt">
bmi: <input type="text" name="bmi" value="{{bmi}}" align:"center"></input>kg/m<sup>3</sup><br/>
</div>
</form>
</div>
</div>
</body>
</html>



views.py
from django.shortcuts import render
def calculateBMI(request):
    bmi=None
    Weight=None
    Height=None
    if request.method == 'POST':
        print("POST method is used")
        Weight=float(request.POST.get("Weight"))
        Height=float(request.POST.get("Height"))/100
        bmi = Weight/(Height**2)
        bmi =round(bmi,2)
        print(f"1Weight in kg: {Weight} ,Height in m: {Height},bmi: {bmi}")
    return render(request,'mathapp/math.html',{'bmi':bmi})


urls.py
from django.contrib import admin
from django.urls import path
from mathapp import views
urlpatterns=[
    path('admin/', admin.site.urls),
    path('',views.calculateBMI,name="home"),
    path('bmi/', views.calculateBMI,name='bmi')
]


```

## SERVER SIDE PROCESSING:
![alt text](<Screenshot (61).png>)

## HOMEPAGE:
![alt text](<Screenshot (62).png>)

## RESULT:
The program for performing server side processing is completed successfully.
