#!/bin/bash

echo "vacation_photo.jpg" >> files_list.txt
echo "report_2025.pdf" >> files_list.txt
echo "icon_main.png" >> files_list.txt
echo "notes.txt" >> files_list.txt
echo "background_image.gif" >> files_list.txt
echo "script.sh" >> files_list.txt
echo "old_backup.zip" >> files_list.txt
echo "avatar.jpg" >> files_list.txt
grep -E "\.(jpg|png|gif)$" files_list.txt 

