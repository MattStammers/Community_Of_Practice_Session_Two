from app.pre_process import Pre_process
from app.logistic_reg import Logictic_model
from app.decision_tree import Decision_tree
from sklearn import metrics
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("KaggleV2-May-2016.csv")

pre_processer = Pre_process(df)
df_proc = pre_processer.format_and_get_df()

log_reg = Logictic_model(df_proc)

l_y_test,l_y_pred = log_reg.log_reg()

print("Logistic regression")
print("Results:")
print("Accuracy", metrics.accuracy_score(l_y_test,l_y_pred))

# save confusion matrix and slice into four pieces
confusion = metrics.confusion_matrix(l_y_test, l_y_pred)
TP = confusion[1, 1]
TN = confusion[0, 0]
FP = confusion[0, 1]
FN = confusion[1, 0]

#Specificity: When the actual value is negative, how often is the prediction correct?
print("Specificity:",TN / float(TN + FP))

#False Positive Rate: When the actual value is negative, how often is the prediction incorrect?
print("False Positive Rate:",FP / float(TN + FP))

#Precision: When a positive value is predicted, how often is the prediction correct?
print("Precision:",metrics.precision_score(l_y_test, l_y_pred))

#Sensitivity:
print("Recall:",metrics.recall_score(l_y_test, l_y_pred))

print("Decision tree")
dev_tree = Decision_tree(df_proc)

tree, t_X_train, t_X_test, t_y_train, t_y_test, t_y_pred = dev_tree.train_tree()

print('Accuracy on the training subset: {:.3f}'.format(tree.score(t_X_train, t_y_train)))
print('Accuracy on the test subset: {:.3f}'.format(tree.score(t_X_test, t_y_test)))


# save confusion matrix and slice into four pieces
confusion = metrics.confusion_matrix(t_y_test, t_y_pred)
TP = confusion[1, 1]
TN = confusion[0, 0]
FP = confusion[0, 1]
FN = confusion[1, 0]

#Specificity: When the actual value is negative, how often is the prediction correct?
print("Specificity:",TN / float(TN + FP))

#False Positive Rate: When the actual value is negative, how often is the prediction incorrect?
print("False Positive Rate:",FP / float(TN + FP))

#Precision: When a positive value is predicted, how often is the prediction correct?
print("Precision:",metrics.precision_score(t_y_test, t_y_pred))

#Sensitivity:
print("Recall:",metrics.recall_score(t_y_test, t_y_pred))


X_train = dev_tree.get_inital_input()

n_features = X_train.shape[1]
plt.barh(range(n_features), tree.feature_importances_, )
plt.yticks(np.arange(n_features), X_train)
plt.xlabel('Feature Importance')
plt.ylabel('Feature')
plt.show()

