#! /usr/bin/env bash
set -e
python -m uvicorn main:app --reload --host 0.0.0.0