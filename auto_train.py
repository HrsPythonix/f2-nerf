import os


trial_list = [  
                "postbank_counter_big_100k", 
                "postbank_counter_clip1_big_100k", 
                "postbank_counter_clip2_big_100k", 
                "postbank_counter_ff_big_100k"
             ]

for t in trial_list:
    os.system("python scripts/run.py --config-name={} +work_dir=$(pwd)".format(t))
