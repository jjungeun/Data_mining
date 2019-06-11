# Elastic search 샤딩



'news' index에 5개의 shard와 2개의 replica로 설정되어 있다.

그러나 'elasticsearch' cluster에 node가 1개여서 replica는 unassigned된 상태이다.



replica를 유지하기 위해서는 최소 2개의 node가 필요하다. 그러나 하나의 노드가 다운된 상태에서도 지속성을 유지하려면 세 개의 노드가 필요하다.

따라서 최대 샤드의 개수는 5 * (2 + 1) = 15개이므로 15개의 샤드를 3개의 node에 나누어 샤딩한다. (노드만 생성하면 자동으로 scaling해준다.)



1. 엘라스틱서치 복사본을 추가적으로 2개를 설치한다. (<https://www.elastic.co/guide/en/elastic-stack-get-started/7.1/get-started-elastic-stack.html#install-elasticsearch> 참고)
2. ES_PATH_CONF/elasticsearch.yml파일에 cluster.name과 node.name 설정한다.
3. split brain상황을 피하기 위해 discovery.zen.minimum_master_nodes을 2으로 설정한다.



밑에는 노드 추가 예시 (출처 : Elasticsearch 공식 사이트 <https://www.elastic.co/guide/en/elastic-stack-overview/current/encrypting-communications-hosts.html>)



예시) 기존 노드

xpack.security.enabled: true

cluster.name: test-cluster

node.name: node-1

discovery.zen.minimum_master_nodes: 2

transport.tcp.port: 9301

discovery.zen.ping.unicast.hosts: ["localhost:9302", "localhost:9303"]



예시) 추가 노드

xpack.security.enabled: true

cluster.name: test-cluster

node.name: node-2

discovery.zen.minimum_master_nodes: 2

transport.tcp.port: 9302

discovery.zen.ping.unicast.hosts: ["localhost:9301", "localhost:9303"]



1. 0에서 다운받은 Elasticsearch node를 시작한다.
2. Kibana도 다시 시작한다.
3. `GET _cat/nodes?v`, `GET _nodes?`, `GET _cluster/health`로 노드생성이 성공적인지 확인한다.



+++ 샤딩 시 중요한 것은 기존 노드와 새 노드는 동일한 스펙의 머신이어야 한다는 것이다!

​		그리고 elasticstack의 버전도 동일해야한다.

# 따라서 docker를 사용해 클러스터링, 샤딩을 진행한다!! elastic_docker.md

**참고 :<http://kimjmin.net/2018/01/2018-01-build-es-cluster-3/> aws 서버 이미지 복사를 사용하여 노드추가**
