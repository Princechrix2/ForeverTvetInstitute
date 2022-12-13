from functools import reduce
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import include, reverse
from .models import Fixed_Fee, Fixed_Fee_Day, Graduate_year, Student, Trade
import datetime
from . import forms 
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required



# Create your views here.



def Error_login(request):
    return render(request, 'Base/Error/Unkownuser_d.html',{})

def dos_user(request):
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            Boys = len(Student.objects.filter(gender = 'M', graduated='False'))
            Girls = len(Student.objects.filter(gender = 'F', graduated='False'))
            All_total = len(Student.objects.filter(graduated='False'))
            
                
            return render(request, 'dos/index.html', {
                "Boys": Boys,
                "Girls": Girls,
                "All_total": All_total,
                
            })
        else:
            return redirect(Login_User)
    else:
        logout(request)
        return redirect(Error_login)





def burser_user(request):
    if request.user.email.endswith('burser@gmail.com'):
        
        if request.user.is_authenticated:
            Boys = len(Student.objects.filter(gender = 'M', graduated='False'))
            Girls = len(Student.objects.filter(gender = 'F', graduated='False'))
            All_total = len(Student.objects.filter(graduated='False'))
                
            return render(request, 'burser/index.html', {
                "Boys": Boys,
                "Girls": Girls,
                "All_total": All_total,
            })
        else:
            return redirect(Login_User)
    else:
        return redirect(Error_login)

def patron_user(request):
    if request.user.email.endswith('patron@gmail.com'):
        
        if request.user.is_authenticated:
            Boys = len(Student.objects.filter(gender = 'M', graduated='False'))
            Girls = len(Student.objects.filter(gender = 'F', graduated='False'))
            All_total = len(Student.objects.filter(graduated='False'))
                
                
            return render(request, 'Patron/index.html', {
                "Boys": Boys,
                "Girls": Girls,
                "All_total": All_total,
            })
        else:
            return redirect(Login_User)
    else:
        return redirect(Error_login)

def cst_class_teacher(request):
    if request.user.email.endswith('cst@gmail.com'):
        
        if request.user.is_authenticated:
            Boys = len(Student.objects.filter(gender = 'M', graduated='False'))
            Girls = len(Student.objects.filter(gender = 'F', graduated='False'))
            All_total = len(Student.objects.filter(graduated='False'))
                
                
            return render(request, 'trainers/index.html', {
                "Boys": Boys,
                "Girls": Girls,
                "All_total": All_total,
            })
        else:
            return redirect(Login_User)
    else:
        return redirect(Error_login)



def rcpo_l3_class_teacher(request):
    if request.user.email.endswith('rcpol3@gmail.com'):
        
        if request.user.is_authenticated:
            Boys = len(Student.objects.filter(gender = 'M', graduated='False'))
            Girls = len(Student.objects.filter(gender = 'F', graduated='False'))
            All_total = len(Student.objects.filter(graduated='False'))
                
                
            return render(request, 'trainers/index.html', {
                "Boys": Boys,
                "Girls": Girls,
                "All_total": All_total,
            })
        else:
            return redirect(Login_User)
    else:
        return redirect(Error_login)




def rcpo_l4_class_teacher(request):
    if request.user.email.endswith('rcpol4@gmail.com'):
        
        if request.user.is_authenticated:
            Boys = len(Student.objects.filter(gender = 'M', graduated='False'))
            Girls = len(Student.objects.filter(gender = 'F', graduated='False'))
            All_total = len(Student.objects.filter(graduated='False'))
                
                
            return render(request, 'trainers/index.html', {
                "Boys": Boys,
                "Girls": Girls,
                "All_total": All_total,
            })
        else:
            return redirect(Login_User)
    else:
        return redirect(Error_login)


def rcpo_l5_class_teacher(request):
    if request.user.email.endswith('rcpol5@gmail.com'):
        
        if request.user.is_authenticated:
            Boys = len(Student.objects.filter(gender = 'M', graduated='False'))
            Girls = len(Student.objects.filter(gender = 'F', graduated='False'))
            All_total = len(Student.objects.filter(graduated='False'))
                
                
            return render(request, 'trainers/index.html', {
                "Boys": Boys,
                "Girls": Girls,
                "All_total": All_total,
            })
        else:
            return redirect(Login_User)
    else:
        return redirect(Error_login)


def ls_l3_class_teacher(request):
    if request.user.email.endswith('lsl3@gmail.com'):
        
        if request.user.is_authenticated:
            Boys = len(Student.objects.filter(gender = 'M', graduated='False'))
            Girls = len(Student.objects.filter(gender = 'F', graduated='False'))
            All_total = len(Student.objects.filter(graduated='False'))
                
                
            return render(request, 'trainers/index.html', {
                "Boys": Boys,
                "Girls": Girls,
                "All_total": All_total,
            })
        else:
            return redirect(Login_User)
    else:
        return redirect(Error_login)

def ls_l4_class_teacher(request):
    if request.user.email.endswith('lsl4@gmail.com'):
        
        if request.user.is_authenticated:
            Boys = len(Student.objects.filter(gender = 'M', graduated='False'))
            Girls = len(Student.objects.filter(gender = 'F', graduated='False'))
            All_total = len(Student.objects.filter(graduated='False'))
                
                
            return render(request, 'trainers/index.html', {
                "Boys": Boys,
                "Girls": Girls,
                "All_total": All_total,
            })
        else:
            return redirect(Login_User)
    else:
        return redirect(Error_login)


def ls_l5_class_teacher(request):
    if request.user.email.endswith('lsl5@gmail.com'):
        
        if request.user.is_authenticated:
            Boys = len(Student.objects.filter(gender = 'M', graduated='False'))
            Girls = len(Student.objects.filter(gender = 'F', graduated='False'))
            All_total = len(Student.objects.filter(graduated='False'))
                
                
            return render(request, 'trainers/index.html', {
                "Boys": Boys,
                "Girls": Girls,
                "All_total": All_total,
            })
        else:
            return redirect(Login_User)
    else:
        return redirect(Error_login)



def elec_l3_class_teacher(request):
    if request.user.email.endswith('elecl3@gmail.com'):
        
        if request.user.is_authenticated:
            Boys = len(Student.objects.filter(gender = 'M', graduated='False'))
            Girls = len(Student.objects.filter(gender = 'F', graduated='False'))
            All_total = len(Student.objects.filter(graduated='False'))
                
                
            return render(request, 'trainers/index.html', {
                "Boys": Boys,
                "Girls": Girls,
                "All_total": All_total,
            })
        else:
            return redirect(Login_User)
    else:
        return redirect(Error_login)



def elec_l4_class_teacher(request):
    if request.user.email.endswith('elecl4@gmail.com'):
        
        if request.user.is_authenticated:
            Boys = len(Student.objects.filter(gender = 'M', graduated='False'))
            Girls = len(Student.objects.filter(gender = 'F', graduated='False'))
            All_total = len(Student.objects.filter(graduated='False'))
                
                
            return render(request, 'trainers/index.html', {
                "Boys": Boys,
                "Girls": Girls,
                "All_total": All_total,
            })
        else:
            return redirect(Login_User)
    else:
        return redirect(Error_login)



def elec_l5_class_teacher(request):
    if request.user.email.endswith('elecl5@gmail.com'):
        
        if request.user.is_authenticated:
            Boys = len(Student.objects.filter(gender = 'M', graduated='False'))
            Girls = len(Student.objects.filter(gender = 'F', graduated='False'))
            All_total = len(Student.objects.filter(graduated='False'))
                
                
            return render(request, 'trainers/index.html', {
                "Boys": Boys,
                "Girls": Girls,
                "All_total": All_total,
            })
        else:
            return redirect(Login_User)
    else:
        return redirect(Error_login)



def sod_l4_class_teacher(request):
    if request.user.email.endswith('sodl4@gmail.com'):
        
        if request.user.is_authenticated:
            Boys = len(Student.objects.filter(gender = 'M', graduated='False'))
            Girls = len(Student.objects.filter(gender = 'F', graduated='False'))
            All_total = len(Student.objects.filter(graduated='False'))
                
                
            return render(request, 'trainers/index.html', {
                "Boys": Boys,
                "Girls": Girls,
                "All_total": All_total,
            })
        else:
            return redirect(Login_User)
    else:
        return redirect(Error_login)



def sod_l5_class_teacher(request):
    if request.user.email.endswith('sodl5@gmail.com'):
        
        if request.user.is_authenticated:
            Boys = len(Student.objects.filter(gender = 'M', graduated='False'))
            Girls = len(Student.objects.filter(gender = 'F', graduated='False'))
            All_total = len(Student.objects.filter(graduated='False'))
                
                
            return render(request, 'trainers/index.html', {
                "Boys": Boys,
                "Girls": Girls,
                "All_total": All_total,
            })
        else:
            return redirect(Login_User)
    else:
        return redirect(Error_login)




def Login_User(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = f'Hello {user.username}! You have been logged in'
                if request.user.is_authenticated:
                    if request.user.email.endswith('patron@gmail.com'):
                        return redirect(patron_user)
                    elif request.user.email.endswith('dos@gmail.com'):
                        return redirect(dos_user)
                    elif request.user.email.endswith('burser@gmail.com'):
                        return redirect(burser_user)
                    elif request.user.email.endswith('cst@gmail.com'):
                        return redirect(cst_class_teacher)
                    elif request.user.email.endswith('rcpol3@gmail.com'):
                        return redirect(rcpo_l3_class_teacher)
                    elif request.user.email.endswith('rcpol4@gmail.com'):
                        return redirect(rcpo_l4_class_teacher)
                    elif request.user.email.endswith('rcpol5@gmail.com'):
                        return redirect(rcpo_l5_class_teacher)
                    elif request.user.email.endswith('lsl3@gmail.com'):
                        return redirect(ls_l3_class_teacher)
                    elif request.user.email.endswith('lsl4@gmail.com'):
                        return redirect(ls_l4_class_teacher)
                    elif request.user.email.endswith('lsl5@gmail.com'):
                        return redirect(ls_l5_class_teacher)
                    elif request.user.email.endswith('elecl3@gmail.com'):
                        return redirect(elec_l3_class_teacher)
                    elif request.user.email.endswith('elecl4@gmail.com'):
                        return redirect(elec_l4_class_teacher)
                    elif request.user.email.endswith('elecl5@gmail.com'):
                        return redirect(elec_l5_class_teacher)
                    elif request.user.email.endswith('sodl4@gmail.com'):
                        return redirect(sod_l4_class_teacher)
                    elif request.user.email.endswith('sodl5@gmail.com'):
                        return redirect(sod_l5_class_teacher)
                else:
                    return redirect(Login_User)
            else:
                message = 'Email or Password is Incorrect!!'
                return render(request, 'Login/login.html', {
                    "message": message
                })
    return render(request, 'Login/login.html', {})

def logout_user(request):
    logout(request)
    return redirect(Login_User)




'''
   Start All Students List
'''

def all_p_students(request):
    if request.user.email.endswith('patron@gmail.com'):
        if request.user.is_authenticated:
            current_year = datetime.datetime.today().year
            students = Student.objects.filter(graduated='False')
            
            return render(request, 'Patron/all_p_students/all_p.html', {
                'students': students,
                'year': current_year
            })
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)
    


def add_all_p(request):
    if request.user.email.endswith('patron@gmail.com'):
        if request.user.is_authenticated:
            current_year = datetime.datetime.today().year
            trades = Trade.objects.all()
            if request.method == 'POST':
                post = Student()
                post.first_name = request.POST.get('firstname')
                post.last_name = request.POST.get('lastname')
                post.trade = request.POST.get('trade')
                post.level = request.POST.get('level')
                post.status = request.POST.get('status')
                post.dob = request.POST.get('dob')
                post.gender = request.POST.get('gender')
                post.index_no = request.POST.get('senior_3_code')
                post.father_names = request.POST.get('father_names')
                post.mother_name = request.POST.get('mother_names')
                post.father_id = request.POST.get('father_id')
                post.father_tel = request.POST.get('father_tel')
                post.mother_tel = request.POST.get('mother_tel')
                post.province = request.POST.get('province')
                post.district = request.POST.get('district')
                post.sector = request.POST.get('sector')
                post.village = request.POST.get('village')
                post.graduated = request.POST.get('graduated')
                post.start_year = request.POST.get('start_year')
                post.save()
                return redirect(all_p_students)
            return render(request, 'Patron/all_p_students/actions/add.html', {
                "trades": trades,
                "year": current_year,
            })
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)
    


def edit_all_p(request, id):

    if request.user.email.endswith('patron@gmail.com'):
        if request.user.is_authenticated:
            
            cst_l3_student_edit = get_object_or_404(Student, pk=id)
            
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    first_name = request.POST.get('firstname'),
                    last_name = request.POST.get('lastname'),
                    index_no = request.POST.get('senior_3_code'),
                    father_names = request.POST.get('father_names'),
                    mother_name = request.POST.get('mother_names'),
                    father_id = request.POST.get('father_id'),
                    father_tel = request.POST.get('father_tel'),
                    mother_tel = request.POST.get('mother_tel'),
                    province = request.POST.get('province'),
                    district = request.POST.get('district'),
                    sector = request.POST.get('sector'),
                    village = request.POST.get('village'),            
                )

                return redirect(all_p_students)
            
            return render(request, 'Patron/all_p_students/actions/edit.html', {
                "student": cst_l3_student_edit
            })
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)


def delete_all_p(request, id):
    if request.user.email.endswith('patron@gmail.com'):
        if request.user.is_authenticated:
            if request.method == 'POST':
                student = Student.objects.get(pk=id)
                student.delete()
            return HttpResponseRedirect(reverse(all_p_students))
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)




'''
   Ends All Students List
'''




''' 
   Starting of Computer Systems Technology Views -> Patron
'''

def cst_l3_p(request):
    if request.user.email.endswith('patron@gmail.com'):
        if request.user.is_authenticated:
            students = Student.objects.filter(trade = "CST", level='L3', graduated='False')
            return render(request, 'Patron/cst/l3/l3.html', {
                "students": students
            })
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)

# CST ACTIONS ADD, UPDATE, DELETE
def add_cst_l3_p(request):
    if request.user.email.endswith('patron@gmail.com'):
        if request.user.is_authenticated:
            current_year = datetime.datetime.today().year
            trades = Trade.objects.all()
            if request.method == 'POST':
                post = Student()
                post.first_name = request.POST.get('firstname')
                post.last_name = request.POST.get('lastname')
                post.trade = request.POST.get('trade')
                post.level = request.POST.get('level')
                post.status = request.POST.get('status')
                post.dob = request.POST.get('dob')
                post.gender = request.POST.get('gender')
                post.index_no = request.POST.get('senior_3_code')
                post.father_names = request.POST.get('father_names')
                post.mother_name = request.POST.get('mother_names')
                post.father_id = request.POST.get('father_id')
                post.father_tel = request.POST.get('father_tel')
                post.mother_tel = request.POST.get('mother_tel')
                post.province = request.POST.get('province')
                post.district = request.POST.get('district')
                post.sector = request.POST.get('sector')
                post.village = request.POST.get('village')
                post.graduated = request.POST.get('graduated')
                post.start_year = request.POST.get('start_year')
                post.save()
                return redirect(cst_l3_p)
                
            return render(request, 'Patron/actions/add.html', {
                "trades": trades,
                "year": current_year,
            })
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)

def view_cst_l3_p(request, id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse(cst_l3_p))

def edit_cst(request, id):
    if request.user.email.endswith('patron@gmail.com'):
        if request.user.is_authenticated:
            cst_l3_student_edit = get_object_or_404(Student, pk=id)
            
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    first_name = request.POST.get('firstname'),
                    last_name = request.POST.get('lastname'),
                    index_no = request.POST.get('senior_3_code'),
                    father_names = request.POST.get('father_names'),
                    mother_name = request.POST.get('mother_names'),
                    father_id = request.POST.get('father_id'),
                    father_tel = request.POST.get('father_tel'),
                    mother_tel = request.POST.get('mother_tel'),
                    province = request.POST.get('province'),
                    district = request.POST.get('district'),
                    sector = request.POST.get('sector'),
                    village = request.POST.get('village'),            
                )

                return redirect(cst_l3_p)
            
            return render(request, 'Patron/cst/l3/actions/edit.html', {
                "student": cst_l3_student_edit
            })
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)





def delete_cst_l3_p(request, id):
    if request.user.email.endswith('patron@gmail.com'):
        if request.user.is_authenticated:
            
            if request.method == 'POST':
                student = Student.objects.get(pk=id)
                student.delete()
            return HttpResponseRedirect(reverse(cst_l3_p))            

        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)





''' End Of Computer Systems Views '''













'''
    Begining of Road Construction & Plant Operation Views -> Patron
'''

def rcpo_l3_p(request):

    if request.user.email.endswith('patron@gmail.com'):
        if request.user.is_authenticated:
            
            students = Student.objects.filter(trade = "RCPO", level='L3', graduated='False')
            return render(request, 'Patron/rcpo/l3/l3.html', {
                "students" : students
            })            

        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)




# RCPO ACTIONS ADD, UPDATE, DELETE
def add_rcpo_l3_p(request):

    if request.user.email.endswith('patron@gmail.com'):
        if request.user.is_authenticated:
            
            trades = Trade.objects.all()
            current_year = datetime.datetime.today().year
            if request.method == 'POST':
                post = Student()
                post.first_name = request.POST.get('firstname')
                post.last_name = request.POST.get('lastname')
                post.trade = request.POST.get('trade')
                post.level = request.POST.get('level')
                post.status = request.POST.get('status')
                post.dob = request.POST.get('dob')
                post.gender = request.POST.get('gender')
                post.index_no = request.POST.get('senior_3_code')
                post.father_names = request.POST.get('father_names')
                post.mother_name = request.POST.get('mother_names')
                post.father_id = request.POST.get('father_id')
                post.father_tel = request.POST.get('father_tel')
                post.mother_tel = request.POST.get('mother_tel')
                post.province = request.POST.get('province')
                post.district = request.POST.get('district')
                post.sector = request.POST.get('sector')
                post.village = request.POST.get('village')
                post.graduated = request.POST.get('graduated')
                post.start_year = request.POST.get('start_year')
                post.save()
                return redirect(rcpo_l3_p)
            return render(request, 'Patron/rcpo/l3/actions/add.html', {
                "trades": trades,
                "year": current_year
            })            

        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)




def delete_rcpo_l3_p(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse(rcpo_l3_p))

