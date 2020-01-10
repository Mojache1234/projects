#!/bin/bash

while IFS='' read -r line || [[ -n "$line" ]]; do
    google-chrome --new-tab "$i"
done
