#!/bin/sh
# Copyright (C) 2012 The Android Open Source Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
adb_options=" "
max_resolution=3
if [ $# -eq 0 ]; then
  echo "assuming default resolution"
elif [ "$1" = "-s" ]; then
  adb_options=""$1" "$2""
fi
echo "Factory Reset" 
adb $adb_options reboot-bootloader
fastboot $adb_options erase userdata
fastboot $adb_options reboot

