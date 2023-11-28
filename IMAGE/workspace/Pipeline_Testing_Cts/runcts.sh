#!/bin/bash
daemonize -E BUILD_ID=dontKillMe
cd /home/logo007/Desktop/IMAGE/workspace/Pipeline_Testing/11_r10/android-cts-11_r10-linux_x86-arm/android-cts/tools
./cts-tradefed run cts -m CtsCameraTestCases --shard-count 2 -s 212555225E0089 -s 212555225E0147



#./cts-tradefed l r
 