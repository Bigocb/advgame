#cd views/vue-argon-dashboard
#pwd
#npm run serve &
#cd ../../
source env/bin/activate
python3 data/src/controller/app.py &
python3 data/src/generator/generate.py &
python3 data/src/tagging/tagging.py
