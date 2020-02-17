#!/usr/bin/env bash

cd ../classification_model/classification_model/datasets
for file in *.zip
do
unzip -P pcp9100 "$file"  
done

