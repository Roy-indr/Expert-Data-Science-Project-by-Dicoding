import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

train_df = pd.read_pickle('cleaned.csv')

y = train_df['Attrition']
X = train_df.drop(columns='Attrition')

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

classifier = RandomForestClassifier(criterion = 'entropy')
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

cm = confusion_matrix(y_test, y_pred)
print(cm)
print(accuracy_score(y_test, y_pred))

# Lakukan Prediksi Di Sini

# Buat list 2 dimensi berisikan value yang akan dipredict
new_data_to_predict = [[]]

result = classifier.predict(X_test)

print(result)