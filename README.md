# This Project Tries to Document Getting Started with Elasticserch and Kibana on OSX

*It's easier to manage and configure these apps with a custom installation as opposed to using homebrew.*

Download these to a drectory called 'apps' where you can keep all unmanaged applications.

- Download the *.zip of elasticsearch from:https://www.elastic.co/downloads/elasticsearch
- Download the *.tar.gz of kibana from: https://www.elastic.co/downloads/kibana

Unzip the downloaded files (this will be the home folders of the respective apps)

##### Starting a local node of Elasticsearch
Issue this command from elasticsearch root folder in terminal:
./bin/elasticsearch f
Issue this command from terminal to shutdown elasticsearch:

curl -XPOST 'http://localhost:9200/_cluster/nodes/_local/_shutdown'

##### Starting and Quiting Kibana
Issue this command from the kibana home folder: ./kibana-4.5.0-darwin-x64/bin/kibana

Kibana resides on localhost:5601 (open it in your favourite browser)

Shutting down Kibana
Issue ctrl + c in the terminal it was launched in.

*NOTE: The start up command for Kibana depends on the version of Kibana downloaded.*

##### Monitoring Elasticsearch with Kopf
Kopf is a free alternative to Marvel. In order to help with the monitoring of Elasticsearch
- Install kopf from:
https://github.com/lmenezes/elasticsearch-kopf

With this command from within Elasticsearch's home folder:
 ./bin/plugin install lmenezes/elasticsearch-kopf/{2.0/v2.1.1}
open http://localhost:9200/_plugin/kopf

##### Timelion
- Install Timelion from within Kibana with:
./apps/kibana-4.5.0-darwin-x64/bin/kibana plugin -i kibana/timelion

NOTES:
Elastic search indices must only have lower case names.

#### Useful Links

- Twitter Sentiment - Python , Elasticsearch & Kibana
https://realpython.com/blog/python/twitter-sentiment-python-docker-elasticsearch-kibana/#disqus_thread

##### Kibana
- Kibana 10 Minute Walk Through
https://www.elastic.co/guide/en/kibana/3.0/using-kibana-for-the-first-time.html
- Introduction to Kibana
https://www.timroes.de/2015/02/07/kibana-4-tutorial-part-1-introduction/
- Kibana Tutorials on YouTube https://www.youtube.com/watch?v=96og3aIgyrc&list=PLhLSfisesZIvA8ad1J2DSdLWnTPtzWSfI
- Plotting a Line Chart
http://stackoverflow.com/questions/30120199/how-to-create-value-over-time-line-chart-in-kibana-4
- Getting Started https://www.elastic.co/guide/en/kibana/current/getting-started.html
- Creating Pie Charts in Kibana 4 https://www.youtube.com/watch?v=Cjww_oug2E8
- Timelion a Timeseries add on: https://www.elastic.co/blog/timelion-timeline

##### Logstash
- Getting started with Logstash
https://kevinkirsche.com/2014/08/22/using-logstash-to-import-logfiles-from-a-directory/

##### Elasticsearch Useful Commands

##### Cluster Health
curl -GET 'http://localhost:9200/_cluster/health'

##### Add an Index
create and index called blogs
curl -XPUT 'http://localhost:9200/blogs/'

##### Delete Indices
curl -XDELETE 'http://localhost:9200/logstash*/'
The example above deletes the logstash with the wild card *

#### Notes
_type = object
_id = unique identifier

