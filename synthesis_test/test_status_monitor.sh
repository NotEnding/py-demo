#!/bin/bash

#source activate synthesis

logdir=$1
backdir=$2
mailserver=$3
username_send=$4
password=$5
username_recv=$6
versiondir=$7
user=$8

for file in `ls $logdir | grep '\.log'`; do
	mkdir -p $backdir
	cp $logdir/$file $backdir/$file
	echo `date` > $logdir/$file
	mv $backdir/$file $backdir/`date +"%Y-%m-%d"`
	rm -r $backdir/`date +"%Y-%m-%d" -d "-32 days"`
	python /home/py-public/bl-tts/server/status_monitor.py --mailserver smtp.163.com --username_send 18947187988@163.com --password jiayan150124 --username_recv 1060036161@qq.com
	bash $versiondir/send_email.sh $mailserver $username_send $password $username_recv $versiondir $user
done
