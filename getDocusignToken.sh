# Purpose: Checks that $PATH contains folder that contains geckodriver executeable. 
# 	If geckodriver exec in /Applications and $PATH points to /Applications, calls initiateOAuth.py.  
# Dependencies: Assumes /Applications contains geckodriver exec. 
# Created by: Erica Ching (eching@aimhigh.org) on 10-18-2019

#!/bin/bash
NC='\033[0m'
GREEN='\033[0;32m'
RED='\033[0;31m'
fail=0

if [[ $PATH =~ :/Applications/$ ]]; then 
	echo "\$PATH variable set correctly."
else
	export PATH=$PATH:/Applications/
	if test $? -eq 0; then
		echo "${GREEN}Success!${NC}"
	else
		echo "${RED}Issue with changing \$PATH variable to include folder where geckodriver executeable lives.${NC}"
		fail=$(( fail + 1 ))
	fi
fi


echo -n "Checking if initiateOAuth.py is in the same folder..."
file="initiateOAuth.py"
if [ -e $file ]; then
	echo -e "${GREEN}passed${NC}"
else
	echo -e "${RED}$file does not exist${NC}"
	fail=$(( fail + 1 ))
fi

echo -n "Checking if python3 is version Python 3.8.0 (as written)..."
yourpy=$(python3 --version)
pyvers="Python 3.8.0"
if [[ $pyvers == $yourpy ]]; then
	echo -e "${GREEN}passed${NC}"
else
	echo -e "${RED}please install most current version of python3${NC}"
	fail=$(( fail + 1 ))
fi

echo -n "Checking if selenium module is installed..."
pip freeze | grep selenium >& /dev/null
if [[ $? -gt 0 ]]; then
	echo -e "${RED}please install selenium module with command 'pip install selenium'"
	fail=$(( fail + 1 ))
else
	echo -e "${GREEN}passed${NC}"
fi

echo -n "Checking if geckodriver is in /Applications folder..."
ls /Applications | grep geckodriver >& /dev/null
if [[ $? -gt 0 ]]; then
	echo -e "${RED}not passed"
	echo -e "${RED}Please install and/or move geckodriver exec into /Applications folder"
	echo -e "${RED}Download here: https://github.com/mozilla/geckodriver/releases${NC}"
	fail=$(( fail + 1 ))
else
	echo -e "${GREEN}passed${NC}"
fi

if [[ $fail -gt 0 ]]; then
	echo -e "${RED}Did not pass all tests...exiting script${NC}"
	exit 1
fi

echo "Initiating process to get new token..."
python3 initiateOAuth.py