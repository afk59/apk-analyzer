# How do I take a snapshot or obtain an album using the hdc command?

1.  Take a snapshot:
    
    hdc shell snapshot\_display -f /data/local/tmp/test111.jpeg # -f specifies the path of the image on the device. If this parameter is not specified, the default directory is displayed after the command is executed.
    hdc file recv /data/local/tmp/test111.jpeg /data/local/tmp
    
2.  Obtain the system album:
    
    hdc file recv /storage/media/100/local/files/Photo # Obtain the album to the directory where the command is executed.
