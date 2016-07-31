Title:JVM Monitor Tool---jvisualvm
Date: 2016-07-26
Category: tricksk 
Tags: java,posts,jvm,profile,trouble shooting
Slug: jvm-monitor-tool-jvisualvm

    :::bash
    jvisualvm -Dcom.sun.management.jmxremote.port=8999 -Dcom.sun.management.jmxremote.ssl=false \
     -Dcom.sun.management.jmxremote.authenticate=false -Djava.rmi.server.hostname=10.86.46.252