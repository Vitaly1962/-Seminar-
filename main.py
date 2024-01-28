# Задача 44: 
# В ячейке ниже представлен код генерирующий DataFrame, 
# которая состоит всего из 1 столбца. Ваша задача перевести
# его в one hot вид. Сможете ли вы это сделать без get_dummies?


# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI': lst})

# # Создаем экземпляр LabelBinarizer и преобразуем столбец 'whoAmI'
# label_binarizer = LabelBinarizer()
# one_hot_encoded = label_binarizer.fit_transform(data['whoAmI'])

# # Создаем новый DataFrame с one hot encoding
# one_hot_df = pd.DataFrame(one_hot_encoded, columns=label_binarizer.classes_)

# # Выводим результат
# result_df = pd.concat([data, one_hot_df], axis=1)
# result_df.head()

# ///////////////////Решение 1////////////////////////////////////
# import random
# import pandas as pd
# from sklearn.preprocessing import LabelBinarizer

# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI': lst})

# label_binarizer = LabelBinarizer()
# one_hot_encoded = label_binarizer.fit_transform(data['whoAmI'])

# # Создаем DataFrame с использованием бинарных представлений исходных классов
# one_hot_df = pd.DataFrame(one_hot_encoded, columns=[label_binarizer.classes_[0] + "_encoded"])

# # Объединяем исходный DataFrame с новым DataFrame
# result_df = pd.concat([data, one_hot_df], axis=1)
# print(result_df.head())

# /////////////////////////Решение 2///////////////////////////
# метода map в pandas

import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Создаем столбец 'human_encoded'
data['human_encoded'] = data['whoAmI'].map({'robot': 1, 'human': 0})

# Выводим результат
print(data.head())
