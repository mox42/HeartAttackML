# Import libriray
import streamlit as st
import numpy as np
import requests
import pickle
import smtplib

# option menu
from streamlit_option_menu import option_menu 

# images
from PIL import Image

# animations
from streamlit_lottie import st_lottie  


def app_one(email=None):
    
    # Load the model
    loaded_model=pickle.load(open("Model_datasets/final_model.pickle","rb"))
    
    
    
    
    
    # Load images
    img_info1 = Image.open("Media/info1.jpg")
    img_info2 = Image.open("Media/info2.jpg")
    img_info3 = Image.open("Media/info3.jpg")
    img_info4 = Image.open("Media/info4.jpg")
    
    # Load lottie animations
    def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    anim_1 = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_zw7jo1.json")
    anim_2 = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_ggxx4yii.json")
    
    # Header style
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color: #FF4B4B;} 
    </style> """, unsafe_allow_html=True)
    
    
    # Horizontal menu
    selected = option_menu(None, ["App","Insight",'Contact'], 
        icons=['activity', "bi bi-info-circle", 'envelope'], 
        menu_icon="cast", default_index=0, orientation="horizontal",   styles={
        "container": {"padding": "5!important", "background-color": "#E3E7EC"},
        "icon": {"color": "black", "font-size": "16px"}, 
        "nav-link": {"font-size": "17px", "text-align": "centered", "margin":"0px", "font-family": " Calibri","--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#FF4B4B"},
    })
    
    
    
    # Email SMTP Server
    def sends(email, result):
       
        # Set up the SMTP server
        server = smtplib.SMTP('smtp.elasticemail.com', 2525)
        
        # Log in to the server
        username = 'HeartResult@heartml.me'
        password = '307F32BC8E1DE5F330393FC8092A03AEDCF6'
        server.login(username, password)
        
        # Send the email
        message = f'Subject: Heart Attack Prediction Result!\n\n{result}'
        sender_email = 'HeartResult@heartml.me'
        recipient_email = email
        server.sendmail(sender_email, recipient_email, message)
        
        # Quit the server
        server.quit()
             
    
    # App Section
    
    if selected == 'App':
        
        # Container is just for organizing the code
        with st.container(): 
            col1, col2 = st.columns(2)
            with col1:
                
                # Header
                st.markdown('<p class="font">Heart Attack Prediction App</p>', unsafe_allow_html=True)
    
                st.caption("This Web-App aims to identify the heart attack risk for people, based on their medical attributes to help **healthcare providers**.")
            
            with col2:
                st_lottie(anim_1, height=150, key="b")
    
    
            # ---- PREDICTION ----
            # Creating a function for Prediction
            def heartdisease_prediction (input_data):
                
                # changing the input data to a numpy array
                numpy_data= np.asarray(input_data)
           
                # Reshaping the numpy array as we are predicting for only on instance
                input_reshaped = numpy_data.reshape (1,-1)
                prediction = loaded_model.predict (input_reshaped)
                
                if (prediction[0] == 0):
                    st.success ("Great! The probability of having a heart attack is low. ✅")
                    txt="Congratulation! The probability of having a heart attack is low."
                    
                    # Result if (prediction=0) = expander 
                    with st.expander("Learn How to protect yourself (and your beloved heart)"):
                        
                        hide_anchor_link()
                        st.markdown("<h1 style='text-align: left;font-size:31px;'font-family':'Calibri'; color: black;'>Lifestyle Changes for Heart Attack Prevention</h1>", unsafe_allow_html=True)
                        st.image('https://cdn.dribbble.com/users/609665/screenshots/2992885/heart-dd.gif')
                        st.subheader("Stop smoking (and mean it)")
                        st.write("Avoid smoking, vaping or using other tobacco products.")
                        st.write("""People who smoke have more than twice the risk of a heart attack compared with people who don’t smoke, 
                                 Even one to two cigarettes a day greatly increases your risk of heart attack or stroke. """)
                        st.subheader("Healthy Eating Habits.")
                        st.write("""A diet full of a variety of fruit and vegetables is linked to healthier hearts and a lower risk of heart disease.""")
                        st.subheader("Move more")
                        url = "https://www.nhs.uk/conditions/heart-attack/prevention"
                        st.write("""Any physical activity is better than none. For more information visit [NHS heath website](%s)"""% url)
                
                
                
                else:
                    # Result if (prediction=0) = Warning 
                    st.error("Warning! The probability of having a heart attack is high.")
                    txt="Kindly consult a doctor immediately, You have high chance of having a heart attack."
                    st.subheader('Kindly consult a doctor immediately!')
                    
                # Return txt messege for email server
                return txt
            
            
            # String
            st.write('<p style="font-size:22px; color:black;">Please fill in the details and click on the button below</p>', unsafe_allow_html=True)

            # Obtain input data from the user
            age=st.select_slider ("Age",range(18,121,1))
            sex = st.radio("Gender", ('Male', 'Female'))
            cp = st.selectbox('Chest Pain Type',("Typical angina","Atypical angina","Non-anginal pain","Asymptomatic")) 
            trestbps=st.select_slider('Resting Blood Pressure',range(1,500,1))
            restecg=st.selectbox('Resting Electrocardiographic Results',("Nothing to note","ST-T Wave abnormality","Possible or definite left ventricular hypertrophy"))
            chol=st.select_slider('Cholesterol Level in mg/dl',range(1,500,1))
            fbs=st.radio("Fasting Blood Sugar higher than 120 mg/dl", ['Yes','No'])
            thalach=st.select_slider('Maximum Heart Rate Achieved',range(1,300,1))
            exang=st.radio('Exercise Induced Angina',["Yes","No"])
            oldpeak=st.number_input('Oldpeak')
            slope = st.selectbox('Heart Rate slope',("Upsloping: better heart rate with excercise(uncommon)","Flatsloping: minimal change(typical healthy heart)","Downsloping: signs of unhealthy heart"))
            ca=st.selectbox('Number of Major Vessels Colored by Fluorosopy',("0","1","2","3"))
            thal=st.selectbox('Thallium Stress Result',("Null","Fixed defect","Normal","Reversible defect"))
    
            # Condition for prediction (categorical input features )
            
            # Gender
            if sex=="male":
                sex=1 
            else:
                sex=0
    
            # Chest Pain Type
            if cp=="Typical angina":
                cp=0
            elif cp=="Atypical angina":
                cp=1
            elif cp=="Non-anginal pain":
                cp=2
            elif cp=="Asymptomatic":
                cp=3
                
            # Number of Major Vessels Colored by Flourosopy
            if ca=="0":
                ca=0
            elif ca=="1":
                ca=1
            elif ca=="2":
                ca=2
            elif ca=="3":
                ca=3  
                
            # Resting Blood Pressure
            if exang=="Yes":
                exang=1
            else:
                exang=0
    
            # Fasting Blood Sugar
            if fbs=="Yes":
                fbs=1
            else:
                fbs=0
    
            # Heart Rate slope
            if slope=="Upsloping: better heart rate with excercise(uncommon)":
                slope=0
            elif slope=="Flatsloping: minimal change(typical healthy heart)":
                slope=1
            elif slope=="Downsloping: signs of unhealthy heart":
                slope=2 
                
    
            # Thallium Stress Result
            if thal=="Fixed defect":
                thal=1
            elif thal=="Normal":
                thal=2
            elif thal=="Reversible defect":
                thal=3
            elif thal=="Null":
                thal=0
    
            # Resting Electrocardiographic Results
            if restecg=="Nothing to note":
                restecg=0
            elif restecg=="ST-T Wave abnormality":
                restecg=1
            elif restecg=="Possible or definite left ventricular hypertrophy":
                restecg=2

    
            # Note that Some of the features, such as age, trestbps, chol etc.. do not require if-else statements
            # because they are numerical inputs and can be directly used in the prediction model
    
                
    
            # Code for Prediction
            diagnosis = " "
            
            # Creating a button for Prediction
            if st.button ("Prediction"):
                diagnosis=heartdisease_prediction ([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])
                
                # Send result to user (from email server)
                sends(email, diagnosis) 
            
        

    
    # Insight Section
    
    if selected == 'Insight':
        
        st.image(img_info1)
        st.write("---")
        
        # Display YouTube video
        youtube_url = "https://www.youtube.com/watch?v=p6RJvWMgy5w"
        st.video(youtube_url)

        st.write("---")
        st.image(img_info2)
        st.write("---")
        st.image(img_info3)
        st.write("---")
        st.image(img_info4)
        st.write("---")
       
    
        
    # Contact Form Section
    
    if selected == 'Contact':

        st.markdown('<p class="font">Contact Form</p>', unsafe_allow_html=True)
        st.write('<p style="font-size:18px; color:grey;">If you have any questions or feedback, please fill out the contact form.</p>', unsafe_allow_html=True)
        st.write('<p style="font-size:18px; color:grey;">I will get in touch with you as soon as possible!</p>', unsafe_allow_html=True)
    
        # Contact Form
        contact_form = """
        <form action="https://formsubmit.co/mohammedqasem442@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email address" required>
        <textarea name="message" placeholder="Write Your message"></textarea>
        <button type="submit">Submit</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)
                
        # Load form style
        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        local_css("style/style.css")
             
        
    
        # Connect with us
        st.write("---")
        with st.container():
            left_column, right_column = st.columns(2)
            with right_column:
                st.write('')
                st.write('')
                st.write('')
                st.write('')
                st.write('<p style="font-size:22px; color:grey;">Connect with Us</p>', unsafe_allow_html=True)
                st.write("[Mohammed](https://www.linkedin.com/in/mo442/) | [Dalia](https://www.linkedin.com/in/dalia-aljahmani-900461262/) | [Rahaf](https://www.linkedin.com/in/rahaf-rsq/)")
                
            with left_column:
                st_lottie(anim_2, height=220, key="coding")

    # end of the function
    return


# ----- Customization -----

# sidebar background color
st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: #E3E7EC;
    }
</style>
""", unsafe_allow_html=True)


# Hide link of the text
def hide_anchor_link():
    st.markdown("""
        <style>
        .css-15zrgzn {display: none}
        .css-eczf16 {display: none}
        .css-jn99sy {display: none}
        </style>
        """, unsafe_allow_html=True) 
