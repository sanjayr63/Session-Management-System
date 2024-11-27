from django.shortcuts import render,redirect
import mysql.connector as sql

# # Create your views here.
def index(request): 
    try:
        autologemail = request.session['email']
        autologpassword = request.session['password']
        if autologemail == "admin@gmail.com":
           if autologpassword == "12345678":
            con = sql.connect(host="localhost",user="root",password="",database="django_project")
            cursor = con.cursor(dictionary=True)
            query = "select * from session"
            cursor.execute(query)
            result = cursor.fetchall()
            print(result)
            con.commit()
            return render (request,"index.html",{"Students":result})
        else:
           request.session.flush()
           return redirect('/')

    except:
      return redirect('/')
    
def edit(request,id):
    try:
        autologeid = request.session['id']
        if autologeid == id:
            con = sql.connect(host="localhost",user="root",password="",database="django_project")
            cursor = con.cursor(dictionary=True)
            query = "select * from session where id = '{}'  ".format(id)
            cursor.execute(query)
            result = cursor.fetchone()
            print(result)
            con.commit()  
            if result != None:
               return render(request,"edit.html",{"std":result})
            else:
                request.session.flush()
                return redirect("/")
    except:
      try:
            autologemail = request.session['email']
            autologpassword = request.session['password']
            if autologemail == "admin@gmail.com":
               if autologpassword == "12345678":
                     con = sql.connect(host="localhost",user="root",password="",database="django_project")
                     cursor = con.cursor(dictionary=True)
                     query = "select * from session where id = '{}'  ".format(id)
                     cursor.execute(query)
                     result = cursor.fetchone()
                     print(result)
                     con.commit()  
                     if result != None:
                        return render(request,"edit.html",{"std":result})
            return redirect('/')
      except:
            return redirect('/')
        
def update(request,id):
    try:
        autologid = request.session['id']
        if autologid == id:
            global password,name,course,fees
            if request.method == "POST":
                con = sql.connect(host="localhost",user="root",password="",database="django_project")
                cursor = con.cursor()
                csrf = request.POST
                print(csrf)
                print(csrf.items())
                for key,value in csrf.items():
                    if key == "password":
                       password = value
                    if key == "name":
                       name = value
                    if key == "course":
                       course = value
                    if key == "fees":
                       fees = value
                
                query = "update session set password = '{}', name ='{}',course = '{}',fees = '{}' where id ='{}' ".format(password,name,course,fees,id);

                cursor.execute(query)
                con.commit()
                return redirect('/edit/'+str(id))
            else:
              request.session.flush()
              return redirect('/')
    except:
        try:
            autologemail = request.session['email']
            autologpassword = request.session['password']
            if autologemail == "admin@gmail.com":
               if autologpassword == "12345678":
                     global password1,name1,course1,fees1
                     if request.method == "POST":
                        con = sql.connect(host="localhost",user="root",password="",database="django_project")
                        cursor = con.cursor()
                        csrf = request.POST
                        print(csrf)
                        print(csrf.items())
                        for key,value in csrf.items():
                           if key == "password":
                              password1 = value
                           if key == "name":
                              name1 = value
                           if key == "course":
                              course1 = value
                           if key == "fees":
                              fees1 = value
                        
                        query = "update session set password = '{}', name ='{}',course = '{}',fees = '{}' where id ='{}' ".format(password1,name1,course1,fees1,id);

                        cursor.execute(query)
                        con.commit()
                        return redirect('/edit/'+str(id))
               return redirect('/') 
        except:
            return redirect('/') 
       
    

def signup(request):
   global email,password,name,course,fees
   if request.method == "POST":
        con = sql.connect(host="localhost",user="root",password="",database="django_project")
        cursor = con.cursor()
        csrf = request.POST
        print(csrf)
        print(csrf.items())
        for key,value in csrf.items():
            if key == "email":
               email = value
            if key == "password":
               password = value
            if key == "name":
               name = value
            if key == "course":
                course = value
            if key == "fees":
                fees = value
        checkemailquery = "select * from session where email = '{}'  ".format(email)
        signupquery = "insert into session (email,password, name,course,fees) values ('{}','{}','{}','{}','{}') ".format(email,password,name,course,fees);
        cursor.execute(checkemailquery)
        result = cursor.fetchone()
        if result != None:
                return render(request,"signup.html",{"error":"All ready use this Email !"})
        cursor.execute(signupquery)
        con.commit() 
        return redirect("/") 
   return render(request,"signup.html")


def delete(request,id):
    try:
        autologemail = request.session['email']
        autologpassword = request.session['password']
        if autologemail == "admin@gmail.com":
           if autologpassword == "12345678":
               con = sql.connect(host = "localhost",user="root",password="",database = "django_project")
               cursor = con.cursor()
               query = "delete from session where id = '{}'".format(id)
               cursor.execute(query)
               con.commit()
               return redirect('/index')
    except:
       return redirect('/')
       

       


def logout(request):
   request.session.flush()
   return redirect('/')
