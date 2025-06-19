'''
3 Problem 3 : Classes more than 5 Students ( https://leetcode.com/problems/classes-more-than-5-students/ )
'''

import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    courses = courses.groupby('class')['student'].count()
    df = courses[courses>=5].reset_index()
    return df[['class']]