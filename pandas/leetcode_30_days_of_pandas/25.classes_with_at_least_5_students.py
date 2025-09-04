#  Problem: Classes With at Least 5 Students
#  Link: https://leetcode.com/problems/classes-with-at-least-5-students/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata


import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    return courses['class'].value_counts().reset_index().query('count >= 5')[['class']]

    # another solution
def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    classes = courses.groupby('class', as_index=False)['student'].count()
    return classes[classes['student'] >= 5][['class']]

    # another solution
def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    classes = courses.groupby('class')['student'].size().reset_index(name='students_count')
    return classes[classes['students_count'] >= 5][['class']]

