# NBA Shot Selection Prediction – Project Summary

## Objective

Predict whether an NBA shot attempt will be successful using machine learning and semi-supervised learning techniques.

---

## Key Approach

- Data preprocessing
- Feature engineering
- Semi-supervised learning (pseudo-labeling)
- Tree-based machine learning models
- Model evaluation

---

## Important Modeling Decisions

### Semi-Supervised Learning

Used labeled and unlabeled data through pseudo-labeling to improve model performance.

### Why SMOTE Was Not Used

Synthetic oversampling combined with pseudo-labeling can introduce noise.

Tree-based models were used instead.

### Why Outliers Were Retained

Extreme shot distances represent real basketball scenarios.

Removing them would reduce real-world applicability.

---

## Models Used

- Logistic Regression
- Random Forest
- XGBoost
- Semi-Supervised Learning Model

---

## Key Findings

- Shot distance strongly influences scoring probability
- Semi-supervised learning improved performance
- Tree-based models handled imbalance effectively

---

## Business Impact

- Better shot selection insights
- Improved sports analytics decision-making
- Enhanced player performance analysis