def edit_rcpo_l3_p(request, id):
    if request.user.email.endswith('patron@gmail.com'):
        if request.user.is_authenticated:
            
            rcpo_l3_student_edit = get_object_or_404(Student, pk=id)
            
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    first_name = request.POST.get('firstname'),
                    last_name = request.POST.get('lastname'),
                    index_no = request.POST.get('senior_3_code'),
                    father_names = request.POST.get('father_names'),
                    mother_name = request.POST.get('mother_names'),
                    father_id = request.POST.get('father_id'),
                    father_tel = request.POST.get('father_tel'),
                    mother_tel = request.POST.get('mother_tel'),
                    province = request.POST.get('province'),
                    district = request.POST.get('district'),
                    sector = request.POST.get('sector'),
                    village = request.POST.get('village'),            
                )

                return redirect(rcpo_l3_p)
            return render(request, 'Patron/rcpo/l3/actions/edit.html', {
                "student": rcpo_l3_student_edit
            })
            

        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)



def rcpo_l4_p(request):

    if request.user.email.endswith('patron@gmail.com'):
        if request.user.is_authenticated:
            
            students = Student.objects.filter(trade = "RCPO", level='L4', graduated='False')
            return render(request, 'Patron/rcpo/l4/l4.html', {
                "students" : students
            })            

        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)



# RCPO ACTIONS ADD, UPDATE, DELETE
def add_rcpo_l4_p(request):
    if request.user.email.endswith('patron@gmail.com'):
        if request.user.is_authenticated:
            
            current_year = datetime.datetime.today().year
            trades = Trade.objects.all()
            if request.method == 'POST':
                post = Student()
                post.first_name = request.POST.get('firstname')
                post.last_name = request.POST.get('lastname')
                post.trade = request.POST.get('trade')
                post.level = request.POST.get('level')
                post.status = request.POST.get('status')
                post.dob = request.POST.get('dob')
                post.gender = request.POST.get('gender')
                post.index_no = request.POST.get('senior_3_code')
                post.father_names = request.POST.get('father_names')
                post.mother_name = request.POST.get('mother_names')
                post.father_id = request.POST.get('father_id')
                post.father_tel = request.POST.get('father_tel')
                post.mother_tel = request.POST.get('mother_tel')
                post.province = request.POST.get('province')
                post.district = request.POST.get('district')
                post.sector = request.POST.get('sector')
                post.village = request.POST.get('village')
                post.graduated = request.POST.get('graduated')
                post.start_year = request.POST.get('start_year')
                post.save()
                return redirect(rcpo_l4_p)
            return render(request, 'Patron/rcpo/l4/actions/add.html', {
                "trades": trades,
                "year": current_year
            })            

        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)



def delete_rcpo_l4_p(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse(rcpo_l4_p))

def edit_rcpo_l4_p(request, id):
    if request.user.email.endswith('patron@gmail.com'):
        if request.user.is_authenticated:
            
            rcpo_l4_student_edit = get_object_or_404(Student, pk=id)
            
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    first_name = request.POST.get('firstname'),
                    last_name = request.POST.get('lastname'),
                    index_no = request.POST.get('senior_3_code'),
                    father_names = request.POST.get('father_names'),
                    mother_name = request.POST.get('mother_names'),
                    father_id = request.POST.get('father_id'),
                    father_tel = request.POST.get('father_tel'),
                    mother_tel = request.POST.get('mother_tel'),
                    province = request.POST.get('province'),
                    district = request.POST.get('district'),
                    sector = request.POST.get('sector'),
                    village = request.POST.get('village'),            
                )

                return redirect(rcpo_l4_p)
            return render(request, 'Patron/rcpo/l4/actions/edit.html', {
                "student": rcpo_l4_student_edit
            })            

        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)






def rcpo_l5_p(request):
    if request.user.email.endswith('patron@gmail.com'):
        if request.user.is_authenticated:
            
            students = Student.objects.filter(trade = "RCPO", level='L5', graduated='False')
            return render(request, 'Patron/rcpo/l5/l5.html', {
                "students": students
            })            

        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)



# RCPO ACTIONS ADD, UPDATE, DELETE

def add_rcpo_l5_p(request):
    if request.user.email.endswith('patron@gmail.com'):
        if request.user.is_authenticated:
            
            current_year = datetime.datetime.today().year
            trades = Trade.objects.all()
            if request.method == 'POST':
                post = Student()
                post.first_name = request.POST.get('firstname')
                post.last_name = request.POST.get('lastname')
                post.trade = request.POST.get('trade')
                post.level = request.POST.get('level')
                post.status = request.POST.get('status')
                post.dob = request.POST.get('dob')
                post.gender = request.POST.get('gender')
                post.index_no = request.POST.get('senior_3_code')
                post.father_names = request.POST.get('father_names')
                post.mother_name = request.POST.get('mother_names')
                post.father_id = request.POST.get('father_id')
                post.father_tel = request.POST.get('father_tel')
                post.mother_tel = request.POST.get('mother_tel')
                post.province = request.POST.get('province')
                post.district = request.POST.get('district')
                post.sector = request.POST.get('sector')
                post.village = request.POST.get('village')
                post.graduated = request.POST.get('graduated')
                post.start_year = request.POST.get('start_year')
                post.save()
                return redirect(rcpo_l5_p)
            return render(request, 'Patron/rcpo/l5/actions/add.html', {
                "trades": trades,
                "year": current_year,
            })            

        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)


def delete_rcpo_l5_p(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse(rcpo_l5_p))

def edit_rcpo_l5_p(request, id):
    if request.user.email.endswith('patron@gmail.com'):
        if request.user.is_authenticated:
            
            rcpo_l5_student_edit = get_object_or_404(Student, pk=id)
            
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    first_name = request.POST.get('firstname'),
                    last_name = request.POST.get('lastname'),
                    index_no = request.POST.get('senior_3_code'),
                    father_names = request.POST.get('father_names'),
                    mother_name = request.POST.get('mother_names'),
                    father_id = request.POST.get('father_id'),
                    father_tel = request.POST.get('father_tel'),
                    mother_tel = request.POST.get('mother_tel'),
                    province = request.POST.get('province'),
                    district = request.POST.get('district'),
                    sector = request.POST.get('sector'),
                    village = request.POST.get('village'),            
                )

                return redirect(rcpo_l5_p)
            return render(request, 'Patron/rcpo/l5/actions/edit.html', {
                "student": rcpo_l5_student_edit
            })
            

        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)





''' End of Road Construction & Plant Operation '''















'''
    Begining of Land Surveying Views -> Patron
'''

def ls_l3_p(request):
    if request.user.email.endswith('patron@gmail.com'):
        if request.user.is_authenticated:
            
            students = Student.objects.filter(trade = "LS", level='L3', graduated='False')
            return render(request, 'Patron/ls/l3/l3.html', {
                "students": students
            })            

        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)


# LAND SURVEYING ACTIONS ADD, UPDATE, DELETE
def add_ls_l3_p(request):

    if request.user.email.endswith('patron@gmail.com'):
        if request.user.is_authenticated:
            
            trades = Trade.objects.all()
            current_year = datetime.datetime.today().year
            if request.method == 'POST':
                post = Student()
                post.first_name = request.POST.get('firstname')
                post.last_name = request.POST.get('lastname')
                post.trade = request.POST.get('trade')
                post.level = request.POST.get('level')
                post.status = request.POST.get('status')
                post.dob = request.POST.get('dob')
                post.gender = request.POST.get('gender')
                post.index_no = request.POST.get('senior_3_code')
                post.father_names = request.POST.get('father_names')
                post.mother_name = request.POST.get('mother_names')
                post.father_id = request.POST.get('father_id')
                post.father_tel = request.POST.get('father_tel')
                post.mother_tel = request.POST.get('mother_tel')
                post.province = request.POST.get('province')
                post.district = request.POST.get('district')
                post.sector = request.POST.get('sector')
                post.village = request.POST.get('village')
                post.graduated = request.POST.get('graduated')
                post.start_year = request.POST.get('start_year')
                post.save()
                return redirect(ls_l3_p)
            return render(request, 'Patron/ls/l3/actions/add.html', {
                "trades": trades,
                "year": current_year,
            })          

        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)



def delete_ls_l3_p(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse(ls_l3_p))

def edit_ls_l3_p(request, id):
    if request.user.email.endswith('patron@gmail.com'):
        if request.user.is_authenticated:
            
            ls_l3_student_edit = get_object_or_404(Student, pk=id)
            
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    first_name = request.POST.get('firstname'),
                    last_name = request.POST.get('lastname'),
                    index_no = request.POST.get('senior_3_code'),
                    father_names = request.POST.get('father_names'),
                    mother_name = request.POST.get('mother_names'),
                    father_id = request.POST.get('father_id'),
                    father_tel = request.POST.get('father_tel'),
                    mother_tel = request.POST.get('mother_tel'),
                    province = request.POST.get('province'),
                    district = request.POST.get('district'),
                    sector = request.POST.get('sector'),
                    village = request.POST.get('village'),            
                )

                return redirect(ls_l3_p)
            return render(request, 'Patron/ls/l3/actions/edit.html', {
                "student": ls_l3_student_edit
            })            

        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)




def ls_l4_p(request):
    if request.user.email.endswith('patron@gmail.com'):
        if request.user.is_authenticated:
            
            students = Student.objects.filter(trade = "LS", level='L4', graduated='False')
            return render(request, 'Patron/ls/l4/l4.html', {
                "students": students
            })            

        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)


# LAND SURVEYING ACTIONS ADD, UPDATE, DELETE
def add_ls_l4_p(request):
    if request.user.email.endswith('patron@gmail.com'):
        if request.user.is_authenticated:
            
            trades = Trade.objects.all()
            current_year = datetime.datetime.today().year
            if request.method == 'POST':
                post = Student()
                post.first_name = request.POST.get('firstname')
                post.last_name = request.POST.get('lastname')
                post.trade = request.POST.get('trade')
                post.level = request.POST.get('level')
                post.status = request.POST.get('status')
                post.dob = request.POST.get('dob')
                post.gender = request.POST.get('gender')
                post.index_no = request.POST.get('senior_3_code')
                post.father_names = request.POST.get('father_names')
                post.mother_name = request.POST.get('mother_names')
                post.father_id = request.POST.get('father_id')
                post.father_tel = request.POST.get('father_tel')
                post.mother_tel = request.POST.get('mother_tel')
                post.province = request.POST.get('province')
                post.district = request.POST.get('district')
                post.sector = request.POST.get('sector')
                post.village = request.POST.get('village')
                post.graduated = request.POST.get('graduated')
                post.start_year = request.POST.get('start_year')
                post.save()
                return redirect(ls_l4_p)
            return render(request, 'Patron/ls/l4/actions/add.html', {
                "trades": trades,
                "year": current_year
            })            

        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)


def delete_ls_l4_p(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse(ls_l4_p))

def edit_ls_l4_p(request, id):
    if request.user.email.endswith('patron@gmail.com'):
        if request.user.is_authenticated:
            
            ls_l4_student_edit = get_object_or_404(Student, pk=id)
            
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    first_name = request.POST.get('firstname'),
                    last_name = request.POST.get('lastname'),
                    index_no = request.POST.get('senior_3_code'),
                    father_names = request.POST.get('father_names'),
                    mother_name = request.POST.get('mother_names'),
                    father_id = request.POST.get('father_id'),
                    father_tel = request.POST.get('father_tel'),
                    mother_tel = request.POST.get('mother_tel'),
                    province = request.POST.get('province'),
                    district = request.POST.get('district'),
                    sector = request.POST.get('sector'),
                    village = request.POST.get('village'),            
                )

                return redirect(ls_l4_p)
            return render(request, 'Patron/ls/l4/actions/edit.html', {
                "student": ls_l4_student_edit
            })
            

        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)






def ls_l5_p(request):
    if request.user.email.endswith('patron@gmail.com'):
        if request.user.is_authenticated:
            
            students = Student.objects.filter(trade = "LS", level='L5', graduated='False')
            return render(request, 'Patron/ls/l5/l5.html', {
                "students": students
            })            

        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)


# LAND SURVEYING ACTIONS ADD, UPDATE, DELETE
def add_ls_l5_p(request):

    if request.user.email.endswith('patron@gmail.com'):
        if request.user.is_authenticated:
            
            current_year = datetime.datetime.today().year
            trades = Trade.objects.all()
            if request.method == 'POST':
                post = Student()
                post.first_name = request.POST.get('firstname')
                post.last_name = request.POST.get('lastname')
                post.trade = request.POST.get('trade')
                post.level = request.POST.get('level')
                post.status = request.POST.get('status')
                post.dob = request.POST.get('dob')
                post.gender = request.POST.get('gender')
                post.index_no = request.POST.get('senior_3_code')
                post.father_names = request.POST.get('father_names')
                post.mother_name = request.POST.get('mother_names')
                post.father_id = request.POST.get('father_id')
                post.father_tel = request.POST.get('father_tel')
                post.mother_tel = request.POST.get('mother_tel')
                post.province = request.POST.get('province')
                post.district = request.POST.get('district')
                post.sector = request.POST.get('sector')
                post.village = request.POST.get('village')
                post.graduated = request.POST.get('graduated')
                post.start_year = request.POST.get('start_year')
                post.save()
                return redirect(ls_l5_p)
            return render(request, 'Patron/ls/l5/actions/add.html', {
                "trades": trades, 
                "year": current_year,
            })            

        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)


def delete_ls_l5_p(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse(ls_l5_p))

def edit_ls_l5_p(request, id):

    if request.user.email.endswith('patron@gmail.com'):
        if request.user.is_authenticated:
            
            ls_l5_student_edit = get_object_or_404(Student, pk=id)
            
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    first_name = request.POST.get('firstname'),
                    last_name = request.POST.get('lastname'),
                    index_no = request.POST.get('senior_3_code'),
                    father_names = request.POST.get('father_names'),
                    mother_name = request.POST.get('mother_names'),
                    father_id = request.POST.get('father_id'),
                    father_tel = request.POST.get('father_tel'),
                    mother_tel = request.POST.get('mother_tel'),
                    province = request.POST.get('province'),
                    district = request.POST.get('district'),
                    sector = request.POST.get('sector'),
                    village = request.POST.get('village'),            
                )

                return redirect(ls_l5_p)
            return render(request, 'Patron/ls/l5/actions/edit.html', {
                "student": ls_l5_student_edit
            })            

        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)






''' End of Land Surveying Views '''









'''
    Begining of Electricity Views -> Patron
'''

def elec_l3_p(request):
    if request.user.email.endswith('patron@gmail.com'):
        if request.user.is_authenticated:
            
            students = Student.objects.filter(trade = "ELEC", level='L3', graduated='False')
            return render(request, 'Patron/elec/l3/l3.html', {
                "students": students
            })            

        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)


# ELECTRICITY ACTIONS ADD, UPDATE, DELETE
def add_elec_l3_p(request):

    if request.user.email.endswith('patron@gmail.com'):
        if request.user.is_authenticated:
            
            current_year = datetime.datetime.today().year
            trades = Trade.objects.all()
            if request.method == 'POST':
                post = Student()
                post.first_name = request.POST.get('firstname')
                post.last_name = request.POST.get('lastname')
                post.trade = request.POST.get('trade')
                post.level = request.POST.get('level')
                post.status = request.POST.get('status')
                post.dob = request.POST.get('dob')
                post.gender = request.POST.get('gender')
                post.index_no = request.POST.get('senior_3_code')
                post.father_names = request.POST.get('father_names')
                post.mother_name = request.POST.get('mother_names')
                post.father_id = request.POST.get('father_id')
                post.father_tel = request.POST.get('father_tel')
                post.mother_tel = request.POST.get('mother_tel')
                post.province = request.POST.get('province')
                post.district = request.POST.get('district')
                post.sector = request.POST.get('sector')
                post.village = request.POST.get('village')
                post.graduated = request.POST.get('graduated')
                post.start_year = request.POST.get('start_year')
                post.save()
                return redirect(elec_l3_p)
            return render(request, 'Patron/elec/l3/actions/add.html', {
                "trades": trades,
                "year": current_year
            })            

        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)



def delete_elec_l3_p(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse(elec_l3_p))

def edit_elec_l3_p(request, id):
    if request.user.email.endswith('patron@gmail.com'):
        if request.user.is_authenticated:
            
            elec_l3_student_edit = get_object_or_404(Student, pk=id)
            
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    first_name = request.POST.get('firstname'),
                    last_name = request.POST.get('lastname'),
                    index_no = request.POST.get('senior_3_code'),
                    father_names = request.POST.get('father_names'),
                    mother_name = request.POST.get('mother_names'),
                    father_id = request.POST.get('father_id'),
                    father_tel = request.POST.get('father_tel'),
                    mother_tel = request.POST.get('mother_tel'),
                    province = request.POST.get('province'),
                    district = request.POST.get('district'),
                    sector = request.POST.get('sector'),
                    village = request.POST.get('village'),            
                )

                return redirect(elec_l3_p)
            return render(request, 'Patron/elec/l3/actions/edit.html', {
                "student": elec_l3_student_edit
            })
            

        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)





def elec_l4_p(request):

    if request.user.email.endswith('patron@gmail.com'):
        if request.user.is_authenticated:
            
            students = Student.objects.filter(trade = "ELEC", level='L4', graduated='False')
            return render(request, 'Patron/elec/l4/l4.html', {
                "students": students
            })            

        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)



# ELECTRICITY ACTIONS ADD, UPDATE, DELETE
def add_elec_l4_p(request):

    if request.user.email.endswith('patron@gmail.com'):
        if request.user.is_authenticated:
            
            trades = Trade.objects.all()
            current_year = datetime.datetime.today().year
            if request.method == 'POST':
                post = Student()
                post.first_name = request.POST.get('firstname')
                post.last_name = request.POST.get('lastname')
                post.trade = request.POST.get('trade')
                post.level = request.POST.get('level')
                post.status = request.POST.get('status')
                post.dob = request.POST.get('dob')
                post.gender = request.POST.get('gender')
                post.index_no = request.POST.get('senior_3_code')
                post.father_names = request.POST.get('father_names')
                post.mother_name = request.POST.get('mother_names')
                post.father_id = request.POST.get('father_id')
                post.father_tel = request.POST.get('father_tel')
                post.mother_tel = request.POST.get('mother_tel')
                post.province = request.POST.get('province')
                post.district = request.POST.get('district')
                post.sector = request.POST.get('sector')
                post.village = request.POST.get('village')
                post.graduated = request.POST.get('graduated')
                post.start_year = request.POST.get('start_year')
                post.save()
                return redirect(elec_l4_p)
            return render(request, 'Patron/ls/l4/actions/add.html', {
                "trades": trades,
                "year": current_year
            })            

        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)



def delete_elec_l4_p(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse(elec_l4_p))

def edit_elec_l4_p(request, id):
    if request.user.email.endswith('patron@gmail.com'):
        if request.user.is_authenticated:
            
            elec_l4_student_edit = get_object_or_404(Student, pk=id)
            
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    first_name = request.POST.get('firstname'),
                    last_name = request.POST.get('lastname'),
                    index_no = request.POST.get('senior_3_code'),
                    father_names = request.POST.get('father_names'),
                    mother_name = request.POST.get('mother_names'),
                    father_id = request.POST.get('father_id'),
                    father_tel = request.POST.get('father_tel'),
                    mother_tel = request.POST.get('mother_tel'),
                    province = request.POST.get('province'),
                    district = request.POST.get('district'),
                    sector = request.POST.get('sector'),
                    village = request.POST.get('village'),            
                )

                return redirect(elec_l4_p)
            return render(request, 'Patron/elec/l4/actions/edit.html', {
                "student": elec_l4_student_edit
            })            

        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)
    




