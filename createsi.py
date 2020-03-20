import csv

samples="""BovA_S8_L001_R1_001
BovA_S8_L002_R1_001
BovB_S4_L001_R1_001
BovB_S4_L002_R1_001
MixInpFEB_S1_L001_R1_001
MixInpFEB_S1_L002_R1_001
MixInpJAN_S16_L001_R1_001
MixInpJAN_S16_L002_R1_001
NanMixsdFEB_S13_L001_R1_001
NanMixsdFEB_S13_L002_R1_001
NanMixsrJAN_S11_L001_R1_001
NanMixsrJAN_S11_L002_R1_001
NanNEWmixsd_S2_L001_R1_001
NanNEWmixsd_S2_L002_R1_001
OctMixsdFEB_S18_L001_R1_001
OctMixsdFEB_S18_L002_R1_001
OctMixsrJAN_S21_L001_R1_001
OctMixsrJAN_S21_L002_R1_001
OctNEWmixsd_S5_L001_R1_001
OctNEWmixsd_S5_L002_R1_001
OctsdAndFEB_S15_L001_R1_001
OctsdAndFEB_S15_L002_R1_001
OctsdEpiFEB_S3_L001_R1_001
OctsdEpiFEB_S3_L002_R1_001
OctsrJAN_S20_L001_R1_001
OctsrJAN_S20_L002_R1_001
SoxMixsdFEB_S9_L001_R1_001
SoxMixsdFEB_S9_L002_R1_001
SoxMixsrJAN_S10_L001_R1_001
SoxMixsrJAN_S10_L002_R1_001
SoxNEWmixsd_S7_L001_R1_001
SoxNEWmixsd_S7_L002_R1_001
acNuc_S19_L001_R1_001
acNuc_S19_L002_R1_001
acOcta_S14_L001_R1_001
acOcta_S14_L002_R1_001
acPreNuc_S12_L001_R1_001
acPreNuc_S12_L002_R1_001
27acNuc_S6_L001_R1_001
27acNuc_S6_L002_R1_001
27acOcta_S17_L001_R1_001""".split()

def get_info(sample_name):
    parts = sample_name.split("_")
    name = parts[0]
    lane = int(parts[2][-1])
    folder = f"Sample_{name}"
    return (sample_name, name, folder, lane, "SE")

with open("sample_info.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(("filename", "name", "folder", "lane", "end"))
    for sample in samples:
        writer.writerow(get_info(sample))

