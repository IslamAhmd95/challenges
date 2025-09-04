#  Problem: Students and Examinations
#  Link: https://leetcode.com/problems/students-and-examinations/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata


import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    students_subs = students.merge(subjects, how='cross')
    exams_count = examinations.groupby(
            ['student_id', 'subject_name'],
        ).agg(
            attended_exams=('subject_name', 'count')
        ).reset_index()
    result = students_subs.merge(exams_count, how='left', on=['student_id', 'subject_name']).sort_values(['student_id', 'subject_name'])
    result['attended_exams'] = result['attended_exams'].fillna(0)
    return result





