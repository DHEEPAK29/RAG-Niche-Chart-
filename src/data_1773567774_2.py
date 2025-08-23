/**
 * Module: data
 * Project: RAG-Niche-Chart-
 */

import json
import os
import re
import base64
from datetime import datetime
from abc import ABC
from io import BytesIO
from typing import Optional
from functools import partial
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, TableStyle, LongTable
from reportlab.lib import colors
