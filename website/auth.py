from flask import Blueprint, render_template, request,flash

auth = Blueprint('auth',__name__)


@auth.route('/adminpage',methods =['GET','POST'] )
def admin():
    return render_template("adminpage.html")

@auth.route('/create-group',methods = ['GET','POST'])
def creategroup():
    return render_template("create-group.html")

@auth.route('/form',methods = ['GET','POST'])
def form():
    return render_template("form.html")

@auth.route('/results',methods = ['GET','POST'])
def results():
    return render_template("results.html")

# @auth.route('/login', methods=['GET','POST'])
# def login():
#     return render_template("home.html")

# @auth.route('/logout')
# def logout():
#     return "<p>Logout</p>"

# @auth.route('/sign-up',methods=['GET','POST'])
# def sign_up():
#     if request.method=='POST':
#         email = request.form.get('email')
#         firstName =request.form.get('firstName')
#         password1=request.form.get('password1')
#         password2=request.form.get('password2')

#         if len(email)<4:
#             flash('email must be greater than 4 characters',category='error')
#         elif len(firstName)<2:
#             flash('first name must be greater than 1 characters',category='error')
#         elif password1 !=password2:
#             flash('Passwords Don\'t match',category='error')
#         elif len(password1)<7:
#             flash('Password must be at least 7 characters',category='error')
#         else:
#             flash('Account created!',category='success')
    
#     return render_template("sign_up.html")