from sklearn.metrics import average_precision_score

y_true=[0,1,1,0,1,1]
y_score=[0.1,0.4,0.35,0.8,0.65,0.9]

ap=average_precision_score(y_true,y_score)

print("Average precision:",ap)
