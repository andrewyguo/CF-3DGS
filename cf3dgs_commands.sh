python run_cf3dgs.py \
-s ./data/data_5170_1104_20mm/noisy_ds004_iso006400_s1_00013/ \
--mode train --data_type custom 

python run_cf3dgs.py \
-s ./data/data_5170_1104_20mm/noisy_ds004_iso051200_s1_00100/ \
--mode train --data_type custom 

python run_cf3dgs.py \
-s ./data/data_5170_1104_20mm/noisy_ds004_iso204800_s1_00800/ \
--mode train --data_type custom 

python run_cf3dgs.py \
-s ./data/data_5170_1104_20mm/noisy_ds004_iso204800_s1_08000/ \
--mode train --data_type custom 


python run_cf3dgs.py \
-s ./data/data_5170_1104_20mm/simple/ \
--mode train --data_type custom 

# 1115 10am: tried to run all of these. if there is out of memory, re-try on Tyche when it is back 
python run_cf3dgs.py \
-s ./data/data_5170_1104_20mm/noisy_ds008_iso006400_s1_00013/ \
--mode train --data_type custom 

python run_cf3dgs.py \
-s ./data/data_5170_1104_20mm/noisy_ds008_iso051200_s1_00100/ \
--mode train --data_type custom 

python run_cf3dgs.py \
-s ./data/data_5170_1104_20mm/noisy_ds008_iso204800_s1_00800/ \
--mode train --data_type custom 

python run_cf3dgs.py \
-s ./data/data_5170_1104_20mm/noisy_ds008_iso204800_s1_08000/ \
--mode train --data_type custom 
