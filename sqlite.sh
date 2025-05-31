#!/bin/sh

# Script to upload JSON files to SQLite database
# Usage: ./upload_json.sh <database_file> <json_file>

# Check if correct number of arguments provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 <database_file> <json_file>"
    echo "Example: $0 mydata.db bug-123.json"
    exit 1
fi

DB_FILE="$1"
JSON_FILE="$2"

# Check if JSON file exists
if [ ! -f "$JSON_FILE" ]; then
    echo "Error: JSON file '$JSON_FILE' does not exist"
    exit 1
fi

# Extract filename without path
FILENAME=$(basename "$JSON_FILE")

# Create table if it doesn't exist
sqlite3 "$DB_FILE" "CREATE TABLE IF NOT EXISTS json_files (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT NOT NULL,
    json_blob TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);"

# Check if table creation was successful
if [ $? -ne 0 ]; then
    echo "Error: Failed to create table"
    exit 1
fi

# Read JSON file content and escape single quotes for SQL
JSON_CONTENT=$(cat "$JSON_FILE" | sed "s/'/''/g")

# Insert the JSON file into the database
sqlite3 "$DB_FILE" "INSERT INTO json_files (filename, json_blob) VALUES ('$FILENAME', '$JSON_CONTENT');"

# Check if insert was successful
if [ $? -eq 0 ]; then
    echo "Successfully uploaded '$FILENAME' to database '$DB_FILE'"

    # Show the record count
    RECORD_COUNT=$(sqlite3 "$DB_FILE" "SELECT COUNT(*) FROM json_files;")
    echo "Total records in database: $RECORD_COUNT"
else
    echo "Error: Failed to insert JSON file into database"
    exit 1
fi