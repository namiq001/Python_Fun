from sklearn.ensemble import IsolationForest
import numpy as np

# Təlim üçün normal trafik məlumatları
X_train = np.random.rand(100, 5)  # 100 normal trafik nümunəsi

# Modeli öyrət
model = IsolationForest(contamination=0.1)
model.fit(X_train)

def is_anomalous(packet_features):
    """
    Gələn paketlərin xüsusiyyətlərini qiymətləndirir və anormal olub-olmadığını qaytarır.
    -1 → anormal, 1 → normal
    """
    prediction = model.predict([packet_features])
    return prediction[0] == -1
