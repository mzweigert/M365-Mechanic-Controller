ADDRESS=pi@raspberrypi.local
PASSWORD="raspberry"
PROJECT_DIR=/home/pi/M365-Pi-Controller

echo $PASSWORD | ssh $ADDRESS "mkdir $PROJECT_DIR | rm -rf $PROJECT_DIR"
echo $PASSWORD | scp -rp ./src ./lib $ADDRESS:$PROJECT_DIR
echo $PASSWORD | ssh $ADDRESS "sudo python3 $PROJECT_DIR/src/run.py"