def elec_l5_p(request):
    if request.user.email.endswith('patron@gmail.com'):
        if request.user.is_authenticated:
            
            students = Student.objects.filter(trade = "ELEC", level='L5', graduated='False')
            return render(request, 'Patron/elec/l5/l5.html', {
                "students": students
            })            

        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)


# ELECTRICITY ACTIONS ADD, UPDATE, DELETE

def add_elec_l5_p(request):
    if request.user.email.endswith('patron@gmail.com'):
        if request.user.is_authenticated:
            
            current_year = datetime.datetime.today().year
            trades = Trade.objects.all()
            if request.method == 'POST':
                post = Student()
                post.first_name = request.POST.get('firstname')
                post.last_name = request.POST.get('lastname')
                post.trade = request.POST.get('trade')
                post.level = request.POST.get('level')
                post.status = request.POST.get('status')
                post.dob = request.POST.get('dob')
                post.gender = request.POST.get('gender')
                post.index_no = request.POST.get('senior_3_code')
                post.father_names = request.POST.get('father_names')
                post.mother_name = request.POST.get('mother_names')
                post.father_id = request.POST.get('father_id')
                post.father_tel = request.POST.get('father_tel')
                post.mother_tel = request.POST.get('mother_tel')
                post.province = request.POST.get('province')
                post.district = request.POST.get('district')
                post.sector = request.POST.get('sector')
                post.village = request.POST.get('village')
                post.graduated = request.POST.get('graduated')
                post.start_year = request.POST.get('start_year')
                post.save()
                return redirect(elec_l5_p)
            return render(request, 'Patron/elec/l5/actions/add.html', {
                "trades": trades,
                "year": current_year
            })            

        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)




def delete_elec_l5_p(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse(elec_l5_p))

def edit_elec_l5_p(request, id):

    if request.user.email.endswith('patron@gmail.com'):
        if request.user.is_authenticated:
            
            elec_l5_student_edit = get_object_or_404(Student, pk=id)
            
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    first_name = request.POST.get('firstname'),
                    last_name = request.POST.get('lastname'),
                    index_no = request.POST.get('senior_3_code'),
                    father_names = request.POST.get('father_names'),
                    mother_name = request.POST.get('mother_names'),
                    father_id = request.POST.get('father_id'),
                    father_tel = request.POST.get('father_tel'),
                    mother_tel = request.POST.get('mother_tel'),
                    province = request.POST.get('province'),
                    district = request.POST.get('district'),
                    sector = request.POST.get('sector'),
                    village = request.POST.get('village'),            
                )

                return redirect(elec_l5_p)
            return render(request, 'Patron/elec/l5/actions/edit.html', {
                "student": elec_l5_student_edit
            })            

        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)



''' End of Electricity Views '''
















'''
    Begining of Software Development Views -> Patron
'''


def sod_l4_p(request):
    if request.user.email.endswith('patron@gmail.com'):
        if request.user.is_authenticated:
            
            students = Student.objects.filter(trade = "SOD", level='L4', graduated='False')
            return render(request, 'Patron/sod/l4/l4.html', {
                "students": students
            })            

        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)


# SOFTWARE DEVELOPMENT ACTIONS ADD, UPDATE, DELETE

def add_sod_l4_p(request):
    if request.user.email.endswith('patron@gmail.com'):
        if request.user.is_authenticated:
            
            current_year = datetime.datetime.today().year
            trades = Trade.objects.all()
            if request.method == 'POST':
                post = Student()
                post.first_name = request.POST.get('firstname')
                post.last_name = request.POST.get('lastname')
                post.trade = request.POST.get('trade')
                post.level = request.POST.get('level')
                post.status = request.POST.get('status')
                post.dob = request.POST.get('dob')
                post.gender = request.POST.get('gender')
                post.index_no = request.POST.get('senior_3_code')
                post.father_names = request.POST.get('father_names')
                post.mother_name = request.POST.get('mother_names')
                post.father_id = request.POST.get('father_id')
                post.father_tel = request.POST.get('father_tel')
                post.mother_tel = request.POST.get('mother_tel')
                post.province = request.POST.get('province')
                post.district = request.POST.get('district')
                post.sector = request.POST.get('sector')
                post.village = request.POST.get('village')
                post.graduated = request.POST.get('graduated')
                post.start_year = request.POST.get('start_year')
                post.save()
                return redirect(sod_l4_p)
            return render(request, 'Patron/sod/l4/actions/add.html', {
                "trades": trades,
                "year": current_year
            })            

        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)


def delete_sod_l4_p(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse(sod_l4_p))

def edit_sod_l4_p(request, id):
    if request.user.email.endswith('patron@gmail.com'):
        if request.user.is_authenticated:
            
            sod_l4_student_edit = get_object_or_404(Student, pk=id)
            
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    first_name = request.POST.get('firstname'),
                    last_name = request.POST.get('lastname'),
                    index_no = request.POST.get('senior_3_code'),
                    father_names = request.POST.get('father_names'),
                    mother_name = request.POST.get('mother_names'),
                    father_id = request.POST.get('father_id'),
                    father_tel = request.POST.get('father_tel'),
                    mother_tel = request.POST.get('mother_tel'),
                    province = request.POST.get('province'),
                    district = request.POST.get('district'),
                    sector = request.POST.get('sector'),
                    village = request.POST.get('village'),            
                )

                return redirect(sod_l4_p)
            return render(request, 'Patron/sod/l4/actions/edit.html', {
                "student": sod_l4_student_edit
            })            

        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)




def sod_l5_p(request):
    if request.user.email.endswith('patron@gmail.com'):
        if request.user.is_authenticated:
            
            students = Student.objects.filter(trade = "SOD", level='L5', graduated='False')
            return render(request, 'Patron/sod/l5/l5.html', {
                "students": students
            })            

        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)


# ELECTRICITY ACTIONS ADD, UPDATE, DELETE
def add_sod_l5_p(request):
    if request.user.email.endswith('patron@gmail.com'):
        if request.user.is_authenticated:
            
            current_year = datetime.datetime.today().year
            trades = Trade.objects.all()
            if request.method == 'POST':
                post = Student()
                post.first_name = request.POST.get('firstname')
                post.last_name = request.POST.get('lastname')
                post.trade = request.POST.get('trade')
                post.level = request.POST.get('level')
                post.status = request.POST.get('status')
                post.dob = request.POST.get('dob')
                post.gender = request.POST.get('gender')
                post.index_no = request.POST.get('senior_3_code')
                post.father_names = request.POST.get('father_names')
                post.mother_name = request.POST.get('mother_names')
                post.father_id = request.POST.get('father_id')
                post.father_tel = request.POST.get('father_tel')
                post.mother_tel = request.POST.get('mother_tel')
                post.province = request.POST.get('province')
                post.district = request.POST.get('district')
                post.sector = request.POST.get('sector')
                post.village = request.POST.get('village')
                post.graduated = request.POST.get('graduated')
                post.start_year = request.POST.get('start_year')
                post.save()
                return redirect(sod_l5_p)
            return render(request, 'Patron/sod/l5/actions/add.html', {
                "trades": trades,
                "year": current_year,
            })            

        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)


def delete_sod_l5_p(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse(sod_l5_p))

def edit_sod_l5_p(request, id):

    if request.user.email.endswith('patron@gmail.com'):
        if request.user.is_authenticated:

            sod_l5_student_edit = get_object_or_404(Student, pk=id)
            
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    first_name = request.POST.get('firstname'),
                    last_name = request.POST.get('lastname'),
                    index_no = request.POST.get('senior_3_code'),
                    father_names = request.POST.get('father_names'),
                    mother_name = request.POST.get('mother_names'),
                    father_id = request.POST.get('father_id'),
                    father_tel = request.POST.get('father_tel'),
                    mother_tel = request.POST.get('mother_tel'),
                    province = request.POST.get('province'),
                    district = request.POST.get('district'),
                    sector = request.POST.get('sector'),
                    village = request.POST.get('village'),            
                )

                return redirect(sod_l5_p)
            return render(request, 'Patron/sod/l5/actions/edit.html', {
                "student": sod_l5_student_edit
            })
            

        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)




''' End of Software Development Views '''

















'''

THIS IS DIRECTOR OF STUDIES VIEWS



'''








'''
   Start All Students List
'''

def graduates_d(request):
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            
            students = Student.objects.filter(graduated='True')
            current_year = datetime.datetime.today().year
            gr_yrs = Graduate_year.objects.all()
            
                    
            return render(request, 'dos/Graduates/index.html', {
                "year":current_year,
                "gr_yrs": gr_yrs,
                "students": students,
            })            

        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)


def all_d_students(request):
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            current_year = datetime.datetime.today().year
            students = Student.objects.filter(graduated='False')
            
            return render(request, 'dos/all_d_students/all_p.html', {
                'students': students,
                'year': current_year
            })            

        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)
    



def add_all_d(request):
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            
            current_year = datetime.datetime.today().year
            trades = Trade.objects.all()
            if request.method == 'POST':
                post = Student()
                post.first_name = request.POST.get('firstname')
                post.last_name = request.POST.get('lastname')
                post.trade = request.POST.get('trade')
                post.level = request.POST.get('level')
                post.status = request.POST.get('status')
                post.dob = request.POST.get('dob')
                post.gender = request.POST.get('gender')
                post.index_no = request.POST.get('senior_3_code')
                post.father_names = request.POST.get('father_names')
                post.mother_name = request.POST.get('mother_names')
                post.father_id = request.POST.get('father_id')
                post.father_tel = request.POST.get('father_tel')
                post.mother_tel = request.POST.get('mother_tel')
                post.province = request.POST.get('province')
                post.district = request.POST.get('district')
                post.sector = request.POST.get('sector')
                post.village = request.POST.get('village')
                post.graduated = request.POST.get('graduated')
                post.start_year = request.POST.get('start_year')
                post.save()
                return redirect(all_d_students)
                
            return render(request, 'dos/all_d_students/actions/add.html', {
                "trades": trades,
                "year": current_year,
            })

        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)




def edit_all_d(request, id):
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            
            cst_l3_student_edit = get_object_or_404(Student, pk=id)
            
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    first_name = request.POST.get('firstname'),
                    last_name = request.POST.get('lastname'),
                    index_no = request.POST.get('senior_3_code'),
                    father_names = request.POST.get('father_names'),
                    mother_name = request.POST.get('mother_names'),
                    father_id = request.POST.get('father_id'),
                    father_tel = request.POST.get('father_tel'),
                    mother_tel = request.POST.get('mother_tel'),
                    province = request.POST.get('province'),
                    district = request.POST.get('district'),
                    sector = request.POST.get('sector'),
                    village = request.POST.get('village'),            
                )

                return redirect(all_d_students)
            
            return render(request, 'dos/all_d_students/actions/edit.html', {
                "student": cst_l3_student_edit
            })            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)

    
def delete_all_d(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse(all_d_students))




'''
   Ends All Students List
'''



  
''' 
   Starting of Computer Systems Technology Views -> Dos
'''

def cst_l3_d(request):
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            trades = Trade.objects.all()
            students = Student.objects.filter(trade = "CST", level='L3', graduated='False')
            return render(request, 'dos/cst/l3/l3.html', {
                "students": students,
                "trades": trades,
            })
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)


# CST ACTIONS ADD, UPDATE, DELETE
def add_cst_l3_d(request):
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            current_year = datetime.datetime.today().year
            trades = Trade.objects.all()
            if request.method == 'POST':
                post = Student()
                post.first_name = request.POST.get('firstname')
                post.last_name = request.POST.get('lastname')
                post.trade = request.POST.get('trade')
                post.level = request.POST.get('level')
                post.status = request.POST.get('status')
                post.dob = request.POST.get('dob')
                post.gender = request.POST.get('gender')
                post.index_no = request.POST.get('senior_3_code')
                post.father_names = request.POST.get('father_names')
                post.mother_name = request.POST.get('mother_names')
                post.father_id = request.POST.get('father_id')
                post.father_tel = request.POST.get('father_tel')
                post.mother_tel = request.POST.get('mother_tel')
                post.province = request.POST.get('province')
                post.district = request.POST.get('district')
                post.sector = request.POST.get('sector')
                post.village = request.POST.get('village')
                post.graduated = request.POST.get('graduated')
                post.start_year = request.POST.get('start_year')
                post.save()
                return redirect(cst_l3_d)
                
            return render(request, 'dos/all_d_students/actions/add.html', {
                "trades": trades,
                "year": current_year
            })            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)


def view_cst_l3_d(request, id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse(cst_l3_d))

def edit_cst_d(request, id):
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            
            cst_l3_student_edit = get_object_or_404(Student, pk=id)
            
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    first_name = request.POST.get('firstname'),
                    last_name = request.POST.get('lastname'),
                    index_no = request.POST.get('senior_3_code'),
                    father_names = request.POST.get('father_names'),
                    mother_name = request.POST.get('mother_names'),
                    father_id = request.POST.get('father_id'),
                    father_tel = request.POST.get('father_tel'),
                    mother_tel = request.POST.get('mother_tel'),
                    province = request.POST.get('province'),
                    district = request.POST.get('district'),
                    sector = request.POST.get('sector'),
                    village = request.POST.get('village'),            
                )

                return redirect(cst_l3_d)
            
            return render(request, 'dos/cst/l3/actions/edit.html', {
                "student": cst_l3_student_edit
            })            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    

def delete_cst_l3_d(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse(cst_l3_d))

def promote_cst_l3_d(request, id): 
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    trade = request.POST.get('trade'),
                    level = request.POST.get('level'),
                )
                return HttpResponseRedirect(reverse(cst_l3_d))            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)     


def change_cst_l3_d(request, id):  
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    trade = request.POST.get('trade'),
                    level = request.POST.get('level'),
                )
                return HttpResponseRedirect(reverse(cst_l3_d))
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    


    

    

''' End Of Computer Systems Views '''













'''
    Begining of Road Construction & Plant Operation Views -> Patron
'''

def rcpo_l3_d(request):
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            
            trades = Trade.objects.all()
            students = Student.objects.filter(trade = "RCPO", level='L3', graduated='False')
            return render(request, 'dos/rcpo/l3/l3.html', {
                "students" : students, 
                "trades": trades,
            })            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    



# RCPO ACTIONS ADD, UPDATE, DELETE
def add_rcpo_l3_d(request):

    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            current_year = datetime.datetime.today().year
            trades = Trade.objects.all()
            if request.method == 'POST':
                post = Student()
                post.first_name = request.POST.get('firstname')
                post.last_name = request.POST.get('lastname')
                post.trade = request.POST.get('trade')
                post.level = request.POST.get('level')
                post.status = request.POST.get('status')
                post.dob = request.POST.get('dob')
                post.gender = request.POST.get('gender')
                post.index_no = request.POST.get('senior_3_code')
                post.father_names = request.POST.get('father_names')
                post.mother_name = request.POST.get('mother_names')
                post.father_id = request.POST.get('father_id')
                post.father_tel = request.POST.get('father_tel')
                post.mother_tel = request.POST.get('mother_tel')
                post.province = request.POST.get('province')
                post.district = request.POST.get('district')
                post.sector = request.POST.get('sector')
                post.village = request.POST.get('village')
                post.graduated = request.POST.get('graduated')
                post.start_year = request.POST.get('start_year')
                post.save()
                return redirect(rcpo_l3_d)
            return render(request, 'dos/rcpo/l3/actions/add.html', {
                "trades": trades,
                "year": current_year,
            })            
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    



def delete_rcpo_l3_d(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse(rcpo_l3_d))

def edit_rcpo_l3_d(request, id):
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            rcpo_l3_student_edit = get_object_or_404(Student, pk=id)
            
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    first_name = request.POST.get('firstname'),
                    last_name = request.POST.get('lastname'),
                    index_no = request.POST.get('senior_3_code'),
                    father_names = request.POST.get('father_names'),
                    mother_name = request.POST.get('mother_names'),
                    father_id = request.POST.get('father_id'),
                    father_tel = request.POST.get('father_tel'),
                    mother_tel = request.POST.get('mother_tel'),
                    province = request.POST.get('province'),
                    district = request.POST.get('district'),
                    sector = request.POST.get('sector'),
                    village = request.POST.get('village'),            
                )

                return redirect(rcpo_l3_d)
            return render(request, 'dos/rcpo/l3/actions/edit.html', {
                "student": rcpo_l3_student_edit
            })            
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    



def promote_rcpo_l3_d(request, id):  
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    trade = request.POST.get('trade'),
                    level = request.POST.get('level'),
                )
                return HttpResponseRedirect(reverse(rcpo_l3_d))
            
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)

def change_rcpo_l3_d(request, id):  
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    trade = request.POST.get('trade'),
                    level = request.POST.get('level'),
                )
                return HttpResponseRedirect(reverse(rcpo_l3_d))            
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)



   



def rcpo_l4_d(request):
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            students = Student.objects.filter(trade = "RCPO", level='L4', graduated='False')
            return render(request, 'dos/rcpo/l4/l4.html', {
                "students" : students
            })            
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    


# RCPO ACTIONS ADD, UPDATE, DELETE
def add_rcpo_l4_d(request):
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            current_year = datetime.datetime.today().year
            trades = Trade.objects.all()
            if request.method == 'POST':
                post = Student()
                post.first_name = request.POST.get('firstname')
                post.last_name = request.POST.get('lastname')
                post.trade = request.POST.get('trade')
                post.level = request.POST.get('level')
                post.status = request.POST.get('status')
                post.dob = request.POST.get('dob')
                post.gender = request.POST.get('gender')
                post.index_no = request.POST.get('senior_3_code')
                post.father_names = request.POST.get('father_names')
                post.mother_name = request.POST.get('mother_names')
                post.father_id = request.POST.get('father_id')
                post.father_tel = request.POST.get('father_tel')
                post.mother_tel = request.POST.get('mother_tel')
                post.province = request.POST.get('province')
                post.district = request.POST.get('district')
                post.sector = request.POST.get('sector')
                post.village = request.POST.get('village')
                post.graduated = request.POST.get('graduated')
                post.start_year = request.POST.get('start_year')
                post.save()
                return redirect(rcpo_l4_d)
            return render(request, 'dos/rcpo/l4/actions/add.html', {
                "trades": trades,
                "year": current_year
            })            
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)


def delete_rcpo_l4_d(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse(rcpo_l4_d))

