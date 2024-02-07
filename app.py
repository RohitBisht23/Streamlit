import streamlit as st

st.title('Title -> Hey Geeks, Welcome to GeeksForGeeks')
st.header('Header -> Hey Geeks, Welcome to GeeksForGeeks')
st.subheader('Sub-Header -> Hey Geeks, Welcome to GeeksForGeeks')
st.text('Text -> Hey Geeks, Welcome to GeeksForGeeks')

#Markdown
st.markdown('Hi')
st.markdown('# Hi')
st.markdown('## Hi')
st.markdown('### Hi')
st.markdown('#### Hi')
st.markdown('####### Hi')
st.markdown('######## Hi')
st.markdown('########## Hi')

st.success('success!')

st.info('Info')


st.warning('Worning')
st.error('Error')

#Custome error
st.subheader('Exception')
exp = ZeroDivisionError(' Division is not possible with 0')
st.exception(exp)

#Help function
st.subheader('Help')
st.help(ZeroDivisionError)

#How to write code
st.subheader('Write')
st.write("Range(1,10)")
st.write(range(1,10))

st.write("1 + 2 + 3")
st.write(1 + 2 + 3)

#Code
st.subheader('Code')
st.code('x * 10\n'
        '\tfor i in range(x):\n'
            't\print(i)'
            )

#Check box and radio button
st.subheader('Checkbox')
st.checkbox('Male')


if (st.checkbox('Adult')):
    st.write('You are an adult')

# st.radio('Select : ', ('Check', 'Uncheck'))
st.subheader('Radio Button')
radioBtn = st.radio('Select:', ('Male','Female','Other'))
if (radioBtn == 'Male'):
    st.write("You area a Male")
elif(radioBtn == 'Female'):
    st.write('You are Female')
else :
    st.write('You are other')

st.subheader('Select Box')
selectBox = st.selectbox('Data Science:', ['Data Analsis', 'Web Scraping',
                                           'Machine Learning','Deep Learning'
                                            'Natuaral Language Processing',
                                            'Computer vision','Image Processing'])

st.write("You've selected :", selectBox)

#MultiSelect Box
st.subheader('Multiselect Box')
multiSelBox = st.multiselect('Data Science:', ['Data Analsis', 'Web Scraping',
                                           'Machine Learning','Deep Learning'
                                            'Natuaral Language Processing',
                                            'Computer vision','Image Processing'])

if(len(multiSelBox) >= 1) :
    st.write("You've selected:",multiSelBox)


#Button
st.subheader('Button')
st.button('Cleck Here')

if(st.button('Cleck me')):
    st.warning('Thanks for clicking me')


#Sliders
st.subheader('Slider')
volume = st.slider('Select the volume', 1,10,step=1)
st.write('The volume is:',volume)

#Taking input from user
st.subheader("Taking user input")
name = st.text_input('Enter your name:')
age = st.text_input('Enter your age:')

if(name and age) :
    st.write('The user name is:', name)
    st.write('The user age is:',age)

username = st.text_input('username')
password = st.text_input('password',type='password')

#Text area
TextArea = st.text_area('Why should we hire you?',height=20)
btn = st.button('Submit')
# st.write(TextArea)
if(btn) :
    st.write(TextArea)


#Input number
st.subheader('Number')
no = st.number_input('Enter number:', 18,30)
st.write(no)

#Input date
st.subheader('Date')
date = st.date_input('select the appoiment the date:')
st.write('Your appoiment date is:',date)

#input Time
st.subheader('Time')
time = st.time_input('Enter the appoiment time:')
st.write('Your appoiment time is:',time)