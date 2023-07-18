from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from django.contrib.sessions.models import Session

from .ctl.LoginCtl import LoginCtl
from .ctl.RegistrationCtl import RegistrationCtl
from .ctl.WelcomeCtl import WelcomeCtl
from .ctl.HomeCtl import HomeCtl
from .ctl.ForgetPasswordCtl import ForgetPasswordCtl
from .ctl.ChangePasswordCtl import ChangePasswordCtl
from .ctl.LogoutCtl import LogoutCtl
from .ctl.MyProfileCtl import MyProfileCtl
from .ctl.UserCtl import UserCtl
from .ctl.UserListCtl import UserListCtl
from .ctl.CourseCtl import CourseCtl
from .ctl.CourseListCtl import CourseListCtl
from .ctl.CollegeCtl import CollegeCtl
from .ctl.CollegeListCtl import CollegeListCtl
from .ctl.MarksheetCtl import MarksheetCtl
from .ctl.MarksheetListCtl import MarksheetListCtl
from .ctl.MarksheetMeritListCtl import MarksheetMeritListCtl
from .ctl.RoleCtl import RoleCtl
from .ctl.RoleListCtl import RoleListCtl
from .ctl.StudentCtl import StudentCtl
from .ctl.StudentListCtl import StudentListCtl
from .ctl.AddFacultyCtl import AddFacultyCtl
from .ctl.AddFacultyListCtl import AddFacultyListCtl
from .ctl.SubjectCtl import SubjectCtl
from .ctl.SubjectListCtl import SubjectListCtl
from .ctl.TimeTableCtl import TimeTableCtl
from .ctl.TimeTableListCtl import TimeTableListCtl


# @csrf_exempt
# def action(request, page, action=""):
#     ctlName = page + "Ctl()"
#     ctlObj = eval(ctlName)
#     return ctlObj.execute(request, {"id": 0})


'''
Calls respective controller with id
'''


@csrf_exempt
def actionId(request, page="", operation="", id=0):
    path = request.META.get('PATH_INFO')
    # print("VVVVVVVVVVVVVVVV", path)
    if request.session.get('user') is not None and page != "":
        ctlName = page + "Ctl()"
        ctlObj = eval(ctlName)
        request.session['msg'] = None
        res = ctlObj.execute(request, {"id": id})
    elif page == "Registration":
        ctlName = "Registration" + "Ctl()"
        ctlObj = eval(ctlName)
        res = ctlObj.execute(request, {"id": id})
    elif page == "Home":
        ctlName = "Home" + "Ctl()"
        ctlObj = eval(ctlName)
        print(ctlName, "temppp mesgggg")
        res = ctlObj.execute(request, {"id": id})
    elif page == "ForgetPassword":
        ctlName = "ForgetPassword" + "Ctl()"
        ctlObj = eval(ctlName)
        res = ctlObj.execute(request, {"id": id})
    elif page == "Login":
        ctlName = page + "Ctl()"
        ctlObj = eval(ctlName)
        request.session['msg'] = None
        print("MMMMMMMMMMM", request.session.get('msg'))
        res = ctlObj.execute(request, {"id": id, })

    else:
        ctlName = "Login" + "Ctl()"
        ctlObj = eval(ctlName)
        request.session['msg'] = "Your Session has been Expired, Please Login again"
        res = ctlObj.execute(request, {"id": id, 'path': path})
    return res


@csrf_exempt
def auth(request, page="", operation="", id=0):
    if page == "Logout":
        Session.objects.all().delete()
        request.session['user'] = None
        out = "LOGOUT SUCCESSFULL"
        ctlName = "Login" + "Ctl()"
        ctlObj = eval(ctlName)
        res = ctlObj.execute(request, {"id": id, "operation": operation, 'out': out})

    # elif page == "ForgetPassword":
    #     ctlName = "ForgetPassword" + "Ctl()"
    #     ctlObj = eval(ctlName)
    #     res = ctlObj.execute(request, {"id": id, "operation": operation})
    return res


def index(request):
    res = render(request, 'project.html')
    return res

# To remove Favicon error


def GET(self):
    return HttpResponse("Hello Guys")
