FileHider
=========

## Intro.. Kind of explanation/background

This script was intended to hide files into other files. The script takes advantage of how computers read files. The initial idea was 
to get the user specify a file to hide and a file to use as the "cover", my BASH script would zip the file to hide, and 
```
cat MaskFile.png SecretZip.zip > DestFile.png
```

This would provide you with a nice PNG file that has a secret ZIP file appended to the end! Whats great about this, is that as long as
the file is not modified, any other user could open the picture, document, bitmap, webpage and find nothing unusual (unless the picture was 1.2GB on size).

To recover the files, I would manually get the file into unzip, which would go over the file and decompress it whlist telling me there were $RANDOM bytes at the begining. That was alright, except, it didnt worked as a script, you had to manually unzip the files
and that was a lame behavior for the program.


## Python

Because I learned python, and found the power of the binascii library, I thought I'd remake this in python. Still, would like to make a bash version since it would be almost universal.

#### Features:

- Hides any file into any other file
- Recovers any file hidden by this script
- Recovers file extension (Trust me, its a feature)
- Its awesome!



