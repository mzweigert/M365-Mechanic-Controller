ADDRESS=pi@raspberrypi.local
PASSWORD="raspberry"
PROJECT_DIR=/home/pi/M365-Pi-Controller

case "$*" in
(*--install*) echo $PASSWORD | ssh $ADDRESS "sh -s" < install_dependencies.sh $PROJECT_DIR;;
esac
echo $PASSWORD | ssh $ADDRESS "sudo rm -rf $PROJECT_DIR/src/; mkdir -p $PROJECT_DIR/src/; sh -s" < unpack_libraries.sh $PROJECT_DIR
echo $PASSWORD | scp -rp ./src $ADDRESS:$PROJECT_DIR
echo $PASSWORD | ssh $ADDRESS "sudo sh $PROJECT_DIR/src/run.sh $PROJECT_DIR"
