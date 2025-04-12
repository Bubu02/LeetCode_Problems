import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    # Create cartesian product of students and subjects
    two_df = students.merge(subjects, how='cross')
    
    # Aggregate examination counts
    exam_count = examinations.groupby(['student_id', 'subject_name']).agg(
        attended_exams=('subject_name', 'count')
    ).reset_index()
    
    # Merge and sort
    all_df = two_df.merge(exam_count, on=['student_id', 'subject_name'], how='left').sort_values(by=['student_id', 'subject_name'])
    
    # Fill only attended_exams with 0, leave student_name as NULL
    all_df['attended_exams'] = all_df['attended_exams'].fillna(0)
    
    return all_df[['student_id', 'student_name', 'subject_name', 'attended_exams']]