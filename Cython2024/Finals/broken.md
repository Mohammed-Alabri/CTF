challange ```Broken```

* In this challange we got pcap file.
* Follow tcp stream, will recognise file being uploaded.
* Use the "File" menu and select "Export Objects" -> "HTTP" and save the file.
* let's open the file in hex editor (I'm using HxD) and check the file.

![](imgs/broken_1.png)

* there is signs that this file is PNG (highlighted) but the file is corrupted.
* remove all bytes before ```IHDR```.

![](imgs/broken_2.png)

* from another png image copy all bytes before ```IHDR```.

![any png image](imgs/broken_3.png)

* paste the copied bytes in broken file.

![corrected broken Image](imgs/broken_4.png)

* open broken image and you will see the flag.