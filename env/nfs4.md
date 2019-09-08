
## NFS4 Configuration under the Archlinux 
---------------
### 1,               Installation
** Both client and server only require the installation of the nfs-utils package.
    yay -S nfs-utils 

### 2, Configuration File
**Server
Global configuration options are set in 
                            /etc/nfs.conf. 
**Users of simple configurations should not need to edit this file.

### 3, Concepts
  The NFS server needs a list of exports (directories to share) which are defined in /etc/exports. 
  These shares are relative to the so-called **NFS root.**  
  A good security practice is to define a NFS root in a discrete directory tree which will keep users limited to that mount point. Bind mounts are used to link the share mount point to the actual directory elsewhere on the filesystem.

Consider this following example wherein:

The NFS root is /srv/nfs.
The export is /srv/nfs/music via a bind mount to the actual target /mnt/music.
    ```
    usally We should use the sudo
    # mkdir -p /srv/nfs/music /mnt/music
    # mount --bind /mnt/music /srv/nfs/music
    ```
**  Write this binding to the filetable, Hard Wiring this config, 
the exports directory bindings will be available after Server resume on
Line** 
/etc/fstab
----------------
```
/mnt/music /srv/nfs/music  none   bind   0   0

```
### 4, Publish the Exports by Configuration in /etc/exports
Add directories to be shared and limit them to a range of addresses via a CIDR or hostname(s) of client machines that will be allowed to mount them in /etc/exports, e.g.:

Tip: Use an asterisk (*) to allow access from any interface.
/etc/exports
-------------
```
/srv/nfs        192.168.1.0/24(rw,sync,crossmnt,fsid=0)
/srv/nfs/music  192.168.1.0/24(rw,sync)
/srv/nfs/home   192.168.1.0/24(rw,sync,nohide)
/srv/nfs/public 192.168.1.0/24(ro,all_squash,insecure) desktop(rw,sync,all_squash,anonuid=99,anongid=99) # map to user/group - in this case nobody  
    ```
It should be noted that modifying /etc/exports while the server is running will require a re-export for changes to take effect:
```
# exportfs -rav
or
# exportfs -v

```
To view the current loaded exports state in more detail, use:

### Server Service enable/Starting

    sudo systemctl enable nfs-server.service

### Client
  sudo mount.nfs4  server:/   /mount/point/client

### Further Study 
        How to explictly define the NFS Root are still in questino 
