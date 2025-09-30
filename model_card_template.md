# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
- **Model Type**: Random Forest Classifier
- **Framework**: scikit-learn (v1.5.1)
- **Training Date**: September 30th 2025
- **Model Version**: 1.0
- **Random State**: 42

## Intended Use
Predicts whether an individuals income exceeds 50k annually based on census data. 
## Training Data
Trained on Census Income Dataset from the UCI Machine Learning Repository.
## Evaluation Data
Evaluated on 20% of the data (6,512 instances) held out from the training set.
## Metrics
- **Precision**: 0.7419
- **Recall**: 0.6384
- **F1-Score**: 0.6863

## Ethical Considerations
- **Bias**: Model uses sensitive attributes like race, sex and native-country which could create historical biases.
- **Fairness**: Performance varies by demographic slices which could lead to disparate impact on different groups.
- **Privacy**: Model was trained on publicly available census data.
## Caveats and Recommendations
- Data is from 1994 and may not reflect current income distributions or demographics
- 50k threshold isn't adjusted for inflation
- Should not be used for actual employment or lending decisions.