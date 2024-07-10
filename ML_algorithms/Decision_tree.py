from sklearn.tree import DecisionTreeClassifier

# Assuming you have a decision tree classifier called 'clf'
clf = DecisionTreeClassifier()

# Train the decision tree model
clf.fit(X_train, y_train)

# Evaluate the performance of the model
accuracy = clf.score(X_test, y_test)
print("Accuracy:", accuracy)