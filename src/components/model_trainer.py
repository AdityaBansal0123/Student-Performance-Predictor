import os
import sys
from dataclasses import dataclass
from src.utils import save_object, evaluate_model
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import (
    RandomForestRegressor,
    AdaBoostRegressor,
    GradientBoostingRegressor,
)
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from catboost import CatBoostRegressor
from xgboost import XGBRegressor
from src.exception import CustomException
from src.logger import logging


@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts", "model.pkl")

class ModelTrainer:
    def __init__(self):  # ✅ Corrected typo here
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array):  # Fixed function name
        try:
            logging.info("Splitting training and test input data")
            X_train, y_train = train_array[:, :-1], train_array[:, -1]
            X_test, y_test = test_array[:, :-1], test_array[:, -1]

            models = {
                "Linear Regression": LinearRegression(),
                "Lasso": Lasso(),
                "Ridge": Ridge(),
                "K-Neighbors Regressor": KNeighborsRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Random Forest Regressor": RandomForestRegressor(),
                "XGBRegressor": XGBRegressor(),
                "CatBoosting Regressor": CatBoostRegressor(verbose=False),
                "GradientBoosting Regressor": GradientBoostingRegressor(),
                "Adaboost Regressor": AdaBoostRegressor(),
                "Support Vector Regressor": SVR(),
            }

            model_report: dict = evaluate_model(
                X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test, models=models
            )
            best_model_score = max(sorted(model_report.values()))
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name]

            if best_model_score < 0.6:
                raise CustomException("No best model found")

            logging.info(f"Best model found: {best_model_name}")
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model,
            )

            predicted = best_model.predict(X_test)
            r2 = r2_score(y_test, predicted)
            return r2

        except Exception as e:
            raise CustomException(e, sys)
