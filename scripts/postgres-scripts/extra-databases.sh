#!/bin/bash

set -Eeo pipefail

docker_process_sql() {
	local query_runner=( psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --no-password --no-psqlrc )
	if [ -n "$POSTGRES_DB" ]; then
		query_runner+=( --dbname "$POSTGRES_DB" )
	fi

	PGHOST= PGHOSTADDR= "${query_runner[@]}" "$@"
}

docker_setup_db() {
    local postgresdb=$1
	local dbAlreadyExists
	dbAlreadyExists="$(
		POSTGRES_DB= docker_process_sql --dbname postgres --set db="$postgresdb" --tuples-only <<-'EOSQL'
			SELECT 1 FROM pg_database WHERE datname = :'db' ;
		EOSQL
	)"
	if [ -z "$dbAlreadyExists" ]; then
		POSTGRES_DB= docker_process_sql --dbname postgres --set db="$postgresdb" <<-'EOSQL'
			CREATE DATABASE :"db" ;
		EOSQL
		echo
	fi
}

if [ -n "$POSTGRES_EXTRA_DB" ]; then
    echo "Extra databases: $POSTGRES_EXTRA_DB"

    for db in $(echo $POSTGRES_EXTRA_DB | tr ',' ' '); do
        docker_setup_db $db
        docker_setup_db test-$db
    done
fi
