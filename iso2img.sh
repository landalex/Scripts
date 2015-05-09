#!/bin/bash

read -p "IMG target path:  " img
read -p "ISO source path: " iso

hdiutil convert -format UDRW -o $img $iso

mv $img.dmg $img

diskutil list

read -p "What number is the disk? " disk

diskutil unmountDisk /dev/disk$disk

echo "Mounting the iso..."

sudo dd if=$img of=/dev/disk$disk bs=1m

echo "All done! Ejecting..."

diskutil eject /dev/disk$disk

echo "Until next time..."
