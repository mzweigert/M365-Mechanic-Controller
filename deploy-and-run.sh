ADDRESS=pi@raspberrypi.local
PASSWORD="raspberry"
PROJECT_DIR=/home/pi/M365-Pi-Controller

if [ ! -f "$HOME/.ssh/raspberry_id" ]; then
     ssh-keygen -t rsa -b 4096 -C "comment" -P "$PASSWORD" -f "$HOME/.ssh/raspberry_id" -q
     yes | ssh-copy-id $ADDRESS
fi


case "$*" in
(*--install*) ssh $ADDRESS "sh -s" < install_dependencies.sh $PROJECT_DIR;;
esac
ssh $ADDRESS "sudo rm -rf $PROJECT_DIR/src/; mkdir -p $PROJECT_DIR/src/; sh -s" < config.sh $PROJECT_DIR
scp -rp ./src $ADDRESS:$PROJECT_DIR
ssh $ADDRESS "sudo sh $PROJECT_DIR/src/run.sh $PROJECT_DIR"
