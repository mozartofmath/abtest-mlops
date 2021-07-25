import mlflow
df = mlflow.search_runs()
print(len(df))

with open('results.txt', 'w') as result:
      result.write('Logistic Regression\n')
      result.write(f'Model Accuracy : 54.21 %\n')

      result.write('\n')
      result.write('Decision Tree\n')
      result.write(f'Model Accuracy : 57.6 %\n')

      result.write('\n')
      result.write('XGBoost\n')
      result.write(f'Model Accuracy : 53.6 %\n')