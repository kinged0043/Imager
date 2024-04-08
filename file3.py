# here mlflow will be used to track and register the model
import mlflow
from mlflow.keras import save_model

mlflow.set_experiment()
mlflow.set_tags()
mlflow.set_tracking_uri() # use port 2024

model = mlflow.pyfunc._load()

with mlflow.run():
    mlflow.log_params()
    mlflow.log_metrics()
    mlflow.log_artifact
    signature = mlflow.sign