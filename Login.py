# Streamlit
import streamlit as st

# Title and icon
st.set_page_config(page_title="Heart Attack Prediction App", page_icon=":hearts:", layout="centered")

#Firebase
import pyrebase

# app page
import app


# Firebase configuration
firebaseConfig = {
    "apiKey": "AIzaSyDdMp9tkDf0mwQDKsI2Z7glVqmdUyydzK0",
    "authDomain": "streamlit-f5cf7.firebaseapp.com",
    "projectId": "streamlit-f5cf7",
    'databaseURL': "https://streamlit-f5cf7-default-rtdb.europe-west1.firebasedatabase.app/",
    "storageBucket": "streamlit-f5cf7.appspot.com",
    "messagingSenderId": "1029196011977",
    "appId": "1:1029196011977:web:f2ed3e0b3a02191ebc7018",
    "measurementId": "G-YHSD70R090"
  }


# Firebase Authentication
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# Authentication sidebar
choice = st.sidebar.selectbox('Login/Signup', ['Login', 'Sign up', 'Reset password'])


# Obtain User Input for email and password
email = st.sidebar.text_input('Please enter your email address')
# if not choosin reset password sidebar then there will be a password input
if choice != 'Reset password':
    password = st.sidebar.text_input('Please enter your password', type='password')
    
else:
    password = ''
    
    
# Login Block
if choice == 'Login':
    login = st.sidebar.checkbox('Login')
    if login:
        try:
            
            # Attempt to sign in with email and password
            user = auth.sign_in_with_email_and_password(email, password)
            
            #Run app function
            app.app_one(email)
            
        except Exception as e:
            # Display an error message if authentication fails
            st.error('Login Failed. Please check your email and password and try again.')
            st.write(e)
            
# Sign up Block
if choice == 'Sign up':
    submit = st.sidebar.button('Create my account')
    if submit:
        try:
            
            # Attempt to create a new user with email and password
            user = auth.create_user_with_email_and_password(email, password)
            st.success('Your account has been successfully created!')
            st.balloons()
            
            # Sign in
            user = auth.sign_in_with_email_and_password(email, password)
            st.info('Login via login drop down selection')
            
        except Exception as e:
            # Display an error message if user creation fails
            st.sidebar.error('Account creation failed. Please try again.')
            st.write(e)
            
# Reset Password Block
if choice == 'Reset password':
    submit = st.sidebar.button('Reset Password')
    if submit:
        try:
            #Reset Password
            auth.send_password_reset_email(email)
            st.success('A password reset email has been sent to your email address.')
        except Exception as e:
            st.sidebar.error('Password reset failed. Please try again.')
            st.write(e)


# ----- Customization -----

# Logo
with st.sidebar:
    st.image("https://i.imgur.com/aNTPhtD.png")


# Center an image on sidebar
st.markdown(
    """
    <style>
        [data-testid=stSidebar] [data-testid=stImage]{
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100%;
        }
    </style>
    """, unsafe_allow_html=True
)


# Sidebar background color
st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: #E3E7EC;
    }
</style>
""", unsafe_allow_html=True)


#Hide defult format
hide_default_format = """
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

# Hide full screen image
hide_img_fs = '''
<style>
button[title="View fullscreen"]{
    visibility: hidden;}
</style>
'''
st.markdown(hide_img_fs, unsafe_allow_html=True)

# Hide link of the text
def hide_anchor_link():
    st.markdown("""
        <style>
        .css-15zrgzn {display: none}
        .css-eczf16 {display: none}
        .css-jn99sy {display: none}
        </style>
        """, unsafe_allow_html=True) 
