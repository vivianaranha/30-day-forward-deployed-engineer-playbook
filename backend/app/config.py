from __future__ import annotations
import os
APP_ENV=os.getenv("APP_ENV","local")
AI_MODE=os.getenv("AI_MODE","demo")
REQUEST_TIMEOUT_SECONDS=float(os.getenv("REQUEST_TIMEOUT_SECONDS","5"))
