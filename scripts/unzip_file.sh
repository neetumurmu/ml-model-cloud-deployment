#!/usr/bin/env bash

for file in *.zip
do
unzip -P pcp9100 "$file"  
done

