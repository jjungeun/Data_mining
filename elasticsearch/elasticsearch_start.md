(이 문서는 depricated 문서입니다. elastic_docker.md문서를 참고하세요.)

관계형 db와 비교

Index - Database

Type - Table

Field - Column

Document - row

Analyze - Index

_id - Primary key

Mapping - Schema

Shard - Pyhsical partition

Route - Logical partition



Kibana dev tool을 사용함

1. 인덱스 생성과 타입 설정(Mapping)

   ```
   PUT /news
   {
   	"settings" :{
   		"number_of_shards" : "5",
   		"number_of_replicas" : "2"
   	},
   	"properties": {
           "url":     {"type": "text"},
           "title":   {"type": "text"},
           "summary": {"type": "text"},
           "topic":   {"type": "text"},
           "reg_date":{"type": "date","format": "yyyy-MM-dd"}
        }
   }
   ```

   이렇게 샤드를 5개, 리플리카를 2개로 설정하고 인덱스를 생성한다.

   타입의 매핑을 설정한다. 직접 설정할 수도 있고 한개의 샘플 데이터를 넣어 자동 매핑할 수도 있다. 그러나 한번 정해진 매핑은 변경할 수 없음! 

   인덱스정보를 확인해 본다.

   ```
   GET /news
   
   {
     "news" : {
       "aliases" : { },
       "mappings" : {
         "properties" : {
           "reg_date" : {
             "type" : "date",
             "format" : "yyyy-MM-dd"
           },
           "summary" : {
             "type" : "text"
           },
           "title" : {
             "type" : "text"
           },
           "topic" : {
             "type" : "text"
           },
           "url" : {
             "type" : "text"
           }
         }
       },
       "settings" : {
         "index" : {
           "creation_date" : "1559544128543",
           "number_of_shards" : "5",
           "number_of_replicas" : "2",
           "uuid" : "gCv1IpwTSnyGWui3FQt1CA",
           "version" : {
             "created" : "7010199"
           },
           "provided_name" : "news"
         }
       }
     }
   }
   
   ```

+ 인덱스 템플릿
  인덱스 템플릿은 인덱스를 새로 생성할때마다 미리 작성된 매핑으로 적용하는 것이다. 기존에 공통적인 매핑정보를 만들고 새로운 매핑을 추가하는 방법으로 새 인덱스를 만들 수도 있다.



2. 노드 2개 추가

   마스터 노드와 같은 버전의 elasticsearch를 2개 더 설치한다. 

   elasticsearch.yml파일을 복사 붙여넣기 하여 운영중인 노드들과 동일한 설정을 한다. node.name은 각각 유니크하게 설정한다.

   discovery.zen.minimum_master_nodes를 2로 설정하고 새 노드의 discovery.zen.ping.unicast.hosts에 기존 노드 주소를 추가하고 cluster.name과 node.name을 설정한다.

   기존 노드가 재시작하는 경우를 대비하여 기존 노드의 yml파일의 discovery.zen.ping.unicast.hosts에 신규 노드의 IP를 추가해도 된다.

   
   
   error !
   
   yml파일을 다음과 같이 설정하고 elasticsearch를 실행했는데 마스터 노드를 못찾는다ㅠ
   
   ```
   cluster.name: elasticsearch
   cluster.initial_master_nodes: node-1
   node.name: node-2
   discovery.zen.ping.unicast.hosts : ["203.253.25.63:9200"]
   discovery.zen.minimum_master_nodes : 2
   ```
   
   ```
   curl -XGET "localhost:9200/_cat/health?v&pretty"
   
   {
     "error" : {
       "root_cause" : [
         {
           "type" : "master_not_discovered_exception",
           "reason" : null
         }
       ],
       "type" : "master_not_discovered_exception",
       "reason" : null
     },
     "status" : 503
   }
   ```
   
   
   
   
