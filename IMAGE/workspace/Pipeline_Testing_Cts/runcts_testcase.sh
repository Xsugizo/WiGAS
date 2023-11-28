            #!/bin/bash 

            cd /home/logo007/Desktop/IMAGE/workspace/Pipeline_Testing/11_r10/android-cts-11_r10-linux_x86-arm/android-cts/tools
            ./cts-tradefed run cts -m CtsPermission2TestCases -t android.permission2.cts.NoReceiveSmsPermissionTest#testAppSpecificSmsToken  exit cts