def edit_rcpo_l4_d(request, id):
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            rcpo_l4_student_edit = get_object_or_404(Student, pk=id)
            
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    first_name = request.POST.get('firstname'),
                    last_name = request.POST.get('lastname'),
                    index_no = request.POST.get('senior_3_code'),
                    father_names = request.POST.get('father_names'),
                    mother_name = request.POST.get('mother_names'),
                    father_id = request.POST.get('father_id'),
                    father_tel = request.POST.get('father_tel'),
                    mother_tel = request.POST.get('mother_tel'),
                    province = request.POST.get('province'),
                    district = request.POST.get('district'),
                    sector = request.POST.get('sector'),
                    village = request.POST.get('village'),            
                )

                return redirect(rcpo_l4_d)
            return render(request, 'dos/rcpo/l4/actions/edit.html', {
                "student": rcpo_l4_student_edit
            })            
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)


def promote_rcpo_l4_d(request, id):  
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    trade = request.POST.get('trade'),
                    level = request.POST.get('level'),
                )
                return HttpResponseRedirect(reverse(rcpo_l4_d))            
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)






def rcpo_l5_d(request):
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            current_year = datetime.datetime.today().year
            students = Student.objects.filter(trade = "RCPO", level='L5', graduated='False')
            return render(request, 'dos/rcpo/l5/l5.html', {
                "students": students,
                "year": current_year,
            })            
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    



# RCPO ACTIONS ADD, UPDATE, DELETE

def add_rcpo_l5_d(request):
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:

            current_year = datetime.datetime.today().year
            trades = Trade.objects.all()
            if request.method == 'POST':
                post = Student()
                post.first_name = request.POST.get('firstname')
                post.last_name = request.POST.get('lastname')
                post.trade = request.POST.get('trade')
                post.level = request.POST.get('level')
                post.status = request.POST.get('status')
                post.dob = request.POST.get('dob')
                post.gender = request.POST.get('gender')
                post.index_no = request.POST.get('senior_3_code')
                post.father_names = request.POST.get('father_names')
                post.mother_name = request.POST.get('mother_names')
                post.father_id = request.POST.get('father_id')
                post.father_tel = request.POST.get('father_tel')
                post.mother_tel = request.POST.get('mother_tel')
                post.province = request.POST.get('province')
                post.district = request.POST.get('district')
                post.sector = request.POST.get('sector')
                post.village = request.POST.get('village')
                post.graduated = request.POST.get('graduated')
                post.start_year = request.POST.get('start_year')
                post.save()
                return redirect(rcpo_l5_d)
            return render(request, 'dos/rcpo/l5/actions/add.html', {
                "trades": trades,
                "year": current_year
            })
            
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)

def delete_rcpo_l5_d(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse(rcpo_l5_d))

def edit_rcpo_l5_d(request, id):
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            rcpo_l5_student_edit = get_object_or_404(Student, pk=id)
            
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    first_name = request.POST.get('firstname'),
                    last_name = request.POST.get('lastname'),
                    index_no = request.POST.get('senior_3_code'),
                    father_names = request.POST.get('father_names'),
                    mother_name = request.POST.get('mother_names'),
                    father_id = request.POST.get('father_id'),
                    father_tel = request.POST.get('father_tel'),
                    mother_tel = request.POST.get('mother_tel'),
                    province = request.POST.get('province'),
                    district = request.POST.get('district'),
                    sector = request.POST.get('sector'),
                    village = request.POST.get('village'),            
                )

                return redirect(rcpo_l5_d)
            return render(request, 'dos/rcpo/l5/actions/edit.html', {
                "student": rcpo_l5_student_edit
            })            
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)

    
def change_rcpo_l3_d(request, id):  
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    trade = request.POST.get('trade'),
                    level = request.POST.get('level'),
                )
                return HttpResponseRedirect(reverse(rcpo_l3_d))
        
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    


def graduate_rcpo_l5_d(request, id):  
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    graduated = request.POST.get('graduated'),
                    g_year = request.POST.get('g_year'),
                )
                return HttpResponseRedirect(reverse(rcpo_l5_d))
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)




''' End of Road Construction & Plant Operation '''















'''
    Begining of Land Surveying Views -> Patron
'''

def ls_l3_d(request):
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            trades = Trade.objects.all()
            students = Student.objects.filter(trade = "LS", level='L3', graduated='False')
            return render(request, 'dos/ls/l3/l3.html', {
                "students": students,
                "trades": trades,
            })            
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)


# LAND SURVEYING ACTIONS ADD, UPDATE, DELETE
def add_ls_l3_d(request):
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            current_year = datetime.datetime.today().year
            trades = Trade.objects.all()
            if request.method == 'POST':
                post = Student()
                post.first_name = request.POST.get('firstname')
                post.last_name = request.POST.get('lastname')
                post.trade = request.POST.get('trade')
                post.level = request.POST.get('level')
                post.status = request.POST.get('status')
                post.dob = request.POST.get('dob')
                post.gender = request.POST.get('gender')
                post.index_no = request.POST.get('senior_3_code')
                post.father_names = request.POST.get('father_names')
                post.mother_name = request.POST.get('mother_names')
                post.father_id = request.POST.get('father_id')
                post.father_tel = request.POST.get('father_tel')
                post.mother_tel = request.POST.get('mother_tel')
                post.province = request.POST.get('province')
                post.district = request.POST.get('district')
                post.sector = request.POST.get('sector')
                post.village = request.POST.get('village')
                post.graduated = request.POST.get('graduated')
                post.start_year = request.POST.get('start_year')
                post.save()
                return redirect(ls_l3_d)
            return render(request, 'dos/ls/l3/actions/add.html', {
                "trades": trades,
                "year": current_year
            })            
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)


def delete_ls_l3_d(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse(ls_l3_d))

def edit_ls_l3_d(request, id):
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            ls_l3_student_edit = get_object_or_404(Student, pk=id)
            
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    first_name = request.POST.get('firstname'),
                    last_name = request.POST.get('lastname'),
                    index_no = request.POST.get('senior_3_code'),
                    father_names = request.POST.get('father_names'),
                    mother_name = request.POST.get('mother_names'),
                    father_id = request.POST.get('father_id'),
                    father_tel = request.POST.get('father_tel'),
                    mother_tel = request.POST.get('mother_tel'),
                    province = request.POST.get('province'),
                    district = request.POST.get('district'),
                    sector = request.POST.get('sector'),
                    village = request.POST.get('village'),            
                )

                return redirect(ls_l3_d)
            return render(request, 'dos/ls/l3/actions/edit.html', {
                "student": ls_l3_student_edit
            })            
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)



def promote_ls_l3_d(request, id):  
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    trade = request.POST.get('trade'),
                    level = request.POST.get('level'),
                )
                return HttpResponseRedirect(reverse(ls_l3_d))            
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)


def change_ls_l3_d(request, id):  
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    trade = request.POST.get('trade'),
                    level = request.POST.get('level'),
                )
                return HttpResponseRedirect(reverse(ls_l3_d))            
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)



   








def ls_l4_d(request):
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            students = Student.objects.filter(trade = "LS", level='L4', graduated='False')
            return render(request, 'dos/ls/l4/l4.html', {
                "students": students
            })            
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)


# LAND SURVEYING ACTIONS ADD, UPDATE, DELETE
def add_ls_l4_d(request):
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            current_year = datetime.datetime.today().year
            trades = Trade.objects.all()
            if request.method == 'POST':
                post = Student()
                post.first_name = request.POST.get('firstname')
                post.last_name = request.POST.get('lastname')
                post.trade = request.POST.get('trade')
                post.level = request.POST.get('level')
                post.status = request.POST.get('status')
                post.dob = request.POST.get('dob')
                post.gender = request.POST.get('gender')
                post.index_no = request.POST.get('senior_3_code')
                post.father_names = request.POST.get('father_names')
                post.mother_name = request.POST.get('mother_names')
                post.father_id = request.POST.get('father_id')
                post.father_tel = request.POST.get('father_tel')
                post.mother_tel = request.POST.get('mother_tel')
                post.province = request.POST.get('province')
                post.district = request.POST.get('district')
                post.sector = request.POST.get('sector')
                post.village = request.POST.get('village')
                post.graduated = request.POST.get('graduated')
                post.start_year = request.POST.get('start_year')
                post.save()
                return redirect(ls_l4_d)
            return render(request, 'dos/ls/l4/actions/add.html', {
                "trades": trades,
                "year": current_year
            })            
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)


def delete_ls_l4_d(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse(ls_l4_d))

def edit_ls_l4_d(request, id):
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            ls_l4_student_edit = get_object_or_404(Student, pk=id)
            
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    first_name = request.POST.get('firstname'),
                    last_name = request.POST.get('lastname'),
                    index_no = request.POST.get('senior_3_code'),
                    father_names = request.POST.get('father_names'),
                    mother_name = request.POST.get('mother_names'),
                    father_id = request.POST.get('father_id'),
                    father_tel = request.POST.get('father_tel'),
                    mother_tel = request.POST.get('mother_tel'),
                    province = request.POST.get('province'),
                    district = request.POST.get('district'),
                    sector = request.POST.get('sector'),
                    village = request.POST.get('village'),            
                )

                return redirect(ls_l4_d)
            return render(request, 'dos/ls/l4/actions/edit.html', {
                "student": ls_l4_student_edit
            })
            
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)

def promote_ls_l4_d(request, id):  
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    trade = request.POST.get('trade'),
                    level = request.POST.get('level'),
                )
                return HttpResponseRedirect(reverse(ls_l4_d))            
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)








def ls_l5_d(request):
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            current_year = datetime.datetime.today().year
            students = Student.objects.filter(trade = "LS", level='L5', graduated='False')
            return render(request, 'dos/ls/l5/l5.html', {
                "students": students,
                "year": current_year
            })            
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)


# LAND SURVEYING ACTIONS ADD, UPDATE, DELETE
def add_ls_l5_d(request):
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            
            current_year = datetime.datetime.today().year
            trades = Trade.objects.all()
            if request.method == 'POST':
                post = Student()
                post.first_name = request.POST.get('firstname')
                post.last_name = request.POST.get('lastname')
                post.trade = request.POST.get('trade')
                post.level = request.POST.get('level')
                post.status = request.POST.get('status')
                post.dob = request.POST.get('dob')
                post.gender = request.POST.get('gender')
                post.index_no = request.POST.get('senior_3_code')
                post.father_names = request.POST.get('father_names')
                post.mother_name = request.POST.get('mother_names')
                post.father_id = request.POST.get('father_id')
                post.father_tel = request.POST.get('father_tel')
                post.mother_tel = request.POST.get('mother_tel')
                post.province = request.POST.get('province')
                post.district = request.POST.get('district')
                post.sector = request.POST.get('sector')
                post.village = request.POST.get('village')
                post.graduated = request.POST.get('graduated')
                post.start_year = request.POST.get('start_year')
                post.save()
                return redirect(ls_l5_d)
            return render(request, 'dos/ls/l5/actions/add.html', {
                "trades": trades,
                "year": current_year,
            })            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)


def delete_ls_l5_d(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse(ls_l5_d))

def edit_ls_l5_d(request, id):
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            
            ls_l5_student_edit = get_object_or_404(Student, pk=id)
            
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    first_name = request.POST.get('firstname'),
                    last_name = request.POST.get('lastname'),
                    index_no = request.POST.get('senior_3_code'),
                    father_names = request.POST.get('father_names'),
                    mother_name = request.POST.get('mother_names'),
                    father_id = request.POST.get('father_id'),
                    father_tel = request.POST.get('father_tel'),
                    mother_tel = request.POST.get('mother_tel'),
                    province = request.POST.get('province'),
                    district = request.POST.get('district'),
                    sector = request.POST.get('sector'),
                    village = request.POST.get('village'),            
                )

                return redirect(ls_l5_d)
            return render(request, 'dos/ls/l5/actions/edit.html', {
                "student": ls_l5_student_edit
            })
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)



def graduate_ls_l5_d(request, id): 
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    graduated = request.POST.get('graduated'),
                    g_year = request.POST.get('g_year'),
                )
                return HttpResponseRedirect(reverse(ls_l5_d))
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login) 




''' End of Land Surveying Views '''









'''
    Begining of Electricity Views -> Patron
'''

def elec_l3_d(request):
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            trades = Trade.objects.all()
            students = Student.objects.filter(trade = "ELEC", level='L3', graduated='False')
            return render(request, 'dos/elec/l3/l3.html', {
                "students": students,
                "trades": trades,
            })            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)


# ELECTRICITY ACTIONS ADD, UPDATE, DELETE
def add_elec_l3_d(request):
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            trades = Trade.objects.all()
            current_year = datetime.datetime.today().year
            if request.method == 'POST':
                post = Student()
                post.first_name = request.POST.get('firstname')
                post.last_name = request.POST.get('lastname')
                post.trade = request.POST.get('trade')
                post.level = request.POST.get('level')
                post.status = request.POST.get('status')
                post.dob = request.POST.get('dob')
                post.gender = request.POST.get('gender')
                post.index_no = request.POST.get('senior_3_code')
                post.father_names = request.POST.get('father_names')
                post.mother_name = request.POST.get('mother_names')
                post.father_id = request.POST.get('father_id')
                post.father_tel = request.POST.get('father_tel')
                post.mother_tel = request.POST.get('mother_tel')
                post.province = request.POST.get('province')
                post.district = request.POST.get('district')
                post.sector = request.POST.get('sector')
                post.village = request.POST.get('village')
                post.graduated = request.POST.get('graduated')
                post.start_year = request.POST.get('start_year')
                post.save()
                return redirect(elec_l3_d)
            return render(request, 'dos/elec/l3/actions/add.html', {
                "trades": trades,
                "year": current_year
            })
            
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)

def delete_elec_l3_d(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse(elec_l3_d))

def edit_elec_l3_d(request, id):
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            elec_l3_student_edit = get_object_or_404(Student, pk=id)
            
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    first_name = request.POST.get('firstname'),
                    last_name = request.POST.get('lastname'),
                    index_no = request.POST.get('senior_3_code'),
                    father_names = request.POST.get('father_names'),
                    mother_name = request.POST.get('mother_names'),
                    father_id = request.POST.get('father_id'),
                    father_tel = request.POST.get('father_tel'),
                    mother_tel = request.POST.get('mother_tel'),
                    province = request.POST.get('province'),
                    district = request.POST.get('district'),
                    sector = request.POST.get('sector'),
                    village = request.POST.get('village'),            
                )

                return redirect(elec_l3_d)
            return render(request, 'dos/elec/l3/actions/edit.html', {
                "student": elec_l3_student_edit
            })            
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)



def promote_elec_l3_d(request, id):  
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    trade = request.POST.get('trade'),
                    level = request.POST.get('level'),
                )
                return HttpResponseRedirect(reverse(elec_l3_d))            
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)


def change_elec_l3_d(request, id):
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    trade = request.POST.get('trade'),
                    level = request.POST.get('level'),
                )
                return HttpResponseRedirect(reverse(elec_l3_d))
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)  


   




def elec_l4_d(request):
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            students = Student.objects.filter(trade = "ELEC", level='L4', graduated='False')
            return render(request, 'dos/elec/l4/l4.html', {
                "students": students
            })            
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)


# ELECTRICITY ACTIONS ADD, UPDATE, DELETE
def add_elec_l4_d(request):
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            trades = Trade.objects.all()
            current_year = datetime.datetime.today().year
            if request.method == 'POST':
                post = Student()
                post.first_name = request.POST.get('firstname')
                post.last_name = request.POST.get('lastname')
                post.trade = request.POST.get('trade')
                post.level = request.POST.get('level')
                post.status = request.POST.get('status')
                post.dob = request.POST.get('dob')
                post.gender = request.POST.get('gender')
                post.index_no = request.POST.get('senior_3_code')
                post.father_names = request.POST.get('father_names')
                post.mother_name = request.POST.get('mother_names')
                post.father_id = request.POST.get('father_id')
                post.father_tel = request.POST.get('father_tel')
                post.mother_tel = request.POST.get('mother_tel')
                post.province = request.POST.get('province')
                post.district = request.POST.get('district')
                post.sector = request.POST.get('sector')
                post.village = request.POST.get('village')
                post.graduated = request.POST.get('graduated')
                post.start_year = request.POST.get('start_year')
                post.save()
                return redirect(elec_l4_d)
            return render(request, 'dos/ls/l4/actions/add.html', {
                "trades": trades,
                "year": current_year,
            })            
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)


def delete_elec_l4_d(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse(elec_l4_d))

def edit_elec_l4_d(request, id):
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            elec_l4_student_edit = get_object_or_404(Student, pk=id)
            
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    first_name = request.POST.get('firstname'),
                    last_name = request.POST.get('lastname'),
                    index_no = request.POST.get('senior_3_code'),
                    father_names = request.POST.get('father_names'),
                    mother_name = request.POST.get('mother_names'),
                    father_id = request.POST.get('father_id'),
                    father_tel = request.POST.get('father_tel'),
                    mother_tel = request.POST.get('mother_tel'),
                    province = request.POST.get('province'),
                    district = request.POST.get('district'),
                    sector = request.POST.get('sector'),
                    village = request.POST.get('village'),            
                )

                return redirect(elec_l4_d)
            return render(request, 'dos/elec/l4/actions/edit.html', {
                "student": elec_l4_student_edit
            })            
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)



def promote_elec_l4_d(request, id):  
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    trade = request.POST.get('trade'),
                    level = request.POST.get('level'),
                )
                return HttpResponseRedirect(reverse(elec_l4_d))
            
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)



def elec_l5_d(request):
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            current_year = datetime.datetime.today().year
            students = Student.objects.filter(trade = "ELEC", level='L5', graduated='False')
            return render(request, 'dos/elec/l5/l5.html', {
                "students": students,
                "year": current_year
            })            
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)


# ELECTRICITY ACTIONS ADD, UPDATE, DELETE

def add_elec_l5_d(request):
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            trades = Trade.objects.all()
            current_year = datetime.datetime.today().year
            if request.method == 'POST':
                post = Student()
                post.first_name = request.POST.get('firstname')
                post.last_name = request.POST.get('lastname')
                post.trade = request.POST.get('trade')
                post.level = request.POST.get('level')
                post.status = request.POST.get('status')
                post.dob = request.POST.get('dob')
                post.gender = request.POST.get('gender')
                post.index_no = request.POST.get('senior_3_code')
                post.father_names = request.POST.get('father_names')
                post.mother_name = request.POST.get('mother_names')
                post.father_id = request.POST.get('father_id')
                post.father_tel = request.POST.get('father_tel')
                post.mother_tel = request.POST.get('mother_tel')
                post.province = request.POST.get('province')
                post.district = request.POST.get('district')
                post.sector = request.POST.get('sector')
                post.village = request.POST.get('village')
                post.graduated = request.POST.get('graduated')
                post.start_year = request.POST.get('start_year')
                post.save()
                return redirect(elec_l5_d)
            return render(request, 'dos/elec/l5/actions/add.html', {
                "trades": trades,
                "year": current_year
            })            
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)


