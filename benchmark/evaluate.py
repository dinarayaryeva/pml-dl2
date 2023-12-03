import pickle
import pandas as pd
from surprise import Dataset, Reader
from surprise import accuracy

DATAPATH = "../data/interim/"
test = pd.read_csv(DATAPATH + 'test.csv')

reader = Reader(rating_scale=(1, 5))
testset = Dataset.load_from_df(test, reader)
testset_full = testset.construct_testset(testset.raw_ratings)

with open('../models/final_model.pkl', 'rb') as f:
    classifier = pickle.load(f)

predictions = classifier.test(testset_full)

accuracy.rmse(predictions)
accuracy.mae(predictions)
