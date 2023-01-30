if [[ $1 == "--new-statics" ]] # Carefully with this command if you have a DB in dokcer with volumes it can delete data!
then
	docker-compose rm
	docker volume rm splitsystems_static --force
	docker volume rm splitsystems_app --force
	docker-compose pull
  docker-compose up --force-recreate -d
	exit
else
  echo "starting containers"
  docker-compose up
  echo "Website launched."
fi