def delete_elec_l5_d(request, id):
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            if request.method == 'POST':
                student = Student.objects.get(pk=id)
                student.delete()
            return HttpResponseRedirect(reverse(elec_l5_d))
            
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)

def edit_elec_l5_d(request, id):
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            elec_l5_student_edit = get_object_or_404(Student, pk=id)
            
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    first_name = request.POST.get('firstname'),
                    last_name = request.POST.get('lastname'),
                    index_no = request.POST.get('senior_3_code'),
                    father_names = request.POST.get('father_names'),
                    mother_name = request.POST.get('mother_names'),
                    father_id = request.POST.get('father_id'),
                    father_tel = request.POST.get('father_tel'),
                    mother_tel = request.POST.get('mother_tel'),
                    province = request.POST.get('province'),
                    district = request.POST.get('district'),
                    sector = request.POST.get('sector'),
                    village = request.POST.get('village'),            
                )

                return redirect(elec_l5_d)
            return render(request, 'dos/elec/l5/actions/edit.html', {
                "student": elec_l5_student_edit
            })            
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)

    
    
    
    
def graduate_elec_l5_d(request, id):  
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    graduated = request.POST.get('graduated'),
                    g_year = request.POST.get('g_year'),
                )
                return HttpResponseRedirect(reverse(elec_l5_d))

            
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)



''' End of Electricity Views '''
















'''
    Begining of Software Development Views -> Patron
'''


def sod_l4_d(request):
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            students = Student.objects.filter(trade = "SOD", level='L4', graduated='False')
            return render(request, 'dos/sod/l4/l4.html', {
                "students": students
            })            
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)


# SOFTWARE DEVELOPMENT ACTIONS ADD, UPDATE, DELETE

def add_sod_l4_d(request):
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            
            current_year = datetime.datetime.today().year
            trades = Trade.objects.all()
            
            if request.method == 'POST':
                post = Student()
                post.first_name = request.POST.get('firstname')
                post.last_name = request.POST.get('lastname')
                post.trade = request.POST.get('trade')
                post.level = request.POST.get('level')
                post.status = request.POST.get('status')
                post.dob = request.POST.get('dob')
                post.gender = request.POST.get('gender')
                post.index_no = request.POST.get('senior_3_code')
                post.father_names = request.POST.get('father_names')
                post.mother_name = request.POST.get('mother_names')
                post.father_id = request.POST.get('father_id')
                post.father_tel = request.POST.get('father_tel')
                post.mother_tel = request.POST.get('mother_tel')
                post.province = request.POST.get('province')
                post.district = request.POST.get('district')
                post.sector = request.POST.get('sector')
                post.village = request.POST.get('village')
                post.graduated = request.POST.get('graduated')
                post.start_year = request.POST.get('start_year')
                post.save()
                return redirect(sod_l4_d)
            return render(request, 'dos/sod/l4/actions/add.html', {
                "trades": trades,
                "year": current_year
            })
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)

def delete_sod_l4_d(request, id):
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            if request.method == 'POST':
                student = Student.objects.get(pk=id)
                student.delete()
            return HttpResponseRedirect(reverse(sod_l4_d))            
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)


def edit_sod_l4_d(request, id):
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            sod_l4_student_edit = get_object_or_404(Student, pk=id)
            
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    first_name = request.POST.get('firstname'),
                    last_name = request.POST.get('lastname'),
                    index_no = request.POST.get('senior_3_code'),
                    father_names = request.POST.get('father_names'),
                    mother_name = request.POST.get('mother_names'),
                    father_id = request.POST.get('father_id'),
                    father_tel = request.POST.get('father_tel'),
                    mother_tel = request.POST.get('mother_tel'),
                    province = request.POST.get('province'),
                    district = request.POST.get('district'),
                    sector = request.POST.get('sector'),
                    village = request.POST.get('village'),            
                )

                return redirect(sod_l4_d)
            return render(request, 'dos/sod/l4/actions/edit.html', {
                "student": sod_l4_student_edit
            })            
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)


def promote_sod_l4_d(request, id):  
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    trade = request.POST.get('trade'),
                    level = request.POST.get('level'),
                )
                return HttpResponseRedirect(reverse(sod_l4_d))
            
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)



def sod_l5_d(request):
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            
            current_year = datetime.datetime.today().year
            students = Student.objects.filter(trade = "SOD", level='L5', graduated='False')
            return render(request, 'dos/sod/l5/l5.html', {
                "students": students,
                "year": current_year
            })            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)


# ELECTRICITY ACTIONS ADD, UPDATE, DELETE
def add_sod_l5_d(request):
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            
            trades = Trade.objects.all()
            current_year = datetime.datetime.today().year
            if request.method == 'POST':
                post = Student()
                post.first_name = request.POST.get('firstname')
                post.last_name = request.POST.get('lastname')
                post.trade = request.POST.get('trade')
                post.level = request.POST.get('level')
                post.status = request.POST.get('status')
                post.dob = request.POST.get('dob')
                post.gender = request.POST.get('gender')
                post.index_no = request.POST.get('senior_3_code')
                post.father_names = request.POST.get('father_names')
                post.mother_name = request.POST.get('mother_names')
                post.father_id = request.POST.get('father_id')
                post.father_tel = request.POST.get('father_tel')
                post.mother_tel = request.POST.get('mother_tel')
                post.province = request.POST.get('province')
                post.district = request.POST.get('district')
                post.sector = request.POST.get('sector')
                post.village = request.POST.get('village')
                post.graduated = request.POST.get('graduated')
                post.start_year = request.POST.get('start_year')
                post.save()
                return redirect(sod_l5_d)
            return render(request, 'dos/sod/l5/actions/add.html', {
                "trades": trades,
                "year": current_year
            })            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)


def delete_sod_l5_d(request, id):
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            if request.method == 'POST':
                student = Student.objects.get(pk=id)
                student.delete()
            return HttpResponseRedirect(reverse(sod_l5_d))            
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)


def edit_sod_l5_d(request, id):
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            
            sod_l5_student_edit = get_object_or_404(Student, pk=id)
            
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    first_name = request.POST.get('firstname'),
                    last_name = request.POST.get('lastname'),
                    index_no = request.POST.get('senior_3_code'),
                    father_names = request.POST.get('father_names'),
                    mother_name = request.POST.get('mother_names'),
                    father_id = request.POST.get('father_id'),
                    father_tel = request.POST.get('father_tel'),
                    mother_tel = request.POST.get('mother_tel'),
                    province = request.POST.get('province'),
                    district = request.POST.get('district'),
                    sector = request.POST.get('sector'),
                    village = request.POST.get('village'),            
                )

                return redirect(sod_l5_d)
            return render(request, 'dos/sod/l5/actions/edit.html', {
                "student": sod_l5_student_edit
            })
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)


    
def graduate_sod_l5_d(request, id):  
    if request.user.email.endswith('dos@gmail.com'):
        if request.user.is_authenticated:
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    graduated = request.POST.get('graduated'),
                    g_year = request.POST.get('g_year'),
                )
                return HttpResponseRedirect(reverse(sod_l5_d))
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)


''' End of Software Development Views '''














'''
    ACCOUNTANT VIEWS / Burser
'''




'''
   Start All Students List
'''

def all_b_students(request):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            current_year = datetime.datetime.today().year
            students = Student.objects.filter(graduated='False')
            Fix_Fee = Fixed_Fee.objects.all()
            Fix_Fee_day = Fixed_Fee_Day.objects.all()
            
            return render(request, 'burser/all_b_students/all_b.html', {
                'students': students,
                'year': current_year,
                'Fixed_Fee': Fix_Fee,
                "Fixed_Fee_day": Fix_Fee_day,
            })
            
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)


def add_all_payement(request, id):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            if request.method == 'POST':
                Student.objects.filter(pk=id).update(
                    first_term_fee = request.POST.get('first_term_fee'),
                    second_term_fee = request.POST.get('second_term_fee'),
                    third_term_fee = request.POST.get('third_term_fee'),       
                )
                return HttpResponseRedirect(reverse(all_b_students))
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    



def add_all_b(request):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            current_year = datetime.datetime.today().year
            trades = Trade.objects.all()
            if request.method == 'POST':
                post = Student()
                post.first_name = request.POST.get('firstname')
                post.last_name = request.POST.get('lastname')
                post.trade = request.POST.get('trade')
                post.level = request.POST.get('level')
                post.status = request.POST.get('status')
                post.dob = request.POST.get('dob')
                post.gender = request.POST.get('gender')
                post.index_no = request.POST.get('senior_3_code')
                post.father_names = request.POST.get('father_names')
                post.mother_name = request.POST.get('mother_names')
                post.father_id = request.POST.get('father_id')
                post.father_tel = request.POST.get('father_tel')
                post.mother_tel = request.POST.get('mother_tel')
                post.province = request.POST.get('province')
                post.district = request.POST.get('district')
                post.sector = request.POST.get('sector')
                post.village = request.POST.get('village')
                post.graduated = request.POST.get('graduated')
                post.start_year = request.POST.get('start_year')
                post.save()
                return redirect(all_b_students)
                
            return render(request, 'burser/all_b_students/actions/add.html', {
                "trades": trades,
                "year": current_year,
            })

            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    


def edit_all_b(request, id):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            cst_l3_student_edit = get_object_or_404(Student, pk=id)
            
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    first_name = request.POST.get('firstname'),
                    last_name = request.POST.get('lastname'),
                    index_no = request.POST.get('senior_3_code'),
                    father_names = request.POST.get('father_names'),
                    mother_name = request.POST.get('mother_names'),
                    father_id = request.POST.get('father_id'),
                    father_tel = request.POST.get('father_tel'),
                    mother_tel = request.POST.get('mother_tel'),
                    province = request.POST.get('province'),
                    district = request.POST.get('district'),
                    sector = request.POST.get('sector'),
                    village = request.POST.get('village'),            
                )

                return redirect(all_b_students)
            
            return render(request, 'burser/all_b_students/actions/edit.html', {
                "student": cst_l3_student_edit
            })
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    

    
def delete_all_b(request, id):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            if request.method == 'POST':
                student = Student.objects.get(pk=id)
                student.delete()
            return HttpResponseRedirect(reverse(all_b_students))

        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    



'''
   Ends All Students List
'''

'''
    START STUDENT STATUS -->
'''

def day_students(request):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            current_year = datetime.datetime.today().year
            students = Student.objects.filter(status='Day', graduated='False')
            Fix_Fee = Fixed_Fee.objects.all()
            Fix_Fee_day = Fixed_Fee_Day.objects.all()

            return render(request, 'burser/status/day.html', {
                "students":students,
                "year": current_year,
                "Fixed_Fee": Fix_Fee,
                "Fixed_Fee_day": Fix_Fee_day,
            })
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    


def day_payement(request, id):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            if request.method == 'POST':
                Student.objects.filter(pk=id).update(
                    first_term_fee = request.POST.get('first_term_fee'),
                    second_term_fee = request.POST.get('second_term_fee'),
                    third_term_fee = request.POST.get('third_term_fee'),       
                )
                return HttpResponseRedirect(reverse(day_students))

            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    


def financial_day(request, id):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:

            fixed_fee = Fixed_Fee.objects.all()
            student = get_object_or_404(Student, pk=id)
            Daily_scholar_fee = Fixed_Fee_Day.objects.all()
            return render(request, 'burser/status/day.html', {
                "student": student,
                "fixed": fixed_fee,
            })            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    


def boarding_students(request):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            current_year = datetime.datetime.today().year
            students = Student.objects.filter(status='Boarding', graduated='False')
            Fix_Fee = Fixed_Fee.objects.all()
            Daily_scholar_fee = Fixed_Fee_Day.objects.all()

            return render(request, 'burser/status/boarding.html', {
                "students":students,
                "year": current_year,
                "Fixed_Fee": Fix_Fee,
                "Fee": Daily_scholar_fee,
            })

            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    

def boarding_payement(request, id):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            if request.method == 'POST':
                Student.objects.filter(pk=id).update(
                    first_term_fee = request.POST.get('first_term_fee'),
                    second_term_fee = request.POST.get('second_term_fee'),
                    third_term_fee = request.POST.get('third_term_fee'),       
                )
                return HttpResponseRedirect(reverse(boarding_students))

            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    

def fee_payement_verification(request, id):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            return render(request, 'burser/cst/l3/l3.html', {})
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    
    

def financial_boarding(request, id):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            fixed_fee = Fixed_Fee.objects.all()
            student = get_object_or_404(Student, pk=id)
            return render(request, 'burser/status/boarding.html', {
                "student": student,
                "fixed": fixed_fee,
            })
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    



def edit_boarding_b(request, id):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:

            cst_l3_student_edit = get_object_or_404(Student, pk=id)
            
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    first_name = request.POST.get('firstname'),
                    last_name = request.POST.get('lastname'),
                    index_no = request.POST.get('senior_3_code'),
                    father_names = request.POST.get('father_names'),
                    mother_name = request.POST.get('mother_names'),
                    father_id = request.POST.get('father_id'),
                    father_tel = request.POST.get('father_tel'),
                    mother_tel = request.POST.get('mother_tel'),
                    province = request.POST.get('province'),
                    district = request.POST.get('district'),
                    sector = request.POST.get('sector'),
                    village = request.POST.get('village'),            
                )

                return redirect(boarding_students)
            
            return render(request, 'burser/status/edit_boarding.html', {
                "student": cst_l3_student_edit
            })            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    

'''
    END STUDENT STATUS -->
'''


def boarding_fix_fee(request):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:

            Fix_Fee = Fixed_Fee.objects.all()
            if request.method == 'POST':
                Fixed_Fee.objects.update(
                    first_fixed_fee = request.POST.get('first_fixed_fee'),
                    second_fixed_fee = request.POST.get('second_fixed_fee'),
                    third_fixed_fee = request.POST.get('third_fixed_fee'),       
                )
                return redirect(boarding_fix_fee)

            return render(request, "burser/Fee_payments/boarding.html", {
                "Fix_Fee": Fix_Fee
            })            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    



def day_fix_fee(request):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            Fix_Fee = Fixed_Fee_Day.objects.all()
            if request.method == 'POST':
                Fixed_Fee_Day.objects.update(
                    first_fixed_fee_day = request.POST.get('first_fixed_fee'),
                    second_fixed_fee_day = request.POST.get('second_fixed_fee'),
                    third_fixed_fee_day = request.POST.get('third_fixed_fee'),       
                )
                return redirect(day_fix_fee)

            return render(request, "burser/Fee_payments/day.html", {
                "Fix_Fee": Fix_Fee
            })

            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    




''' 
   Starting of Computer Systems Technology Views -> Patron
'''

def cst_l3_b(request):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            students = Student.objects.filter(trade = "CST", level='L3', graduated='False')
            Fix_Fee = Fixed_Fee.objects.all()
            Fix_Fee_day = Fixed_Fee_Day.objects.all()

            if request.method == 'POST':
                Fixed_Fee_Day.objects.update(
                    first_fixed_fee_day = request.POST.get('first_term_fee_day'),
                    second_fixed_fee_day = request.POST.get('second_term_fee_day'),
                    third_fixed_fee_day = request.POST.get('third_term_fee_day'),       
                )
                return HttpResponseRedirect(reverse(cst_l3_b))


            
            return render(request, 'burser/cst/l3/l3.html', {
                "students": students,
                "Fixed_Fee": Fix_Fee,
                "Fixed_Fee_day": Fix_Fee_day,
            })


            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    


# CST ACTIONS ADD, UPDATE, DELETE
def add_cst_l3_b(request):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            current_year = datetime.datetime.today().year
            trades = Trade.objects.all()
            if request.method == 'POST':
                post = Student()
                post.first_name = request.POST.get('firstname')
                post.last_name = request.POST.get('lastname')
                post.trade = request.POST.get('trade')
                post.level = request.POST.get('level')
                post.dob = request.POST.get('dob')
                post.gender = request.POST.get('gender')
                post.status = request.POST.get('status')
                post.index_no = request.POST.get('senior_3_code')
                post.father_names = request.POST.get('father_names')
                post.mother_name = request.POST.get('mother_names')
                post.father_id = request.POST.get('father_id')
                post.father_tel = request.POST.get('father_tel')
                post.mother_tel = request.POST.get('mother_tel')
                post.province = request.POST.get('province')
                post.district = request.POST.get('district')
                post.sector = request.POST.get('sector')
                post.village = request.POST.get('village')
                post.graduated = request.POST.get('graduated')
                post.start_year = request.POST.get('start_year')
                post.save()
                return redirect(cst_l3_b)
                
            return render(request, 'burser/cst/l3/actions/add.html', {
                "trades": trades,
                "year": current_year,
            })
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    


def add_cst_l3_payement_fix(request, id):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            if request.method == 'POST':
                Fixed_Fee_Day.objects.update(
                    first_fixed_fee_day = request.POST.get('first_term_fee_day'),
                    second_fixed_fee_day = request.POST.get('second_term_fee_day'),
                    third_fixed_fee_day = request.POST.get('third_term_fee_day'),       
                )
                return HttpResponseRedirect(reverse(cst_l3_b))
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    



def add_cst_l3_payement(request, id):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            if request.method == 'POST':
                Student.objects.filter(pk=id).update(
                    first_term_fee = request.POST.get('first_term_fee'),
                    second_term_fee = request.POST.get('second_term_fee'),
                    third_term_fee = request.POST.get('third_term_fee'),       
                )
                return HttpResponseRedirect(reverse(cst_l3_b))
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    



def fee_payement_verification(request, id):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            return render(request, 'burser/cst/l3/l3.html', {})
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    
    

def financial_cst(request, id):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            fixed_fee = Fixed_Fee.objects.all()
            student = get_object_or_404(Student, pk=id)
            Daily_scholar_fee = Fixed_Fee_Day.objects.all()
            return render(request, 'burser/cst/l3/actions/financial.html', {
                "student": student,
                "fixed": fixed_fee,
                "fixed_day": Daily_scholar_fee,
            })
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    

def financial_day(request, id):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:

            student = get_object_or_404(Student, pk=id)
            Daily_scholar_fee = Fixed_Fee_Day.objects.all()
            return render(request, 'burser/cst/l3/actions/financial_day.html', {
                "student": student,
                "fixed_day": Daily_scholar_fee,
            })
                            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    


def view_cst_l3_b(request, id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse(cst_l3_b))

def edit_cst_b(request, id):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            cst_l3_student_edit = get_object_or_404(Student, pk=id)
            
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    first_name = request.POST.get('firstname'),
                    last_name = request.POST.get('lastname'),
                    index_no = request.POST.get('senior_3_code'),
                    father_names = request.POST.get('father_names'),
                    mother_name = request.POST.get('mother_names'),
                    father_id = request.POST.get('father_id'),
                    father_tel = request.POST.get('father_tel'),
                    mother_tel = request.POST.get('mother_tel'),
                    province = request.POST.get('province'),
                    district = request.POST.get('district'),
                    sector = request.POST.get('sector'),
                    village = request.POST.get('village'),            
                )

                return redirect(cst_l3_b)
            
            return render(request, 'burser/cst/l3/actions/edit.html', {
                "student": cst_l3_student_edit
            })
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    

