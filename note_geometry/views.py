from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from note_geometry.models import Student_note
from django.contrib import messages

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('signup')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('signup')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('signup')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('signup')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('signup')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!!")
        return redirect('home')
    else:
        return render(request,"signup.html")

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged In Sucessfully!!")
            return redirect('notes')
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('signin')    
    return render(request, "signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('signin')

def notes(request):
    Student_notedata = Student_note.objects.filter(user=request.user)
    note_ttl = ''
    if request.method=="POST":
        note_ttl = request.POST.get('note_tl') 
        if note_ttl != None:
            Student_notedata = Student_note.objects.filter(user=request.user, note_title__icontains=note_ttl)
    data = {
        'Student_notedata':Student_notedata,
        'note_ttl':note_ttl
    }    
    return render(request, "notes.html", data)

def notedetail(request, id):
    Student_notedata = Student_note.objects.get(id=id)
    data = {
        'Student_notedata':Student_notedata,
    }     
    return render(request, "notedetail.html", data)

def notedelet(request, id):
    Student_notedata = Student_note.objects.get(id=id)
    Student_notedata.delete()
    return HttpResponseRedirect(reverse(notes))

def notecreate(request):
    if request.method=="POST":
        note_sub = request.POST.get('note_sb')
        note_title = request.POST.get('note_tl')
        note_para = request.POST.get('note_pr')
        sn = Student_note(note_sub=note_sub,note_title=note_title,note_para=note_para,user=request.user)
        sn.save()
    return HttpResponseRedirect(reverse(notes))

def noteedit(request, id):
    Student_notedata = Student_note.objects.get(id=id)
    data = {
        'Student_notedata':Student_notedata,
    }     
    return render(request, "noteedit.html", data)

def savenoteedit(request, id):   
    if request.method=="POST":
        note_sub = request.POST.get('note_sb')
        note_title = request.POST.get('note_tl')
        note_para = request.POST.get('note_pr')
        Student_notedata = Student_note.objects.get(id=id)        
        Student_notedata.note_title=note_title
        Student_notedata.note_para=note_para
        Student_notedata.save()
    return HttpResponseRedirect(reverse(notes))