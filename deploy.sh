#!/bin/bash

set -e

/home/help/.virtualenvs/nikola/bin/nikola build 
/home/help/.virtualenvs/nikola/bin/nikola deploy

