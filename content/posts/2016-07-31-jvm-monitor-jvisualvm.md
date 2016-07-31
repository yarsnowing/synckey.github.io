Title:JVM Monitor--jvisualvm
Date: 2016-07-26
Category: java,posts,jvm,profile,trouble shooting
Tags: life
Slug: jvm-monitor-tool-jvisualvm

    :::bash
    jvisualvm -Dcom.sun.management.jmxremote.port=8999 -Dcom.sun.management.jmxremote.ssl=false \
     -Dcom.sun.management.jmxremote.authenticate=false -Djava.rmi.server.hostname=10.86.46.252