def delete_cst_l3_b(request, id):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            if request.method == 'POST':
                student = Student.objects.get(pk=id)
                student.delete()
            return HttpResponseRedirect(reverse(cst_l3_b))

            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    


''' End Of Computer Systems Views '''













'''
    Begining of Road Construction & Plant Operation Views -> Patron
'''

def rcpo_l3_b(request):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            students = Student.objects.filter(trade = "RCPO", level='L3', graduated='False')
            Fix_Fee = Fixed_Fee.objects.all()
            Fix_Fee_day = Fixed_Fee_Day.objects.all()
            return render(request, 'burser/rcpo/l3/l3.html', {
                "students" : students,
                "Fixed_Fee": Fix_Fee,
                "Fixed_Fee_day": Fix_Fee_day,

            })
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    



# Add RCPO Payment


# RCPO ACTIONS ADD, UPDATE, DELETE

def add_rcpo_l3_payement(request, id):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:

            if request.method == 'POST':
                Student.objects.filter(pk=id).update(
                    first_term_fee = request.POST.get('first_term_fee'),
                    second_term_fee = request.POST.get('second_term_fee'),
                    third_term_fee = request.POST.get('third_term_fee'),       
                )
                return HttpResponseRedirect(reverse(rcpo_l3_b))

            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    


def add_rcpo_l3_b(request):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            trades = Trade.objects.all()
            current_year = datetime.datetime.today().year
            if request.method == 'POST':
                post = Student()
                post.first_name = request.POST.get('firstname')
                post.last_name = request.POST.get('lastname')
                post.trade = request.POST.get('trade')
                post.level = request.POST.get('level')
                post.status = request.POST.get('status')
                post.dob = request.POST.get('dob')
                post.gender = request.POST.get('gender')
                post.index_no = request.POST.get('senior_3_code')
                post.father_names = request.POST.get('father_names')
                post.mother_name = request.POST.get('mother_names')
                post.father_id = request.POST.get('father_id')
                post.father_tel = request.POST.get('father_tel')
                post.mother_tel = request.POST.get('mother_tel')
                post.province = request.POST.get('province')
                post.district = request.POST.get('district')
                post.sector = request.POST.get('sector')
                post.village = request.POST.get('village')
                post.graduated = request.POST.get('graduated')
                post.start_year = request.POST.get('start_year')
                post.save()
                return redirect(rcpo_l3_b)
            return render(request, 'burser/rcpo/l3/actions/add.html', {
                "trades": trades,
                "year": current_year
            })
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    


def delete_rcpo_l3_b(request, id):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            if request.method == 'POST':
                student = Student.objects.get(pk=id)
                student.delete()
            return HttpResponseRedirect(reverse(rcpo_l3_b))
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    


def edit_rcpo_l3_b(request, id):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            rcpo_l3_student_edit = get_object_or_404(Student, pk=id)
            
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    first_name = request.POST.get('firstname'),
                    last_name = request.POST.get('lastname'),
                    index_no = request.POST.get('senior_3_code'),
                    father_names = request.POST.get('father_names'),
                    mother_name = request.POST.get('mother_names'),
                    father_id = request.POST.get('father_id'),
                    father_tel = request.POST.get('father_tel'),
                    mother_tel = request.POST.get('mother_tel'),
                    province = request.POST.get('province'),
                    district = request.POST.get('district'),
                    sector = request.POST.get('sector'),
                    village = request.POST.get('village'),            
                )

                return redirect(rcpo_l3_b)
            return render(request, 'burser/rcpo/l3/actions/edit.html', {
                "student": rcpo_l3_student_edit
            })
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    




def rcpo_l4_b(request):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            students = Student.objects.filter(trade = "RCPO", level='L4', graduated='False')
            Fix_Fee = Fixed_Fee.objects.all()
            Fix_Fee_day = Fixed_Fee_Day.objects.all()
            return render(request, 'burser/rcpo/l4/l4.html', {
                "students" : students,
                "Fixed_Fee": Fix_Fee,
                "Fixed_Fee_day": Fix_Fee_day,
            })
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    


def add_rcpo_l4_payement(request, id):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            if request.method == 'POST':
                Student.objects.filter(pk=id).update(
                    first_term_fee = request.POST.get('first_term_fee'),
                    second_term_fee = request.POST.get('second_term_fee'),
                    third_term_fee = request.POST.get('third_term_fee'),       
                )
                return HttpResponseRedirect(reverse(rcpo_l4_b))

            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    

# RCPO ACTIONS ADD, UPDATE, DELETE
def add_rcpo_l4_b(request):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            current_year = datetime.datetime.today().year
            trades = Trade.objects.all()
            if request.method == 'POST':
                post = Student()
                post.first_name = request.POST.get('firstname')
                post.last_name = request.POST.get('lastname')
                post.trade = request.POST.get('trade')
                post.level = request.POST.get('level')
                post.status = request.POST.get('status')
                post.dob = request.POST.get('dob')
                post.gender = request.POST.get('gender')
                post.index_no = request.POST.get('senior_3_code')
                post.father_names = request.POST.get('father_names')
                post.mother_name = request.POST.get('mother_names')
                post.father_id = request.POST.get('father_id')
                post.father_tel = request.POST.get('father_tel')
                post.mother_tel = request.POST.get('mother_tel')
                post.province = request.POST.get('province')
                post.district = request.POST.get('district')
                post.sector = request.POST.get('sector')
                post.village = request.POST.get('village')
                post.graduated = request.POST.get('graduated')
                post.start_year = request.POST.get('start_year')
                post.save()
                return redirect(rcpo_l4_b)
            return render(request, 'burser/rcpo/l4/actions/add.html', {
                "trades": trades,
                "year": current_year
            })
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    


def delete_rcpo_l4_b(request, id):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            if request.method == 'POST':
                student = Student.objects.get(pk=id)
                student.delete()
            return HttpResponseRedirect(reverse(rcpo_l4_b))
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    


def edit_rcpo_l4_b(request, id):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            rcpo_l4_student_edit = get_object_or_404(Student, pk=id)
            
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    first_name = request.POST.get('firstname'),
                    last_name = request.POST.get('lastname'),
                    index_no = request.POST.get('senior_3_code'),
                    father_names = request.POST.get('father_names'),
                    mother_name = request.POST.get('mother_names'),
                    father_id = request.POST.get('father_id'),
                    father_tel = request.POST.get('father_tel'),
                    mother_tel = request.POST.get('mother_tel'),
                    province = request.POST.get('province'),
                    district = request.POST.get('district'),
                    sector = request.POST.get('sector'),
                    village = request.POST.get('village'),            
                )

                return redirect(rcpo_l4_b)
            return render(request, 'burser/rcpo/l4/actions/edit.html', {
                "student": rcpo_l4_student_edit
            })
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    






def rcpo_l5_b(request):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            students = Student.objects.filter(trade = "RCPO", level='L5', graduated='False')
            Fix_Fee = Fixed_Fee.objects.all()
            Fix_Fee_day = Fixed_Fee_Day.objects.all()
            return render(request, 'burser/rcpo/l5/l5.html', {
                "students" : students,
                "Fixed_Fee": Fix_Fee,
                "Fixed_Fee_day": Fix_Fee_day,
            })
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    





def add_rcpo_l5_payement(request, id):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:

            if request.method == 'POST':
                Student.objects.filter(pk=id).update(
                    first_term_fee = request.POST.get('first_term_fee'),
                    second_term_fee = request.POST.get('second_term_fee'),
                    third_term_fee = request.POST.get('third_term_fee'),       
                )
                return HttpResponseRedirect(reverse(rcpo_l5_b))

            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    

# RCPO ACTIONS ADD, UPDATE, DELETE

def add_rcpo_l5_b(request):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            current_year = datetime.datetime.today().year
            trades = Trade.objects.all()
            if request.method == 'POST':
                post = Student()
                post.first_name = request.POST.get('firstname')
                post.last_name = request.POST.get('lastname')
                post.trade = request.POST.get('trade')
                post.level = request.POST.get('level')
                post.status = request.POST.get('status')
                post.dob = request.POST.get('dob')
                post.gender = request.POST.get('gender')
                post.index_no = request.POST.get('senior_3_code')
                post.father_names = request.POST.get('father_names')
                post.mother_name = request.POST.get('mother_names')
                post.father_id = request.POST.get('father_id')
                post.father_tel = request.POST.get('father_tel')
                post.mother_tel = request.POST.get('mother_tel')
                post.province = request.POST.get('province')
                post.district = request.POST.get('district')
                post.sector = request.POST.get('sector')
                post.village = request.POST.get('village')
                post.graduated = request.POST.get('graduated')
                post.start_year = request.POST.get('start_year')
                post.save()
                return redirect(rcpo_l5_b)
            return render(request, 'burser/rcpo/l5/actions/add.html', {
                "trades": trades,
                "year": current_year,
            })
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    


def delete_rcpo_l5_b(request, id):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            if request.method == 'POST':
                student = Student.objects.get(pk=id)
                student.delete()
            return HttpResponseRedirect(reverse(rcpo_l5_b))
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    


def edit_rcpo_l5_b(request, id):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            rcpo_l5_student_edit = get_object_or_404(Student, pk=id)
            
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    first_name = request.POST.get('firstname'),
                    last_name = request.POST.get('lastname'),
                    index_no = request.POST.get('senior_3_code'),
                    father_names = request.POST.get('father_names'),
                    mother_name = request.POST.get('mother_names'),
                    father_id = request.POST.get('father_id'),
                    father_tel = request.POST.get('father_tel'),
                    mother_tel = request.POST.get('mother_tel'),
                    province = request.POST.get('province'),
                    district = request.POST.get('district'),
                    sector = request.POST.get('sector'),
                    village = request.POST.get('village'),            
                )

                return redirect(rcpo_l5_b)
            return render(request, 'burser/rcpo/l5/actions/edit.html', {
                "student": rcpo_l5_student_edit
            })

            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    





''' End of Road Construction & Plant Operation '''















'''
    Begining of Land Surveying Views -> Patron
'''

def ls_l3_b(request):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            students = Student.objects.filter(trade = "LS", level='L3', graduated='False')
            Fix_Fee = Fixed_Fee.objects.all()
            Fix_Fee_day = Fixed_Fee_Day.objects.all()
            return render(request, 'burser/ls/l3/l3.html', {
                "students": students,
                "students" : students,
                "Fixed_Fee": Fix_Fee,
                "Fixed_Fee_day": Fix_Fee_day,
            })
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    


def add_ls_l3_payement(request, id):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            if request.method == 'POST':
                Student.objects.filter(pk=id).update(
                    first_term_fee = request.POST.get('first_term_fee'),
                    second_term_fee = request.POST.get('second_term_fee'),
                    third_term_fee = request.POST.get('third_term_fee'),       
                )
                return HttpResponseRedirect(reverse(ls_l3_b))

            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    

# LAND SURVEYING ACTIONS ADD, UPDATE, DELETE
def add_ls_l3_b(request):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            trades = Trade.objects.all()
            current_year = datetime.datetime.today().year
            if request.method == 'POST':
                post = Student()
                post.first_name = request.POST.get('firstname')
                post.last_name = request.POST.get('lastname')
                post.trade = request.POST.get('trade')
                post.level = request.POST.get('level')
                post.status = request.POST.get('status')
                post.dob = request.POST.get('dob')
                post.gender = request.POST.get('gender')
                post.index_no = request.POST.get('senior_3_code')
                post.father_names = request.POST.get('father_names')
                post.mother_name = request.POST.get('mother_names')
                post.father_id = request.POST.get('father_id')
                post.father_tel = request.POST.get('father_tel')
                post.mother_tel = request.POST.get('mother_tel')
                post.province = request.POST.get('province')
                post.district = request.POST.get('district')
                post.sector = request.POST.get('sector')
                post.village = request.POST.get('village')
                post.graduated = request.POST.get('graduated')
                post.start_year = request.POST.get('start_year')
                post.save()
                return redirect(ls_l3_b)
            return render(request, 'burser/ls/l3/actions/add.html', {
                "trades": trades,
                "year": current_year,
            })
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    


def delete_ls_l3_b(request, id):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            if request.method == 'POST':
                student = Student.objects.get(pk=id)
                student.delete()
            return HttpResponseRedirect(reverse(ls_l3_b))
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    


def edit_ls_l3_b(request, id):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            ls_l3_student_edit = get_object_or_404(Student, pk=id)
            
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    first_name = request.POST.get('firstname'),
                    last_name = request.POST.get('lastname'),
                    index_no = request.POST.get('senior_3_code'),
                    father_names = request.POST.get('father_names'),
                    mother_name = request.POST.get('mother_names'),
                    father_id = request.POST.get('father_id'),
                    father_tel = request.POST.get('father_tel'),
                    mother_tel = request.POST.get('mother_tel'),
                    province = request.POST.get('province'),
                    district = request.POST.get('district'),
                    sector = request.POST.get('sector'),
                    village = request.POST.get('village'),            
                )

                return redirect(ls_l3_b)
            return render(request, 'burser/ls/l3/actions/edit.html', {
                "student": ls_l3_student_edit
            })
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    





def ls_l4_b(request):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            students = Student.objects.filter(trade = "LS", level='L4', graduated='False')
            Fix_Fee = Fixed_Fee.objects.all()
            Fix_Fee_day = Fixed_Fee_Day.objects.all()
            return render(request, 'burser/ls/l4/l4.html', {
                "students": students,
                "students" : students,
                "Fixed_Fee": Fix_Fee,
                "Fixed_Fee_day": Fix_Fee_day,
            })

            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    


def add_ls_l4_payement(request, id):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            if request.method == 'POST':
                Student.objects.filter(pk=id).update(
                    first_term_fee = request.POST.get('first_term_fee'),
                    second_term_fee = request.POST.get('second_term_fee'),
                    third_term_fee = request.POST.get('third_term_fee'),       
                )
                return HttpResponseRedirect(reverse(ls_l4_b))

            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    


# LAND SURVEYING ACTIONS ADD, UPDATE, DELETE
def add_ls_l4_b(request):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            trades = Trade.objects.all()
            current_year = datetime.datetime.today().year
            if request.method == 'POST':
                post = Student()
                post.first_name = request.POST.get('firstname')
                post.last_name = request.POST.get('lastname')
                post.trade = request.POST.get('trade')
                post.level = request.POST.get('level')
                post.status = request.POST.get('status')
                post.dob = request.POST.get('dob')
                post.gender = request.POST.get('gender')
                post.index_no = request.POST.get('senior_3_code')
                post.father_names = request.POST.get('father_names')
                post.mother_name = request.POST.get('mother_names')
                post.father_id = request.POST.get('father_id')
                post.father_tel = request.POST.get('father_tel')
                post.mother_tel = request.POST.get('mother_tel')
                post.province = request.POST.get('province')
                post.district = request.POST.get('district')
                post.sector = request.POST.get('sector')
                post.village = request.POST.get('village')
                post.graduated = request.POST.get('graduated')
                post.start_year = request.POST.get('start_year')
                post.save()
                return redirect(ls_l4_b)
            return render(request, 'burser/ls/l4/actions/add.html', {
                "trades": trades,
                "year": current_year
            })
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    


def delete_ls_l4_b(request, id):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            if request.method == 'POST':
                student = Student.objects.get(pk=id)
                student.delete()
            return HttpResponseRedirect(reverse(ls_l4_b))
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    


def edit_ls_l4_b(request, id):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            ls_l4_student_edit = get_object_or_404(Student, pk=id)
            
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    first_name = request.POST.get('firstname'),
                    last_name = request.POST.get('lastname'),
                    index_no = request.POST.get('senior_3_code'),
                    father_names = request.POST.get('father_names'),
                    mother_name = request.POST.get('mother_names'),
                    father_id = request.POST.get('father_id'),
                    father_tel = request.POST.get('father_tel'),
                    mother_tel = request.POST.get('mother_tel'),
                    province = request.POST.get('province'),
                    district = request.POST.get('district'),
                    sector = request.POST.get('sector'),
                    village = request.POST.get('village'),            
                )

                return redirect(ls_l4_b)
            return render(request, 'burser/ls/l4/actions/edit.html', {
                "student": ls_l4_student_edit
            })

            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    






def ls_l5_b(request):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            students = Student.objects.filter(trade = "LS", level='L5', graduated='False')
            Fix_Fee = Fixed_Fee.objects.all()
            Fix_Fee_day = Fixed_Fee_Day.objects.all()
            return render(request, 'burser/ls/l5/l5.html', {
                "students": students,
                "Fixed_Fee": Fix_Fee,
                "Fixed_Fee_day": Fix_Fee_day,
            })
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    


def add_ls_l5_payement(request, id):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            if request.method == 'POST':
                Student.objects.filter(pk=id).update(
                    first_term_fee = request.POST.get('first_term_fee'),
                    second_term_fee = request.POST.get('second_term_fee'),
                    third_term_fee = request.POST.get('third_term_fee'),       
                )
                return HttpResponseRedirect(reverse(ls_l5_b))
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    


# LAND SURVEYING ACTIONS ADD, UPDATE, DELETE
def add_ls_l5_b(request):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            current_year = datetime.datetime.today().year
            trades = Trade.objects.all()
            if request.method == 'POST':
                post = Student()
                post.first_name = request.POST.get('firstname')
                post.last_name = request.POST.get('lastname')
                post.trade = request.POST.get('trade')
                post.level = request.POST.get('level')
                post.status = request.POST.get('status')
                post.dob = request.POST.get('dob')
                post.gender = request.POST.get('gender')
                post.index_no = request.POST.get('senior_3_code')
                post.father_names = request.POST.get('father_names')
                post.mother_name = request.POST.get('mother_names')
                post.father_id = request.POST.get('father_id')
                post.father_tel = request.POST.get('father_tel')
                post.mother_tel = request.POST.get('mother_tel')
                post.province = request.POST.get('province')
                post.district = request.POST.get('district')
                post.sector = request.POST.get('sector')
                post.village = request.POST.get('village')
                post.graduated = request.POST.get('graduated')
                post.start_year = request.POST.get('start_year')
                post.save()
                return redirect(ls_l5_b)
            return render(request, 'burser/ls/l5/actions/add.html', {
                "trades": trades, 
                "year": current_year,
            })
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    


def delete_ls_l5_b(request, id):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            if request.method == 'POST':
                student = Student.objects.get(pk=id)
                student.delete()
            return HttpResponseRedirect(reverse(ls_l5_b))

            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    

