from naivebays_dog_cat.naivebays_naver_movie import NaiveBayesClassfier
context = './data/'
model = NaiveBayesClassfier()
model.train(context+'review_train.csv')
print(model.classfy('내 인생 쓰레기같은 영화'))