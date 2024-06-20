import os
import yaml

# Directory containing the dbt model YAML files
dbt_folder = './dbt'

# Function to escape single quotes in descriptions
def escape_single_quotes(description):
    return description.replace("'", "\\'")

# Function to quote column names with dots
def quote_column_name(name):
    if '.' in name:
        return f'"{name}"'
    return name

# Function to convert dbt model to DBML format
# TODO: Would be great to be able to introspect this.
def convert_dbt_to_dbml(dbt_model):
    dbml = f"Table {dbt_model['name']} {{\n"
    for column in dbt_model['columns']:
        name = quote_column_name(column['name'])
        description = column.get('description', '')
        db_type = 'x'  # Default type, adjust based on your schema if needed
        if 'integer' in name:
            db_type = 'integer'
        elif 'timestamp' in name:
            db_type = 'timestamp'
        elif 'text' in name:
            db_type = 'text'
        elif 'email' in name:
            db_type = 'varchar'
        # Add more type checks as necessary

        # Escape single quotes in description
        description = escape_single_quotes(description)

        # Add note if description exists
        if description:
            dbml += f"    {name} {db_type} [note: '{description}']\n"
        else:
            dbml += f"    {name} {db_type}\n"
    dbml += "}\n"
    return dbml

# Function to read and convert YAML files to DBML
def process_dbt_files(dbt_folder):
    dbml_output = ""
    for filename in os.listdir(dbt_folder):
        if filename.endswith('.yml'):
            with open(os.path.join(dbt_folder, filename), 'r') as file:
                dbt_data = yaml.safe_load(file)
                for model in dbt_data['models']:
                    dbml_output += convert_dbt_to_dbml(model)
    return dbml_output

# Generate DBML output from dbt files
dbml_output = process_dbt_files(dbt_folder)
print(dbml_output)

# Optionally, write the DBML output to a file
with open('output.dbml', 'w') as output_file:
    output_file.write(dbml_output)
