
"""importing libraries"""


import numpy as np
import pickle
import streamlit as st
import sklearn
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler

"loading models"
loaded_model=pickle.load((open('svmmodel.pkl','rb')))
scaler_model=pickle.load((open('scaler.pkl','rb')))

#create a function for prediction
def arrival(input_data):
    #scaling

    scaled=scaler_model.transform(np.array([input_data]).reshape(1, -1))
    # change input to array
    #input_data_array = np.asarray(scaled)
    # reshape data
    input_data_reshaped = scaled.reshape(1,-1)
    # standardize data
    # input_data_std=scaler.transform(input_data_reshaped)
    prediction = loaded_model.predict(input_data_reshaped)
    #print(prediction)
    #prediction_label = [np.argmax(prediction])
    #print(prediction_label)
    if (prediction == 0):
        return 'May not  Arrive'
    else:
        return 'May arrive'


def main():
    #title
    st.title('Customer Arrival Web App')
    #getting i/p data
    #Age = st.text_input('Age of customer')
    Age= st.number_input('Age of Cutomer',min_value=1,max_value=130)
    #st.write('The current number is ', number)
    DaysSinceCreation = st.text_input('DaysSinceCreation')
    AverageLeadTime= st.text_input('AverageLeadTime')
    TotalRevenue= st.text_input('Total Revenue(LodgingRevenue+OtherRevenue)')
    PersonsNights=st.text_input('PersonsNights')
    DaysSinceFirstStay=st.text_input('DaysSinceFirstStay')
    SRHighFloor=st.text_input('SRHighFloor')
    SRLowFloor=st.text_input('SRLowFloor')
    SRAccessibleRoom=st.text_input('SRAccessibleRoom')
    SRMediumFloor=st.text_input('SRMediumFloor')
    SRBathtub=st.text_input('SRBathtub')
    SRShower=st.text_input('SRShower')
    SRCrib=st.text_input('SRCrib')
    SRKingSizeBed=st.text_input('SRKingSizeBed')
    SRTwinBed=st.text_input('SRTwinBed')
    SRAwayFromElevator=st.text_input('SRAwayFromElevator')
    SRQuietRoom=st.text_input('SRQuietRoom')
    DistributionChannel = st.selectbox('Enter DistributionChannel',('Travel_AgentOperator', 'Direct', 'Corporate','Electronic_Distribution'))
    if (DistributionChannel == 'Travel_AgentOperator'):
        Travel_AgentOperator = 1
        Direct = 0
        Corporate = 0
        Electronic_Distribution = 0

    elif (DistributionChannel == 'Direct'):
        Travel_AgentOperator = 0
        Direct = 1
        Corporate = 0
        Electronic_Distribution = 0

    elif (DistributionChannel == 'Electronic_Distribution'):
        Travel_AgentOperator = 0
        Direct = 0
        Corporate =0
        Electronic_Distribution = 1

    else:
        Travel_AgentOperator = 0
        Direct = 0
        Corporate = 0
        Electronic_Distribution = 0


    MarketSegment = st.selectbox('Enter MarketSegment',('Travel_AgentOperator1', 'Direct', 'Corporate', 'Complementary','Aviation','Other'))
    if (MarketSegment=='Travel_AgentOperator'):
        Travel_AgentOperator1 = 1
        Direct1 = 0
        Corporate = 0
        Complementary=0
        Aviation = 0
        Other=0

    elif (MarketSegment=='Direct'):
        Travel_AgentOperator1 = 0
        Direct1= 1
        Corporate = 0
        Complementary = 0
        Aviation = 0
        Other=0

    elif (MarketSegment=='Corporate'):
        Travel_AgentOperator1 = 0
        Direct1 = 0
        Corporate = 1
        Complementary = 0
        Aviation = 0
        Other=0
    elif (MarketSegment == 'Complementary'):
        Travel_AgentOperator1 = 0
        Direct1 = 0
        Corporate = 0
        Complementary = 1
        Aviation = 0
        Other = 0
    elif (MarketSegment == 'Aviation'):
        Travel_AgentOperator1 = 0
        Direct1 = 0
        Corporate = 0
        Aviation = 1
        Other = 0
    else:
        Travel_AgentOperator1 = 0
        Direct1 = 0
        Corporate = 0
        Aviation = 0
        Other = 0

 #prediction
    state=st.checkbox('Are the Values Entered True?',value=False)
    if (state==True):
        prediction=''
        if st.button('Will the customer arrive?'):
            prediction=arrival([Age,AverageLeadTime,PersonsNights,DaysSinceFirstStay,SRHighFloor,SRLowFloor,SRAccessibleRoom,SRMediumFloor,SRBathtub,SRShower,SRCrib,SRKingSizeBed,SRTwinBed,SRAwayFromElevator,SRQuietRoom,TotalRevenue,Complementary,Corporate,
                                Direct1,Other,Travel_AgentOperator1,Direct,Electronic_Distribution,Travel_AgentOperator])

            st.success(prediction)
    else:
        st.write('Enter correct values')



if __name__=='__main__':
    main()







