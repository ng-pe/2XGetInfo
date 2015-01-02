# 2XGetInfo : Python script to get information from admin port of 2X RAS.

2XGetInfo is Python script (or/and Windows Binarie EXE) to get information from 2X RAS Server.

It grab information from 2X Admin port (TCP 20002)

  - Get all information available from 2X Farms
  - CPU, Mermory, IP/Hostname
  - Connected user, user login, Published App.
 
... and PASSWORD IS NOT REQUIRED!!!!

(this script is tested safe with 2X RAS Server 10.X and 11.X)

### Version
0.0, it's a PoC ;) use this PoC to create a monitoring script...

### Installation/Usage

You need Python 2.7 installed on your system (or use Windows Binarie):

```sh
$ 2XGetInfo.exe -h
Get Info from 2X 20002 Admin port (PoC)
coded by Nicolas GOLLET (blog.ng.pe)
Usage: 2XGetInfo.exe [options]

Options:
  -h, --help            show this help message and exit
  -d HOSTNAME, --destination=HOSTNAME
                        Destination hostname or IP
  -f FILE, --file=FILE  write report to FILE
```

### Sample usage
```txt
F:\sample>2XGetInfo.exe -d ****** -f demo.xml
Get Info from 2X 20002 Admin port (PoC)
coded by Nicolas GOLLET (blog.ng.pe)
connecting to ****** port 20002
>> sending "01005832020000001200000010000000"
<< Get 2X Header
<<datasize =  "10184" bytes
<<received "< R o o t X M L   x m l n s : d t = " u r n : s c h e m a s - m i c
r o s o f t - c o m : d a t a t y p e s " > < A c t C o n n   d t : d t = " u i
4 " > 6 < / A c t C o n n > < A u d i t i n g O n   d t : d t = " u i 4 " > 1 <
/ A u d i t i n g O n > < G e n S e r v e r s   d t : d t = " u i 4 " > 3 < / G
e n S e r v e r s > < S e r v e r 0 > < A c t C o n n   d t : d t = " u i 4 " >
6 < / A c t C o n n > < A c t i v e S e s s i o n s   d t : d t = " u i 4 " > 2
< / A c t i v e S e s s i o n s > < C P U L o a d   d t : d t = " u i 4 " > 0 <
/ C P U L o a d > < D i s c S e s s i o n s   d t : d t = " u i 4 " > 9 < / D i
s c S e s s i o n s > < M e m L o a d   d t : d t = " u i 4 " > 4 7 < / M e m L
o a d > < S e r v e r E n a b l e d   d t : d t = " u i 4 " > 1 < / S e r v e r
E n a b l e d > < S e r v e r I D   d t : d t =
x R D P > < M e m L o a d   d t : d t = " u i 4 " > 4 7 < / M e m L o a d > < N
e w G W   d t : d t = " u i 4 " > 0 < / N e w G W > < R D P S e s s   d t : d t
= " u i 4 " > 1 < / R D P S e s s > < S e c u r i t y M o d e   d t : d t = " u
i 4 " > 0 < / S e c u r i t y M o d e > < S e r v e r E n a b l e d   d t : d t
= " u i 4 " > 1 < / S e r v e r E n a b l e d > < S e r v e r I D   d t : d t =
" u i 4 " > 2 3 < / S e r v e r I D > < S e r v e r N a m e   d t : d t = " s t
r i n g " > * * O W M * O F F I * E 1 < / S e r v e r N a m e > < S e r v e r O
S   d t : d t = " s t r i n g " > M i c r o s o f t   W i n d o w s   S e r v e
r   2 0 0 8   R 2   D a t a c e n t e r   E d i t i o n   ( W O W   6 4 )   S e
r v i c e   P a c k   1 < / S e r v e r O S > < S e r v e r T y p e   d t : d t
= " s t r i n g " > G a t e w a y < / S e r v e r T y p e > < S e r v e r V e r
i f i e d   d t : d t = " u i 4 " > 1 < / S e r v e r V e r i f i e d > < S "
....
....
<<received "e r v e r V e r s i o n   d t : d t = " s t r i n g " > 1 0 . 5   (
b u i l d   1 3 2 7 ) < / S e r v e r V e r s i o n > < / S e r v e r 2 > < / R
  o t X M L >
   "

XML Data file saved to demo.xml
closing socket
```


License
----

GPLV3


**Free Software, Hell Yeah!**

[2X]:http://www.2X.com/
[blog]:http://blog.ng.pe/
