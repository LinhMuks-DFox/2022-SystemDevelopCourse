import csv

from cv2 import mean
import _configs
import numpy as np
import scipy.stats as sp
# min(male), min(female)
# max(male), max(female)
# コード,全国，都道府県，市区町村,総数,男,女

code_data = []
place_data = []
total_data = []
female_data = []
male_data = []


with open(_configs.TARGET_FILE, "r", encoding=_configs.TARGET_FILE_ENCODE) as csv_fin:
    reader = csv.DictReader(csv_fin)
    file_raw0 = next(reader)

    for raw in reader:
        code_data.append(raw["コード"])
        place_data.append(raw["全国，都道府県，市区町村"])

        total_data.append(
            0 if (r := raw["総数"].replace(",", "")) == "-" else int(r))

        male_data.append(
            0 if (r := raw["男"].replace(",", "")) == "-" else int(r))

        female_data.append(
            0 if (r := raw["女"].replace(",", "")) == "-" else int(r))


total_data = np.array(total_data)
female_data = np.array(female_data)
male_data = np.array(male_data)

print(
    f"For {len(place_data)} place:\n",
    f"Mean of female: {female_data.mean()}\n",
    f"Mean of male: {male_data.mean()}\n",
    f"Total mean:{total_data.mean()}\n",
    f"Median of female: {np.median(female_data)}\n",
    f"Median of male: {np.median(male_data)}\n",
    f"Mode of female: {sp.mode(female_data)[0]}\n",
    f"Mode of male: {sp.mode(male_data)[0]}\n",
    f"Variance of Female: {female_data.var()}\n",
    f"Variance of male: {male_data.var()}\n",
    f"Standard of Female: {female_data.std()}\n",
    f"Standard of male: {male_data.std()}\n",
    f"Max female number region:{(place_data[(c:=female_data.argmax())])}(={female_data[c]})\n"
    f"Max male number region:{(place_data[(c:=male_data.argmax())])}(={male_data[c]})\n"
)
