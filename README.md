mean-heap
=========

A simple Python script for calculating the mean JVM Heap (OldGen and PermGen) from a detailed GC log file. Tested with Oracle's Java Version 7. Works with the following GCs:

* ParallelGC (-XX:+UseParallelGC) - Default GC in Oracle JRE/JDK as of Version 6
* ParallelOldGC (-XX:+UseParallelOldGC)

Does not work with SerialGC, CMS or G1. 

Requires that you start your JVM with detailed GC logging (-XX:-PrintGCDetails).

Usage
--------

calculate-mean-heap.py /path/to/gc.log

This obviously requires that you have a gc.log lying around. You can enable adequate GC logging by passing the following options to your JVM:

    -XX:+PrintGC -XX:+PrintGCDetails -XX:+PrintGCDateStamps -Xloggc:/var/log/gc.log 

After restarting your Java application, Garbage Collection details will be logged to /var/log/gc.log
