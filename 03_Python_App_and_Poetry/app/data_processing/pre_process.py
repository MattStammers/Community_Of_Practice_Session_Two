import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder


class Pre_process:
    def __init__(self, df):
        # Make a deep copy of the DataFrame to ensure that changes don't affect the original DataFrame.
        self.df = df.copy()

    def _preprocess(self):
        # Rename columns
        self.df = self.df.rename(
            columns={
                "ApointmentData": "AppointmentData",
                "Alcoolism": "Alcoholism",
                "Hipertension": "Hypertension",
                "Handcap": "Handicap",
            }
        )

        # Convert to datetime and calculate days between
        self.df["AppointmentDay"] = pd.to_datetime(self.df["AppointmentDay"])
        self.df["ScheduledDay"] = pd.to_datetime(self.df["ScheduledDay"])
        self.df["Sched_Appt"] = (
            self.df["AppointmentDay"] - self.df["ScheduledDay"]
        ).dt.days
        self.df.replace([np.inf, -np.inf], np.nan, inplace=True)

        # Binary encoding for 'Gender' and 'No-show' columns
        self.df["Gender"] = self.df["Gender"].apply(lambda x: 1 if x == "F" else 0)
        self.df["No-show"] = self.df["No-show"].apply(lambda x: 1 if x == "Yes" else 0)

        # Filter Age
        self.df = self.df[(self.df.Age >= 0) & (self.df.Age <= 100)].copy()

    def _calc_date(self):
        # Adding day of the week (numerical and name) as new columns
        self.df["ScheduledDay_DayOfWeek_Num"] = self.df["ScheduledDay"].dt.dayofweek
        self.df["ScheduledDay_DayOfWeek_Name"] = self.df["ScheduledDay"].dt.day_name()

    def _calc_awaiting_time(self):
        # Calculate awaiting time and make it positive
        self.df["AwaitingTime"] = (
            self.df["AppointmentDay"] - self.df["ScheduledDay"]
        ).dt.days.abs()

    def _split_day_month_year(self):
        # Split date into year, month, and day, then drop the original datetime columns
        self.df["ScheduledDay_Y"] = self.df["ScheduledDay"].dt.year
        self.df["ScheduledDay_M"] = self.df["ScheduledDay"].dt.month
        self.df["ScheduledDay_D"] = self.df["ScheduledDay"].dt.day
        self.df.drop(["ScheduledDay"], axis=1, inplace=True)

        self.df["AppointmentDay_Y"] = self.df["AppointmentDay"].dt.year
        self.df["AppointmentDay_M"] = self.df["AppointmentDay"].dt.month
        self.df["AppointmentDay_D"] = self.df["AppointmentDay"].dt.day
        self.df.drop(["AppointmentDay"], axis=1, inplace=True)

    def _add_labels(self):
        # Encode categorical variables
        le = LabelEncoder()
        self.df["Gender"] = le.fit_transform(self.df["Gender"])
        self.df["Neighbourhood"] = le.fit_transform(self.df["Neighbourhood"])
        self.df["ScheduledDay_DOW"] = le.fit_transform(
            self.df["ScheduledDay_DayOfWeek_Name"]
        )
        self.df["No-show"] = le.fit_transform(self.df["No-show"])

    def _final_tidy(self):
        # Convert to appropriate data types and drop unnecessary columns
        self.df.PatientId = self.df.PatientId.astype(int)
        self.df.drop(
            ["Sched_Appt", "ScheduledDay_DayOfWeek_Name", "PatientId", "AppointmentID"],
            axis=1,
            inplace=True,
        )

    def format_and_get_df(self):
        self._preprocess()
        self._calc_date()
        self._calc_awaiting_time()
        self._split_day_month_year()
        self._add_labels()
        self._final_tidy()
        return self.df
