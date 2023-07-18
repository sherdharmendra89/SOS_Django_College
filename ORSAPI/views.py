from django.views.decorators.csrf import csrf_exempt
from .restctl.ChangepasswordCtl import ChangepasswordCtl
from .restctl.CollegeCtl import CollegeCtl
from .restctl.CourseCtl import CourseCtl
from .restctl.FacultyCtl import FacultyCtl
from .restctl.ForgetpasswordCtl import ForgetpasswordCtl
from .restctl.LoginCtl import LoginCtl
from .restctl.MarksheetCtl import MarksheetCtl
from .restctl.RegistrationCtl import RegistrationCtl
from .restctl.RoleCtl import RoleCtl
from .restctl.StudentCtl import StudentCtl
from .restctl.SubjectCtl import SubjectCtl
from .restctl.TimeTableCtl import TimeTableCtl
from .restctl.UserCtl import UserCtl



# Create your view here
def info(request,page,action):
    print("Request Method -----",request.method)
    print("Page -----",page)
    print("Action -----", action)
    print("Base Path:---- ", __file__)


@csrf_exempt
def action(request,page,action="get",id=0,pageNo=1):
    print("ID ---",id)
    info(request,page,action)
    methodCall = page + "Ctl()." + action + "(request,{'id':id, 'pageNo':pageNo})"
    response = eval(methodCall)
    return response


