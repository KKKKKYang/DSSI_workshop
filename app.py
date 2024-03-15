import streamlit as st
from src.inference import get_prediction

#Initialise session state variable
if 'input_features' not in st.session_state:
    st.session_state['input_features'] = {}

def app_sidebar():
    st.sidebar.header('User Details')
    yearly_income=st.sidebar.number_input("Yearly Income",min_value=0,value=50000,step=1000)
    is_female=st.sidebar.radio("Gender",('Female','Male'))
    months_residence=st.sidebar.number_input("Months of Residence",min_value=0,value=12,step=1)
    dual_income=st.sidebar.radio("Dual Income",('Yes','No'))
    have_minors=st.sidebar.radio("Have Minors",('Yes','No'))
    
    def get_input_features():
        input_features = {'yearly_income': yearly_income,
                          'is_female': 1 if is_female == 'Female' else 0,
             'months_residence': months_residence,
             'dual_income': 1 if dual_income == 'Yes' else 0,
             'have_minors': 1 if have_minors == 'Yes' else 0
                         }
        return input_features
    
    
    sdb_col1, sdb_col2 = st.sidebar.columns(2)
    with sdb_col1:
        predict_button = st.sidebar.button("Assess", key="predict")
    with sdb_col2:
        reset_button = st.sidebar.button("Reset", key="clear")
    if predict_button:
        st.session_state['input_features'] = get_input_features()
    if reset_button:
        st.session_state['input_features'] = {}
    return None

def app_body():
    title = '<p style="font-family:arial, sans-serif; color:Black; font-size: 40px;"><b> Welcome to Coupon Decision System</b></p>'
    st.markdown(title, unsafe_allow_html=True)
    default_msg = '**System assessment says:** {}'
    if st.session_state['input_features']:
        assessment = get_prediction(yearly_income=st.session_state['input_features']['yearly_income'],
                                    is_female=st.session_state['input_features']['is_female'],
                                    months_residence=st.session_state['input_features']['months_residence'],
                                    dual_income=st.session_state['input_features']['dual_income'],
                                    have_minors=st.session_state['input_features']['have_minors'])
        if assessment ==1:
            st.success(default_msg.format('Approved'))
        else:
            st.warning(default_msg.format('Rejected'))
    return None

def main():
    app_sidebar()
    app_body()
    return None

if __name__ == "__main__":
    main()