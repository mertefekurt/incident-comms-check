from __future__ import annotations

from incident_comms_check.models import Rule

PROJECT_NAME = 'incident-comms-check'
SUMMARY = 'Validate incident communication drafts for impact, ETA, and owner clarity.'
SAMPLE_RISK = 'incident update impact unknown eta missing owner none'
SAMPLE_CLEAN = 'incident update impact 420 users eta 30m owner support-lead'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "path", "service", "endpoint", "field", "event")

RULES = (
    Rule(
        code='unknown-impact',
        severity='high',
        pattern='impact\\s+(unknown|missing|none)',
        message='impact is not clear',
        recommendation='state affected users, tenants, or functions',
    ),
    Rule(
        code='missing-eta',
        severity='medium',
        pattern='eta\\s+(missing|unknown|none)',
        message='ETA is missing',
        recommendation='provide next update time or recovery estimate',
    ),
    Rule(
        code='ownerless-update',
        severity='low',
        pattern='owner\\s+(none|unknown|missing)',
        message='communication owner is missing',
        recommendation='assign a comms owner',
    ),
)
