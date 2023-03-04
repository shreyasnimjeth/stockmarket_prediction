import pickle
from pathlib import Path


import requests
import streamlit as st
import streamlit_authenticator as stauth
from streamlit_lottie import st_lottie
import pandas as pd
import altair as alt
alt.themes.enable("streamlit")
st.set_page_config(page_title="STOCK MARKET PREDICTION", page_icon=":tada:", layout="wide")
def app():
    with open('style1.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
    # --- USER AUTHENTICATION ---
    
    names = ["Shreyas Nimje"]
    usernames = ["shreyas"]
    
    # load hashed passwords
    file_path = Path(__file__).parent / "hashed_pw.pkl"
    with file_path.open("rb") as file:
        hashed_passwords = pickle.load(file)
    
    authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
        "sales_dashboard", "abcdef", cookie_expiry_days=30)
    
    
    st.header(' ')
    st.header(' ')
    st.header(' ')
    col1, col2, col3 = st.columns(3)
    with col1:
       st.write(' ')
    
    with col2:
        name, authentication_status, username = authenticator.login("Login", "main")
    
        if authentication_status == False:
            st.error("Username/password is incorrect")
    
        if authentication_status == None:
            st.warning("Please enter your username and password")
            
    with col3:
       st.write(' ')
    
    if authentication_status:
        # ---- READ EXCEL ----
        @st.cache
        def load_lottieurl(url):
            r = requests.get(url)
            if r.status_code !=200:
                    return None
            return r.json()
        
        #use css
        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
        local_css("style/style.css")
        
        #load animation
        lottie_down = load_lottieurl("https://assets8.lottiefiles.com/private_files/lf30_by9lgy8q.json")
        lottie_stock = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_kuhijlvx.json")
        lottie_coding = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_3rwasyjy.json")
        lottie_contact = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_kdx6cani.json")
        lottie_up = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_oat3z2uf.json")
        #header section
        
        
        
        
        left_column, right_column = st.columns(2)
        with left_column:
            st.subheader("Hi, Welcome :wave:")
            st.title('STOCK MARKET PREDICTION')
        
            st.write("Welcome to Stock Market Prediction Webpage, we'll help you to predict and analyse stock data in the best way.")
        
        
        with right_column:
                st_lottie(lottie_stock, height=300,key="stock")
        
        #container
        with st.container():
            st.write("---")
            left_column, right_column = st.columns(2)
            with left_column:
                st.write("##")
             
        #creat sidebar
        authenticator.logout("Logout", "sidebar")
        st.sidebar.title(f"Welcome {name}")
        st.sidebar.header("Select Stocks")
        
        def get_input():
            start_date = st.sidebar.text_input("Start Date", "01-11-2022")
            end_date = st.sidebar.text_input("End Date", "30-11-2022")
            stocks = ('WIPRO', 'NTPC', 'ITC', 'CANARA BANK')
            stock_symbol = st.sidebar.selectbox('Select Stocks for Prediction', stocks)
            
            years = st.sidebar.slider('Years of prediction:', 1, 8)
            period = years * 365
            return start_date, end_date, stock_symbol, years,period
        
        
        #fun for get company name
        def get_company_name(symbol):
            if symbol == 'WIPRO':
                return 'WIPRO'
            elif symbol == 'NTPC':
                return 'NTPC'
            elif symbol == 'ITC':
                return 'ITC'
            elif symbol == 'CANARA BANK':
                return 'CANARA BANK'
            else:
                'None'
                
        # fun for company data
        
        def get_data(symbol,start,end):
            
            #load data
            if symbol.upper()=='WIPRO':
                df = pd.read_csv("C:/Users/Shreyas Nimje/stockmarket_project/WIPRO.csv")
            elif symbol.upper() == 'NTPC':
                df = pd.read_csv("C:/Users/Shreyas Nimje/stockmarket_project/NTPC.csv")
            elif symbol.upper() == 'ITC':
                df = pd.read_csv("C:/Users/Shreyas Nimje/stockmarket_project/ITC.csv")
                
            elif symbol.upper() == 'CANARA BANK':
                df = pd.read_csv("C:/Users/Shreyas Nimje/stockmarket_project/canara.csv")
            else:
                df = pd.DataFrame(columns = ['Date','Open','High','Low','Close','No.of Shares','Total Turnover'])
                
        #get the date range
            start = pd.to_datetime(start)
            end = pd.to_datetime(end)
        
        #start and end index rows to 0
            start_row=0
            end_row=0
        
        #start the date from the top of the data set and go down
            for i in range(0,len(df)):
                if start <= pd.to_datetime(df['Date'][i]):
                    start_row = i
                    break
        #start from the bottom of the data set to go up
            for j in range(0, len(df)):
                if end>=pd.to_datetime(df['Date'][len (df) -1 - j]):
                    end_row = len(df) -1 - j
                    break
        
        #set the index to the date
            df = df.set_index(pd.DatetimeIndex(df['Date'].values))
            return df.iloc[start_row:end_row+1, :]
        
        #get the user input
        start,end, symbol,years,period = get_input()
        #get the data
        df = get_data(symbol,start,end)
        #get the company name
        company_name = get_company_name(symbol.upper())
        
        
        
        #display open prise
        col1, col2 = st.columns(2)
        with col1:
            st.header(company_name+" Open Prise\n")
            st.line_chart(df['Open'])
        with col2:
            st_lottie(lottie_up, height=300, key="up")
        
        #display Total Turnover
        col1, col2 = st.columns(2)
        with col2:
            st.header(company_name+" Total Turnover\n")
            st.line_chart(df['Total Turnover'])
        with col1:
            st_lottie(lottie_down, height=250, key="down")
        
        #statistic on data
        col1, col2 = st.columns(2)
        with col1:
            st.header('Data Statistics')
            st.write(df.describe())
        with col2:
            st_lottie(lottie_coding, height=300, key="coding")
        
        
        
        #contact form
        with st.container():
            st.write("---")
            st.header("Contact Us")
            st.write("##")
        
        contact_form = """
        
        <form action="https://formsubmit.co/shreyasnimjeth@gmail.com" method="POST">
             <input type="hidden" name="_captcha" value="false">     
             <input type="text" name="name" placeholder="Your name" required>
             <input type="email" name="email" placeholder="Your email" required>
             <textarea name="message" placeholder="Your message here" required></textarea>
             <button type="submit">Send</button>
        </form>
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st_lottie(lottie_contact, height=300, key="contact")
        
        
    
    
    
