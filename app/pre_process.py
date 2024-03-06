# Inital working version of https://www.kaggle.com/code/ivanovskia1/predicting-no-shows-at-medical-appointments#These-are-the-final-features-and--target-variable

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt


df = pd.read_csv("KaggleV2-May-2016.csv")

class Pre_process():
    def __init__(self, df):
        self.df = df

    def preprocess(self):
        self.df['No-show'].replace("No", 0,inplace=True)
        self.df['No-show'].replace("Yes", 1,inplace=True) 
        #Convert to Categorical
        self.df['Handcap'] = pd.Categorical(self.df['Handcap'])
        #Convert to Dummy Variables
        Handicap = pd.get_dummies(self.df['Handcap'], prefix = 'Handicap')
        self.df = pd.concat([self.df, Handicap], axis=1)
        self.df = self.df[(self.df.Age >= 0) & (self.df.Age <= 100)]


    def convert_datetime(self):
        # Converts the two variables to datetime variables
        self.df['ScheduledDay'] = pd.to_datetime(df['ScheduledDay'])
        self.df['AppointmentDay'] = pd.to_datetime(df['AppointmentDay'])


    def calc_waiting_time(self):
        # Create a variable called "AwaitingTime" by subtracting the date the patient made the appointment and the date of the appointment.
        self.df['AwaitingTime'] = self.df["AppointmentDay"].sub(self.df["ScheduledDay"], axis=0)
        # Convert the result "AwaitingTime" to number of days between appointment day and scheduled day. 
        self.df["AwaitingTime"] = (self.df["AwaitingTime"] / np.timedelta64(1, 'D')).abs()


    def calc_no_shows(self):
        # Number of Appointments Missed by Patient
        new_col = self.df.groupby('PatientId')['No-show'].apply(lambda x: x.cumsum())
        self.df["Num_App_Missed"] = new_col.reset_index(level=0, drop=True)
    
    def format_and_get_df(self):
        self.preprocess()
        self.convert_datetime()
        self.calc_waiting_time()
        self.calc_no_shows()
        return self.df
        


