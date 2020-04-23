#!/bin/bash
set -e 
exec python server2.py &
exec python ../app/server.py serve
