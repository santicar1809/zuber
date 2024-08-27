from src.preprocessing.load_data import load_datasets
from src.preprocessing.preprocess import preprocess_data
from src.EDA.EDA import eda_report
from src.EDA.hypotesis_test import hypotesis_test

def main():
    '''This main function progresses through various stages to process data, 
    evaluate variables, and create a robust model for predicting churned users. 
    For more detailed information, please refer to the README.md file. '''

    data = load_datasets() #Loading stage
    preprocessed_data = preprocess_data(data) #Preprocessing stage
    eda_report(preprocessed_data)
    results=hypotesis_test(preprocessed_data)
    return results

results = main()

print(results)