def edit_ls_l5_b(request, id):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            ls_l5_student_edit = get_object_or_404(Student, pk=id)
            
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    first_name = request.POST.get('firstname'),
                    last_name = request.POST.get('lastname'),
                    index_no = request.POST.get('senior_3_code'),
                    father_names = request.POST.get('father_names'),
                    mother_name = request.POST.get('mother_names'),
                    father_id = request.POST.get('father_id'),
                    father_tel = request.POST.get('father_tel'),
                    mother_tel = request.POST.get('mother_tel'),
                    province = request.POST.get('province'),
                    district = request.POST.get('district'),
                    sector = request.POST.get('sector'),
                    village = request.POST.get('village'),            
                )

                return redirect(ls_l5_b)
            return render(request, 'burser/ls/l5/actions/edit.html', {
                "student": ls_l5_student_edit
            })

            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    




''' End of Land Surveying Views '''









'''
    Begining of Electricity Views -> Patron
'''

def elec_l3_b(request):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            students = Student.objects.filter(trade = "ELEC", level='L3', graduated='False')
            Fix_Fee = Fixed_Fee.objects.all()
            Fix_Fee_day = Fixed_Fee_Day.objects.all()
            return render(request, 'burser/elec/l3/l3.html', {
                "students": students,
                "Fixed_Fee": Fix_Fee,
                "Fixed_Fee_day": Fix_Fee_day,
            })

            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    


def add_elec_l3_payement(request, id):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            if request.method == 'POST':
                Student.objects.filter(pk=id).update(
                    first_term_fee = request.POST.get('first_term_fee'),
                    second_term_fee = request.POST.get('second_term_fee'),
                    third_term_fee = request.POST.get('third_term_fee'),       
                )
                return HttpResponseRedirect(reverse(elec_l3_b))
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    



# ELECTRICITY ACTIONS ADD, UPDATE, DELETE
def add_elec_l3_b(request):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            current_year = datetime.datetime.today().year
            trades = Trade.objects.all()
            if request.method == 'POST':
                post = Student()
                post.first_name = request.POST.get('firstname')
                post.last_name = request.POST.get('lastname')
                post.trade = request.POST.get('trade')
                post.level = request.POST.get('level')
                post.status = request.POST.get('status')
                post.dob = request.POST.get('dob')
                post.gender = request.POST.get('gender')
                post.index_no = request.POST.get('senior_3_code')
                post.father_names = request.POST.get('father_names')
                post.mother_name = request.POST.get('mother_names')
                post.father_id = request.POST.get('father_id')
                post.father_tel = request.POST.get('father_tel')
                post.mother_tel = request.POST.get('mother_tel')
                post.province = request.POST.get('province')
                post.district = request.POST.get('district')
                post.sector = request.POST.get('sector')
                post.village = request.POST.get('village')
                post.graduated = request.POST.get('graduated')
                post.start_year = request.POST.get('start_year')
                post.save()
                return redirect(elec_l3_b)
            return render(request, 'burser/elec/l3/actions/add.html', {
                "trades": trades,
                "year": current_year
            })
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    


def delete_elec_l3_b(request, id):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            if request.method == 'POST':
                student = Student.objects.get(pk=id)
                student.delete()
            return HttpResponseRedirect(reverse(elec_l3_b))
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    


def edit_elec_l3_b(request, id):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            elec_l3_student_edit = get_object_or_404(Student, pk=id)
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    first_name = request.POST.get('firstname'),
                    last_name = request.POST.get('lastname'),
                    index_no = request.POST.get('senior_3_code'),
                    father_names = request.POST.get('father_names'),
                    mother_name = request.POST.get('mother_names'),
                    father_id = request.POST.get('father_id'),
                    father_tel = request.POST.get('father_tel'),
                    mother_tel = request.POST.get('mother_tel'),
                    province = request.POST.get('province'),
                    district = request.POST.get('district'),
                    sector = request.POST.get('sector'),
                    village = request.POST.get('village'),            
                )

                return redirect(elec_l3_b)
            return render(request, 'burser/elec/l3/actions/edit.html', {
                "student": elec_l3_student_edit
            })

            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    

    





def elec_l4_b(request):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            students = Student.objects.filter(trade = "ELEC", level='L4', graduated='False')
            Fix_Fee = Fixed_Fee.objects.all()
            Fix_Fee_day = Fixed_Fee_Day.objects.all()
            return render(request, 'burser/elec/l4/l4.html', {
                "students": students,
                "Fixed_Fee": Fix_Fee,
                "Fixed_Fee_day": Fix_Fee_day,
            })

            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    

def add_elec_l4_payement(request, id):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            if request.method == 'POST':
                Student.objects.filter(pk=id).update(
                    first_term_fee = request.POST.get('first_term_fee'),
                    second_term_fee = request.POST.get('second_term_fee'),
                    third_term_fee = request.POST.get('third_term_fee'),       
                )
                return HttpResponseRedirect(reverse(elec_l4_b))
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    



# ELECTRICITY ACTIONS ADD, UPDATE, DELETE
def add_elec_l4_b(request):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            trades = Trade.objects.all()
            current_year = datetime.datetime.today().year
            if request.method == 'POST':
                post = Student()
                post.first_name = request.POST.get('firstname')
                post.last_name = request.POST.get('lastname')
                post.trade = request.POST.get('trade')
                post.level = request.POST.get('level')
                post.status = request.POST.get('status')
                post.dob = request.POST.get('dob')
                post.gender = request.POST.get('gender')
                post.index_no = request.POST.get('senior_3_code')
                post.father_names = request.POST.get('father_names')
                post.mother_name = request.POST.get('mother_names')
                post.father_id = request.POST.get('father_id')
                post.father_tel = request.POST.get('father_tel')
                post.mother_tel = request.POST.get('mother_tel')
                post.province = request.POST.get('province')
                post.district = request.POST.get('district')
                post.sector = request.POST.get('sector')
                post.village = request.POST.get('village')
                post.graduated = request.POST.get('graduated')
                post.start_year = request.POST.get('start_year')
                post.save()
                return redirect(elec_l4_b)
            return render(request, 'burser/elec/l4/actions/add.html', {
                "trades": trades,
                "year": current_year
            })
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    


def delete_elec_l4_b(request, id):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            if request.method == 'POST':
                student = Student.objects.get(pk=id)
                student.delete()
            return HttpResponseRedirect(reverse(elec_l4_b))
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    


def edit_elec_l4_b(request, id):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:

            elec_l4_student_edit = get_object_or_404(Student, pk=id)
            
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    first_name = request.POST.get('firstname'),
                    last_name = request.POST.get('lastname'),
                    index_no = request.POST.get('senior_3_code'),
                    father_names = request.POST.get('father_names'),
                    mother_name = request.POST.get('mother_names'),
                    father_id = request.POST.get('father_id'),
                    father_tel = request.POST.get('father_tel'),
                    mother_tel = request.POST.get('mother_tel'),
                    province = request.POST.get('province'),
                    district = request.POST.get('district'),
                    sector = request.POST.get('sector'),
                    village = request.POST.get('village'),            
                )

                return redirect(elec_l4_b)
            return render(request, 'burser/elec/l4/actions/edit.html', {
                "student": elec_l4_student_edit
            })
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    




def elec_l5_b(request):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            students = Student.objects.filter(trade = "ELEC", level='L5', graduated='False')
            Fix_Fee = Fixed_Fee.objects.all()
            Fix_Fee_day = Fixed_Fee_Day.objects.all()
            return render(request, 'burser/elec/l5/l5.html', {
                "students": students,
                "Fixed_Fee": Fix_Fee,
                "Fixed_Fee_day": Fix_Fee_day,
            })
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    



def add_elec_l5_payement(request, id):

    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            if request.method == 'POST':
                Student.objects.filter(pk=id).update(
                    first_term_fee = request.POST.get('first_term_fee'),
                    second_term_fee = request.POST.get('second_term_fee'),
                    third_term_fee = request.POST.get('third_term_fee'),       
                )
                return HttpResponseRedirect(reverse(elec_l5_b))
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    



# ELECTRICITY ACTIONS ADD, UPDATE, DELETE

def add_elec_l5_b(request):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            current_year = datetime.datetime.today().year
            trades = Trade.objects.all()
            if request.method == 'POST':
                post = Student()
                post.first_name = request.POST.get('firstname')
                post.last_name = request.POST.get('lastname')
                post.trade = request.POST.get('trade')
                post.level = request.POST.get('level')
                post.status = request.POST.get('status')
                post.dob = request.POST.get('dob')
                post.gender = request.POST.get('gender')
                post.index_no = request.POST.get('senior_3_code')
                post.father_names = request.POST.get('father_names')
                post.mother_name = request.POST.get('mother_names')
                post.father_id = request.POST.get('father_id')
                post.father_tel = request.POST.get('father_tel')
                post.mother_tel = request.POST.get('mother_tel')
                post.province = request.POST.get('province')
                post.district = request.POST.get('district')
                post.sector = request.POST.get('sector')
                post.village = request.POST.get('village')
                post.graduated = request.POST.get('graduated')
                post.start_year = request.POST.get('start_year')
                post.save()
                return redirect(elec_l5_b)
            return render(request, 'burser/elec/l5/actions/add.html', {
                "trades": trades,
                "year": current_year
            })
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    


def delete_elec_l5_b(request, id):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            if request.method == 'POST':
                student = Student.objects.get(pk=id)
                student.delete()
            return HttpResponseRedirect(reverse(elec_l5_b))
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    


def edit_elec_l5_b(request, id):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            elec_l5_student_edit = get_object_or_404(Student, pk=id)
            
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    first_name = request.POST.get('firstname'),
                    last_name = request.POST.get('lastname'),
                    index_no = request.POST.get('senior_3_code'),
                    father_names = request.POST.get('father_names'),
                    mother_name = request.POST.get('mother_names'),
                    father_id = request.POST.get('father_id'),
                    father_tel = request.POST.get('father_tel'),
                    mother_tel = request.POST.get('mother_tel'),
                    province = request.POST.get('province'),
                    district = request.POST.get('district'),
                    sector = request.POST.get('sector'),
                    village = request.POST.get('village'),            
                )

                return redirect(elec_l5_b)
            return render(request, 'burser/elec/l5/actions/edit.html', {
                "student": elec_l5_student_edit
            })
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    



''' End of Electricity Views '''
















'''
    Begining of Software Development Views -> Patron
'''


def sod_l4_b(request):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            students = Student.objects.filter(trade = "SOD", level='L4', graduated='False')
            Fix_Fee = Fixed_Fee.objects.all()
            Fix_Fee_day = Fixed_Fee_Day.objects.all()
            return render(request, 'burser/sod/l4/l4.html', {
                "students": students,
                "Fixed_Fee": Fix_Fee,
                "Fixed_Fee_day": Fix_Fee_day,
            })
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    



def add_sod_l4_payement(request, id):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            if request.method == 'POST':
                Student.objects.filter(pk=id).update(
                    first_term_fee = request.POST.get('first_term_fee'),
                    second_term_fee = request.POST.get('second_term_fee'),
                    third_term_fee = request.POST.get('third_term_fee'),       
                )
                return HttpResponseRedirect(reverse(sod_l4_b))
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    


# SOFTWARE DEVELOPMENT ACTIONS ADD, UPDATE, DELETE

def add_sod_l4_b(request):

    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:

            current_year = datetime.datetime.today().year
            trades = Trade.objects.all()
            if request.method == 'POST':
                post = Student()
                post.first_name = request.POST.get('firstname')
                post.last_name = request.POST.get('lastname')
                post.trade = request.POST.get('trade')
                post.level = request.POST.get('level')
                post.status = request.POST.get('status')
                post.dob = request.POST.get('dob')
                post.gender = request.POST.get('gender')
                post.index_no = request.POST.get('senior_3_code')
                post.father_names = request.POST.get('father_names')
                post.mother_name = request.POST.get('mother_names')
                post.father_id = request.POST.get('father_id')
                post.father_tel = request.POST.get('father_tel')
                post.mother_tel = request.POST.get('mother_tel')
                post.province = request.POST.get('province')
                post.district = request.POST.get('district')
                post.sector = request.POST.get('sector')
                post.village = request.POST.get('village')
                post.graduated = request.POST.get('graduated')
                post.start_year = request.POST.get('start_year')
                post.save()
                return redirect(sod_l4_b)
            return render(request, 'burser/sod/l4/actions/add.html', {
                "trades": trades,
                "year": current_year
            })            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    



def delete_sod_l4_b(request, id):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            if request.method == 'POST':
                student = Student.objects.get(pk=id)
                student.delete()
            return HttpResponseRedirect(reverse(sod_l4_b))
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    


def edit_sod_l4_b(request, id):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            sod_l4_student_edit = get_object_or_404(Student, pk=id)
            
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    first_name = request.POST.get('firstname'),
                    last_name = request.POST.get('lastname'),
                    index_no = request.POST.get('senior_3_code'),
                    father_names = request.POST.get('father_names'),
                    mother_name = request.POST.get('mother_names'),
                    father_id = request.POST.get('father_id'),
                    father_tel = request.POST.get('father_tel'),
                    mother_tel = request.POST.get('mother_tel'),
                    province = request.POST.get('province'),
                    district = request.POST.get('district'),
                    sector = request.POST.get('sector'),
                    village = request.POST.get('village'),            
                )

                return redirect(sod_l4_b)
            return render(request, 'burser/sod/l4/actions/edit.html', {
                "student": sod_l4_student_edit
            })
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    




def sod_l5_b(request):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            students = Student.objects.filter(trade = "SOD", level='L5', graduated='False')
            Fix_Fee = Fixed_Fee.objects.all()
            Fix_Fee_day = Fixed_Fee_Day.objects.all()
            return render(request, 'burser/sod/l5/l5.html', {
                "students": students,
                "Fixed_Fee": Fix_Fee,
                "Fixed_Fee_day": Fix_Fee_day,
            })
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    



def add_sod_l5_payement(request, id):

    if request.method == 'POST':
        Student.objects.filter(pk=id).update(
            first_term_fee = request.POST.get('first_term_fee'),
            second_term_fee = request.POST.get('second_term_fee'),
            third_term_fee = request.POST.get('third_term_fee'),       
        )
        return HttpResponseRedirect(reverse(sod_l5_b))

# ELECTRICITY ACTIONS ADD, UPDATE, DELETE
def add_sod_l5_b(request):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            current_year = datetime.datetime.today().year
            trades = Trade.objects.all()
            if request.method == 'POST':
                post = Student()
                post.first_name = request.POST.get('firstname')
                post.last_name = request.POST.get('lastname')
                post.trade = request.POST.get('trade')
                post.level = request.POST.get('level')
                post.status = request.POST.get('status')
                post.dob = request.POST.get('dob')
                post.gender = request.POST.get('gender')
                post.index_no = request.POST.get('senior_3_code')
                post.father_names = request.POST.get('father_names')
                post.mother_name = request.POST.get('mother_names')
                post.father_id = request.POST.get('father_id')
                post.father_tel = request.POST.get('father_tel')
                post.mother_tel = request.POST.get('mother_tel')
                post.province = request.POST.get('province')
                post.district = request.POST.get('district')
                post.sector = request.POST.get('sector')
                post.village = request.POST.get('village')
                post.graduated = request.POST.get('graduated')
                post.start_year = request.POST.get('start_year')
                post.save()
                return redirect(sod_l5_b)
            return render(request, 'burser/sod/l5/actions/add.html', {
                "trades": trades,
                "year": current_year,
            })
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    


def delete_sod_l5_b(request, id):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            if request.method == 'POST':
                student = Student.objects.get(pk=id)
                student.delete()
            return HttpResponseRedirect(reverse(sod_l5_b))
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    


def edit_sod_l5_b(request, id):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            sod_l5_student_edit = get_object_or_404(Student, pk=id)
            
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    first_name = request.POST.get('firstname'),
                    last_name = request.POST.get('lastname'),
                    index_no = request.POST.get('senior_3_code'),
                    father_names = request.POST.get('father_names'),
                    mother_name = request.POST.get('mother_names'),
                    father_id = request.POST.get('father_id'),
                    father_tel = request.POST.get('father_tel'),
                    mother_tel = request.POST.get('mother_tel'),
                    province = request.POST.get('province'),
                    district = request.POST.get('district'),
                    sector = request.POST.get('sector'),
                    village = request.POST.get('village'),            
                )

                return redirect(sod_l5_b)
            return render(request, 'burser/sod/l5/actions/edit.html', {
                "student": sod_l5_student_edit
            })
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    





''' End of Software Development Views '''



''' FIXED FEES '''

# Boarding Fixed Fee

def B_Fixed_Fee(request):
    if request.user.email.endswith('burser@gmail.com'):
        if request.user.is_authenticated:
            fixed_boarding = Fixed_Fee.objects.all()

            return HttpResponseRedirect(reverse(burser_user))

            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    






# Class Teacherss View


'''
This is CST L3 Class Teacher
'''



def cst_l3_teacher(request):
    if request.user.email.endswith('cst@gmail.com'):
        if request.user.is_authenticated:
            trades = Trade.objects.all()
            students = Student.objects.filter(trade = "CST", level='L3', graduated='False')
            return render(request, 'trainers/cst/l3/l3.html', {
                "students": students,
                "trades": trades,
            })

        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    


# CST ACTIONS ADD, UPDATE, DELETE

def view_cst_l3_d(request, id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse(cst_l3_d))

def promote_cst_l3_teacher(request, id):  
    if request.user.email.endswith('cst@gmail.com'):
        if request.user.is_authenticated:
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    trade = request.POST.get('trade'),
                    level = request.POST.get('level'),
                    first_term_fee = request.POST.get('first_term_fee'),
                    second_term_fee = request.POST.get('second_term_fee'),
                    third_term_fee = request.POST.get('third_term_fee'),
                )
                return HttpResponseRedirect(reverse(cst_l3_teacher))
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    



def day_students_for_cst(request):
    if request.user.email.endswith('cst@gmail.com'):
        if request.user.is_authenticated:
            current_year = datetime.datetime.today().year
            students = Student.objects.filter(status='Day', graduated='False', trade='CST', level='L3')


            return render(request, 'trainers/cst/l3/status/day.html', {
                "students":students,
                "year": current_year,
            })

            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)      


def boarding_students_for_cst(request):
    if request.user.email.endswith('cst@gmail.com'):
        if request.user.is_authenticated:

            current_year = datetime.datetime.today().year
            students = Student.objects.filter(status='Boarding', graduated='False', trade='CST', level='L3')


            return render(request, 'trainers/cst/l3/status/boarding.html', {
                "students":students,
                "year": current_year,
            })
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)   




'''
This is RCPO L3 Class Teacher
'''



def rcpo_l3_teacher(request):
    if request.user.email.endswith('rcpol3@gmail.com'):
        if request.user.is_authenticated:
            trades = Trade.objects.all()
            students = Student.objects.filter(trade = "RCPO", level='L3', graduated='False')
            return render(request, 'trainers/rcpo/l3/l3.html', {
                "students": students,
                "trades": trades,
            })
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)   


