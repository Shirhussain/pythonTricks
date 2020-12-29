if you want to dumpdata of your apps models you cand do as follows:
1 =  ./manage.py dumpdata appName --indent=2
2 = ./manage.py dumpdata --help 
3 = if you wanna extrat to some folders or files so do this: ./manage.py dumpdata courses --indent=2 --output=courses/fixtures/subjects.json
4 = if you wanna load tata back to your database form that file so do this:  ./manage.py loaddata subjects.json
by default django look for files in fixtures directory of each application but you can specify to complite fixture file

