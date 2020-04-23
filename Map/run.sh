#!/bin/bash
set -e 
exec python ../Map/server2.py &
exec python ../app/server.py serve
