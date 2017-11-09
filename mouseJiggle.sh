#Jiggle the mouse every 5 minutes to keep display from going to sleep
while :
do
	xdotool mousemove_relative 1 1
	sleep 300
done
