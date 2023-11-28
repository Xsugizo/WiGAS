adb devices
read -p "input serial number(ip):" id
echo -e "\n Your serial number is:${id}"
adb connect ${id}
adb -s ${id} shell svc power stayon true # set stay awake to true
adb -s ${id} shell locksettings set-disabled true # set lock screen to none
adb -s ${id} shell media volume --show --stream 0 --set 1 # in call
adb -s ${id} shell media volume --show --stream 1 --set 1 # notifications/ring
#adb -s ${id} shell media volume --show --stream 2 --set 1 # notifications/ring
adb -s ${id} shell media volume --show --stream 3 --set 1 # media
adb -s ${id} shell media volume --show --stream 4 --set 1  # alarm
adb -s ${id} shell settings put global verifier_verify_adb_installs 0 #set verify apps over USB to disable
adb -s ${id} shell bmgr enable true
#adb -s ${id} shell am start -a android.net.wifi.PICK_WIFI_NETWORK #open Wi-Fi setting
#adb -s ${id} shell input keyevent 3
#sleep 1.5
### auto open Chrome
adb -s ${id} shell am start -n com.android.chrome/com.google.android.apps.chrome.Main # open GMS chrome
adb -s ${id} shell am start -n org.chromium.chrome/com.google.android.apps.chrome.Main # open non GMS chrome

#adb -s ${id}  shell input keyevent 61#input tab
#sleep 1.5
#adb -s ${id}  shell input keyevent 61
#sleep 1.5
#adb -s ${id}  shell input keyevent 61
#sleep 1.5
#adb -s ${id}  shell input keyevent 66
#sleep 1.5
#adb -s ${id}  shell input keyevent 61
#sleep 1.5
#adb -s ${id}  shell input keyevent 61
#sleep 1.5
#adb -s ${id}  shell input keyevent 66 #input enter
#adb -s ${id}  shell input keyevent 3 #input home

#adb shell input tap 500 1650 # mufasa accept
#adb shell input tap 300 1100 # simba/lightning accept
#adb shell input tap 400 1200 # Thunder accept
#adb shell input tap 200 700 # Glatus accept

#adb shell input tap 100 1100 # simba no thanks
#adb shell input tap 150 1200 # Thunder no thanks
#adb shell input tap 70 680 # Glatus no thanks
#adb shell input tap 200 1650 # mufasa no thanks
#adb shell input tap 300 1100 # lightning non GMS next
#adb shell input keyevent 3
#chmod u+x copy_media.sh
#chmod u+x copy_images.sh
#./copy_media.sh -s ${id}
#./copy_images.sh -s ${id}
