from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from lightgbm import LGBMRegressor
from xgboost import XGBRegressor
from catboost import Pool, CatBoostRegressor
from statsmodels.tsa.seasonal import seasonal_decompose
import numpy as np

## Logistic Regression Model
def all_models():
    '''This function will host all the model parameters, can be used to iterate the
    grid search '''

    lr_pipeline = Pipeline([
        ('scaler',StandardScaler()),
        ('Linreg', LinearRegression())
    ])

    lr_param_grid = {
        }

    lr = ['Linreg',lr_pipeline,lr_param_grid]

    xg_pipeline = Pipeline([
        ('scaler',StandardScaler()),
        ('xgboost', XGBRegressor(random_state=1234))
    ])

    xg_param_grid = {
    'xgboost__n_estimators': [50, 100, 200],
    'xgboost__max_depth': [3, 5, 7],
    'xgboost__learning_rate': [0.01, 0.1, 0.2]
    
}

    xg = ['XGboost',xg_pipeline,xg_param_grid]
    
    rf_pipeline = Pipeline([
    ('scaler',StandardScaler()),
    ('random_forest', RandomForestRegressor(random_state=1234))])

    # Crear el grid de parámetros para Random Forest
    rf_param_grid = {
        'random_forest__n_estimators': [10,20,30],  # Número de árboles en el bosque
        'random_forest__max_depth': [10, 20, 30],  # Profundidad máxima del árbol
        'random_forest__min_samples_split': [2, 5, 10] # Número mínimo de muestras requeridas para estar en un nodo hoja
    }

    # Evaluar el modelo con la función model_evaluation
    rf = ['Random_Forest',rf_pipeline,rf_param_grid]
    
    
    dt_pipeline=Pipeline([
    ('scaler',StandardScaler()),
    ('dt',DecisionTreeRegressor())])
    
    dt_params={
        'dt__max_depth': [3,4,2,1],
        'dt__max_features':[np.random.randint(1, 9)],
        'dt__min_samples_leaf': [1, 2, 4]
    }
    
    dt=['dt',dt_pipeline,dt_params]
    
    models = [lr,xg,rf,dt] #Activate to run all the models
    return models

def category_models(cat_features):
    lgbm_pipeline = Pipeline([
        ('lightgbm', LGBMRegressor())
    ])

    lgbm_param_grid = {
        'lightgbm__max_depth': [3, 5, 7],  # Profundidad máxima del árbol
        'lightgbm__learning_rate': [0.1, 0.01, 0.001],  # Tasa de aprendizaje
        'lightgbm__n_estimators': [10, 50, 100],  # Número de árboles en el bosque
        
    }
    
    lgbm = ['lightgbm',lgbm_pipeline,lgbm_param_grid]
    
    cat_param_grid = {
        'cat__iterations': range(50, 201, 50),
        'cat__depth': range(1, 11)
    }
    
    cat_pipeline = Pipeline([
        ('cat',CatBoostRegressor(random_state=1234,cat_features=cat_features))])
    
    cat = ['cat',cat_pipeline,cat_param_grid]
    
    models = [cat,lgbm]
    #models = [lgbm]
    return models