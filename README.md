# About dbt2dbml
This is a little script to parse a [dbt](https://www.getdbt.com/) model file like:

```
version: '2'
models:
- name: table_name
  description: Table description
  meta:
  columns:
  - name: column1
    description: Column 1 description
    tests:
    - not_null
    - unique
    - at_least_one
  - name: column2
    description: Column 2 description
...
  ```

...and turn it into a [DBML](https://dbml.dbdiagram.io/docs/) definition, like so:

```
Table {
  column1 x [note: "Column 1 description"]
  column2 x [note: "Column 2 description"]
]
```

# Ok... Why do I care?
Because THEN you can paste it into https://dbdiagram.io/ and get a lovely auto-generated E-R diagram like this! 🤩

<img width="1200" alt="Screenshot 2024-06-20 at 1 56 20 PM" src="https://github.com/webchick/dbt2dbml/assets/332535/1d5fc4c0-0048-45dd-9092-f11c3f8307a9">

# Usage
1. Clone the repo
2. Create a 'dbt' folder inside
3. Put 1-N of your dbt model YAML files into it.
4. Run ```python3 dbt2dbml.py```
5. Profit! ;)

## Credits
* Honestly, credit where credit is due, ChatGPT 4o wrote most of this. 😅
* @pcreux from [Creating an ERD for your dbt project](https://discourse.getdbt.com/t/creating-an-erd-for-your-dbt-project/1436) for enlighteing me that DBML is a thing! :D
