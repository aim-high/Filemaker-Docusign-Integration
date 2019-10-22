#!/bin/bash

# Purpose: 

# Created by: Erica Ching (eching@aimhigh.org)

NC='\033[0m'
GREEN='\033[0;32m'
RED='\033[0;31m'
fail=0

echo -n "Checking if initialAuth.py is in the same folder..."
file="file.py"
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
