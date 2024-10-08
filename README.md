# cloudant-scripts
#### scripts to generate documents for IBM Cloudant db
----

Script `gen_doc.py` provides a flexible way to generate as many documents as needed for testing or populating a Cloudant database. 

You can easily adjust the `number_of_documents` variable to create any desired quantity.

example upload bulk docs to cloudant db

```
curl -u username -H "Content-Type: application/json" -d@generated_documents.json -X POST "https://cloudant.com/dbname/_bulk_docs" | jq .
```

----

`generate-json.py` can be helpful with [couchrestore](https://www.npmjs.com/package/@cloudant/couchbackup) CLI to upload bulk docs to a Cloudant database.

adjust `target_file_size_gb = 0.002` to generate a large json file containing json docs suitable for a Cloudant database.

`0.002` means a 2MB json file.
