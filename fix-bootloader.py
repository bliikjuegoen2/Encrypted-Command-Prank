#!/usr/bin/python3
import subprocess as sp 

for i in ["/", "/home", "/boot/efi"]:
	msg = f"please enter partition for: {i}"
	partition = sp.check_output(["zenity", "--entry", f"--text={str(msg)}"], text = True)[:-1]
	sp.run(["sudo", "mount", partition, f"/mnt{i}"])


for i in ["/sys", "/proc", "/run", "/dev"]:
	sp.run(["sudo", "mount", "--bind", i, f"/mnt{i}"])

for i in ["grub-install --efi-directory=/boot/efi", "grub-mkconfig -o /boot/grub.cfg"]:
	sp.run(["sudo", "chroot", "/mnt"] + i.split())



#print("""
#sudo chroot /mnt 
#grub-install --efi-directory=/boot/efi
#grub-mkconfig -o /boot/grub.cfg
#""")
