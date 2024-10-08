# cloudant-scripts
#### scripts to generate documents for IBM Cloudant db
----

Script `gen_doc.py` provides a flexible way to generate as many documents as needed for testing or populating a Cloudant database. 

You can easily adjust the `number_of_documents` variable to create json documents in desired quantity, the script will put them in a `generated_documents.json` file.

`number_of_documents = 10000` creates 10,000 json documents.

example upload bulk docs to cloudant db

```
curl -u username -H "Content-Type: application/json" -d@generated_documents.json -X POST "https://cloudant.com/dbname/_bulk_docs" | jq .
```

----

Script `generate-json.py` can be helpful with [couchrestore](https://www.npmjs.com/package/@cloudant/couchbackup) CLI , it generates sample json documents and includes them in  a `.txt` file of the required size for uploading  to the Cloudant database.

adjust `target_file_size_gb` to generate a large `.txt` file containing json docs suitable for a Cloudant database.

`target_file_size_gb = 0.002` means a 2MB txt file.

`target_file_size_gb = 1` means a 1GB txt file.

example upload bulk docs to cloudant db using `couchrestore` CLI
```
export COUCH_URL=https://myusername:mypassword@myhost.cloudant.com
export COUCH_DATABASE=dbname
export COUCH_PARALLELISM=7
export COUCH_BUFFER_SIZE=1500
export COUCH_RESUME=true

cat sample_json_1MB.txt  | couchrestore


output
-------
% cat sample_json_1MB.txt | couchrestore                                                                              [9/10/24 | 12:21:22]
================================================================================
Performing restore on https://****:****@myhost.cloudant.com/one_mb using configuration:
{
  "bufferSize": 1500,
  "parallelism": 7,
  "requestTimeout": 120000
}
================================================================================
  couchbackup:restore:batch restored 1500 +0ms
  couchbackup:restore:batch restored 2109 +34ms
  couchbackup:restore:batch restored 3609 +573ms
  couchbackup:restore:batch restored 5109 +58ms
  couchbackup:restore:batch restored 6609 +103ms
  couchbackup:restore finished { total: 6609 } +0ms
```
