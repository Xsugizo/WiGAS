#!/bin/bash


# echo "run unlock reboot tool"
# cd ~/Desktop/unlock\ tool/
# python3 ./unlocktool_fastboot.py


# source ./progress-bar.sh
# progress-bar 90
# # run times setting
# # python3 ./newUI.py
# echo "CTS"
# cd ~/Desktop/IMAGE/workspace/Pipeline_Testing_Cts


# run times setting
# python3 ./newUI.py

# read adb device number
devices=$(./device_info.py 2>&1)

# # switch to fastboot mode
# for x in $devices
# do
#     adb -s $x reboot bootloader &
# done
# wait
# sleep 30

# # get fastboot parameter for flash image
# f_info=$(./get_fastboot_info.py 2>&1)


# my_array=$(echo $f_info | tr "," "\n")
# echo "$my_array"

# fastboot devices |  cut -sf 1 | xargs -IX fastboot -s X reboot

# echo "sleep 60 sec waiting for devices finishing rebooting"
# source ./progress-bar.sh
# progress-bar 60
# # sleep 60

# # multiple devices flash image in parallel

# for x in $devices
# do

#     f1="$(echo "$my_array" | cut -d' ' -f1)"
#     f2="$(echo "$my_array" | cut -d' ' -f2)"
#     f3="$(echo "$my_array" | cut -d' ' -f3)"
#     my_array=$(echo $my_array | sed "s/$f1 //1")
#     my_array=$(echo $my_array | sed "s/$f2 //1")
#     my_array=$(echo $my_array | sed "s/$f3 //1")
#     echo "$f1"
#     echo "$f2"
#     echo "$f3"
#     echo "wait for 3 sec then $x will flash image"
#     source ./progress-bar.sh
#     progress-bar 3
#     # gnome-terminal -- bash -e 'StrictHostKeyChecking=no ./flashImage1.sh $f1 $f2 $f3 &; exec bash'   
#     # StrictHostKeyChecking=no ./flashImage1.sh $f1 $f2 $f3 &
#     python3 ./flashImageA13.py --s $f1 $f2 $f3 &
#     # gnome-terminal -e "bash -c command;bash"
#     # ./flashImage1.sh $f1 $f2 $f3 >> $f1.txy&
# done
# wait
# echo "sleep 6 min waiting for next steps "
# source ./progress-bar.sh
# progress-bar 360




# echo "devices set up for Cts testing "
# sleep 5
# python3 ./multi_session_device_setup.py

# # echo "Please enter y/n .."
# # read check
# # if [ "$check" = "y" ]
# # then
# #     echo ""
# # fi

# # set up
# # for x in $devices
# #     do
# #         echo "CBN check device info "
# #         (./CBN.py --name $x 
# #         # python3 ./multi_devices_setup3.py $x
# #         echo "devices set up for cts testing "
# #         python3 ./multi_devices_setup_A13.py $x
# #         # python3 ./multi_devices_setup_A13_gts.py $x
# #         # python3 ./multi_devices_setup_A13_terminal.py $x

# #         echo "set up chrome "
# #         python3 ./cts_device_setup_for_chrome_Jonathan.py $x

# #         echo "push media "
# #         ./CAD_test.py --name $x)&
# #         # )&

# #     done

# #     wait

echo "Ready to run after 30s "
source ./progress-bar.sh
progress-bar 10

## CTS test
# python3 ./newpytest.py
python3 ./newpytest_cmd_final.py
