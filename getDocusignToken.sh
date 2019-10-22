# Purpose: Set $PATH to include /Applications, the folder that holds geckodriver executeable. 
# 	Geckodriver executeable is required to run authentication script for Docusign, as part
# 	of selenium module.  
# Dependencies: Assumes /Applications contains geckodriver exec. 
# Created by: Erica Ching (eching@aimhigh.org)

#!/bin/bash
if [[ $PATH =~ :/Applications/$ ]]; then 
	echo "\$PATH variable set correctly."
else
	export PATH=$PATH:/Applications/
	if test $? -eq 0; then
		echo "Success!"
	else
		echo "Issue with changing \$PATH variable to include folder where geckodriver executeable lives."
		exit 1
	fi
fi

echo "Initiating process to get new token..."
python3 initiateOAuth.py