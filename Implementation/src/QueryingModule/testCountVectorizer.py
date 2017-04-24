from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
a=["The boy is a nice boy except that he can be not so nice a boy at times"]
data=np.array(a)
v=CountVectorizer()
fittedModel=v.fit(data)
termDocMatrix=v.transform(data)
print ("term doc matrix: "+str(termDocMatrix.todense()))
print ("getting feature names:"+str(v.get_feature_names()))