import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder


df = pd.read_csv("KaggleV2-May-2016.csv")

class Pre_process():
    def __init__(self, df):
        self.df = df

    def _preprocess(self):
        self.df.rename(columns = {'ApointmentData':'AppointmentData',
                         'Alcoolism': 'Alchoholism',
                         'Hipertension': 'Hypertension',
                         'Handcap': 'Handicap'}, inplace = True)
        self.df['AppointmentDay'] = pd.to_datetime(self.df['AppointmentDay'])
        self.df['ScheduledDay'] = pd.to_datetime(self.df['ScheduledDay'])
        self.df['Sched_Appt'] = self.df['AppointmentDay'] - self.df['ScheduledDay']
        self.df['Sched_To_Appt'] = self.df['Sched_Appt'].dt.days
        self.df.replace([np.inf, -np.inf], np.nan, inplace=True)
        self.df['Gender'] = self.df['Gender'].apply(lambda x: 1 if x == 'F' else 0)
        self.df['No-show'] = self.df['No-show'].apply(lambda x: 1 if x == 'Yes' else 0)
        self.df = self.df[(self.df.Age >= 0) & (self.df.Age <= 100)]


    def _calc_date(self):
        # Converts the two variables to datetime variables
        self.df['ScheduledDay_DayOfWeek_Num'] = self.df['ScheduledDay'].dt.dayofweek
        self.df['ScheduledDay_DayOfWeek_Name'] = self.df['ScheduledDay'].dt.day_name()

    def _calc_awaiting_time(self):
        # Create a variable called "AwaitingTime" by subtracting the date the patient made the appointment and the date of the appointment.
        self.df['AwaitingTime'] = self.df["AppointmentDay"].sub(self.df["ScheduledDay"], axis=0)
        # Convert the result "AwaitingTime" to number of days between appointment day and scheduled day. 
        self.df["AwaitingTime"] = (self.df["AwaitingTime"] / np.timedelta64(1, 'D')).abs()

    def _calc_no_shows(self):
        # Number of Appointments Missed by Patient
        self.df['No-show'] = pd.to_numeric(self.df['No-show'], errors='coerce')
    
    def _split_day_month_year(self):
        self.df['ScheduledDay_Y'] = self.df['ScheduledDay'].dt.year
        self.df['ScheduledDay_M'] = self.df['ScheduledDay'].dt.month
        self.df['ScheduledDay_D'] = self.df['ScheduledDay'].dt.day
        self.df.drop(['ScheduledDay'], axis=1, inplace=True)

        self.df['AppointmentDay_Y'] = self.df['AppointmentDay'].dt.year
        self.df['AppointmentDay_M'] = self.df['AppointmentDay'].dt.month
        self.df['AppointmentDay_D'] = self.df['AppointmentDay'].dt.day
        self.df.drop(['AppointmentDay'], axis=1, inplace=True)
    
    def _add_labels(self):
        le = LabelEncoder()
        self.df['Gender'] = le.fit_transform(self.df['Gender'])
        le = LabelEncoder()
        self.df['Neighbourhood'] = le.fit_transform(self.df['Neighbourhood'])
        le = LabelEncoder()
        self.df['ScheduledDay_DOW'] = le.fit_transform(self.df['ScheduledDay_DayOfWeek_Name'])
        le = LabelEncoder()
        self.df['No-show'] = le.fit_transform(self.df['No-show'])
    
    def _final_tidy(self):
        self.df.PatientId = self.df.PatientId.astype(int)
        self.df.drop(['Sched_Appt'], axis=1, inplace=True)
        self.df.drop(['ScheduledDay_DayOfWeek_Name'], axis=1, inplace=True)
        self.df.drop(['PatientId'], axis=1, inplace=True)
        self.df.drop(['AppointmentID'], axis=1, inplace=True)
    
    def format_and_get_df(self):
        self._preprocess()
        self._calc_date()
        self._calc_awaiting_time()
        self._calc_no_shows()
        self._split_day_month_year()
        self._add_labels()
        self._final_tidy()
        return self.df
        


