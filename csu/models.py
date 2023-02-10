""" Model OpenIMIS Be CSU Program concept
Models of Program Concept
Adding capability to manage differents programs in the same openIMIS instance and manage right on different objects
"""
import datetime
from dataclasses import dataclass

from django.core.exceptions import ValidationError
from django.db import models
from core import models as core_models
from core.models import InteractiveUser
from django.http import request
from django.utils import timezone as django_tz 
import pandas as pd
import logging

logger = logging.getLogger(__name__)