# CST ACTIONS ADD, UPDATE, DELETE


def promote_rcpo_l3_teacher(request, id):  
    if request.user.email.endswith('rcpol3@gmail.com'):
        if request.user.is_authenticated:

            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    trade = request.POST.get('trade'),
                    level = request.POST.get('level'),
                    first_term_fee = request.POST.get('first_term_fee'),
                    second_term_fee = request.POST.get('second_term_fee'),
                    third_term_fee = request.POST.get('third_term_fee'),
                )
                return HttpResponseRedirect(reverse(rcpo_l3_teacher))


            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)   

def day_students_for_rcpo(request):
    if request.user.email.endswith('rcpol3@gmail.com'):
        if request.user.is_authenticated:

            current_year = datetime.datetime.today().year
            students = Student.objects.filter(status='Day', graduated='False', trade='RCPO', level='L3')


            return render(request, 'trainers/rcpo/l3/status/day.html', {
                "students":students,
                "year": current_year,
            })
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)   


def boarding_students_for_rcpo(request):
    if request.user.email.endswith('rcpol3@gmail.com'):
        if request.user.is_authenticated:

            current_year = datetime.datetime.today().year
            students = Student.objects.filter(status='Boarding', graduated='False', trade='RCPO', level='L3')


            return render(request, 'trainers/rcpo/l3/status/boarding.html', {
                "students":students,
                "year": current_year,
            })
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)   




def rcpo_l4_teacher(request):
    if request.user.email.endswith('rcpol4@gmail.com'):
        if request.user.is_authenticated:
            trades = Trade.objects.all()
            students = Student.objects.filter(trade = "RCPO", level='L4', graduated='False')
            return render(request, 'trainers/rcpo/l4/l4.html', {
                "students": students,
                "trades": trades,
            })
            
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)   
    



# CST ACTIONS ADD, UPDATE, DELETE





def promote_rcpo_l4_teacher(request, id):  
    if request.user.email.endswith('rcpol4@gmail.com'):
        if request.user.is_authenticated:
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    trade = request.POST.get('trade'),
                    level = request.POST.get('level'),
                    first_term_fee = request.POST.get('first_term_fee'),
                    second_term_fee = request.POST.get('second_term_fee'),
                    third_term_fee = request.POST.get('third_term_fee'),
                )
                return HttpResponseRedirect(reverse(rcpo_l4_teacher))
            
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)   
    



def day_students_for_rcpo_l4(request):
    if request.user.email.endswith('rcpol4@gmail.com'):
        if request.user.is_authenticated:

            current_year = datetime.datetime.today().year
            students = Student.objects.filter(status='Day', graduated='False', trade='RCPO', level='L4')            
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)   
    



    return render(request, 'trainers/rcpo/l4/status/day.html', {
        "students":students,
        "year": current_year,
    })

def boarding_students_for_rcpo_l4(request):
    if request.user.email.endswith('rcpol4@gmail.com'):
        if request.user.is_authenticated:

            current_year = datetime.datetime.today().year
            students = Student.objects.filter(status='Boarding', graduated='False', trade='RCPO', level='L4')


            return render(request, 'trainers/rcpo/l4/status/boarding.html', {
                "students":students,
                "year": current_year,
            })            
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)   
    






def rcpo_l5_teacher(request):
    if request.user.email.endswith('rcpol5@gmail.com'):
        if request.user.is_authenticated:

            current_year = datetime.datetime.today().year
            trades = Trade.objects.all()
            students = Student.objects.filter(trade = "RCPO", level='L5', graduated='False')
            return render(request, 'trainers/rcpo/l5/l5.html', {
                "students": students,
                "trades": trades,
                "year": current_year,
            })            
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)   
    





def promote_rcpo_l5_teacher(request, id):  
    if request.user.email.endswith('rcpol5@gmail.com'):
        if request.user.is_authenticated:
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    trade = request.POST.get('trade'),
                    level = request.POST.get('level'),
                    first_term_fee = request.POST.get('first_term_fee'),
                    second_term_fee = request.POST.get('second_term_fee'),
                    third_term_fee = request.POST.get('third_term_fee'),
                )
                return HttpResponseRedirect(reverse(rcpo_l5_teacher))
            
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)   


def day_students_for_rcpo_l5(request):
    if request.user.email.endswith('rcpol5@gmail.com'):
        if request.user.is_authenticated:
            current_year = datetime.datetime.today().year
            students = Student.objects.filter(status='Day', graduated='False', trade='RCPO', level='L5')


            return render(request, 'trainers/rcpo/l5/status/day.html', {
                "students":students,
                "year": current_year,
            })
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)   
    


def boarding_students_for_rcpo_l5(request):
    if request.user.email.endswith('rcpol5@gmail.com'):
        if request.user.is_authenticated:
            current_year = datetime.datetime.today().year
            students = Student.objects.filter(status='Boarding', graduated='False', trade='RCPO', level='L5')


            return render(request, 'trainers/rcpo/l5/status/boarding.html', {
                "students":students,
                "year": current_year,
            })            
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login) 



def graduate_rcpo_l5_t(request, id):  
    if request.user.email.endswith('rcpol5@gmail.com'):
        if request.user.is_authenticated:
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    graduated = request.POST.get('graduated'),
                    g_year = request.POST.get('g_year'),
                )
                return HttpResponseRedirect(reverse(rcpo_l5_teacher))
          
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login) 


# LAND SURVEYING LEVEL 3 -> TRAINERS




def ls_l3_teacher(request):
    if request.user.email.endswith('lsl3@gmail.com'):
        if request.user.is_authenticated:
            trades = Trade.objects.all()
            students = Student.objects.filter(trade = "LS", level='L3', graduated='False')
            return render(request, 'trainers/ls/l3/l3.html', {
                "students": students,
                "trades": trades,
            })          
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login) 



# CST ACTIONS ADD, UPDATE, DELETE


def promote_ls_l3_teacher(request, id):  
    if request.user.email.endswith('lsl3@gmail.com'):
        if request.user.is_authenticated:
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    trade = request.POST.get('trade'),
                    level = request.POST.get('level'),
                    first_term_fee = request.POST.get('first_term_fee'),
                    second_term_fee = request.POST.get('second_term_fee'),
                    third_term_fee = request.POST.get('third_term_fee'),
                )
                return HttpResponseRedirect(reverse(ls_l3_teacher))
          
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login) 


def day_students_for_ls_l3(request):
    if request.user.email.endswith('lsl3@gmail.com'):
        if request.user.is_authenticated:
            current_year = datetime.datetime.today().year
            students = Student.objects.filter(status='Day', graduated='False', trade='LS', level='L3')


            return render(request, 'trainers/ls/l3/status/day.html', {
                "students":students,
                "year": current_year,
            })          
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)


def boarding_students_for_ls_l3(request):
    if request.user.email.endswith('lsl3@gmail.com'):
        if request.user.is_authenticated:
            current_year = datetime.datetime.today().year
            students = Student.objects.filter(status='Boarding', graduated='False', trade='LS', level='L3')


            return render(request, 'trainers/ls/l3/status/boarding.html', {
                "students":students,
                "year": current_year,
            })          
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)




def ls_l4_teacher(request):
    if request.user.email.endswith('lsl4@gmail.com'):
        if request.user.is_authenticated:
            trades = Trade.objects.all()
            students = Student.objects.filter(trade = "LS", level='L4', graduated='False')
            return render(request, 'trainers/ls/l4/l4.html', {
                "students": students,
                "trades": trades,
            })            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)



# CST ACTIONS ADD, UPDATE, DELETE


def promote_ls_l4_teacher(request, id): 
    if request.user.email.endswith('lsl4@gmail.com'):
        if request.user.is_authenticated:
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    trade = request.POST.get('trade'),
                    level = request.POST.get('level'),
                    first_term_fee = request.POST.get('first_term_fee'),
                    second_term_fee = request.POST.get('second_term_fee'),
                    third_term_fee = request.POST.get('third_term_fee'),
                )
                return HttpResponseRedirect(reverse(ls_l4_teacher))

          
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login) 

def day_students_for_ls_l4(request):
    if request.user.email.endswith('lsl4@gmail.com'):
        if request.user.is_authenticated:
            current_year = datetime.datetime.today().year
            students = Student.objects.filter(status='Day', graduated='False', trade='LS', level='L4')


            return render(request, 'trainers/ls/l4/status/day.html', {
                "students":students,
                "year": current_year,
            })          
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)


def boarding_students_for_ls_l4(request):
    if request.user.email.endswith('lsl4@gmail.com'):
        if request.user.is_authenticated:
            current_year = datetime.datetime.today().year
            students = Student.objects.filter(status='Boarding', graduated='False', trade='LS', level='L4')


            return render(request, 'trainers/ls/l4/status/boarding.html', {
                "students":students,
                "year": current_year,
            })          
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)



def ls_l5_teacher(request):
    if request.user.email.endswith('lsl5@gmail.com'):
        if request.user.is_authenticated:
            current_year = datetime.datetime.today().year
            trades = Trade.objects.all()
            students = Student.objects.filter(trade = "LS", level='L5', graduated='False')
            return render(request, 'trainers/ls/l5/l5.html', {
                "students": students,
                "trades": trades,
                "year": current_year,
            })          
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)



# CST ACTIONS ADD, UPDATE, DELETE

def day_students_for_ls_l5(request):
    if request.user.email.endswith('lsl5@gmail.com'):
        if request.user.is_authenticated:
            current_year = datetime.datetime.today().year
            students = Student.objects.filter(status='Day', graduated='False', trade='LS', level='L5')


            return render(request, 'trainers/ls/l5/status/day.html', {
                "students":students,
                "year": current_year,
            })          
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)


def boarding_students_for_ls_l5(request):
    if request.user.email.endswith('lsl5@gmail.com'):
        if request.user.is_authenticated:
            current_year = datetime.datetime.today().year
            students = Student.objects.filter(status='Boarding', graduated='False', trade='LS', level='L5')


            return render(request, 'trainers/ls/l5/status/boarding.html', {
                "students":students,
                "year": current_year,
            })          
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)


def graduate_ls_l5_t(request, id):  
    if request.user.email.endswith('lsl5@gmail.com'):
        if request.user.is_authenticated:
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    graduated = request.POST.get('graduated'),
                    g_year = request.POST.get('g_year'),
                )
                return HttpResponseRedirect(reverse(ls_l5_teacher))          
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)









def elec_l3_teacher(request):
    if request.user.email.endswith('elecl3@gmail.com'):
        if request.user.is_authenticated:
            trades = Trade.objects.all()
            students = Student.objects.filter(trade = "ELEC", level='L3', graduated='False')
            return render(request, 'trainers/elec/l3/l3.html', {
                "students": students,
                "trades": trades,
            })          
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)



# CST ACTIONS ADD, UPDATE, DELETE


def promote_elec_l3_teacher(request, id):  
    if request.user.email.endswith('elecl3@gmail.com'):
        if request.user.is_authenticated:
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    trade = request.POST.get('trade'),
                    level = request.POST.get('level'),
                    first_term_fee = request.POST.get('first_term_fee'),
                    second_term_fee = request.POST.get('second_term_fee'),
                    third_term_fee = request.POST.get('third_term_fee'),
                )
                return HttpResponseRedirect(reverse(elec_l3_teacher))

          
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)

def day_students_for_elec_l3(request):
    if request.user.email.endswith('elecl3@gmail.com'):
        if request.user.is_authenticated:
          
            current_year = datetime.datetime.today().year
            students = Student.objects.filter(status='Day', graduated='False', trade='ELEC', level='L3')


            return render(request, 'trainers/elec/l3/status/day.html', {
                "students":students,
                "year": current_year,
            })            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)    


def boarding_students_for_elec_l3(request):
    if request.user.email.endswith('elecl3@gmail.com'):
        if request.user.is_authenticated:
            current_year = datetime.datetime.today().year
            students = Student.objects.filter(status='Boarding', graduated='False', trade='ELEC', level='L3')


            return render(request, 'trainers/elec/l3/status/boarding.html', {
                "students":students,
                "year": current_year,
            })
          
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)  







def elec_l4_teacher(request):
    if request.user.email.endswith('elecl4@gmail.com'):
        if request.user.is_authenticated:
            trades = Trade.objects.all()
            students = Student.objects.filter(trade = "ELEC", level='L4', graduated='False')
            return render(request, 'trainers/elec/l4/l4.html', {
                "students": students,
                "trades": trades,
            })          
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)  



# CST ACTIONS ADD, UPDATE, DELETE


def promote_elec_l4_teacher(request, id):  
    if request.user.email.endswith('elecl4@gmail.com'):
        if request.user.is_authenticated:
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    trade = request.POST.get('trade'),
                    level = request.POST.get('level'),
                    first_term_fee = request.POST.get('first_term_fee'),
                    second_term_fee = request.POST.get('second_term_fee'),
                    third_term_fee = request.POST.get('third_term_fee'),
                )
                return HttpResponseRedirect(reverse(elec_l4_teacher))          
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login) 



def day_students_for_elec_l4(request):
    if request.user.email.endswith('elecl4@gmail.com'):
        if request.user.is_authenticated:
            current_year = datetime.datetime.today().year
            students = Student.objects.filter(status='Day', graduated='False', trade='ELEC', level='L4')


            return render(request, 'trainers/elec/l4/status/day.html', {
                "students":students,
                "year": current_year,
            })          
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login) 


def boarding_students_for_elec_l4(request):
    if request.user.email.endswith('elecl4@gmail.com'):
        if request.user.is_authenticated:
            current_year = datetime.datetime.today().year
            students = Student.objects.filter(status='Boarding', graduated='False', trade='ELEC', level='L4')


            return render(request, 'trainers/elec/l4/status/boarding.html', {
                "students":students,
                "year": current_year,
            })
          
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login) 





def elec_l5_teacher(request):
    if request.user.email.endswith('elecl5@gmail.com'):
        if request.user.is_authenticated:
            current_year = datetime.datetime.today().year
            trades = Trade.objects.all()
            students = Student.objects.filter(trade = "ELEC", level='L5', graduated='False')
            return render(request, 'trainers/elec/l5/l5.html', {
                "students": students,
                "trades": trades,
                "year": current_year,
            })          
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login) 



# CST ACTIONS ADD, UPDATE, DELETE


def day_students_for_elec_l5(request):
    if request.user.email.endswith('elecl5@gmail.com'):
        if request.user.is_authenticated:
            current_year = datetime.datetime.today().year
            students = Student.objects.filter(status='Day', graduated='False', trade='ELEC', level='L5')


            return render(request, 'trainers/elec/l5/status/day.html', {
                "students":students,
                "year": current_year,
            })          
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login) 


def boarding_students_for_elec_l5(request):
    if request.user.email.endswith('elecl5@gmail.com'):
        if request.user.is_authenticated:
            current_year = datetime.datetime.today().year
            students = Student.objects.filter(status='Boarding', graduated='False', trade='ELEC', level='L5')


            return render(request, 'trainers/elec/l5/status/boarding.html', {
                "students":students,
                "year": current_year,
            })          
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login) 



def graduate_elec_l5_t(request, id):  
    if request.user.email.endswith('elecl5@gmail.com'):
        if request.user.is_authenticated:
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    graduated = request.POST.get('graduated'),
                    g_year = request.POST.get('g_year'),
                )
                return HttpResponseRedirect(reverse(elec_l5_teacher))

          
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login) 







def sod_l4_teacher(request):
    if request.user.email.endswith('sodl4@gmail.com'):
        if request.user.is_authenticated:
            trades = Trade.objects.all()
            students = Student.objects.filter(trade = "SOD", level='L4', graduated='False')
            return render(request, 'trainers/sod/l4/l4.html', {
                "students": students,
                "trades": trades,
            })            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login) 



# CST ACTIONS ADD, UPDATE, DELETE


def promote_sod_l4_teacher(request, id): 
    if request.user.email.endswith('sodl4@gmail.com'):
        if request.user.is_authenticated:
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    trade = request.POST.get('trade'),
                    level = request.POST.get('level'),
                    first_term_fee = request.POST.get('first_term_fee'),
                    second_term_fee = request.POST.get('second_term_fee'),
                    third_term_fee = request.POST.get('third_term_fee'),
                )
                return HttpResponseRedirect(reverse(sod_l4_teacher))
          
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login)  


def day_students_for_sod_l4(request):
    if request.user.email.endswith('sodl4@gmail.com'):
        if request.user.is_authenticated:
            current_year = datetime.datetime.today().year
            students = Student.objects.filter(status='Day', graduated='False', trade='SOD', level='L4')


            return render(request, 'trainers/sod/l4/status/day.html', {
                "students":students,
                "year": current_year,
            })          
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login) 


def boarding_students_for_sod_l4(request):
    if request.user.email.endswith('sodl4@gmail.com'):
        if request.user.is_authenticated:
            current_year = datetime.datetime.today().year
            students = Student.objects.filter(status='Boarding', graduated='False', trade='SOD', level='L4')


            return render(request, 'trainers/sod/l4/status/boarding.html', {
                "students":students,
                "year": current_year,
            })          
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login) 











def sod_l5_teacher(request):
    if request.user.email.endswith('sodl5@gmail.com'):
        if request.user.is_authenticated:
            current_year = datetime.datetime.today().year
            trades = Trade.objects.all()
            students = Student.objects.filter(trade = "SOD", level='L5', graduated='False')
            return render(request, 'trainers/sod/l5/l5.html', {
                "students": students,
                "trades": trades,
                "year": current_year,
            })            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login) 



# CST ACTIONS ADD, UPDATE, DELETE


def graduate_sod_l5_t(request, id):  
    if request.user.email.endswith('sodl5@gmail.com'):
        if request.user.is_authenticated:
            if request.method == "POST":
                Student.objects.filter(pk=id).update(
                    graduated = request.POST.get('graduated'),
                    g_year = request.POST.get('g_year'),
                )
                return HttpResponseRedirect(reverse(sod_l5_teacher))
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login) 




def day_students_for_sod_l5(request):
    if request.user.email.endswith('sodl5@gmail.com'):
        if request.user.is_authenticated:
            current_year = datetime.datetime.today().year
            students = Student.objects.filter(status='Day', graduated='False', trade='SOD', level='L5')


            return render(request, 'trainers/sod/l5/status/day.html', {
                "students":students,
                "year": current_year,
            })          
            
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login) 


def boarding_students_for_sod_l5(request):
    if request.user.email.endswith('sodl5@gmail.com'):
        if request.user.is_authenticated:
            current_year = datetime.datetime.today().year
            students = Student.objects.filter(status='Boarding', graduated='False', trade='SOD', level='L5')


            return render(request, 'trainers/sod/l5/status/boarding.html', {
                "students":students,
                "year": current_year,
            })
        
        else:
            return redirect(Login_User)
    else:
        logout_user(request)
        return redirect(Error_login) 
