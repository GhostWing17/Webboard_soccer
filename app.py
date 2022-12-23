import streamlit as st
from app_home import run_home_app
from app_total import run_total_app
from app_liverpool import run_liverpool_app
from app_arsenal import run_arsenal_app
from app_tottenham import run_tottenham_app
from app_manutd import run_manutd_app
from app_mancity import run_mancity_app

def main() :
    
    st.title('Welcome to Premier League!')
    
    st.sidebar.markdown('EPL Premier League')
    with st.sidebar:
        st.image("https://topnaija.ng/wp-content/uploads/2019/08/lo.gif")
        
    menu = ['Home', 'Total', 'Arsenal', 'Liverpool', 'Manchester United', 'Manchester City', 'Tottenham Hotspur']
    choice = st.sidebar.selectbox('Club Selection', menu)
    
    if choice == 'Home' :
        run_home_app()
    
    elif choice == 'Total' :
        run_total_app()
        
    elif choice == 'Arsenal' :
        run_arsenal_app()
        
    elif choice == 'Liverpool' :
        run_liverpool_app()
    
    elif choice == 'Manchester United' :
        run_manutd_app()
        
    elif choice == 'Manchester City' :
        run_mancity_app()
        
    elif choice == 'Tottenham Hotspur' :
        run_tottenham_app()
    
    
if __name__ == '__main__' :
    main()