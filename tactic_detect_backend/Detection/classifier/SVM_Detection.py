import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from Detection.feature.tf_iwf import Tfiwf
from sklearn.preprocessing import LabelEncoder
from sklearn import svm
from Detection.evaluate import evaluate
from Detection.buffer import filepath, data_process, namedata_filepath
from collections import Counter

# 确保每次生成的随即数都相同
np.random.seed(500)

# train_file_path = namedata_filepath.get_authorize_name_data()
train_file_path = filepath.get_voting_train()
CorpusTrain = data_process.read_csv(train_file_path)
# 数据处理
CorpusTrain = data_process.base_tokenizer(CorpusTrain)
Train_X = CorpusTrain['text_final']
Train_Y = CorpusTrain['label']
Encoder = LabelEncoder()
Train_Y = Encoder.fit_transform(Train_Y)
print(Counter(Train_Y))
# tf-idf向量化
tfidf_vector = TfidfVectorizer(max_features=5000)
tfidf_vector.fit(Train_X)
Train_X_Tfidf = tfidf_vector.transform(Train_X)
# # tf-iwf向量化
# tfiwf_vector = Tfiwf(Train_X)
# result1 = tfiwf_vector.get_tfiwf(Train_X)
# Train_X_Tfiwf = tfiwf_vector.transform(Train_X)


# ------SVM------
SVM = svm.SVC(C=1.0, kernel='linear', degree=3, gamma='auto', probability=True)
evaluate.n_fold_evaluate(SVM, Train_X_Tfidf, Train_Y, k_neighbours=3, cv=10)
