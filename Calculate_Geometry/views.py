from django.shortcuts import render
import math
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, "home.html")

def Square(request):
    Area = ''
    Perimeter = ''
    n1 = ''
    data = {}
    try:
        if request.method=="GET":
            n1 = eval(request.GET.get('SideA'))
            Perimeter = 4*n1
            Area =  n1*n1
    except:
        messages.error(request, "Enter valid values")
    data = {
        'Area':Area,
        'Perimeter':Perimeter,
        'n1':n1,
    }
    return render(request, 'shape_cal/Square.html', data) 

def Rectangle(request):
    Area = ''
    Perimeter = ''
    n1 = ''
    n2 = ''
    data = {}
    try:
        if request.method=="GET":
            n1 = eval(request.GET.get('SideA'))
            n2 = eval(request.GET.get('SideB'))
            Perimeter = 2*n1+2*n2
            Area =  n1*n2
    except:
        messages.error(request, "Enter valid values")
    data = {
        'Area':Area,
        'Perimeter':Perimeter,
        'n1':n1,
        'n2':n2,
    }
    return render(request, 'shape_cal/Rectangle.html', data) 

def Triangle(request):
    Area = ''
    Perimeter = ''
    SemiPerimeter = ''
    n1 = ''
    n2 = ''
    n3 = ''
    data = {}
    try:
        if request.method=="GET":
            n1 = eval(request.GET.get('SideA'))
            n2 = eval(request.GET.get('SideB'))
            n3 = eval(request.GET.get('SideC'))
            Perimeter = n1+n2+n3
            SemiPerimeter = Perimeter / 2
            a = SemiPerimeter - n1 
            b = SemiPerimeter - n2
            c = SemiPerimeter - n3
            Area = math.sqrt(SemiPerimeter * a * b * c)   
    except:
        messages.error(request, "Enter valid values")
    data = {
        'Area':Area,
        'Perimeter':Perimeter,
        'SemiPerimeter':SemiPerimeter,
        'n1':n1,
        'n2':n2,
        'n3':n3,
    }
    return render(request, 'shape_cal/Triangle.html', data)    

def Circle(request):
    pi = 3.1415926535898
    Area = ''
    Diameter = ''
    Circumference = ''
    n1 = ''
    data = {}
    try:
        if request.method=="GET":
            n1 = eval(request.GET.get('SideA'))
            Area =  pi*n1*n1
            Diameter = 2*n1
            Circumference = 2*pi*n1
    except:
        messages.error(request, "Enter valid values")
    data = {
        'Area':Area,
        'Diameter':Diameter,
        'n1':n1,
        'Circumference':Circumference,
    }
    return render(request, 'shape_cal/Circle.html', data) 
    
def Cube(request):
    Area = ''
    volume = ''
    n1 = ''
    data = {}
    try:
        if request.method=="GET":
            n1 = eval(request.GET.get('SideA'))
            volume = n1*n1*n1
            Area =  6*n1*n1
    except:
        messages.error(request, "Enter valid values")
    data = {
        'Area':Area,
        'volume':volume,
        'n1':n1,
    }
    return render(request, 'shape_cal/Cube.html', data)
    
def Cuboid(request):
    Area = ''
    volume = ''
    L = ''
    B = ''
    H = ''
    data = {}
    try:
        if request.method=="GET":
            L = eval(request.GET.get('SideL'))
            B = eval(request.GET.get('SideB'))
            H = eval(request.GET.get('SideH'))
            volume = L*B*H
            Area =  2*L*B+2*L*H+2*B*H
    except:
        messages.error(request, "Enter valid values")
    data = {
        'Area':Area,
        'volume':volume,
        'L':L,
        'B':B,
        'H':H,
    }
    return render(request, 'shape_cal/Cuboid.html', data)
    
def Sphere(request):
    Area = ''
    volume = ''
    r = ''
    pi = 3.1415926535898
    data = {}
    try:
        if request.method=="GET":
            r = eval(request.GET.get('SideA'))
            volume = 1.3333333*pi*r*r*r
            Area =  4*pi*r*r
    except:
        messages.error(request, "Enter valid values")
    data = {
        'Area':Area,
        'volume':volume,
        'r':r,
    }
    return render(request, 'shape_cal/Sphere.html', data)
    
def Cylinder(request):
    pi = 3.1415926535898
    Area = ''
    volume = ''
    r = ''
    h = ''
    data = {}
    try:
        if request.method=="GET":
            r = eval(request.GET.get('SideA'))
            h = eval(request.GET.get('SideB'))
            volume = pi*r*r*h
            Area =  2*pi*r*h+2*pi*r*r
    except:
        messages.error(request, "Enter valid values")
    data = {
        'Area':Area,
        'volume':volume,
        'r':r,
        'h':h,
    }
    return render(request, 'shape_cal/Cylinder.html', data)
    
def Cone(request):
    pi = 3.1415926535898
    Area = ''
    volume = ''
    r = ''
    h = ''
    data = {}
    try:
        if request.method=="GET":
            r = eval(request.GET.get('SideA'))
            h = eval(request.GET.get('SideB'))
            volume = 0.33333*pi*r*r*h
            n = math.sqrt(r*r+h*h)
            Area =  pi*r*n+pi*r*r
    except:
        messages.error(request, "Enter valid values")
    data = {
        'Area':Area,
        'volume':volume,
        'r':r,
        'h':h,
    }
    return render(request, 'shape_cal/Cone.html', data)